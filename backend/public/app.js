// State Management
let curriculumData = {};
let lessonUrlsData = {};
let nestedQuizData = {};
let defaultQuizData = {};

let currentClass = 'CLASS 1';
let currentSubject = 'MATHS';
let currentLesson = '';
let currentLessonIndex = 0;
let currentLessonsList = [];

// Quiz State
let activeQuizQuestions = [];
let currentQuizIndex = 0;
let quizScore = 0;

// Game State
let currentLevel = 0; // 0 to 9
let boardSize = 3;
let boardState = [];
let emptyIndex = 8;
let gameMoves = 0;
let gameTimerSeconds = 0;
let gameTimerInterval = null;
let gameStarted = false;

// User / Auth State
let currentUser = null;

// Initialize on DOM Load
document.addEventListener('DOMContentLoaded', async () => {
  await loadAppData();
  loadUserSession();
  setupClassSelectors();
  setupTextbookSelectors();
  setupQuestionSelectors();
  setupGameLevels();
  checkResumeBanner();
  initGame();

  if (window.location.hash === '#register') {
    switchPortalTab('register');
  } else if (window.location.hash === '#forgot') {
    switchPortalTab('forgot');
  } else if (window.location.hash === '#profile') {
    navigateTo('profile');
  }
});

// Load JSON data files
async function loadAppData() {
  try {
    const [currRes, urlRes, nqRes, dqRes] = await Promise.all([
      fetch('/data/curriculum.json').then(r => r.json()),
      fetch('/data/lessonUrls.json').then(r => r.json()),
      fetch('/data/nestedQuizBank.json').then(r => r.json()),
      fetch('/data/defaultQuizBank.json').then(r => r.json()),
    ]);
    curriculumData = currRes;
    lessonUrlsData = urlRes;
    nestedQuizData = nqRes;
    defaultQuizData = dqRes;
  } catch (err) {
    console.warn('Could not load full JSON, falling back:', err);
  }
}

// Navigation between sections
function navigateTo(sectionId) {
  document.querySelectorAll('.page-section').forEach(sec => sec.classList.remove('active'));
  document.querySelectorAll('.nav-btn').forEach(btn => {
    btn.classList.toggle('active', btn.dataset.target === sectionId);
  });

  const targetSec = document.getElementById(`section-${sectionId}`);
  if (targetSec) {
    targetSec.classList.add('active');
    window.scrollTo({ top: 0, behavior: 'smooth' });
  }

  if (sectionId === 'profile') {
    renderProfileView();
  }
}

// Setup Class Selector Pills for Learn Section
function setupClassSelectors() {
  const container = document.getElementById('classSelector');
  if (!container) return;
  container.innerHTML = '';

  const classes = Object.keys(curriculumData).length > 0 
    ? Object.keys(curriculumData) 
    : ['CLASS 1', 'CLASS 2', 'CLASS 3', 'CLASS 4', 'CLASS 5', 'CLASS 6'];

  classes.forEach((cls, idx) => {
    const btn = document.createElement('button');
    btn.className = `pill-btn ${cls === currentClass ? 'active' : ''}`;
    btn.textContent = cls;
    btn.onclick = () => selectClass(cls);
    container.appendChild(btn);
  });

  selectClass(currentClass);
}

function selectClass(cls) {
  currentClass = cls;
  document.querySelectorAll('#classSelector .pill-btn').forEach(b => {
    b.classList.toggle('active', b.textContent === cls);
  });

  const subjects = (curriculumData[cls] && Object.keys(curriculumData[cls])) || ['MATHS', 'ENGLISH', 'TELUGU'];
  if (!subjects.includes(currentSubject)) {
    currentSubject = subjects[0];
  }
  setupSubjectSelectors(subjects);
}

function setupSubjectSelectors(subjects) {
  const container = document.getElementById('subjectSelector');
  if (!container) return;
  container.innerHTML = '';

  subjects.forEach(sub => {
    const btn = document.createElement('button');
    btn.className = `pill-btn ${sub === currentSubject ? 'active' : ''}`;
    btn.textContent = sub;
    btn.onclick = () => selectSubject(sub);
    container.appendChild(btn);
  });

  renderLessons();
}

function selectSubject(sub) {
  currentSubject = sub;
  document.querySelectorAll('#subjectSelector .pill-btn').forEach(b => {
    b.classList.toggle('active', b.textContent === sub);
  });
  renderLessons();
}

// Render Lessons List
function renderLessons() {
  const container = document.getElementById('lessonsContainer');
  const activeView = document.getElementById('activeLessonView');
  if (activeView) activeView.style.display = 'none';
  if (!container) return;

  const lessons = (curriculumData[currentClass] && curriculumData[currentClass][currentSubject]) || [];
  currentLessonsList = lessons;
  container.innerHTML = '';

  if (lessons.length === 0) {
    container.innerHTML = `<p style="grid-column: 1/-1; color: var(--text-muted);">No lessons found for this subject.</p>`;
    return;
  }

  lessons.forEach((lesson, index) => {
    const card = document.createElement('div');
    card.className = 'lesson-card';
    card.onclick = () => openLesson(lesson, index);

    card.innerHTML = `
      <div class="lesson-card-header">
        <div class="lesson-num">${index + 1}</div>
        <h4>${lesson}</h4>
      </div>
      <div class="lesson-card-footer">
        <span><i class="fa-solid fa-circle-play"></i> Video &bull; Quiz</span>
        <span class="card-link"><i class="fa-solid fa-arrow-right"></i></span>
      </div>
    `;
    container.appendChild(card);
  });
}

// Open Active Lesson
function openLesson(lesson, index) {
  currentLesson = lesson;
  currentLessonIndex = index;

  saveLastProgress(currentClass, currentSubject, lesson);

  const container = document.getElementById('lessonsContainer');
  const activeView = document.getElementById('activeLessonView');
  if (container) container.style.display = 'none';
  if (activeView) activeView.style.display = 'block';

  document.getElementById('activeLessonBadge').textContent = `${currentClass} • ${currentSubject}`;
  document.getElementById('activeLessonTitle').textContent = `${index + 1}. ${lesson}`;

  // Hide quiz initially
  const quizCont = document.getElementById('quizContainer');
  if (quizCont) quizCont.style.display = 'none';

  // Find video URL
  let rawUrl = '';
  if (lessonUrlsData[currentClass] && lessonUrlsData[currentClass][currentSubject]) {
    rawUrl = lessonUrlsData[currentClass][currentSubject][lesson] || '';
  }

  const embedUrl = convertToEmbedUrl(rawUrl);
  const iframe = document.getElementById('videoIframe');
  iframe.src = embedUrl;

  activeView.scrollIntoView({ behavior: 'smooth' });
}

