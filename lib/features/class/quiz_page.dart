import 'package:flutter/material.dart';
import 'package:http/http.dart' as http;
import 'dart:convert';
import 'quiz_bank.dart'; // contains nestedQuizBank and defaultQuizBank
import 'package:skillplay/data.dart';
import 'package:skillplay/backend_config.dart';

class QuizPage extends StatefulWidget {
  final String selectedClass;
  final String selectedSubject;
  final String selectedLesson;

  const QuizPage({
    required this.selectedClass,
    required this.selectedSubject,
    required this.selectedLesson,
    super.key,
  });

  @override
  State<QuizPage> createState() => _QuizPageState();
}

class _QuizPageState extends State<QuizPage> {
  late List<Map<String, dynamic>> questions;
  int currentIndex = 0;
  int? selectedOption;
  bool answered = false;
  int score = 0;
  bool quizFinished = false;
  late String quizId;
  bool isDefaultQuiz = false;

  @override
  void initState() {
    super.initState();
    quizId = '${widget.selectedClass}_${widget.selectedSubject}_${widget.selectedLesson}';
    UserData.setCurrentQuizId(quizId);

    questions = nestedQuizBank[widget.selectedClass]?[widget.selectedSubject]?[widget.selectedLesson] ?? [];

    if (questions.isEmpty) {
      questions = defaultQuizBank[widget.selectedSubject] ?? [];
      isDefaultQuiz = true;
    }
  }

  Future<void> updateUserCountIfFirstAttempt() async {
    const String updateUrl = '$backendBaseUrl/update-count';

    try {
      final response = await http.post(
        Uri.parse(updateUrl),
        headers: {'Content-Type': 'application/json'},
        body: jsonEncode({
          'email': UserData.email,
          'increment': 2,
          'quizId': quizId,
        }),
      );

      if (response.statusCode == 200) {
        // Count updated successfully
      } else {
        // Failed to update count
      }
    } catch (e) {
      // Error updating count
    }
  }

  void handleOptionTap(int index) {
    if (answered) return;
    setState(() {
      selectedOption = index;
      answered = true;
      if (questions[currentIndex]['answer'] == index) {
        score++;
      }
    });
  }

  void goToNext() {
    if (currentIndex < questions.length - 1) {
      setState(() {
        currentIndex++;
        selectedOption = null;
        answered = false;
      });
    }
  }

  void submitQuiz() {
    setState(() {
      quizFinished = true;
    });
  }

  Widget buildResultScreen() {
    return Scaffold(
      backgroundColor: const Color(0xFF0F1C3F),
      body: Center(
        child: SingleChildScrollView(
          padding: const EdgeInsets.all(24),
          child: Container(
            padding: const EdgeInsets.all(24),
            decoration: BoxDecoration(
              color: Colors.white,
              borderRadius: BorderRadius.circular(20),
              boxShadow: [
                BoxShadow(
                  color: Colors.black.withValues(alpha: 0.2),
                  blurRadius: 12,
                  offset: const Offset(0, 6),
                ),
              ],
            ),
            child: Column(
              mainAxisSize: MainAxisSize.min,
              children: [
                const Icon(Icons.check_circle, size: 80, color: Colors.green),
                const SizedBox(height: 20),
                Text(
                  isDefaultQuiz ? 'Default Quiz Finished!' : 'Quiz Finished!',
                  style: const TextStyle(fontSize: 22, fontWeight: FontWeight.bold, color: Colors.black),
                ),
                const SizedBox(height: 12),
                Text(
                  'Congratulations! You got $score out of ${questions.length} correct.\nKeep up the good work!',
                  textAlign: TextAlign.center,
                  style: const TextStyle(fontSize: 15, color: Colors.black87),
                ),
                const SizedBox(height: 24),
                ElevatedButton(
                  onPressed: () async {
                    await updateUserCountIfFirstAttempt();
                    if (mounted) {
                      Navigator.pop(context);
                    }
                  },
                  style: ElevatedButton.styleFrom(
                    backgroundColor: Colors.deepPurple.shade700,
                    padding: const EdgeInsets.symmetric(horizontal: 32, vertical: 14),
                    shape: RoundedRectangleBorder(borderRadius: BorderRadius.circular(8)),
                  ),
                  child: const Text('DONE', style: TextStyle(fontSize: 16, color: Colors.white)),
                ),
              ],
            ),
          ),
        ),
      ),
    );
  }

