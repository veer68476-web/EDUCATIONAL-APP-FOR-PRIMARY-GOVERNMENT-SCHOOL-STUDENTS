const express = require('express');
const bodyParser = require('body-parser');
const cors = require('cors');
const oracledb = require('oracledb');
const bcrypt = require('bcrypt');
const nodemailer = require('nodemailer');
const dbConfig = require('./dbConfig');

process.env.NLS_LANG = 'AMERICAN_AMERICA.AL32UTF8';

const app = express();
app.use(cors());
app.use(bodyParser.json());

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

  let connection;
  try {
    connection = await oracledb.getConnection(dbConfig);
    const result = await connection.execute(
      `SELECT id FROM users WHERE email = :email`,
      { email }
    );

    if (result.rows.length === 0) {
      return res.status(404).json({ error: 'Email not found' });
    }

    const otp = generateOtp();
    otpStore.set(email, otp);

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
  } finally {
    if (connection) await connection.close();
  }
});

// ✅ Verify OTP
app.post('/verify-otp', (req, res) => {
  const { email, otp } = req.body;

  if (!email || !otp) {
    return res.status(400).json({ error: 'Email and OTP required' });
  }

  const storedOtp = otpStore.get(email);
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

  let connection;
  try {
    const hashedPassword = await bcrypt.hash(newPassword, 10);
    connection = await oracledb.getConnection(dbConfig);

    await connection.execute(
      `UPDATE users SET password = :password WHERE email = :email`,
      { password: hashedPassword, email },
      { autoCommit: true }
    );

    otpStore.delete(email);
    res.status(200).json({ message: 'Password reset successful' });
  } catch (err) {
    res.status(500).json({ error: 'Server error', details: err.message });
  } finally {
    if (connection) await connection.close();
  }
});

// ✅ Register
app.post('/register', async (req, res) => {
  const { name, email, phone, password } = req.body;
  const userId = generateUniqueId();

  if (!name || !email || !phone || !password) {
    return res.status(400).json({ error: 'All fields are required' });
  }

  let connection;
  try {
    const hashedPassword = await bcrypt.hash(password, 10);
    connection = await oracledb.getConnection(dbConfig);

    await connection.execute(
      `INSERT INTO users (id, name, email, phone, password, count) 
       VALUES (:id, :name, :email, :phone, :password, :count)`,
      {
        id: userId,
        name,
        email,
        phone,
        password: hashedPassword,
        count: 0
      },
      { autoCommit: true }
    );

    res.status(200).json({ message: 'User registered', userId });
  } catch (err) {
    res.status(500).json({ error: 'Database error', details: err.message });
  } finally {
    if (connection) await connection.close();
  }
});

// ✅ Login
app.post('/login', async (req, res) => {
  const { email, password } = req.body;

  let connection;
  try {
    connection = await oracledb.getConnection(dbConfig);

    const result = await connection.execute(
      `SELECT password FROM users WHERE email = :email`,
      { email }
    );

    if (result.rows.length === 0) {
      return res.status(401).json({ error: 'Invalid email or password' });
    }

    const hashedPassword = result.rows[0][0];
    const isMatch = await bcrypt.compare(password, hashedPassword);

    if (!isMatch) {
      return res.status(401).json({ error: 'Invalid email or password' });
    }

    res.status(200).json({ message: 'Login successful' });
  } catch (err) {
    res.status(500).json({ error: 'Server error', details: err.message });
  } finally {
    if (connection) await connection.close();
  }
});

// ✅ Profile
app.get('/profile', async (req, res) => {
  const { email } = req.query;

  if (!email) {
    return res.status(400).json({ error: 'Email is required' });
  }

  let connection;
  try {
    connection = await oracledb.getConnection(dbConfig);

    const result = await connection.execute(
      `SELECT name, email, phone, count FROM users WHERE email = :email`,
      { email }
    );

    if (result.rows.length === 0) {
      return res.status(404).json({ error: 'User not found' });
    }

    const [name, emailOut, phone, count] = result.rows[0];

    res.status(200).json({
      name,
      email: emailOut,
      phone,
      count
    });
  } catch (err) {
    res.status(500).json({ error: 'Database error', details: err.message });
  } finally {
    if (connection) await connection.close();
  }
});

app.post('/update-count', async (req, res) => {
  const { email, increment } = req.body;
  console.log('📥 Received update-count request:', req.body);

  if (!email || increment === undefined) {
    return res.status(400).json({ error: 'Email and increment are required' });
  }

  let connection;
  try {
    connection = await oracledb.getConnection(dbConfig);

    const binds = {
      inc: Number(increment),
      em: email
    };

    await connection.execute(
      `UPDATE users SET count = count + :inc WHERE email = :em`,
      binds,
      { autoCommit: true }
    );

    res.status(200).json({ message: 'Count updated successfully' });
  } catch (err) {
    console.error('❌ OracleDB error:', err);
    res.status(500).json({ error: 'Database error', details: err.message });
  } finally {
    if (connection) await connection.close();
  }
});

const PORT = process.env.PORT || 3001;
const server = app.listen(PORT, '0.0.0.0', () => {
  console.log(`Server running at http://0.0.0.0:${PORT}`);
});

server.on('error', (err) => {
  if (err.code === 'EADDRINUSE') {
    console.error(`Port ${PORT} is already in use. Set PORT to a different port or free the current one.`);
  } else {
    console.error('Server error:', err);
  }
  process.exit(1);
});