function closeActiveLesson() {
  const container = document.getElementById('lessonsContainer');
  const activeView = document.getElementById('activeLessonView');
  const iframe = document.getElementById('videoIframe');
  if (iframe) iframe.src = '';
  if (activeView) activeView.style.display = 'none';
  if (container) container.style.display = 'grid';
}

function prevLesson() {
  if (currentLessonIndex > 0) {
    openLesson(currentLessonsList[currentLessonIndex - 1], currentLessonIndex - 1);
  }
}

function nextLesson() {
  if (currentLessonIndex < currentLessonsList.length - 1) {
    openLesson(currentLessonsList[currentLessonIndex + 1], currentLessonIndex + 1);
  }
}

function convertToEmbedUrl(url) {
  if (!url) return 'https://www.youtube.com/embed/dQw4w9WgXcQ';
  try {
    if (url.includes('youtu.be/')) {
      const id = url.split('youtu.be/')[1].split('?')[0];
      return `https://www.youtube.com/embed/${id}?autoplay=1`;
    }
    if (url.includes('youtube.com/watch')) {
      const urlObj = new URL(url);
      const v = urlObj.searchParams.get('v');
      return `https://www.youtube.com/embed/${v}?autoplay=1`;
    }
    if (url.includes('youtube.com/playlist')) {
      const urlObj = new URL(url);
      const list = urlObj.searchParams.get('list');
      return `https://www.youtube.com/embed/videoseries?list=${list}`;
    }
  } catch (e) {}
  return url;
}

// Quiz System
function openQuiz() {
  const quizCont = document.getElementById('quizContainer');
  if (!quizCont) return;
  quizCont.style.display = 'block';

  let questions = [];
  if (nestedQuizData[currentClass] && nestedQuizData[currentClass][currentSubject]) {
    questions = nestedQuizData[currentClass][currentSubject][currentLesson] || [];
  }
  if (!questions || questions.length === 0) {
    questions = (defaultQuizData && defaultQuizData[currentSubject]) || [
      {
        id: 1,
        question: `What is the key takeaway of ${currentLesson}?`,
        options: ['Core concept understanding', 'Memorization only', 'Skip questions', 'None of these'],
        answer: 0
      },
      {
        id: 2,
        question: `Which fundamental principle applies to ${currentSubject}?`,
        options: ['Consistent daily practice', 'Random guessing', 'Never reviewing', 'Ignoring formulas'],
        answer: 0
      }
    ];
  }

  activeQuizQuestions = questions;
  currentQuizIndex = 0;
  quizScore = 0;
  renderQuizQuestion();
  quizCont.scrollIntoView({ behavior: 'smooth' });
}

function renderQuizQuestion() {
  const body = document.getElementById('quizBody');
  const progressText = document.getElementById('quizProgressText');
  const progressFill = document.getElementById('quizProgressFill');

  if (currentQuizIndex >= activeQuizQuestions.length) {
    // Finished Quiz!
    const pct = Math.round((quizScore / activeQuizQuestions.length) * 100);
    const earnedPoints = quizScore * 10;
    awardPoints(earnedPoints);
    incrementUserStats('quizzes');

    body.innerHTML = `
      <div class="quiz-score-banner">
        <div class="quiz-score-circle">${pct}%</div>
        <h3>Quiz Completed!</h3>
        <p>You answered <strong>${quizScore}</strong> of <strong>${activeQuizQuestions.length}</strong> questions correctly!</p>
        <p style="color: #34d399; font-weight: 700; margin: 12px 0;">+${earnedPoints} Learning Points Added to Profile</p>
        <button class="btn btn-primary" onclick="openQuiz()">Retake Quiz</button>
      </div>
    `;
    progressFill.style.width = '100%';
    progressText.textContent = 'Completed!';
    return;
  }

  const q = activeQuizQuestions[currentQuizIndex];
  const total = activeQuizQuestions.length;
  progressText.textContent = `Question ${currentQuizIndex + 1} of ${total}`;
  progressFill.style.width = `${((currentQuizIndex + 1) / total) * 100}%`;

  let optionsHtml = '';
  q.options.forEach((opt, idx) => {
    optionsHtml += `
      <button class="quiz-option-btn" onclick="selectQuizAnswer(${idx}, ${q.answer})">
        <span style="font-weight:700; color: #a78bfa;">${String.fromCharCode(65 + idx)}.</span>
        <span>${opt}</span>
      </button>
    `;
  });

  body.innerHTML = `
    <h4 class="quiz-question-title">${q.id || currentQuizIndex + 1}. ${q.question}</h4>
    <div class="quiz-options">${optionsHtml}</div>
  `;
}

function selectQuizAnswer(selectedIdx, correctIdx) {
  const buttons = document.querySelectorAll('.quiz-option-btn');
  buttons.forEach((btn, idx) => {
    btn.disabled = true;
    if (idx === correctIdx) {
      btn.classList.add('correct');
    } else if (idx === selectedIdx) {
      btn.classList.add('wrong');
    }
  });

  if (selectedIdx === correctIdx) {
    quizScore++;
  }

  setTimeout(() => {
    currentQuizIndex++;
    renderQuizQuestion();
  }, 1200);
}

// Dynamic Textbook Mapping
const textbookMap = {
  'CLASS 1': {
    'MATHS': '/assets/text/class1/maths.pdf',
    'ENGLISH': '/assets/text/class1/english.pdf',
    'TELUGU': '/assets/text/class1/telugu.pdf',
  },
  'CLASS 2': {
    'MATHS': '/assets/text/class2/maths.pdf',
    'ENGLISH': '/assets/text/class2/english.pdf',
    'TELUGU': '/assets/text/class2/telugu.pdf',
  },
  'CLASS 3': {
    'MATHS': '/assets/text/class3/maths.pdf',
    'ENGLISH': '/assets/text/class3/english.pdf',
    'TELUGU': '/assets/text/class3/telugu.pdf',
    'EVS': '/assets/text/class3/evs.pdf',
  },
  'CLASS 4': {
    'MATHS': '/assets/text/class4/maths.pdf',
    'ENGLISH': '/assets/text/class4/english.pdf',
    'TELUGU': '/assets/text/class4/telugu.pdf',
    'EVS': '/assets/text/class4/evs.pdf',
  },
  'CLASS 5': {
    'MATHS': '/assets/text/class5/maths.pdf',
    'ENGLISH': '/assets/text/class5/english.pdf',
    'TELUGU': '/assets/text/class5/telugu.pdf',
    'EVS': '/assets/text/class5/evs.pdf',
  },
  'CLASS 6': {
    'MATHS': '/assets/text/class6/maths.pdf',
    'ENGLISH': '/assets/text/class6/english.pdf',
    'TELUGU': '/assets/text/class6/telugu.pdf',
    'HINDI': '/assets/text/class6/hindi.pdf',
    'SCIENCE': '/assets/text/class6/science.pdf',
    'SOCIAL': '/assets/text/class6/social.pdf',
  }
};

