const Map<String, Map<String, Map<String, String>>> answerPaths = {
  'CLASS 1': {
    'MATHS': {
      'Numbers (0 – 9)': 'assets/answers/class_1/maths/1.pdf',
      'Addition': 'assets/answers/class_1/maths/2.pdf',
      'Subtraction': 'assets/answers/class_1/maths/3.pdf',
      'Money': 'assets/answers/class_1/maths/4.pdf',
      'Numbers (10 – 99)': 'assets/answers/class_1/maths/5.pdf',
      'Measurements': 'assets/answers/class_1/maths/6.pdf',
      'Time': 'assets/answers/class_1/maths/7.pdf',
      'Patterns': 'assets/answers/class_1/maths/8.pdf',
      'How many?': 'assets/answers/class_1/maths/9.pdf',
    },
    'ENGLISH': {
      'Unit 1.1 I Am Special': 'assets/answers/class_1/english/1-1.pdf',
      'Unit 1.2 My Body Parts': 'assets/answers/class_1/english/1-2.pdf',
      'Unit 2 My Family': 'assets/answers/class_1/english/2.pdf',
      'Unit 3.1 My Fun': 'assets/answers/class_1/english/3-1.pdf',
      'Unit 3.2 My Actions': 'assets/answers/class_1/english/3-2.pdf',
      'Unit 4.1 Numbers': 'assets/answers/class_1/english/4-1.pdf',
      'Unit 4.2 Colours': 'assets/answers/class_1/english/4-2.pdf',
      'Unit 5.1 Fruits': 'assets/answers/class_1/english/5-1.pdf',
      'Unit 5.2 Vegetables': 'assets/answers/class_1/english/5-2.pdf',
      'Unit 6.1 Birds': 'assets/answers/class_1/english/6-1.pdf',
      'Unit 6.2 Animals Around Us': 'assets/answers/class_1/english/6-2.pdf',
      'Unit 7.1 Play Time': 'assets/answers/class_1/english/7-1.pdf',
      'Unit 7.2 Dancing Time': 'assets/answers/class_1/english/7-2.pdf',
      'Unit 8.1 Days of the Week': 'assets/answers/class_1/english/8-1.pdf',
      'Unit 8.2 Months of the Year': 'assets/answers/class_1/english/8-2.pdf',
    },
    'TELUGU': {
      'పడవ, చందమామ రావె': 'assets/answers/class_1/telugu/1.pdf',
      'మేలుకొలుపు, ఉడత ఉడత హూచ్': 'assets/answers/class_1/telugu/2.pdf',
      'తకధిమితోం, అరక': 'assets/answers/class_1/telugu/3.pdf',
      'ఊహల ఊయల, బావా బావా పన్నీరు': 'assets/answers/class_1/telugu/4.pdf',
      'ఆట, జడ – దండ': 'assets/answers/class_1/telugu/5.pdf',
      'ఇల్లు – ఈగ, ఎలుకమ్మ': 'assets/answers/class_1/telugu/6.pdf',
      'అమ్మ ఒడి, మేఘం – ఛత్రం': 'assets/answers/class_1/telugu/7.pdf',
      'పాఠశాల పండుగ, శుభదాయిని': 'assets/answers/class_1/telugu/8.pdf',
      'గలగల మాటలు, గుణింతాలం': 'assets/answers/class_1/telugu/9.pdf',
    },
  },
};

const Map<String, String> defaultSubjectPDFs = {
  'MATHS': 'assets/answers/class_1/default/31.pdf',
  'ENGLISH': 'assets/answers/class_1/default/21.pdf',
  'TELUGU': 'assets/answers/class_1/telugu/1.pdf',
  'EVS': 'assets/answers/class_1/default/11.pdf',
  'SCIENCE': 'assets/answers/class_1/default/11.pdf',
  'SOCIAL': 'assets/answers/class_1/default/41.pdf',
  'HINDI': 'assets/answers/class_1/default/61.pdf',
};

String getQuestionAnswerPdf(String selectedClass, String selectedSubject, String lesson, int lessonIndex) {
  // Check explicit map
  final explicit = answerPaths[selectedClass]?[selectedSubject]?[lesson];
  if (explicit != null) return explicit;

  // Class 1 dynamic resolution
  if (selectedClass == 'CLASS 1') {
    if (selectedSubject == 'MATHS') {
      final idx = (lessonIndex % 9) + 1;
      return 'assets/answers/class_1/maths/$idx.pdf';
    } else if (selectedSubject == 'TELUGU') {
      final idx = (lessonIndex % 9) + 1;
      return 'assets/answers/class_1/telugu/$idx.pdf';
    } else if (selectedSubject == 'ENGLISH') {
      const englishFiles = [
        '1-1.pdf', '1-2.pdf', '2.pdf', '3-1.pdf', '3-2.pdf',
        '4-1.pdf', '4-2.pdf', '5-1.pdf', '5-2.pdf', '6-1.pdf',
        '6-2.pdf', '7-1.pdf', '7-2.pdf', '8-1.pdf', '8-2.pdf'
      ];
      final file = englishFiles[lessonIndex % englishFiles.length];
      return 'assets/answers/class_1/english/$file';
    }
  }

  // Classes 2-6 resolution correctly matched by SUBJECT
  if (selectedSubject == 'TELUGU') {
    final idx = (lessonIndex % 9) + 1;
    return 'assets/answers/class_1/telugu/$idx.pdf';
  }
  if (selectedSubject == 'MATHS') {
    return 'assets/answers/class_1/default/31.pdf';
  }
  if (selectedSubject == 'ENGLISH') {
    return 'assets/answers/class_1/default/21.pdf';
  }
  if (selectedSubject == 'EVS' || selectedSubject == 'SCIENCE') {
    return 'assets/answers/class_1/default/11.pdf';
  }
  if (selectedSubject == 'SOCIAL') {
    return 'assets/answers/class_1/default/41.pdf';
  }
  if (selectedSubject == 'HINDI') {
    return 'assets/answers/class_1/default/61.pdf';
  }

  return defaultSubjectPDFs[selectedSubject] ?? 'assets/answers/class_1/default/11.pdf';
}

