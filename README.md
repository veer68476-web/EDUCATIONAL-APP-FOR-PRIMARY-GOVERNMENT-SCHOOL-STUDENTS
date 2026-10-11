# SkillPlay - Educational App for Primary Government School Students

[![Live Production](https://img.shields.io/badge/Live%20Deployment-Vercel-black?logo=vercel)](https://skillplay-ten.vercel.app)
[![GitHub Repository](https://img.shields.io/badge/GitHub-Repository-blue?logo=github)](https://github.com/veer68476-web/EDUCATIONAL-APP-FOR-PRIMARY-GOVERNMENT-SCHOOL-STUDENTS)
[![Node.js Backend](https://img.shields.io/badge/Backend-Node.js%20%7C%20Express-green?logo=node.js)](https://skillplay-ten.vercel.app/api/developer)
[![Database](https://img.shields.io/badge/Database-MongoDB%20Cloud-brightgreen?logo=mongodb)](https://skillplay-ten.vercel.app/database.html)

**SkillPlay** is a gamified, interactive educational platform designed for primary school students. It provides digital curriculum access, interactive puzzles, video lessons, textbook solutions, and automated user management with administrative controls and login tracking.

---

## 🌐 Live Production URL (Worldwide Access)

- **Production App**: 👉 [https://skillplay-ten.vercel.app](https://skillplay-ten.vercel.app)
- **Live Database Viewer**: 👉 [https://skillplay-ten.vercel.app/database.html](https://skillplay-ten.vercel.app/database.html)
- **Developer API**: 👉 [https://skillplay-ten.vercel.app/api/developer](https://skillplay-ten.vercel.app/api/developer)
- **Admin Login Credentials**:
  - **Email**: `raghuveer081014@gmail.com`
  - **Password**: `password123`

---

## 👨‍💻 Developer & Administrator Information

| Property | Details |
| :--- | :--- |
| **Lead Developer** | **Raghu Veer** |
| **Official Email** | [`raghuveer*****@gmail.com`](mailto:raghuveer081014@gmail.com) |
| **Contact Number** | `+91 *******335` |
| **System Role** | **Administrator** (`role: 'admin'`, `isAdmin: true`) |
| **Developer API** | [`https://skillplay-ten.vercel.app/api/developer`](https://skillplay-ten.vercel.app/api/developer) |

---

## 🚀 Quick Verification & Direct Links

### 1. 🌐 Website & Login Portal
- **Live URL**: [https://skillplay-ten.vercel.app](https://skillplay-ten.vercel.app)
- **Local URL**: [http://localhost:3001](http://localhost:3001)
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
│   ├── text/                  # All 24 official textbook PDFs (Class 1 to 6, all subjects)
│   ├── answers/               # Complete solved question papers and model answer guides
│   ├── puzzle_0.jpg to 9.jpg  # Interactive brain puzzle tiles
│   └── first_bg.jpg           # Background visual assets
├── lib/
│   ├── main.dart              # Flutter application entrypoint
│   └── features/
│       ├── class/             # Quiz bank (Classes 1 to 6, over 1,320+ curriculum questions)
│       ├── testbook/          # Dynamic textbook loader for all classes
│       ├── questions/         # Subject-matched solved question paper viewer
│       ├── profile/           # User profile & developer admin views
│       └── home_page.dart     # Main learning navigation
├── offline_database.html      # Standalone offline database viewer
├── database_export.json       # Exported database snapshot
└── README.md                  # Project documentation & verification guide
```

---

## 📚 Curriculum, Textbooks & Question Bank (Classes 1 – 6)

| Class | Available Subjects | Textbooks | Question Papers & Solutions | Interactive Quizzes |
| :--- | :--- | :--- | :--- | :--- |
| **Class 1** | Maths, English, Telugu | Complete PDFs | Lesson-specific solved PDFs (1.pdf–9.pdf, 1-1.pdf–8-2.pdf) | 33 lessons, 210 questions |
| **Class 2** | Maths, English, Telugu | Complete PDFs | Subject-matched solved papers & study guides | 33 lessons, 165 questions |
| **Class 3** | Maths, English, Telugu, EVS | Complete PDFs | Subject-matched solved papers & study guides | 38 lessons, 190 questions |
| **Class 4** | Maths, English, Telugu, EVS | Complete PDFs | Subject-matched solved papers & study guides | 38 lessons, 190 questions |
| **Class 5** | Maths, English, Telugu, EVS | Complete PDFs | Subject-matched solved papers & study guides | 39 lessons, 195 questions |
| **Class 6** | Maths, English, Telugu, Hindi, Science, Social | Complete PDFs | Subject-matched solved papers & study guides | 74 lessons, 370 questions |

- **Total Learning Coverage**: **1,320+ curriculum-aligned questions** covering every lesson in the AP State Board curriculum.
- **Dual Viewer Mode**: Students can toggle between **📄 PDF View** (for full documents & downloads) and **📖 Chapter / Solved Q&A Guide** (for quick mobile-friendly study with key formulas, summaries, and model answers).


---

## 🔒 Security & Data Persistence

- **Password Encryption**: All user passwords are encrypted using `bcrypt` (10 salt rounds) prior to storage in MongoDB.
- **Login Audit Trail**: Every authentication attempt triggers an automated audit entry into the `loginhistories` collection with client user-agent and timestamp.
- **Role-Based Access**: Distinguishes between standard student accounts and system administrators (`role: 'admin'`).

---

## 📜 License & Ownership

Developed by **Raghu Veer** for the **Educational App for Primary Government School Students** project.  
GitHub: [@veer68476-web](https://github.com/veer68476-web)
