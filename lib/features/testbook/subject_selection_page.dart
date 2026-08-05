import 'package:flutter/material.dart';
import 'package:flutter/services.dart' show rootBundle;
import 'package:path_provider/path_provider.dart';
import 'dart:io';

import 'flutter_pdf_view.dart';
import 'answer_path.dart';
import 'package:skillplay/features/curriculum_data.dart';

class SubjectSelectionPage extends StatelessWidget {
  final String selectedClass;

  const SubjectSelectionPage({required this.selectedClass, super.key});

  Future<String> preparePdf(String assetPath) async {
    final byteData = await rootBundle.load(assetPath);
    final buffer = byteData.buffer;
    final directory = await getApplicationDocumentsDirectory();
    final file = File('${directory.path}/${assetPath.split('/').last}');
    await file.writeAsBytes(buffer.asUint8List(byteData.offsetInBytes, byteData.lengthInBytes));
    return file.path;
  }

  @override
  Widget build(BuildContext context) {
    final subjects = curriculum[selectedClass]?.keys.toList() ?? [];

    return Scaffold(
      backgroundColor: Colors.white,
      appBar: AppBar(
        backgroundColor: Colors.deepPurple.shade700,
        title: Text('Subjects for $selectedClass', style: const TextStyle(color: Colors.white)),
        iconTheme: const IconThemeData(color: Colors.white),
      ),
      body: Padding(
        padding: const EdgeInsets.all(16.0),
        child: GridView.count(
          crossAxisCount: 2,
          children: subjects.map((subject) {
            return SubjectButton(
              label: subject,
              color: Colors.deepPurple.shade700,
              onTap: () async {
                final assetPath = answerPaths[selectedClass]?[subject];

                if (assetPath != null) {
                  try {
                    final localPath = await preparePdf(assetPath);
                    if (!context.mounted) return;
                    Navigator.push(
                      context,
                      MaterialPageRoute(
                        builder: (_) => FlutterPDFView(assetPath: localPath),
                      ),
                    );
                  } catch (e) {
                    if (!context.mounted) return;
                    ScaffoldMessenger.of(context).showSnackBar(
                      SnackBar(content: Text('Error loading PDF for "$subject": $e')),
                    );
                  }
                } else {
                  if (!context.mounted) return;
                  ScaffoldMessenger.of(context).showSnackBar(
                    SnackBar(content: Text('PDF not found for "$subject"')),
                  );
                }
              },
            );
          }).toList(),
        ),
      ),
    );
  }
}

class SubjectButton extends StatelessWidget {
  final String label;
  final VoidCallback onTap;
  final Color color;

  const SubjectButton({
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
                offset: const Offset(0, 4),
              ),
            ],
          ),
          alignment: Alignment.center,
          child: Text(
            label,
            style: const TextStyle(
              color: Colors.white,
              fontSize: 18,
              fontWeight: FontWeight.bold,
            ),
            textAlign: TextAlign.center,
          ),
        ),
      ),
    );
  }
}