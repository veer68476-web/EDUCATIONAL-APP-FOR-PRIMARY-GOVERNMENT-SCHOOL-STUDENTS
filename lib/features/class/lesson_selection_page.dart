import 'package:flutter/material.dart';
import 'concept_page.dart';
import 'package:skillplay/features/curriculum_data.dart';

class LessonSelectionPage extends StatelessWidget {
  final String selectedClass;
  final String selectedSubject;

  const LessonSelectionPage({
    required this.selectedClass,
    required this.selectedSubject,
    super.key,
  });

  @override
  Widget build(BuildContext context) {
    final lessons = curriculum[selectedClass]?[selectedSubject] ?? [];

    return Scaffold(
      backgroundColor: Colors.white,
      appBar: AppBar(
        backgroundColor: Colors.deepPurple.shade700,
        title: Text('$selectedSubject Lessons', style: TextStyle(color: Colors.white)),
        iconTheme: IconThemeData(color: Colors.white),
      ),
      body: Padding(
        padding: const EdgeInsets.all(16.0),
        child: GridView.count(
          crossAxisCount: 2,
          children: lessons.map((lesson) {
            return LessonButton(
              label: lesson,
              color: Colors.deepPurple.shade700,
              onTap: () {
                Navigator.push(
                  context,
                  MaterialPageRoute(
                    builder: (_) => ConceptPage(
                      selectedClass: selectedClass,
                      selectedSubject: selectedSubject,
                      selectedLesson: lesson,
                    ),
                  ),
                );
              },
            );
          }).toList(),
        ),
      ),
    );
  }
}

class LessonButton extends StatelessWidget {
  final String label;
  final VoidCallback onTap;
  final Color color;

  const LessonButton({
    required this.label,
    required this.onTap,
    required this.color,
    super.key,
  });

  @override
  Widget build(BuildContext context) {
    return Material(
      color: Colors.transparent,
      child: InkWell(
        onTap: onTap,
        splashColor: color.withValues(alpha: 0.3),
        highlightColor: color.withValues(alpha: 0.15),
        borderRadius: BorderRadius.circular(20),
        child: Container(
          margin: const EdgeInsets.all(8),
          decoration: BoxDecoration(
            color: color,
            borderRadius: BorderRadius.circular(20),
            boxShadow: [
              BoxShadow(
                color: color.withValues(alpha: 0.4),
                blurRadius: 6,
                offset: Offset(0, 4),
              ),
            ],
          ),
          alignment: Alignment.center,
          child: Text(
            label,
            style: const TextStyle(
              color: Colors.white,
              fontSize: 16,
              fontWeight: FontWeight.bold,
            ),
            textAlign: TextAlign.center,
          ),
        ),
      ),
    );
  }
}