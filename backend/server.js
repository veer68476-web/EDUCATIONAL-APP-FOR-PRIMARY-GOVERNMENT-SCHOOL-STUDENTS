require('dotenv').config();
const express = require('express');
const bodyParser = require('body-parser');
const cors = require('cors');
const bcrypt = require('bcrypt');
const nodemailer = require('nodemailer');
const path = require('path');
const fs = require('fs');
const mongoose = require('mongoose');
const { connectDB, User, LoginHistory } = require('./db');

const app = express();
app.use(cors());
app.use(bodyParser.json());
app.use('/assets', express.static(path.join(__dirname, '../assets')));
app.use(express.static(path.join(__dirname, 'public')));

// Serverless DB connection middleware
app.use(async (req, res, next) => {
  try {
    await connectDB();
  } catch (err) {
    // continue
  }
  next();
});

function generateUniqueId() {
  return Math.floor(100000 + Math.random() * 900000);
}

function generateOtp() {
  return Math.floor(100000 + Math.random() * 900000).toString();
}

function isValidEmail(email) {
  const regex = /^[\w-\.]+@([\w-]+\.)+[\w]{2,4}$/;
  return regex.test(email);
}

const otpStore = new Map();

// ✅ Send OTP
app.post('/send-otp', async (req, res) => {
  const { email } = req.body;

  if (!email || !isValidEmail(email)) {
    return res.status(400).json({ error: 'Invalid email format' });
  }

  try {
    const user = await User.findOne({ email: email.toLowerCase() });
    if (!user) {
      return res.status(404).json({ error: 'Email not found in database' });
    }

    const otp = generateOtp();
    otpStore.set(email.toLowerCase(), otp);

    const transporter = nodemailer.createTransport({
      service: 'gmail',
      auth: {
        user: 'vinaykumardasari47@gmail.com',
        pass: 'zyfr mgpt omxq drun'
      }
    });

    await transporter.sendMail({
      from: 'SkillPlay App',
      to: email,
      subject: 'Your OTP for Password Reset',
      text: `Your OTP is: ${otp}`
    });

    res.status(200).json({ message: 'OTP sent to email' });
  } catch (err) {
    res.status(500).json({ error: 'Server error', details: err.message });
  }
});

// ✅ Verify OTP
app.post('/verify-otp', (req, res) => {
  const { email, otp } = req.body;

  if (!email || !otp) {
    return res.status(400).json({ error: 'Email and OTP required' });
  }

  const storedOtp = otpStore.get(email.toLowerCase());
  if (storedOtp !== otp) {
    return res.status(401).json({ error: 'Invalid OTP' });
  }

  res.status(200).json({ message: 'OTP verified' });
});

// ✅ Reset Password
app.post('/reset-password', async (req, res) => {
  const { email, newPassword, confirmPassword } = req.body;

  if (!email || !newPassword || !confirmPassword) {
    return res.status(400).json({ error: 'All fields are required' });
  }

  if (newPassword !== confirmPassword) {
    return res.status(400).json({ error: 'Passwords do not match' });
  }

  try {
    const hashedPassword = await bcrypt.hash(newPassword, 10);
    const updated = await User.findOneAndUpdate(
      { email: email.toLowerCase() },
      { password: hashedPassword, updatedAt: new Date() }
    );

    if (!updated) {
      return res.status(404).json({ error: 'Email not found' });
    }

    otpStore.delete(email.toLowerCase());
    res.status(200).json({ message: 'Password reset successful' });
  } catch (err) {
    res.status(500).json({ error: 'Server error', details: err.message });
  }
});

// ✅ Register (Saves to MongoDB)
app.post('/register', async (req, res) => {
  const { name, email, phone, password } = req.body;
  const userId = generateUniqueId();

  if (!name || !email || !phone || !password) {
    return res.status(400).json({ error: 'All fields are required' });
  }

  try {
    const cleanEmail = email.toLowerCase().trim();
    const existing = await User.findOne({ email: cleanEmail });
    if (existing) {
      return res.status(400).json({ error: 'User already registered with this email' });
    }

    const hashedPassword = await bcrypt.hash(password, 10);

    const newUser = new User({
      id: userId,
      name: name.trim(),
      email: cleanEmail,
      phone: phone.trim(),
      password: hashedPassword,
      count: 0
    });

    await newUser.save();
    console.log(`✅ [MongoDB Compass] New user registered: ${name} (${cleanEmail})`);
    res.status(200).json({ message: 'User registered', userId });
  } catch (err) {
    console.error('❌ MongoDB Register error:', err);
    res.status(500).json({ error: 'Database error', details: err.message });
  }
});

