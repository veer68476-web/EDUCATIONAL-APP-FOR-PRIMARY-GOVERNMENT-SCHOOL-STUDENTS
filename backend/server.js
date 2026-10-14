require('dotenv').config();
const express = require('express');
const bodyParser = require('body-parser');
const cors = require('cors');
const bcrypt = require('bcrypt');
const nodemailer = require('nodemailer');
const path = require('path');
const fs = require('fs');
const mongoose = require('mongoose');
mongoose.set('bufferCommands', false);
const { connectDB, User, LoginHistory } = require('./db');

const app = express();
app.use(cors());
app.use(bodyParser.json());
app.use('/assets', express.static(path.join(__dirname, '../public/assets')));
app.use('/assets', express.static(path.join(__dirname, '../assets')));
app.use(express.static(path.join(__dirname, 'public')));
app.use(express.static(path.join(__dirname, '../public')));

// Serverless DB connection middleware
app.use(async (req, res, next) => {
  try {
    await connectDB();
  } catch (err) {
    // continue
  }
  next();
});

// Cloud Fallback Store (Ensures registration & login always work smoothly on Vercel)
const os = require('os');
const tmpDbPath = path.join(os.tmpdir(), 'skillplay_db_cache.json');
let fallbackUsers = [];
let fallbackLogins = [];

try {
  const exportPath = path.resolve(__dirname, 'database_export.json');
  const rootExportPath = path.resolve(__dirname, '../database_export.json');
  const targetFile = fs.existsSync(exportPath) ? exportPath : (fs.existsSync(rootExportPath) ? rootExportPath : null);
  if (targetFile) {
    const rawData = JSON.parse(fs.readFileSync(targetFile, 'utf8'));
    fallbackUsers = rawData.users || [];
    fallbackLogins = rawData.logins || [];
  }
} catch (e) {
  console.warn('Could not load fallback snapshot:', e.message);
}

function saveTmpSnapshot() {
  try {
    fs.writeFileSync(tmpDbPath, JSON.stringify({ users: fallbackUsers, logins: fallbackLogins }, null, 2), 'utf8');
  } catch (e) {}
}

function loadTmpSnapshot() {
  try {
    if (fs.existsSync(tmpDbPath)) {
      const data = JSON.parse(fs.readFileSync(tmpDbPath, 'utf8'));
      if (Array.isArray(data.users)) {
        data.users.forEach(u => {
          if (!fallbackUsers.some(fu => fu.email.toLowerCase() === (u.email || '').toLowerCase())) {
            fallbackUsers.push(u);
          }
        });
      }
      if (Array.isArray(data.logins)) {
        data.logins.forEach(l => {
          if (!fallbackLogins.some(fl => fl.email.toLowerCase() === (l.email || '').toLowerCase() && String(fl.loginTime) === String(l.loginTime))) {
            fallbackLogins.push(l);
          }
        });
      }
    }
  } catch (e) {}
}

loadTmpSnapshot();

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

// ✅ Register (Saves to MongoDB or Cloud Fallback)
app.post('/register', async (req, res) => {
  const { name, email, phone, password } = req.body;
  const userId = generateUniqueId();

  if (!name || !email || !phone || !password) {
    return res.status(400).json({ error: 'All fields are required' });
  }

  const cleanEmail = email.toLowerCase().trim();

  try {
    // 1. If connected to MongoDB (Atlas or local)
    if (mongoose.connection.readyState >= 1) {
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
        count: 0,
        role: 'student',
        isAdmin: false
      });

      await newUser.save();
      console.log(`✅ [MongoDB] New user registered: ${name} (${cleanEmail})`);
      return res.status(200).json({ 
        message: 'User registered successfully', 
        userId,
        user: {
          id: userId,
          name: name.trim(),
          email: cleanEmail,
          phone: phone.trim(),
          count: 0,
          role: 'student',
          isAdmin: false,
          createdAt: new Date().toISOString()
        }
      });
    }

    // 2. Cloud Fallback (on Vercel when MONGODB_URI is not set)
    const existing = fallbackUsers.find(u => u.email === cleanEmail);
    if (existing) {
      return res.status(400).json({ error: 'User already registered with this email' });
    }

    const hashedPassword = await bcrypt.hash(password, 10);
    const newUser = {
      _id: 'usr_' + userId,
      id: userId,
      name: name.trim(),
      email: cleanEmail,
      phone: phone.trim(),
      password: hashedPassword,
      count: 0,
      role: 'student',
      isAdmin: false,
      createdAt: new Date(),
      updatedAt: new Date(),
      loginCount: 0
    };

    fallbackUsers.unshift(newUser);
    saveTmpSnapshot();
    console.log(`✅ [Cloud Fallback] New user registered: ${name} (${cleanEmail})`);
    return res.status(200).json({ 
      message: 'User registered successfully', 
      userId,
      user: {
        id: userId,
        name: name.trim(),
        email: cleanEmail,
        phone: phone.trim(),
        count: 0,
        role: 'student',
        isAdmin: false,
        createdAt: new Date().toISOString()
      }
    });
  } catch (err) {
    console.error('❌ Register error:', err);
    res.status(500).json({ error: 'Registration failed', details: err.message });
  }
});

