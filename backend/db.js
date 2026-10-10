require('dotenv').config();
const mongoose = require('mongoose');
const path = require('path');
const fs = require('fs');

let mongodInstance = null;

const userSchema = new mongoose.Schema({
  id: { type: Number, required: true, unique: true },
  name: { type: String, required: true },
  email: { type: String, required: true, unique: true, lowercase: true, trim: true },
  phone: { type: String, default: '' },
  password: { type: String, required: true },
  count: { type: Number, default: 0 },
  role: { type: String, default: 'student' },
  isAdmin: { type: Boolean, default: false },
  lastLogin: { type: Date, default: null },
  loginCount: { type: Number, default: 0 },
  createdAt: { type: Date, default: Date.now },
  updatedAt: { type: Date, default: Date.now }
});

const User = mongoose.model('User', userSchema);

const loginHistorySchema = new mongoose.Schema({
  userId: { type: Number },
  name: { type: String, required: true },
  email: { type: String, required: true, lowercase: true, trim: true },
  phone: { type: String, default: '' },
  loginTime: { type: Date, default: Date.now },
  status: { type: String, default: 'SUCCESS' },
  ip: { type: String, default: '' },
  userAgent: { type: String, default: '' }
});

const LoginHistory = mongoose.model('LoginHistory', loginHistorySchema);

async function connectDB() {
  if (mongoose.connection.readyState >= 1) {
    return;
  }

  const customUri = process.env.MONGODB_URI;

  if (customUri) {
    try {
      console.log('Connecting to custom MongoDB URI...');
      await mongoose.connect(customUri, { serverSelectionTimeoutMS: 5000 });
      console.log('Connected to custom MongoDB successfully!');
      return;
    } catch (err) {
      console.error('Failed to connect to custom MongoDB:', err.message);
      return;
    }
  }

  // If running in Vercel serverless environment and MONGODB_URI is not set
  if (process.env.VERCEL) {
    console.warn('Running on Vercel without MONGODB_URI. Add MONGODB_URI in Vercel environment variables for Atlas connection.');
    return;
  }

  // Check if an external MongoDB is already listening on 27017
  const defaultLocalUri = 'mongodb://127.0.0.1:27017/skillplay_db';
  try {
    await mongoose.connect(defaultLocalUri, { serverSelectionTimeoutMS: 1500 });
    console.log('Connected to standalone MongoDB on localhost:27017!');
    return;
  } catch (err) {
    console.log('Starting MongoDB service on port 27017 for MongoDB Compass...');
  }

  // Start embedded persistent MongoDB on port 27017
  try {
    const { MongoMemoryServer } = require('mongodb-memory-server');
    const dbPath = path.resolve(__dirname, '../mongodb_data');
    if (!fs.existsSync(dbPath)) fs.mkdirSync(dbPath, { recursive: true });

    mongodInstance = await MongoMemoryServer.create({
      instance: {
        port: 27017,
        dbPath: dbPath,
        storageEngine: 'wiredTiger',
        dbName: 'skillplay_db'
      }
    });

    const uri = 'mongodb://127.0.0.1:27017/skillplay_db';
    await mongoose.connect(uri);

    console.log('========================================================');
    console.log('🎉 MongoDB Server is running on port 27017!');
    console.log('👉 Open MongoDB Compass and connect to:');
    console.log('   mongodb://localhost:27017');
    console.log('   Database: skillplay_db');
    console.log('   Collection: users');
    console.log('========================================================');
  } catch (err) {
    console.warn('MongoMemoryServer fallback notice:', err.message);
  }
}

module.exports = { connectDB, User, LoginHistory };
