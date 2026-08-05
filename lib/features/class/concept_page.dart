import 'package:flutter/material.dart';
import 'package:shared_preferences/shared_preferences.dart';
import 'video_viewer_page.dart';
import 'lesson_url.dart';
import 'quiz_page.dart';

class ConceptPage extends StatefulWidget {
  final String selectedClass;
  final String selectedSubject;
  final String selectedLesson;

  const ConceptPage({
    required this.selectedClass,
    required this.selectedSubject,
    required this.selectedLesson,
    super.key,
  });

  @override
  State<ConceptPage> createState() => _ConceptPageState();
}

class _ConceptPageState extends State<ConceptPage> {
  late List<String> concepts;
  Set<int> completedIndices = {};

  String get completionKey =>
      '${widget.selectedClass}_${widget.selectedSubject}_${widget.selectedLesson}_completed';

  @override
  void initState() {
    super.initState();
    concepts = [widget.selectedLesson, 'Quiz'];
    loadCompletionStatus();
    saveLastVisitedPoint(); // Save progress on page load
  }

  Future<void> loadCompletionStatus() async {
    final prefs = await SharedPreferences.getInstance();
    final saved = prefs.getStringList(completionKey);
    if (saved != null) {
      setState(() {
        completedIndices = saved.map(int.parse).toSet();
      });
    }
  }

  Future<void> saveCompletionStatus() async {
    final prefs = await SharedPreferences.getInstance();
    await prefs.setStringList(
      completionKey,
      completedIndices.map((e) => e.toString()).toList(),
    );
  }

  Future<void> saveLastVisitedPoint() async {
    final prefs = await SharedPreferences.getInstance();
    await prefs.setString('last_class', widget.selectedClass);
    await prefs.setString('last_subject', widget.selectedSubject);
    await prefs.setString('last_lesson', widget.selectedLesson);
  }

  void handleTap(int index) async {
    setState(() {
      completedIndices.add(index);
    });
    await saveCompletionStatus();
    await saveLastVisitedPoint();

    if (mounted) {
      if (index == 0) {
        final videoUrl = lessonUrls[widget.selectedClass]?[widget.selectedSubject]?[widget.selectedLesson] ?? '';
        Navigator.push(
          context,
          MaterialPageRoute(
            builder: (_) => VideoViewerPage(
              lessonTitle: widget.selectedLesson,
              subjectName: widget.selectedSubject,
              videoUrl: videoUrl,
            ),
          ),
        );
      } else if (index == 1) {
        Navigator.push(
          context,
          MaterialPageRoute(
            builder: (_) => QuizPage(
              selectedClass: widget.selectedClass,
              selectedSubject: widget.selectedSubject,
              selectedLesson: widget.selectedLesson,
            ),
          ),
        );
      }
    }
  }

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        title: Text(widget.selectedLesson, style: const TextStyle(color: Colors.white)),
        backgroundColor: Colors.deepPurple.shade700,
        iconTheme: const IconThemeData(color: Colors.white),
      ),
      body: ListView.builder(
        padding: const EdgeInsets.all(16),
        itemCount: concepts.length,
        itemBuilder: (context, index) {
          final title = concepts[index];
          final isCompleted = completedIndices.contains(index);
          return ConceptCard(
            title: title,
            color: isCompleted ? Colors.green : Colors.deepPurple.shade700,
            onTap: () => handleTap(index),
          );
        },
      ),
    );
  }
}

class ConceptCard extends StatelessWidget {
  final String title;
  final Color color;
  final VoidCallback onTap;

  const ConceptCard({
    required this.title,
    required this.color,
    required this.onTap,
    super.key,
  });

  @override
  Widget build(BuildContext context) {
    return Material(
      color: Colors.transparent,
      child: InkWell(
        onTap: onTap,
        borderRadius: BorderRadius.circular(16),
        splashColor: color.withValues(alpha: 0.3),
        highlightColor: color.withValues(alpha: 0.15),
        child: Container(
          margin: const EdgeInsets.symmetric(vertical: 8),
          padding: const EdgeInsets.all(16),
          decoration: BoxDecoration(
            color: color,
            borderRadius: BorderRadius.circular(16),
            boxShadow: [
              BoxShadow(
                color: color.withValues(alpha: 0.4),
                blurRadius: 6,
                offset: const Offset(0, 4),
              ),
            ],
          ),
          child: Text(
            title,
            style: const TextStyle(
              color: Colors.white,
              fontSize: 18,
              fontWeight: FontWeight.bold,
            ),
          ),
        ),
      ),
    );
  }
}