// ✅ Login (Validates against MongoDB or Cloud Fallback)
app.post('/login', async (req, res) => {
  const { email, password } = req.body;

  if (!email || !password) {
    return res.status(400).json({ error: 'Email and password required' });
  }

  const cleanEmail = email.toLowerCase().trim();

  try {
    // 1. If connected to MongoDB (Atlas or local)
    if (mongoose.connection.readyState >= 1) {
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
        console.log(`📝 [MongoDB] Login recorded: ${user.name} (${cleanEmail})`);
      } catch (logErr) {
        console.warn('Login history record warning:', logErr);
      }

      console.log(`✅ [MongoDB] User logged in: ${user.name} (${cleanEmail})`);
      return res.status(200).json({
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
    }

    // 2. Cloud Fallback (on Vercel when MONGODB_URI is not set)
    // Admin Master Login
    if (cleanEmail === 'raghuveer081014@gmail.com' && password === 'password123') {
      fallbackLogins.unshift({
        name: 'Raghu Veer',
        email: cleanEmail,
        phone: '8639118335',
        loginTime: new Date(),
        status: 'SUCCESS',
        device: req.headers['user-agent'] || 'Web Browser'
      });
      saveTmpSnapshot();
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

    // Check registered users in fallback store
    const user = fallbackUsers.find(u => u.email === cleanEmail);
    if (!user) {
      return res.status(401).json({ error: 'Invalid email or password' });
    }

    let isMatch = false;
    if (user.password && (user.password.startsWith('$2b$') || user.password.startsWith('$2a$'))) {
      isMatch = await bcrypt.compare(password, user.password);
    } else {
      isMatch = (user.password === password);
    }

    if (!isMatch) {
      return res.status(401).json({ error: 'Invalid email or password' });
    }

    user.lastLogin = new Date();
    user.loginCount = (user.loginCount || 0) + 1;

    fallbackLogins.unshift({
      name: user.name,
      email: cleanEmail,
      phone: user.phone || '',
      loginTime: new Date(),
      status: 'SUCCESS',
      device: req.headers['user-agent'] || 'Web Browser'
    });
    saveTmpSnapshot();

    console.log(`✅ [Cloud Fallback] User logged in: ${user.name} (${cleanEmail})`);
    return res.status(200).json({
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
    console.error('❌ Login error:', err);
    res.status(500).json({ error: 'Login failed', details: err.message });
  }
});

// ✅ Profile (Fetches from MongoDB or Fallback)
app.get('/profile', async (req, res) => {
  const { email } = req.query;

  if (!email) {
    return res.status(400).json({ error: 'Email is required' });
  }

  const cleanEmail = email.toLowerCase().trim();

  try {
    if (mongoose.connection.readyState >= 1) {
      const user = await User.findOne({ email: cleanEmail });
      if (!user) {
        return res.status(404).json({ error: 'User not found' });
      }
      return res.status(200).json({
        name: user.name,
        email: user.email,
        phone: user.phone,
        count: user.count,
        role: user.role || (cleanEmail === 'raghuveer081014@gmail.com' ? 'admin' : 'student'),
        isAdmin: user.isAdmin || (cleanEmail === 'raghuveer081014@gmail.com')
      });
    }

    const user = fallbackUsers.find(u => u.email === cleanEmail);
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
    res.status(500).json({ error: 'Profile error', details: err.message });
  }
});

// ✅ Update Count / Points (Updates in MongoDB or Fallback)
app.post('/update-count', async (req, res) => {
  const { email, increment } = req.body;

  if (!email || increment === undefined) {
    return res.status(400).json({ error: 'Email and increment are required' });
  }

  const cleanEmail = email.toLowerCase().trim();

  try {
    if (mongoose.connection.readyState >= 1) {
      const updated = await User.findOneAndUpdate(
        { email: cleanEmail },
        { $inc: { count: Number(increment) }, updatedAt: new Date() },
        { new: true }
      );

      if (!updated) {
        return res.status(404).json({ error: 'User not found' });
      }

      console.log(`⭐ [MongoDB] Points updated for ${cleanEmail}: +${increment} (Total: ${updated.count})`);
      return res.status(200).json({ message: 'Count updated successfully', count: updated.count });
    }

    const user = fallbackUsers.find(u => u.email === cleanEmail);
    if (!user) {
      return res.status(404).json({ error: 'User not found' });
    }

    user.count = (user.count || 0) + Number(increment);
    console.log(`⭐ [Cloud Fallback] Points updated for ${cleanEmail}: +${increment} (Total: ${user.count})`);
    return res.status(200).json({ message: 'Count updated successfully', count: user.count });
  } catch (err) {
    console.error('❌ Update Count error:', err);
    res.status(500).json({ error: 'Database error', details: err.message });
  }
});

// ✅ View all registered users (for database inspection)
app.get('/api/users', async (req, res) => {
  try {
    if (mongoose.connection.readyState >= 1) {
      const users = await User.find({}, { password: 0 }).sort({ createdAt: -1 });
      return res.status(200).json({
        database: 'skillplay_db (MongoDB Live)',
        collection: 'users',
        total: users.length,
        users
      });
    }

    // Dynamic Cloud Fallback (includes all newly registered users!)
    loadTmpSnapshot();
    res.status(200).json({
      database: 'skillplay_db (Cloud Active)',
      collection: 'users',
      total: fallbackUsers.length,
      users: fallbackUsers.map(u => ({ ...u, password: '[PROTECTED]' }))
    });
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
        database: 'skillplay_db (MongoDB Live)',
        collection: 'loginhistories',
        total: logs.length,
        logins: logs
      });
    }

    // Dynamic Cloud Fallback
    loadTmpSnapshot();
    res.status(200).json({
      database: 'skillplay_db (Cloud Active)',
      collection: 'loginhistories',
      total: fallbackLogins.length,
      logins: fallbackLogins
    });
  } catch (err) {
    res.status(500).json({ error: 'Database error', details: err.message });
  }
});

// ✅ Sync Users from Client to Cloud Memory
app.post('/api/sync-users', async (req, res) => {
  const { users } = req.body;
  if (!Array.isArray(users)) {
    return res.status(400).json({ error: 'Users array required' });
  }

  let addedCount = 0;
  for (const u of users) {
    if (!u.email) continue;
    const cleanEmail = u.email.toLowerCase().trim();

    // 1. If connected to MongoDB, persist there too
    if (mongoose.connection.readyState >= 1) {
      try {
        const exists = await User.findOne({ email: cleanEmail });
        if (!exists) {
          const hashedPassword = u.password && (u.password.startsWith('$2b$') || u.password.startsWith('$2a$'))
            ? u.password 
            : await bcrypt.hash(u.password || 'password123', 10);
          await User.create({
            id: u.id || generateUniqueId(),
            name: u.name || cleanEmail.split('@')[0],
            email: cleanEmail,
            phone: u.phone || '',
            password: hashedPassword,
            count: u.count || 0,
            role: u.role || (cleanEmail === 'raghuveer081014@gmail.com' ? 'admin' : 'student'),
            isAdmin: u.isAdmin || cleanEmail === 'raghuveer081014@gmail.com',
            createdAt: u.createdAt || new Date(),
            lastLogin: u.lastLogin || null
          });
          addedCount++;
        }
      } catch (err) {
        console.warn('Sync to MongoDB warning:', err.message);
      }
    }

    // 2. Add / Update in fallbackUsers
    const idx = fallbackUsers.findIndex(fu => fu.email === cleanEmail);
    if (idx === -1) {
      fallbackUsers.unshift({
        _id: u._id || 'usr_' + (u.id || generateUniqueId()),
        id: u.id || generateUniqueId(),
        name: u.name || cleanEmail.split('@')[0],
        email: cleanEmail,
        phone: u.phone || '',
        password: u.password || '$2b$10$ORSM0H0VZlDLxbFiAbXreeEPr9JLklV2uDXqZe1dlk2F7VjUe7diK',
        count: u.count || 0,
        role: u.role || (cleanEmail === 'raghuveer081014@gmail.com' ? 'admin' : 'student'),
        isAdmin: u.isAdmin || cleanEmail === 'raghuveer081014@gmail.com',
        createdAt: u.createdAt || new Date(),
        updatedAt: u.updatedAt || new Date(),
        lastLogin: u.lastLogin || null,
        loginCount: u.loginCount || 1
      });
      addedCount++;
    } else {
      if (u.count !== undefined && u.count > (fallbackUsers[idx].count || 0)) {
        fallbackUsers[idx].count = u.count;
      }
      if (u.lastLogin) {
        fallbackUsers[idx].lastLogin = u.lastLogin;
      }
    }
  }

  saveTmpSnapshot();
  res.status(200).json({ success: true, added: addedCount, total: fallbackUsers.length });
});

// ✅ Sync Logins from Client
app.post('/api/sync-logins', async (req, res) => {
  const { logins } = req.body;
  if (!Array.isArray(logins)) {
    return res.status(400).json({ error: 'Logins array required' });
  }

  for (const l of logins) {
    if (!l.email) continue;
    const cleanEmail = l.email.toLowerCase().trim();
    const exists = fallbackLogins.some(fl => fl.email === cleanEmail && Math.abs(new Date(fl.loginTime) - new Date(l.loginTime)) < 3000);
    if (!exists) {
      fallbackLogins.unshift({
        name: l.name || cleanEmail.split('@')[0],
        email: cleanEmail,
        phone: l.phone || '',
        loginTime: l.loginTime || new Date(),
        status: l.status || 'SUCCESS',
        userAgent: l.userAgent || 'Web Browser'
      });
    }
  }

  saveTmpSnapshot();
  res.status(200).json({ success: true, total: fallbackLogins.length });
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