// ✅ Login (Validates against MongoDB)
app.post('/login', async (req, res) => {
  const { email, password } = req.body;

  if (!email || !password) {
    return res.status(400).json({ error: 'Email and password required' });
  }

  try {
    const cleanEmail = email.toLowerCase().trim();

    // Fallback if cloud DB is still connecting on Vercel
    if (mongoose.connection.readyState < 1) {
      if (cleanEmail === 'raghuveer081014@gmail.com' && password === 'password123') {
        return res.status(200).json({
          message: 'Login successful',
          user: {
            name: 'Raghu Veer',
            email: 'raghuveer081014@gmail.com',
            phone: '8639118335',
            count: 50,
            role: 'admin',
            isAdmin: true
          }
        });
      }
      return res.status(503).json({ error: 'Database is connecting. Please configure MONGODB_URI in Vercel environment variables or login with Admin credentials.' });
    }

    const user = await User.findOne({ email: cleanEmail });

    if (!user) {
      return res.status(401).json({ error: 'Invalid email or password' });
    }

    const isMatch = await bcrypt.compare(password, user.password);

    if (!isMatch) {
      return res.status(401).json({ error: 'Invalid email or password' });
    }

    // ✅ Update user login stats in MongoDB
    await User.updateOne(
      { email: cleanEmail },
      {
        $set: { lastLogin: new Date(), updatedAt: new Date() },
        $inc: { loginCount: 1 }
      }
    );

    // ✅ Save login event to login_histories collection
    try {
      const loginLog = new LoginHistory({
        userId: user.id,
        name: user.name,
        email: cleanEmail,
        phone: user.phone || '',
        loginTime: new Date(),
        status: 'SUCCESS',
        ip: req.ip || req.headers['x-forwarded-for'] || '127.0.0.1',
        userAgent: req.headers['user-agent'] || 'Browser'
      });
      await loginLog.save();
      console.log(`📝 [MongoDB Compass] Login recorded: ${user.name} (${cleanEmail})`);
    } catch (logErr) {
      console.warn('Login history record warning:', logErr);
    }

    console.log(`✅ [MongoDB Compass] User logged in: ${user.name} (${cleanEmail})`);
    res.status(200).json({
      message: 'Login successful',
      user: {
        name: user.name,
        email: user.email,
        phone: user.phone,
        count: user.count,
        role: user.role || (cleanEmail === 'raghuveer081014@gmail.com' ? 'admin' : 'student'),
        isAdmin: user.isAdmin || (cleanEmail === 'raghuveer081014@gmail.com')
      }
    });
  } catch (err) {
    console.error('❌ MongoDB Login error:', err);
    res.status(500).json({ error: 'Server error', details: err.message });
  }
});

// ✅ Profile (Fetches from MongoDB)
app.get('/profile', async (req, res) => {
  const { email } = req.query;

  if (!email) {
    return res.status(400).json({ error: 'Email is required' });
  }

  try {
    const cleanEmail = email.toLowerCase().trim();
    const user = await User.findOne({ email: cleanEmail });

    if (!user) {
      return res.status(404).json({ error: 'User not found' });
    }

    res.status(200).json({
      name: user.name,
      email: user.email,
      phone: user.phone,
      count: user.count,
      role: user.role || (cleanEmail === 'raghuveer081014@gmail.com' ? 'admin' : 'student'),
      isAdmin: user.isAdmin || (cleanEmail === 'raghuveer081014@gmail.com')
    });
  } catch (err) {
    res.status(500).json({ error: 'Database error', details: err.message });
  }
});

// ✅ Update Count / Points (Updates in MongoDB)
app.post('/update-count', async (req, res) => {
  const { email, increment } = req.body;

  if (!email || increment === undefined) {
    return res.status(400).json({ error: 'Email and increment are required' });
  }

  try {
    const cleanEmail = email.toLowerCase().trim();
    const updated = await User.findOneAndUpdate(
      { email: cleanEmail },
      { $inc: { count: Number(increment) }, updatedAt: new Date() },
      { new: true }
    );

    if (!updated) {
      return res.status(404).json({ error: 'User not found' });
    }

    console.log(`⭐ [MongoDB Compass] Points updated for ${cleanEmail}: +${increment} (Total: ${updated.count})`);
    res.status(200).json({ message: 'Count updated successfully', count: updated.count });
  } catch (err) {
    console.error('❌ MongoDB Update Count error:', err);
    res.status(500).json({ error: 'Database error', details: err.message });
  }
});