let tbCurrentClass = 'CLASS 1';
let tbCurrentSubject = 'MATHS';

// Textbooks Setup
function setupTextbookSelectors() {
  const classCont = document.getElementById('tbClassSelector');
  if (!classCont) return;

  const classes = Object.keys(textbookMap);
  classCont.innerHTML = '';
  classes.forEach((c) => {
    const b = document.createElement('button');
    b.className = `pill-btn ${c === tbCurrentClass ? 'active' : ''}`;
    b.textContent = c;
    b.onclick = () => selectTbClass(c);
    classCont.appendChild(b);
  });

  selectTbClass(tbCurrentClass);
}

function selectTbClass(cls) {
  tbCurrentClass = cls;
  document.querySelectorAll('#tbClassSelector .pill-btn').forEach(btn => {
    btn.classList.toggle('active', btn.textContent === cls);
  });

  const availableSubjects = Object.keys(textbookMap[cls] || {});
  if (!availableSubjects.includes(tbCurrentSubject)) {
    tbCurrentSubject = availableSubjects[0] || 'MATHS';
  }

  const subCont = document.getElementById('tbSubjectSelector');
  if (!subCont) return;
  subCont.innerHTML = '';

  availableSubjects.forEach(s => {
    const b = document.createElement('button');
    b.className = `pill-btn ${s === tbCurrentSubject ? 'active' : ''}`;
    b.textContent = s;
    b.onclick = () => selectTbSubject(s);
    subCont.appendChild(b);
  });

  updateTbTextbook();
}

function selectTbSubject(sub) {
  tbCurrentSubject = sub;
  document.querySelectorAll('#tbSubjectSelector .pill-btn').forEach(btn => {
    btn.classList.toggle('active', btn.textContent === sub);
  });
  updateTbTextbook();
}

let tbViewMode = 'pdf';

function switchTbMode(mode) {
  tbViewMode = mode;
  const pdfWrapper = document.getElementById('tbPdfWrapper');
  const guideWrapper = document.getElementById('tbGuideWrapper');
  const btnPdf = document.getElementById('tbBtnPdf');
  const btnGuide = document.getElementById('tbBtnGuide');

  if (mode === 'pdf') {
    if (pdfWrapper) pdfWrapper.style.display = 'block';
    if (guideWrapper) guideWrapper.style.display = 'none';
    if (btnPdf) btnPdf.classList.add('active');
    if (btnGuide) btnGuide.classList.remove('active');
  } else {
    if (pdfWrapper) pdfWrapper.style.display = 'none';
    if (guideWrapper) guideWrapper.style.display = 'block';
    if (btnPdf) btnPdf.classList.remove('active');
    if (btnGuide) btnGuide.classList.add('active');
    renderTbGuide();
  }
}

