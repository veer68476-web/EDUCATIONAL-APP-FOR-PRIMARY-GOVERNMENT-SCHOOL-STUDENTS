class UserData {
  static String email = '';
  static int choice = 0;
  static String id = ''; // ✅ This must exist
  static String currentQuizId = '';

  static void setUser(String newEmail) {
    email = newEmail;
    choice = 1;
  }

  static void setId(String newId) {
    id = newId;
  }

  static void setCurrentQuizId(String quizId) {
    currentQuizId = quizId;
  }

  static void reset() {
    email = '';
    choice = 0;
    id = '';
    currentQuizId = '';
  }
}