// ✅ View all registered users (for database inspection)
app.get('/api/users', async (req, res) => {
  try {
    if (mongoose.connection.readyState >= 1) {
      const users = await User.find({}, { password: 0 }).sort({ createdAt: -1 });
      return res.status(200).json({
        database: 'skillplay_db',
        collection: 'users',
        total: users.length,
        users
      });
    }

    // Fallback snapshot if database is still connecting in cloud
    const exportPath = path.resolve(__dirname, 'database_export.json');
    const rootExportPath = path.resolve(__dirname, '../database_export.json');
    const targetFile = fs.existsSync(exportPath) ? exportPath : (fs.existsSync(rootExportPath) ? rootExportPath : null);

    if (targetFile) {
      const data = JSON.parse(fs.readFileSync(targetFile, 'utf8'));
      return res.status(200).json({
        database: 'skillplay_db (Cloud Snapshot)',
        collection: 'users',
        total: (data.users || []).length,
        users: (data.users || []).map(u => ({ ...u, password: '[PROTECTED]' }))
      });
    }

    res.status(200).json({ database: 'skillplay_db', collection: 'users', total: 0, users: [] });
  } catch (err) {
    res.status(500).json({ error: 'Database error', details: err.message });
  }
});

// ✅ View all login events (for database inspection)
app.get('/api/logins', async (req, res) => {
  try {
    if (mongoose.connection.readyState >= 1) {
      const logs = await LoginHistory.find({}).sort({ loginTime: -1 }).limit(100);
      return res.status(200).json({
        database: 'skillplay_db',
        collection: 'loginhistories',
        total: logs.length,
        logins: logs
      });
    }

    // Fallback snapshot if database is still connecting in cloud
    const exportPath = path.resolve(__dirname, 'database_export.json');
    const rootExportPath = path.resolve(__dirname, '../database_export.json');
    const targetFile = fs.existsSync(exportPath) ? exportPath : (fs.existsSync(rootExportPath) ? rootExportPath : null);

    if (targetFile) {
      const data = JSON.parse(fs.readFileSync(targetFile, 'utf8'));
      return res.status(200).json({
        database: 'skillplay_db (Cloud Snapshot)',
        collection: 'loginhistories',
        total: (data.logins || []).length,
        logins: data.logins || []
      });
    }

    res.status(200).json({ database: 'skillplay_db', collection: 'loginhistories', total: 0, logins: [] });
  } catch (err) {
    res.status(500).json({ error: 'Database error', details: err.message });
  }
});

// ✅ Developer Information
app.get('/api/developer', (req, res) => {
  res.status(200).json({
    developer: 'Raghu Veer',
    email: 'raghuveer081014@gmail.com',
    phone: '8639118335',
    role: 'admin',
    isAdmin: true,
    application: 'SkillPlay Educational Platform',
    version: '2.0.0'
  });
});

const PORT = process.env.PORT || 3001;

async function startServer() {
  await connectDB();

  // Create sample/demo student user if collection is empty
  const count = await User.countDocuments();
  if (count === 0) {
    const samplePassword = await bcrypt.hash('password123', 10);
    await User.create({
      id: 100001,
      name: 'Raghu Veer',
      email: 'raghuveer081014@gmail.com',
      phone: '8639118335',
      password: samplePassword,
      count: 50,
      role: 'admin',
      isAdmin: true
    });
    console.log('✅ Created default user in MongoDB: raghuveer081014@gmail.com (admin) (password: password123)');
  }

  const server = app.listen(PORT, '0.0.0.0', () => {
    console.log(`Server running at http://0.0.0.0:${PORT}`);
  });

  server.on('error', (err) => {
    if (err.code === 'EADDRINUSE') {
      console.error(`Port ${PORT} is already in use.`);
    } else {
      console.error('Server error:', err);
    }
    process.exit(1);
  });
}

if (require.main === module) {
  startServer();
}

module.exports = app;

