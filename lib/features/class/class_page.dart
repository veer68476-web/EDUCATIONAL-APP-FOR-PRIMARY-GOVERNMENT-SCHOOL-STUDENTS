import 'package:flutter/material.dart';
import 'subject_selection_page.dart';

class ClassPage extends StatelessWidget {
  ClassPage({super.key});

  final List<String> classes = ['CLASS 1', 'CLASS 2', 'CLASS 3', 'CLASS 4', 'CLASS 5', 'CLASS 6'];

  final Color lightColor = Colors.white;
  final Color darkColor = Colors.deepPurple.shade700;

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      backgroundColor: lightColor,
      appBar: AppBar(
        backgroundColor: darkColor,
        title: Text('Class Option', style: TextStyle(color: lightColor)),
        iconTheme: IconThemeData(color: lightColor),
      ),
      body: Padding(
        padding: const EdgeInsets.all(16.0),
        child: GridView.count(
          crossAxisCount: 2,
          children: classes.map((className) {
            return SelectionButton(
              label: className,
              color: darkColor,
              onTap: () {
                Navigator.push(
                  context,
                  MaterialPageRoute(
                    builder: (_) => SubjectSelectionPage(selectedClass: className),
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

class SelectionButton extends StatelessWidget {
  final String label;
  final VoidCallback onTap;
  final Color color;

  const SelectionButton({
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
          margin: EdgeInsets.all(8),
          decoration: BoxDecoration(
            color: color,
            borderRadius: BorderRadius.circular(20),
            boxShadow: [
              BoxShadow(color: color.withValues(alpha: 0.4), blurRadius: 6, offset: Offset(0, 4)),
            ],
          ),
          alignment: Alignment.center,
          child: Text(
            label,
            style: TextStyle(color: Colors.white, fontSize: 18, fontWeight: FontWeight.bold),
          ),
        ),
      ),
    );
  }
}