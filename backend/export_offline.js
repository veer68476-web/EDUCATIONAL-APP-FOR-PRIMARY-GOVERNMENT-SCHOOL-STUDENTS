const fs = require('fs');
const mongoose = require('./node_modules/mongoose');

async function run() {
  await mongoose.connect('mongodb://localhost:27017/skillplay_db');
  const users = await mongoose.connection.db.collection('users').find().toArray();
  const logins = await mongoose.connection.db.collection('loginhistories').find().sort({ loginTime: -1 }).toArray();

  fs.writeFileSync('D:/skillplay/database_export.json', JSON.stringify({ users, logins, exportedAt: new Date() }, null, 2));

  const userRows = users.map(u => {
    const isAdmin = u.email === 'raghuveer081014@gmail.com' || u.role === 'admin' || u.isAdmin === true;
    const badge = isAdmin ? '<span class="admin-badge"><i class="fa-solid fa-shield-halved"></i> Admin</span>' : '';
    const roleText = isAdmin ? '<strong style="color: #10b981;">Administrator</strong>' : 'Student';
    const dateStr = u.createdAt ? new Date(u.createdAt).toLocaleString() : '10/10/2026';
    return `<tr>
      <td><code>${(u._id || '').toString().slice(-6)}</code></td>
      <td><div class="user-pill"><i class="fa-solid fa-circle-user" style="color: #7c4dff;"></i><strong>${u.name || 'User'}</strong>${badge}</div></td>
      <td><strong style="color: #34d399;">${u.email}</strong></td>
      <td><strong>${u.phone || 'N/A'}</strong></td>
      <td><span class="points-tag">⭐ ${u.points || 0} pts</span></td>
      <td>${roleText}</td>
      <td class="date-tag">${dateStr}</td>
    </tr>`;
  }).join('\n');

  const loginRows = logins.map(l => {
    const dateStr = l.loginTime ? new Date(l.loginTime).toLocaleString() : '10/10/2026';
    return `<tr>
      <td><strong>${l.name || 'User'}</strong></td>
      <td><strong style="color: #34d399;">${l.email}</strong></td>
      <td>${l.phone || 'N/A'}</td>
      <td class="date-tag">${dateStr}</td>
      <td><span class="success-badge"><i class="fa-solid fa-check"></i> SUCCESS</span></td>
      <td>${l.device || 'Web Browser'}</td>
    </tr>`;
  }).join('\n');

  const html = `<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0" />
  <title>SkillPlay - Offline Database Snapshot</title>
  <link rel="preconnect" href="https://fonts.googleapis.com" />
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin />
  <link href="https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@400;500;600;700;800&family=JetBrains+Mono:wght@400;600&display=swap" rel="stylesheet" />
  <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.5.1/css/all.min.css" />
  <style>
    :root { --primary: #582cd1; --primary-light: #7c4dff; --accent-green: #10b981; --accent-amber: #f59e0b; --bg-dark: #0f0c20; --bg-card: #181433; --border: rgba(255, 255, 255, 0.12); --text-main: #f8fafc; --text-muted: #94a3b8; }
    * { box-sizing: border-box; margin: 0; padding: 0; }
    body { font-family: 'Plus Jakarta Sans', sans-serif; background: var(--bg-dark); color: var(--text-main); min-height: 100vh; padding: 32px 20px; }
    .container { max-width: 1140px; margin: 0 auto; }
    .header { display: flex; justify-content: space-between; align-items: center; margin-bottom: 24px; flex-wrap: wrap; gap: 16px; }
    .brand { display: flex; align-items: center; gap: 12px; }
    .brand-icon { width: 48px; height: 48px; border-radius: 12px; background: linear-gradient(135deg, #10b981, #059669); display: flex; align-items: center; justify-content: center; font-size: 24px; color: #fff; box-shadow: 0 0 20px rgba(16, 185, 129, 0.4); }
    .badge-offline { background: rgba(16, 185, 129, 0.15); color: #34d399; border: 1px solid rgba(16, 185, 129, 0.35); padding: 8px 16px; border-radius: 20px; font-size: 13px; font-weight: 700; display: inline-flex; align-items: center; gap: 8px; }
    .info-grid { display: grid; grid-template-columns: repeat(auto-fit, minmax(220px, 1fr)); gap: 16px; margin-bottom: 24px; }
    .info-card { background: var(--bg-card); border: 1px solid var(--border); border-radius: 14px; padding: 18px 20px; }
    .info-card .label { font-size: 12px; color: var(--text-muted); text-transform: uppercase; font-weight: 600; letter-spacing: 0.5px; }
    .info-card .value { font-size: 20px; font-weight: 800; margin-top: 6px; color: #fff; }
    .info-card .value.green { color: #34d399; }
    .card { background: var(--bg-card); border: 1px solid var(--border); border-radius: 16px; padding: 24px; margin-bottom: 24px; box-shadow: 0 10px 30px rgba(0,0,0,0.3); }
    .card-title { display: flex; justify-content: space-between; align-items: center; font-size: 17px; font-weight: 700; margin-bottom: 18px; border-bottom: 1px solid var(--border); padding-bottom: 12px; }
    table { width: 100%; border-collapse: collapse; text-align: left; font-size: 14px; }
    th { background: rgba(255, 255, 255, 0.04); padding: 12px 14px; font-size: 12px; text-transform: uppercase; letter-spacing: 0.5px; color: var(--text-muted); border-bottom: 1px solid var(--border); }
    td { padding: 14px; border-bottom: 1px solid rgba(255, 255, 255, 0.06); vertical-align: middle; }
    tr:hover td { background: rgba(255, 255, 255, 0.02); }
    .admin-badge { background: linear-gradient(135deg, #10b981, #059669); color: white; padding: 3px 8px; border-radius: 6px; font-size: 11px; font-weight: 700; display: inline-flex; align-items: center; gap: 4px; margin-left: 8px; }
    .user-pill { display: flex; align-items: center; gap: 8px; }
    .points-tag { background: rgba(245, 158, 11, 0.15); color: #fbbf24; border: 1px solid rgba(245, 158, 11, 0.3); padding: 3px 8px; border-radius: 8px; font-weight: 700; font-size: 12px; }
    .date-tag { font-family: 'JetBrains Mono', monospace; font-size: 12px; color: var(--text-muted); }
    .success-badge { background: rgba(16, 185, 129, 0.15); color: #34d399; border: 1px solid rgba(16, 185, 129, 0.35); padding: 3px 8px; border-radius: 6px; font-size: 11px; font-weight: 700; display: inline-flex; align-items: center; gap: 4px; }
    code { background: rgba(255, 255, 255, 0.08); padding: 2px 6px; border-radius: 4px; font-family: 'JetBrains Mono', monospace; font-size: 12px; color: #a5b4fc; }
  </style>
</head>
<body>
  <div class="container">
    <div class="header">
      <div class="brand">
        <div class="brand-icon"><i class="fa-solid fa-server"></i></div>
        <div>
          <h1 style="font-size: 22px; font-weight: 800;">SkillPlay Database Viewer (Offline Snapshot)</h1>
          <p style="color: var(--text-muted); font-size: 13px;">Developer: <strong>Raghu Veer</strong> &bull; Email: <strong>raghuveer081014@gmail.com</strong> &bull; Phone: <strong>8639118335</strong></p>
        </div>
      </div>
      <div><span class="badge-offline"><i class="fa-solid fa-circle-check"></i> Always Accessible Offline (No Server Needed)</span></div>
    </div>
    <div class="info-grid">
      <div class="info-card"><div class="label">Database Name</div><div class="value green">skillplay_db</div></div>
      <div class="info-card"><div class="label">MongoDB Windows Service</div><div class="value green">Running 24/7 (Port 27017)</div></div>
      <div class="info-card"><div class="label">Total Registered Accounts</div><div class="value">${users.length} Users</div></div>
      <div class="info-card"><div class="label">App Developer & Admin</div><div class="value green">Raghu Veer</div></div>
    </div>
    <div class="card">
      <div class="card-title"><div><i class="fa-solid fa-users"></i> Registered Accounts (Collection: <code>users</code>)</div></div>
      <div style="overflow-x: auto;"><table><thead><tr><th>User ID</th><th>Full Name</th><th>Email Address</th><th>Mobile Number</th><th>Points</th><th>Role</th><th>Registered On</th></tr></thead><tbody>
        ${userRows}
      </tbody></table></div>
    </div>
    <div class="card">
      <div class="card-title"><div><i class="fa-solid fa-clock-rotate-left"></i> Login Activity Log (Collection: <code>loginhistories</code>)</div></div>
      <div style="overflow-x: auto;"><table><thead><tr><th>User Name</th><th>Login Email</th><th>Mobile Number</th><th>Login Timestamp</th><th>Status</th><th>Device / Browser</th></tr></thead><tbody>
        ${loginRows}
      </tbody></table></div>
    </div>
  </div>
</body>
</html>`;

  fs.writeFileSync('D:/skillplay/offline_database.html', html, 'utf8');
  console.log('SUCCESS');
  process.exit(0);
}

run().catch(console.error);