function renderTbGuide() {
  const guideWrapper = document.getElementById('tbGuideWrapper');
  if (!guideWrapper) return;

  const lessons = (curriculumData[tbCurrentClass] && curriculumData[tbCurrentClass][tbCurrentSubject]) || [];
  
  let html = `
    <div class="guide-header-box">
      <div class="guide-header-title">
        <i class="fa-solid fa-book"></i> ${tbCurrentClass} &bull; ${tbCurrentSubject} Curriculum & Study Guide
      </div>
      <span class="badge">${lessons.length} Chapters</span>
    </div>
    <div class="guide-chapter-grid">
  `;

  lessons.forEach((les, idx) => {
    const escapedLes = les.replace(/'/g, "\\'");
    html += `
      <div class="guide-chapter-card">
        <span class="chapter-badge">Chapter ${idx + 1}</span>
        <h4 class="chapter-card-title">${les}</h4>
        <div class="chapter-card-actions">
          <button class="btn btn-sm btn-outline" onclick="goToQuestionLesson('${tbCurrentClass}', '${tbCurrentSubject}', ${idx})">
            <i class="fa-solid fa-file-circle-question"></i> Solved Papers
          </button>
          <button class="btn btn-sm btn-primary" onclick="goToLearnQuiz('${tbCurrentClass}', '${tbCurrentSubject}', '${escapedLes}')">
            <i class="fa-solid fa-circle-question"></i> Take Quiz
          </button>
        </div>
      </div>
    `;
  });

  html += `</div>`;
  guideWrapper.innerHTML = html;
}

function goToQuestionLesson(cls, subj, lessonIdx) {
  switchTab('questions');
  selectQClass(cls);
  selectQSubject(subj);
  setTimeout(() => {
    const lessonButtons = document.querySelectorAll('#qLessonSelector .pill-btn');
    if (lessonButtons[lessonIdx]) {
      lessonButtons[lessonIdx].click();
    }
  }, 100);
}

function goToLearnQuiz(cls, subj, lessonName) {
  switchTab('learn');
  selectClass(cls);
  selectSubject(subj);
  setTimeout(() => {
    selectLesson(lessonName);
  }, 100);
}

function updateTbTextbook() {
  const isLocal = window.location.hostname === 'localhost' || window.location.hostname === '127.0.0.1';
  const pdfUrl = (textbookMap[tbCurrentClass] && textbookMap[tbCurrentClass][tbCurrentSubject]) || '/assets/one.pdf';
  const iframe = document.getElementById('tbPdfIframe');
  const titleEl = document.getElementById('tbCurrentTitle');
  const downloadBtn = document.getElementById('tbDownloadBtn');
  const fullscreenBtn = document.getElementById('tbFullscreenBtn');
  const spinner = document.getElementById('tbLoadingSpinner');
  const cloudCard = document.getElementById('tbCloudNoticeCard');
  const cloudTitle = document.getElementById('tbCloudCardTitle');

  if (titleEl) {
    titleEl.innerHTML = `<i class="fa-solid fa-file-pdf"></i> ${tbCurrentClass} &bull; ${tbCurrentSubject} Textbook`;
  }

  const officialSubjectSearch = `https://diksha.gov.in/explore?channel=01246736412128870417&subject=${encodeURIComponent(tbCurrentSubject)}`;

  if (downloadBtn) {
    if (isLocal) {
      downloadBtn.href = pdfUrl;
      downloadBtn.setAttribute('download', `${tbCurrentClass.replace(' ', '_')}_${tbCurrentSubject}_Textbook.pdf`);
      downloadBtn.innerHTML = `<i class="fa-solid fa-download"></i> Download Textbook`;
    } else {
      downloadBtn.href = officialSubjectSearch;
      downloadBtn.target = '_blank';
      downloadBtn.removeAttribute('download');
      downloadBtn.innerHTML = `<i class="fa-solid fa-book-open-reader"></i> AP Board Digital Book`;
    }
  }

  if (fullscreenBtn) {
    fullscreenBtn.href = isLocal ? pdfUrl : officialSubjectSearch;
    fullscreenBtn.target = '_blank';
  }

  if (cloudTitle) {
    cloudTitle.textContent = `${tbCurrentClass} • ${tbCurrentSubject} Textbook`;
  }

  // Handle cloud vs local: never show 404 iframe on Vercel
  if (!isLocal) {
    if (iframe) iframe.style.display = 'none';
    if (cloudCard) cloudCard.style.display = 'flex';
    if (spinner) spinner.style.display = 'none';
  } else {
    if (cloudCard) cloudCard.style.display = 'none';
    if (iframe) {
      iframe.style.display = 'block';
      if (spinner) spinner.style.display = 'flex';
      iframe.onload = () => {
        if (spinner) spinner.style.display = 'none';
      };
      iframe.src = `${pdfUrl}#toolbar=1`;
    }
  }

  renderTbGuide();

  setTimeout(() => {
    if (spinner) spinner.style.display = 'none';
  }, 1200);
}

// Question Papers & Solutions Setup
let qCurrentClass = 'CLASS 1';
let qCurrentSubject = 'MATHS';
let qCurrentLessonIdx = 0;

function setupQuestionSelectors() {
  const classCont = document.getElementById('qClassSelector');
  if (!classCont) return;

  const classes = ['CLASS 1', 'CLASS 2', 'CLASS 3', 'CLASS 4', 'CLASS 5', 'CLASS 6'];
  classCont.innerHTML = '';
  classes.forEach(c => {
    const b = document.createElement('button');
    b.className = `pill-btn ${c === qCurrentClass ? 'active' : ''}`;
    b.textContent = c;
    b.onclick = () => selectQClass(c);
    classCont.appendChild(b);
  });

  selectQClass(qCurrentClass);
}

function selectQClass(cls) {
  qCurrentClass = cls;
  document.querySelectorAll('#qClassSelector .pill-btn').forEach(b => {
    b.classList.toggle('active', b.textContent === cls);
  });

  const subjects = (curriculumData[cls] && Object.keys(curriculumData[cls])) || ['MATHS', 'ENGLISH', 'TELUGU'];
  if (!subjects.includes(qCurrentSubject)) {
    qCurrentSubject = subjects[0];
  }

  const subCont = document.getElementById('qSubjectSelector');
  if (subCont) {
    subCont.innerHTML = '';
    subjects.forEach(s => {
      const b = document.createElement('button');
      b.className = `pill-btn ${s === qCurrentSubject ? 'active' : ''}`;
      b.textContent = s;
      b.onclick = () => selectQSubject(s);
      subCont.appendChild(b);
    });
  }

  renderQLessons();
  updateQQuestionPaper();
}

function selectQSubject(sub) {
  qCurrentSubject = sub;
  document.querySelectorAll('#qSubjectSelector .pill-btn').forEach(b => {
    b.classList.toggle('active', b.textContent === sub);
  });
  renderQLessons();
  updateQQuestionPaper();
}

function renderQLessons() {
  const group = document.getElementById('qLessonGroup');
  const container = document.getElementById('qLessonSelector');
  if (!container || !group) return;

  const lessons = (curriculumData[qCurrentClass] && curriculumData[qCurrentClass][qCurrentSubject]) || [];
  if (lessons.length === 0) {
    group.style.display = 'none';
    return;
  }

  group.style.display = 'flex';
  container.innerHTML = '';
  qCurrentLessonIdx = 0;

  lessons.forEach((les, idx) => {
    const b = document.createElement('button');
    b.className = `pill-btn ${idx === 0 ? 'active' : ''}`;
    b.textContent = `Lesson ${idx + 1}`;
    b.title = les;
    b.onclick = () => {
      qCurrentLessonIdx = idx;
      document.querySelectorAll('#qLessonSelector .pill-btn').forEach(btn => btn.classList.remove('active'));
      b.classList.add('active');
      updateQQuestionPaper();
    };
    container.appendChild(b);
  });
}

let qViewMode = 'pdf';

function switchQMode(mode) {
  qViewMode = mode;
  const pdfWrapper = document.getElementById('qPdfWrapper');
  const guideWrapper = document.getElementById('qGuideWrapper');
  const btnPdf = document.getElementById('qBtnPdf');
  const btnGuide = document.getElementById('qBtnGuide');

  if (mode === 'pdf') {
    if (pdfWrapper) pdfWrapper.style.display = 'block';
    if (guideWrapper) guideWrapper.style.display = 'none';
    if (btnPdf) btnPdf.classList.add('active');
    if (btnGuide) btnGuide.classList.remove('active');
  } else {
    if (pdfWrapper) pdfWrapper.style.display = 'none';
    if (guideWrapper) guideWrapper.style.display = 'block';
    if (btnPdf) btnPdf.classList.remove('active');
    if (btnGuide) btnGuide.classList.add('active');
    renderQGuide();
  }
}

function renderQGuide() {
  const guideWrapper = document.getElementById('qGuideWrapper');
  if (!guideWrapper) return;

  const lessons = (curriculumData[qCurrentClass] && curriculumData[qCurrentClass][qCurrentSubject]) || [];
  const currentLessonName = lessons[qCurrentLessonIdx] || `Lesson ${qCurrentLessonIdx + 1}`;
  
  let questions = [];
  if (nestedQuizData && nestedQuizData[qCurrentClass] && nestedQuizData[qCurrentClass][qCurrentSubject]) {
    questions = nestedQuizData[qCurrentClass][qCurrentSubject][currentLessonName] || [];
  }

  const escapedLesson = currentLessonName.replace(/'/g, "\\'");

  let html = `
    <div class="guide-header-box">
      <div>
        <div class="guide-header-title">
          <i class="fa-solid fa-clipboard-check"></i> ${qCurrentClass} &bull; ${qCurrentSubject} &bull; ${currentLessonName}
        </div>
        <p style="margin: 4px 0 0 0; font-size: 13px; color: var(--text-muted);">
          Official curriculum model questions, key concepts, and verified solutions.
        </p>
      </div>
      <button class="btn btn-sm btn-primary" onclick="goToLearnQuiz('${qCurrentClass}', '${qCurrentSubject}', '${escapedLesson}')">
        <i class="fa-solid fa-play"></i> Practice Quiz
      </button>
    </div>
    <div class="qa-guide-container">
  `;

  if (questions.length > 0) {
    questions.forEach((item, idx) => {
      const correctText = item.options[item.answer] || 'Solution Verified';
      html += `
        <div class="qa-card-item">
          <h4 class="qa-question-title">
            <span class="badge">Q${idx + 1}</span>
            <span>${item.question}</span>
          </h4>
          <div class="qa-options-grid">
            ${item.options.map((opt, optIdx) => `
              <div class="qa-option-pill ${optIdx === item.answer ? 'correct' : ''}">
                <strong>${String.fromCharCode(65 + optIdx)}.</strong> ${opt}
                ${optIdx === item.answer ? ' <i class="fa-solid fa-circle-check"></i>' : ''}
              </div>
            `).join('')}
          </div>
          <div class="qa-solution-box">
            <strong><i class="fa-solid fa-lightbulb"></i> Correct Answer:</strong> Option ${String.fromCharCode(65 + item.answer)} (${correctText})
          </div>
        </div>
      `;
    });
  } else {
    html += `
      <div class="empty-state">
        <i class="fa-solid fa-file-lines"></i>
        <h3>Solution Guide</h3>
        <p>Comprehensive question paper for this chapter is available in PDF view or via direct download.</p>
      </div>
    `;
  }

  html += `</div>`;
  guideWrapper.innerHTML = html;
}

function updateQQuestionPaper() {
  let paperUrl = `/assets/answers/class_1/default/11.pdf`;

  if (qCurrentClass === 'CLASS 1') {
    if (qCurrentSubject === 'MATHS') {
      const num = Math.min(Math.max(qCurrentLessonIdx + 1, 1), 9);
      paperUrl = `/assets/answers/class_1/maths/${num}.pdf`;
    } else if (qCurrentSubject === 'TELUGU') {
      const num = Math.min(Math.max(qCurrentLessonIdx + 1, 1), 9);
      paperUrl = `/assets/answers/class_1/telugu/${num}.pdf`;
    } else if (qCurrentSubject === 'ENGLISH') {
      const englishFiles = ['1-1.pdf', '1-2.pdf', '2.pdf', '3-1.pdf', '3-2.pdf', '4-1.pdf', '4-2.pdf', '5-1.pdf', '5-2.pdf', '6-1.pdf', '6-2.pdf', '7-1.pdf', '7-2.pdf', '8-1.pdf', '8-2.pdf'];
      const file = englishFiles[qCurrentLessonIdx % englishFiles.length];
      paperUrl = `/assets/answers/class_1/english/${file}`;
    }
  } else {
    // Correctly matched by subject across all classes
    if (qCurrentSubject === 'TELUGU') {
      const num = (qCurrentLessonIdx % 9) + 1;
      paperUrl = `/assets/answers/class_1/telugu/${num}.pdf`;
    } else if (qCurrentSubject === 'MATHS') {
      paperUrl = `/assets/answers/class_1/default/31.pdf`;
    } else if (qCurrentSubject === 'ENGLISH') {
      paperUrl = `/assets/answers/class_1/default/21.pdf`;
    } else if (qCurrentSubject === 'EVS' || qCurrentSubject === 'SCIENCE') {
      paperUrl = `/assets/answers/class_1/default/11.pdf`;
    } else if (qCurrentSubject === 'SOCIAL') {
      paperUrl = `/assets/answers/class_1/default/41.pdf`;
    } else if (qCurrentSubject === 'HINDI') {
      paperUrl = `/assets/answers/class_1/default/61.pdf`;
    } else {
      paperUrl = `/assets/answers/class_1/default/11.pdf`;
    }
  }

  const iframe = document.getElementById('qPdfIframe');
  const titleEl = document.getElementById('qCurrentTitle');
  const downloadBtn = document.getElementById('qDownloadBtn');
  const fullscreenBtn = document.getElementById('qFullscreenBtn');
  const spinner = document.getElementById('qLoadingSpinner');

  if (titleEl) {
    titleEl.innerHTML = `<i class="fa-solid fa-file-pdf"></i> ${qCurrentClass} &bull; ${qCurrentSubject} &bull; Lesson ${qCurrentLessonIdx + 1} Solution`;
  }

  if (downloadBtn) {
    downloadBtn.href = paperUrl;
    downloadBtn.setAttribute('download', `${qCurrentClass.replace(' ', '_')}_${qCurrentSubject}_Lesson${qCurrentLessonIdx + 1}_Solution.pdf`);
  }

  if (fullscreenBtn) {
    fullscreenBtn.href = paperUrl;
  }

  if (spinner) spinner.style.display = 'flex';

  if (iframe) {
    iframe.onload = () => {
      if (spinner) spinner.style.display = 'none';
    };
    iframe.src = `${paperUrl}#toolbar=1`;
  }

  renderQGuide();

  setTimeout(() => {
    if (spinner) spinner.style.display = 'none';
  }, 1500);
}

// Puzzle Game Logic
function setupGameLevels() {
  const container = document.getElementById('gameLevelPills');
  if (!container) return;
  container.innerHTML = '';

  for (let i = 0; i < 10; i++) {
    const btn = document.createElement('button');
    btn.className = `level-btn ${i === currentLevel ? 'active' : ''}`;
    btn.textContent = i + 1;
    btn.onclick = () => selectGameLevel(i);
    container.appendChild(btn);
  }
}

function selectGameLevel(level) {
  currentLevel = level;
  document.querySelectorAll('#gameLevelPills .level-btn').forEach((b, idx) => {
    b.classList.toggle('active', idx === level);
  });
  document.getElementById('previewImage').src = `/assets/puzzle_${level}.jpg`;
  initGame();
}

function initGame() {
  clearInterval(gameTimerInterval);
  gameMoves = 0;
  gameTimerSeconds = 0;
  gameStarted = false;
  document.getElementById('gameMoves').textContent = '0';
  document.getElementById('gameTimer').textContent = '00:00';

  const totalTiles = boardSize * boardSize;
  boardState = [];
  for (let i = 0; i < totalTiles; i++) {
    boardState.push(i);
  }
  emptyIndex = totalTiles - 1;

  // Shuffle with guaranteed solvability by performing random valid moves
  for (let s = 0; s < 70; s++) {
    const neighbors = getNeighbors(emptyIndex);
    const randNeighbor = neighbors[Math.floor(Math.random() * neighbors.length)];
    // swap
    boardState[emptyIndex] = boardState[randNeighbor];
    boardState[randNeighbor] = totalTiles - 1;
    emptyIndex = randNeighbor;
  }

  renderGameBoard();
}

function getNeighbors(index) {
  const row = Math.floor(index / boardSize);
  const col = index % boardSize;
  const neighbors = [];

  if (row > 0) neighbors.push(index - boardSize); // Up
  if (row < boardSize - 1) neighbors.push(index + boardSize); // Down
  if (col > 0) neighbors.push(index - 1); // Left
  if (col < boardSize - 1) neighbors.push(index + 1); // Right

  return neighbors;
}

function renderGameBoard() {
  const board = document.getElementById('puzzleBoard');
  if (!board) return;
  board.innerHTML = '';

  const totalTiles = boardSize * boardSize;
  const imgUrl = `/assets/puzzle_${currentLevel}.jpg`;

  boardState.forEach((val, idx) => {
    const tile = document.createElement('div');
    tile.className = 'puzzle-tile';

    if (val === totalTiles - 1) {
      tile.classList.add('empty');
    } else {
      tile.style.backgroundImage = `url('${imgUrl}')`;
      const origRow = Math.floor(val / boardSize);
      const origCol = val % boardSize;
      const xPercent = (origCol / (boardSize - 1)) * 100;
      const yPercent = (origRow / (boardSize - 1)) * 100;
      tile.style.backgroundPosition = `${xPercent}% ${yPercent}%`;
      tile.innerHTML = `<span class="tile-number">${val + 1}</span>`;
      tile.onclick = () => handleTileClick(idx);
    }
    board.appendChild(tile);
  });
}

function handleTileClick(index) {
  const neighbors = getNeighbors(emptyIndex);
  if (!neighbors.includes(index)) return; // Not adjacent

  if (!gameStarted) {
    gameStarted = true;
    startTimer();
  }

  // Swap clicked with empty
  boardState[emptyIndex] = boardState[index];
  boardState[index] = boardSize * boardSize - 1;
  emptyIndex = index;
  gameMoves++;
  document.getElementById('gameMoves').textContent = gameMoves;

  renderGameBoard();
  checkWinCondition();
}

function startTimer() {
  clearInterval(gameTimerInterval);
  gameTimerInterval = setInterval(() => {
    gameTimerSeconds++;
    const mins = String(Math.floor(gameTimerSeconds / 60)).padStart(2, '0');
    const secs = String(gameTimerSeconds % 60).padStart(2, '0');
    document.getElementById('gameTimer').textContent = `${mins}:${secs}`;
  }, 1000);
}

function checkWinCondition() {
  const total = boardSize * boardSize;
  for (let i = 0; i < total; i++) {
    if (boardState[i] !== i) return;
  }

  clearInterval(gameTimerInterval);
  const timeFormatted = document.getElementById('gameTimer').textContent;
  document.getElementById('winMessage').textContent = `You completed Level ${currentLevel + 1} in ${gameMoves} moves and ${timeFormatted}!`;
  
  awardPoints(20);
  incrementUserStats('puzzles');
  document.getElementById('winModal').style.display = 'flex';
}

function togglePreview() {
  const card = document.getElementById('previewCard');
  const btnText = document.getElementById('previewBtnText');
  const isHidden = card.style.display === 'none';
  card.style.display = isHidden ? 'block' : 'none';
  btnText.textContent = isHidden ? 'Hide Preview' : 'Show Preview';
}

function nextLevelGame() {
  closeWinModal();
  currentLevel = (currentLevel + 1) % 10;
  selectGameLevel(currentLevel);
}

function closeWinModal() {
  document.getElementById('winModal').style.display = 'none';
}

// Modal Authentication Handlers
function openAuthModal(tab = 'login') {
  document.getElementById('authModal').style.display = 'flex';
  switchAuthTab(tab);
}

function closeAuthModal() {
  document.getElementById('authModal').style.display = 'none';
  hideAuthAlert();
}

function switchAuthTab(tab) {
  document.querySelectorAll('#authModal .auth-tab').forEach(t => t.classList.remove('active'));
  document.querySelectorAll('#authModal .auth-form').forEach(f => f.style.display = 'none');
  hideAuthAlert();

  if (tab === 'login') {
    const t = document.getElementById('tabLogin');
    const f = document.getElementById('formLogin');
    if (t) t.classList.add('active');
    if (f) f.style.display = 'block';
  } else if (tab === 'register') {
    const t = document.getElementById('tabRegister');
    const f = document.getElementById('formRegister');
    if (t) t.classList.add('active');
    if (f) f.style.display = 'block';
  } else if (tab === 'forgot') {
    const t = document.getElementById('tabForgot');
    const f = document.getElementById('formForgot');
    if (t) t.classList.add('active');
    if (f) f.style.display = 'block';
    const s1 = document.getElementById('forgotStep1');
    const s2 = document.getElementById('forgotStep2');
    if (s1) s1.style.display = 'block';
    if (s2) s2.style.display = 'none';
  }
}

function showAuthAlert(msg, type = 'error') {
  const alert = document.getElementById('authAlert');
  if (!alert) return;
  alert.textContent = msg;
  alert.className = `auth-alert ${type}`;
  alert.style.display = 'block';
}

function hideAuthAlert() {
  const alert = document.getElementById('authAlert');
  if (alert) alert.style.display = 'none';
}

async function handleLogin(e) {
  e.preventDefault();
  const email = document.getElementById('loginEmail').value.trim();
  const password = document.getElementById('loginPassword').value;

  try {
    const res = await fetch('/login', {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({ email, password })
    });
    const data = await res.json();
    if (!res.ok) throw new Error(data.error || 'Login failed');

    // Fetch profile
    let profile = { name: email.split('@')[0], email, phone: '', count: 0 };
    try {
      const pRes = await fetch(`/profile?email=${encodeURIComponent(email)}`);
      if (pRes.ok) profile = await pRes.json();
    } catch (_) {}

    setUserSession({
      name: profile.name || email.split('@')[0],
      email: profile.email || email,
      phone: profile.phone || '',
      count: profile.count || 0
    });

    closeAuthModal();
    unlockApp();
  } catch (err) {
    showAuthAlert(err.message, 'error');
  }
}

async function handleRegister(e) {
  e.preventDefault();
  const name = document.getElementById('regName').value.trim();
  const email = document.getElementById('regEmail').value.trim();
  const phone = document.getElementById('regPhone').value.trim();
  const password = document.getElementById('regPassword').value;

  try {
    const res = await fetch('/register', {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({ name, email, phone, password })
    });
    const data = await res.json();
    if (!res.ok) throw new Error(data.error || 'Registration failed');

    showAuthAlert('Account created successfully! Please sign in.', 'success');
    setTimeout(() => switchAuthTab('login'), 1200);
  } catch (err) {
    showAuthAlert(err.message, 'error');
  }
}

async function handleForgot(e) {
  e.preventDefault();
  const email = document.getElementById('forgotEmail').value.trim();
  try {
    const res = await fetch('/send-otp', {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({ email })
    });
    const data = await res.json();
    if (!res.ok) throw new Error(data.error || 'Could not send OTP');

    showAuthAlert('OTP sent to email! Check your inbox.', 'success');
    document.getElementById('forgotStep1').style.display = 'none';
    document.getElementById('forgotStep2').style.display = 'block';
  } catch (err) {
    showAuthAlert(err.message, 'error');
  }
}

async function handleResetPassword() {
  const email = document.getElementById('forgotEmail').value.trim();
  const otp = document.getElementById('forgotOtp').value.trim();
  const newPassword = document.getElementById('forgotNewPass').value;
  const confirmPassword = document.getElementById('forgotConfirmPass').value;

  try {
    const vRes = await fetch('/verify-otp', {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({ email, otp })
    });
    if (!vRes.ok) throw new Error('Invalid OTP');

    const rRes = await fetch('/reset-password', {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({ email, newPassword, confirmPassword })
    });
    const rData = await rRes.json();
    if (!rRes.ok) throw new Error(rData.error || 'Reset failed');

    showAuthAlert('Password successfully reset! Please sign in.', 'success');
    setTimeout(() => switchAuthTab('login'), 1500);
  } catch (err) {
    showAuthAlert(err.message, 'error');
  }
}

function continueAsGuest() {
  setUserSession({
    name: 'Guest Learner',
    email: 'guest@skillplay.local',
    phone: 'N/A',
    count: 50
  });
  closeAuthModal();
  unlockApp();
}

// ========================================================
// INITIAL AUTH GATE / PORTAL CONTROLLERS
// ========================================================
function togglePasswordVisibility(inputId, btn) {
  const input = document.getElementById(inputId);
  if (!input) return;
  const isPass = input.type === 'password';
  input.type = isPass ? 'text' : 'password';
  const icon = btn.querySelector('i');
  if (icon) {
    icon.className = isPass ? 'fa-solid fa-eye-slash' : 'fa-solid fa-eye';
  }
}

function switchPortalTab(tab) {
  document.querySelectorAll('#authPortal .auth-tab').forEach(t => t.classList.remove('active'));
  document.querySelectorAll('#authPortal .auth-form').forEach(f => f.style.display = 'none');
  hidePortalAlert();

  if (tab === 'login') {
    const tabEl = document.getElementById('portalTabLogin');
    const formEl = document.getElementById('portalFormLogin');
    if (tabEl) tabEl.classList.add('active');
    if (formEl) formEl.style.display = 'block';
  } else if (tab === 'register') {
    const tabEl = document.getElementById('portalTabRegister');
    const formEl = document.getElementById('portalFormRegister');
    if (tabEl) tabEl.classList.add('active');
    if (formEl) formEl.style.display = 'block';
  } else if (tab === 'forgot') {
    const tabEl = document.getElementById('portalTabForgot');
    const formEl = document.getElementById('portalFormForgot');
    if (tabEl) tabEl.classList.add('active');
    if (formEl) formEl.style.display = 'block';
    const s1 = document.getElementById('portalForgotStep1');
    const s2 = document.getElementById('portalForgotStep2');
    if (s1) s1.style.display = 'block';
    if (s2) s2.style.display = 'none';
  }
}

function showPortalAlert(msg, type = 'error') {
  const alert = document.getElementById('portalAuthAlert');
  if (!alert) return;
  alert.textContent = msg;
  alert.className = `auth-alert ${type}`;
  alert.style.display = 'block';
}

function hidePortalAlert() {
  const alert = document.getElementById('portalAuthAlert');
  if (alert) alert.style.display = 'none';
}

async function handlePortalLogin(e) {
  e.preventDefault();
  hidePortalAlert();
  const btn = document.getElementById('portalLoginSubmit');
  const origText = btn ? btn.innerHTML : '';
  if (btn) {
    btn.disabled = true;
    btn.innerHTML = '<i class="fa-solid fa-spinner fa-spin"></i> Signing in...';
  }

  const email = document.getElementById('portalLoginEmail').value.trim();
  const password = document.getElementById('portalLoginPassword').value;

  try {
    const res = await fetch('/login', {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({ email, password })
    });
    const data = await res.json();
    if (!res.ok) throw new Error(data.error || 'Login failed');

    // Fetch user profile from MongoDB backend
    let profile = { name: email.split('@')[0], email, phone: '', count: 0 };
    try {
      const pRes = await fetch(`/profile?email=${encodeURIComponent(email)}`);
      if (pRes.ok) profile = await pRes.json();
    } catch (_) {}

    setUserSession({
      name: profile.name || email.split('@')[0],
      email: profile.email || email,
      phone: profile.phone || '',
      count: profile.count || 0
    });

    unlockApp();
    navigateTo('home');
  } catch (err) {
    showPortalAlert(err.message, 'error');
  } finally {
    if (btn) {
      btn.disabled = false;
      btn.innerHTML = origText;
    }
  }
}

async function handlePortalRegister(e) {
  e.preventDefault();
  hidePortalAlert();
  const btn = document.getElementById('portalRegSubmit');
  const origText = btn ? btn.innerHTML : '';
  if (btn) {
    btn.disabled = true;
    btn.innerHTML = '<i class="fa-solid fa-spinner fa-spin"></i> Creating Account...';
  }

  const name = document.getElementById('portalRegName').value.trim();
  const email = document.getElementById('portalRegEmail').value.trim();
  const phone = document.getElementById('portalRegPhone').value.trim();
  const password = document.getElementById('portalRegPassword').value;

  try {
    const res = await fetch('/register', {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({ name, email, phone, password })
    });
    const data = await res.json();
    if (!res.ok) throw new Error(data.error || 'Registration failed');

    showPortalAlert('🎉 Account created successfully! Please sign in with your password.', 'success');
    const loginEmail = document.getElementById('portalLoginEmail');
    if (loginEmail) loginEmail.value = email;

    setTimeout(() => {
      switchPortalTab('login');
      const pwdInput = document.getElementById('portalLoginPassword');
      if (pwdInput) pwdInput.focus();
    }, 1200);
  } catch (err) {
    showPortalAlert(err.message, 'error');
  } finally {
    if (btn) {
      btn.disabled = false;
      btn.innerHTML = origText;
    }
  }
}

async function handlePortalForgot(e) {
  e.preventDefault();
  const email = document.getElementById('portalForgotEmail').value.trim();
  try {
    const res = await fetch('/send-otp', {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({ email })
    });
    const data = await res.json();
    if (!res.ok) throw new Error(data.error || 'Could not send OTP');

    showPortalAlert('OTP sent to email! Check your inbox or terminal.', 'success');
    document.getElementById('portalForgotStep1').style.display = 'none';
    document.getElementById('portalForgotStep2').style.display = 'block';
  } catch (err) {
    showPortalAlert(err.message, 'error');
  }
}

async function handlePortalResetPassword() {
  const email = document.getElementById('portalForgotEmail').value.trim();
  const otp = document.getElementById('portalForgotOtp').value.trim();
  const newPassword = document.getElementById('portalForgotNewPass').value;
  const confirmPassword = document.getElementById('portalForgotConfirmPass').value;

  try {
    const vRes = await fetch('/verify-otp', {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({ email, otp })
    });
    if (!vRes.ok) throw new Error('Invalid OTP code');

    const rRes = await fetch('/reset-password', {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({ email, newPassword, confirmPassword })
    });
    const rData = await rRes.json();
    if (!rRes.ok) throw new Error(rData.error || 'Password reset failed');

    showPortalAlert('Password successfully reset! Please sign in.', 'success');
    const loginEmail = document.getElementById('portalLoginEmail');
    if (loginEmail) loginEmail.value = email;
    setTimeout(() => switchPortalTab('login'), 1500);
  } catch (err) {
    showPortalAlert(err.message, 'error');
  }
}

function continueAsGuestPortal() {
  setUserSession({
    name: 'Guest Learner',
    email: 'guest@skillplay.local',
    phone: 'N/A',
    count: 50
  });
  unlockApp();
  navigateTo('home');
}

// Session Management & Gate Locks
function lockApp() {
  currentUser = null;
  document.body.classList.add('auth-gate-active');
  const portal = document.getElementById('authPortal');
  if (portal) {
    portal.style.display = 'flex';
    switchPortalTab('login');
  }
  updateUserUI();
}

function unlockApp() {
  document.body.classList.remove('auth-gate-active');
  const portal = document.getElementById('authPortal');
  if (portal) portal.style.display = 'none';
  updateUserUI();
}

function showAuthPortal(tab = 'login') {
  lockApp();
  switchPortalTab(tab);
}

function loadUserSession() {
  const saved = localStorage.getItem('skillplay_user');
  if (saved) {
    try {
      const parsed = JSON.parse(saved);
      if (parsed && parsed.email && parsed.email !== 'guest@skillplay.local') {
        currentUser = parsed;
        unlockApp();
        return;
      }
    } catch (e) {
      console.warn('Invalid saved session format:', e);
    }
  }

  // First time or unauthenticated: Lock app and show Login & Register fields first
  lockApp();
}

function setUserSession(user) {
  currentUser = user;
  localStorage.setItem('skillplay_user', JSON.stringify(user));
  updateUserUI();
}

function logoutUser() {
  localStorage.removeItem('skillplay_user');
  currentUser = null;
  lockApp();
  navigateTo('home');
}

function updateUserUI() {
  const pointsEl = document.getElementById('userPoints');
  const btnContainer = document.getElementById('authButtonContainer');

  if (pointsEl) pointsEl.textContent = currentUser ? currentUser.count : '0';

  if (!btnContainer) return;
  if (currentUser && currentUser.email && currentUser.email !== 'guest@skillplay.local') {
    const isAdmin = currentUser.isAdmin || currentUser.role === 'admin' || currentUser.email === 'raghuveer081014@gmail.com';
    btnContainer.innerHTML = `
      <div style="display: flex; align-items: center; gap: 8px;">
        ${isAdmin ? `
          <a href="/database.html" target="_blank" class="btn btn-outline btn-admin-nav" title="Admin Database Console">
            <i class="fa-solid fa-shield-halved"></i> Admin DB
          </a>
        ` : ''}
        <button class="btn btn-outline" onclick="navigateTo('profile')" title="View Profile">
          <i class="fa-solid fa-user-astronaut"></i> ${currentUser.name.split(' ')[0]}
          ${isAdmin ? `<span class="admin-badge">Admin</span>` : ''}
        </button>
        <button class="btn btn-outline btn-logout" onclick="logoutUser()" title="Sign Out">
          <i class="fa-solid fa-arrow-right-from-bracket"></i> Logout
        </button>
      </div>
    `;
  } else if (currentUser && currentUser.email === 'guest@skillplay.local') {
    btnContainer.innerHTML = `
      <div style="display: flex; align-items: center; gap: 8px;">
        <span class="guest-pill"><i class="fa-solid fa-user-secret"></i> Guest</span>
        <button class="btn btn-primary" onclick="showAuthPortal('login')">
          <i class="fa-solid fa-arrow-right-to-bracket"></i> Sign In / Register
        </button>
      </div>
    `;
  } else {
    btnContainer.innerHTML = `
      <button class="btn btn-primary" onclick="showAuthPortal('login')">
        <i class="fa-solid fa-arrow-right-to-bracket"></i> Login / Register
      </button>
    `;
  }
}

async function awardPoints(pts) {
  if (!currentUser) return;
  currentUser.count = (currentUser.count || 0) + pts;
  localStorage.setItem('skillplay_user', JSON.stringify(currentUser));
  updateUserUI();

  // Try updating Oracle backend
  if (currentUser.email && currentUser.email !== 'guest@skillplay.local') {
    try {
      await fetch('/update-count', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ email: currentUser.email, increment: pts })
      });
    } catch (e) {
      console.warn('Backend update count offline:', e);
    }
  }
}