  @override
  Widget build(BuildContext context) {
    if (questions.isEmpty) {
      return Scaffold(
        appBar: AppBar(
          title: Text(widget.selectedLesson, style: const TextStyle(color: Colors.white)),
          backgroundColor: Colors.deepPurple.shade700,
          foregroundColor: Colors.white,
        ),
        body: const Center(child: Text('No quiz available for this lesson.')),
      );
    }

    if (quizFinished) return buildResultScreen();

    final question = questions[currentIndex];
    final correctAnswer = question['answer'];

    return Scaffold(
      backgroundColor: const Color(0xFF0F1C3F),
      appBar: AppBar(
        title: Text(widget.selectedLesson, style: const TextStyle(color: Colors.white)),
        backgroundColor: Colors.deepPurple.shade700,
        foregroundColor: Colors.white,
        elevation: 0,
      ),
      body: SingleChildScrollView(
        padding: const EdgeInsets.all(16),
        child: Container(
          padding: const EdgeInsets.all(20),
          decoration: BoxDecoration(
            color: Colors.white,
            borderRadius: BorderRadius.circular(16),
            boxShadow: [
              BoxShadow(
                color: Colors.black.withValues(alpha: 0.1),
                blurRadius: 8,
                offset: const Offset(0, 4),
              ),
            ],
          ),
          child: Column(
            crossAxisAlignment: CrossAxisAlignment.start,
            children: [
              Text(
                '${currentIndex + 1}. ${question['question']}',
                style: const TextStyle(
                  fontSize: 17,
                  fontWeight: FontWeight.w600,
                  color: Colors.black,
                ),
              ),
              const SizedBox(height: 20),
              ...List.generate(question['options'].length, (i) {
                Color bgColor = Colors.white;
                Color textColor = Colors.black;
                if (answered) {
                  if (i == correctAnswer) {
                    bgColor = Colors.green.shade400;
                    textColor = Colors.white;
                  } else if (i == selectedOption) {
                    bgColor = Colors.red.shade400;
                    textColor = Colors.white;
                  }
                }

                return GestureDetector(
                  onTap: () => handleOptionTap(i),
                  child: Container(
                    margin: const EdgeInsets.symmetric(vertical: 6),
                    padding: const EdgeInsets.symmetric(vertical: 12, horizontal: 16),
                    width: double.infinity,
                    decoration: BoxDecoration(
                      color: bgColor,
                      borderRadius: BorderRadius.circular(10),
                      border: Border.all(color: Colors.grey.shade300),
                    ),
                    child: Text(
                      question['options'][i],
                      style: TextStyle(
                        fontSize: 14,
                        color: textColor,
                        fontWeight: FontWeight.w500,
                      ),
                    ),
                  ),
                );
              }),
              const SizedBox(height: 24),
              Row(
                mainAxisAlignment: MainAxisAlignment.spaceBetween,
                children: [
                  Text(
                    '${currentIndex + 1} of ${questions.length} questions',
                    style: const TextStyle(fontSize: 13, color: Colors.grey),
                  ),
                  ElevatedButton(
                    onPressed: answered
                        ? (currentIndex == questions.length - 1 ? submitQuiz : goToNext)
                        : null,
                    style: ElevatedButton.styleFrom(
                      backgroundColor: Colors.deepPurple.shade700,
                      padding: const EdgeInsets.symmetric(horizontal: 20, vertical: 10),
                                            shape: RoundedRectangleBorder(borderRadius: BorderRadius.circular(8)),
                    ),
                    child: Text(
                      currentIndex == questions.length - 1 ? 'Submit' : 'Next',
                      style: const TextStyle(fontSize: 15, color: Colors.white),
                    ),
                  ),
                ],
              ),
            ],
          ),
        ),
      ),
    );
  }
}