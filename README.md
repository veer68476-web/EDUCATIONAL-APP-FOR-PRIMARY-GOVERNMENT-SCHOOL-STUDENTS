# SkillPlay - Educational App for Primary Government School Students

[![GitHub Repository](https://img.shields.io/badge/GitHub-Repository-blue?logo=github)](https://github.com/veer68476-web/EDUCATIONAL-APP-FOR-PRIMARY-GOVERNMENT-SCHOOL-STUDENTS)
[![Node.js Backend](https://img.shields.io/badge/Backend-Node.js%20%7C%20Express-green?logo=node.js)](http://localhost:3001)
[![Database](https://img.shields.io/badge/Database-MongoDB%2024%2F7-brightgreen?logo=mongodb)](http://localhost:3001/database.html)
[![Flutter](https://img.shields.io/badge/Frontend-Flutter%20%7C%20Web-02569B?logo=flutter)](https://flutter.dev)

**SkillPlay** is a gamified, interactive educational platform designed for primary school students. It provides digital curriculum access, interactive puzzles, video lessons, textbook solutions, and automated user management with administrative controls and login tracking.

---

## 👨‍💻 Developer & Administrator Information

| Property | Details |
| :--- | :--- |
| **Lead Developer** | **Raghu Veer** |
| **Official Email** | [`raghuveer081014@gmail.com`](mailto:raghuveer081014@gmail.com) |
| **Contact Number** | `+91 8639118335` |
| **System Role** | **Administrator** (`role: 'admin'`, `isAdmin: true`) |
| **Developer API** | [`http://localhost:3001/api/developer`](http://localhost:3001/api/developer) |

---

## 🚀 Quick Verification & Direct Links

### 1. 🌐 Website & Login Portal
- **URL**: [http://localhost:3001](http://localhost:3001)
- **Admin Credentials**:
  - **Email**: `raghuveer081014@gmail.com`
  - **Password**: `password123`
- **Features**: Full-screen authentication gate protecting the main dashboard. Shows student and admin details, points, and lesson materials upon login.

### 2. 🛡️ Live Database Viewer
- **URL**: [http://localhost:3001/database.html](http://localhost:3001/database.html)
- **Features**: Real-time view of:
  - **Registered Accounts (`users`)**: Full name, email, phone number, points, and **🛡 ADMIN** badges.
  - **Login Activity Log (`loginhistories`)**: Live timestamps, device details, and success status for every login attempt.

### 3. ⚡ Developer API Endpoint
- **URL**: [http://localhost:3001/api/developer](http://localhost:3001/api/developer)
- Returns structured JSON confirming developer credentials, role, and database connection status.

### 4. 💻 Offline Database Viewer (No Server Needed)
- **File Location**: `D:\skillplay\offline_database.html`
- **Direct Link**: [`file:///D:/skillplay/offline_database.html`](file:///D:/skillplay/offline_database.html)
- **How to Use**: Simply **double-click** `offline_database.html` in Windows File Explorer. It opens instantly in any browser without needing to run Node.js or any terminal command.
- **Data Backup**: `D:\skillplay\database_export.json` provides a complete, raw JSON snapshot of all registered users and login logs.

---

## 🛠️ How to Run the Project

### A. Web Server & Backend (Node.js + MongoDB)

1. Ensure **MongoDB** is running (runs automatically as a Windows background service on port `27017`).
2. Open a terminal in the `backend/` directory:
   ```bash
   cd D:\skillplay\backend
   npm install
   node server.js
   ```
3. Open your browser and navigate to:
   - Web App: [http://localhost:3001](http://localhost:3001)
   - Database Viewer: [http://localhost:3001/database.html](http://localhost:3001/database.html)

---

### B. MongoDB Compass (GUI)

You do **not** need to start the web server to inspect the database in MongoDB Compass:
1. Open **MongoDB Compass**.
2. Connect to: `mongodb://localhost:27017`
3. Select database: **`skillplay_db`**
   - Collection **`users`**: View all registered students and administrators.
   - Collection **`loginhistories`**: View all tracked login events with timestamps.

---

### C. Flutter Mobile Application

1. Open a terminal in the root directory:
   ```bash
   cd D:\skillplay
   flutter pub get
   ```
2. Run on your desired platform:
   ```bash
   # Run on connected Android device / emulator
   flutter run -d android

   # Run on Windows desktop
   flutter run -d windows

   # Run on Chrome
   flutter run -d chrome
   ```

---

## 📂 Project Architecture

```
skillplay/
├── backend/
│   ├── server.js              # Express API server (Auth, Logins, Developer endpoints)
│   ├── db.js                  # Mongoose models (User, LoginHistory)
│   ├── dbConfig.js            # Database configuration
│   ├── export_offline.js      # Offline database export script
│   └── public/                # Web application frontend
│       ├── index.html         # Main dashboard & Auth portal gate
│       ├── database.html      # Live database inspection dashboard
│       ├── app.js             # Client authentication & UI logic
│       ├── style.css          # Glassmorphic dark UI styling
│       └── data/              # Curriculum & quiz question banks
├── assets/
│   ├── answers/               # Textbook solution PDFs (Class 1-5)
│   ├── puzzle_0.jpg to 9.jpg  # Interactive puzzle tiles
│   └── first_bg.jpg           # Background visuals
├── lib/
│   ├── main.dart              # Flutter application entrypoint
│   └── features/
│       ├── profile/           # User profile & developer admin views
│       └── home_page.dart     # Main learning navigation
├── offline_database.html      # Standalone offline database viewer
├── database_export.json       # Exported database snapshot
└── README.md                  # Project documentation & verification guide
```

---

## 🔒 Security & Data Persistence

- **Password Encryption**: All user passwords are encrypted using `bcrypt` (10 salt rounds) prior to storage in MongoDB.
- **Login Audit Trail**: Every authentication attempt triggers an automated audit entry into the `loginhistories` collection with client user-agent and timestamp.
- **Role-Based Access**: Distinguishes between standard student accounts and system administrators (`role: 'admin'`).

---

## 📜 License & Ownership

Developed by **Raghu Veer** for the **Educational App for Primary Government School Students** project.  
GitHub: [@veer68476-web](https://github.com/veer68476-web)