function incrementUserStats(key) {
  const statsKey = `skillplay_stats_${key}`;
  const curr = parseInt(localStorage.getItem(statsKey) || '0', 10);
  localStorage.setItem(statsKey, (curr + 1).toString());
}

function renderProfileView() {
  if (!currentUser) return;
  const isAdmin = currentUser.isAdmin || currentUser.role === 'admin' || currentUser.email === 'raghuveer081014@gmail.com';
  const nameEl = document.getElementById('profileName');
  if (nameEl) {
    nameEl.innerHTML = `${currentUser.name} ${isAdmin ? `<span class="admin-badge"><i class="fa-solid fa-shield-halved"></i> Administrator</span>` : ''}`;
  }
  document.getElementById('profileEmail').textContent = currentUser.email;
  document.getElementById('profilePoints').textContent = currentUser.count;

  const quizzes = localStorage.getItem('skillplay_stats_quizzes') || '0';
  const puzzles = localStorage.getItem('skillplay_stats_puzzles') || '0';
  document.getElementById('profileQuizzes').textContent = quizzes;
  document.getElementById('profilePuzzles').textContent = puzzles;
}

// Last Visited Resume System
function saveLastProgress(cls, sub, lesson) {
  localStorage.setItem('skillplay_last_class', cls);
  localStorage.setItem('skillplay_last_sub', sub);
  localStorage.setItem('skillplay_last_lesson', lesson);
  checkResumeBanner();
}

function checkResumeBanner() {
  const cls = localStorage.getItem('skillplay_last_class');
  const sub = localStorage.getItem('skillplay_last_sub');
  const lesson = localStorage.getItem('skillplay_last_lesson');
  const banner = document.getElementById('resumeBanner');
  const details = document.getElementById('resumeDetails');
  const btn = document.getElementById('resumeBtn');

  if (cls && sub && lesson && banner) {
    banner.style.display = 'flex';
    details.textContent = `${cls} • ${sub} • ${lesson}`;
    btn.onclick = () => {
      navigateTo('learn');
      selectClass(cls);
      selectSubject(sub);
      openLesson(lesson, 0);
    };
  }
}
