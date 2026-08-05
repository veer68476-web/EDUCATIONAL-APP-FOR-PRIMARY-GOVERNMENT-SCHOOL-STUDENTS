import 'package:flutter/material.dart';
import 'package:shared_preferences/shared_preferences.dart';
import 'profile/profile_page.dart';
import 'class/concept_page.dart';
import 'class/class_page.dart';
import 'testbook/testbook_page.dart';
import 'questions/questions_page.dart';
import 'games/games_page.dart';

class HomePage extends StatelessWidget {
  final String email;

  HomePage({required this.email, super.key});

  final Color lightColor = Colors.white;
  final Color darkColor = Colors.deepPurple.shade700;

  Future<void> _continue(BuildContext context) async {
    final prefs = await SharedPreferences.getInstance();
    final selectedClass = prefs.getString('last_class');
    final selectedSubject = prefs.getString('last_subject');
    final selectedLesson = prefs.getString('last_lesson');

    if (selectedClass != null && selectedSubject != null && selectedLesson != null) {
      if (!context.mounted) return;
      Navigator.push(
        context,
        MaterialPageRoute(
          builder: (_) => ConceptPage(
            selectedClass: selectedClass,
            selectedSubject: selectedSubject,
            selectedLesson: selectedLesson,
          ),
        ),
      );
    } else {
      if (!context.mounted) return;
      ScaffoldMessenger.of(context).showSnackBar(
        const SnackBar(content: Text('No saved progress found')),
      );
    }
  }

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      backgroundColor: lightColor,
      body: SafeArea(
        child: Column(
          children: [
            Container(
              color: darkColor,
              padding: const EdgeInsets.symmetric(horizontal: 16.0, vertical: 12),
              child: Row(
                mainAxisAlignment: MainAxisAlignment.spaceBetween,
                children: [
                  Row(
                    children: [
                      const Icon(Icons.home, size: 28, color: Colors.white),
                      const SizedBox(width: 8),
                      const Text(
                        'Home',
                        style: TextStyle(
                          fontSize: 24,
                          fontWeight: FontWeight.bold,
                          color: Colors.white,
                        ),
                      ),
                    ],
                  ),
                  IconButton(
                    icon: const Icon(Icons.person, size: 28, color: Colors.white),
                    onPressed: () {
                      Navigator.push(
                        context,
                        MaterialPageRoute(
                          builder: (_) => ProfilePage(email: email),
                        ),
                      );
                    },
                  ),
                ],
              ),
            ),
            Expanded(
              child: Container(
                color: lightColor,
                child: GridView.count(
                  crossAxisCount: 2,
                  padding: const EdgeInsets.all(16),
                  children: [
                    AnimatedButton(
                      label: 'CONTINUE',
                      icon: Icons.play_arrow,
                      color: darkColor,
                      onPressed: () => _continue(context),
                    ),
                    AnimatedButton(
                      label: 'CLASS',
                      icon: Icons.school,
                      color: darkColor,
                      onPressed: () {
                        Navigator.push(context, MaterialPageRoute(builder: (_) => ClassPage()));
                      },
                    ),
                    AnimatedButton(
                      label: 'TESTBOOK',
                      icon: Icons.book,
                      color: darkColor,
                      onPressed: () {
                        Navigator.push(context, MaterialPageRoute(builder: (_) => TestbookPage()));
                      },
                    ),
                    AnimatedButton(
                      label: 'TEXTBOOK ANSWERS',
                      icon: Icons.menu_book,
                      color: darkColor,
                      onPressed: () {
                        Navigator.push(context, MaterialPageRoute(builder: (_) => QuestionsPage()));
                      },
                    ),
                    AnimatedButton(
                      label: 'GAMES',
                      icon: Icons.videogame_asset,
                      color: darkColor,
                      onPressed: () {
                        Navigator.push(context, MaterialPageRoute(builder: (_) => GamesPage()));
                      },
                    ),
                  ],
                ),
              ),
            ),
          ],
        ),
      ),
    );
  }
}

class AnimatedButton extends StatelessWidget {
  final String label;
  final IconData icon;
  final Color color;
  final VoidCallback onPressed;

  const AnimatedButton({
    required this.label,
    required this.icon,
    required this.color,
    required this.onPressed,
    super.key,
  });

  @override
  Widget build(BuildContext context) {
    return Material(
      color: Colors.transparent,
      child: InkWell(
        onTap: onPressed,
        splashColor: color.withValues(alpha: 0.3),
        highlightColor: color.withValues(alpha: 0.15),
        borderRadius: BorderRadius.circular(20),
        child: Container(
          margin: const EdgeInsets.all(8),
          padding: const EdgeInsets.symmetric(horizontal: 12, vertical: 24),
          decoration: BoxDecoration(
            color: color,
            borderRadius: BorderRadius.circular(20),
            boxShadow: [
              BoxShadow(
                color: color.withValues(alpha: 0.4),
                blurRadius: 8,
                offset: const Offset(0, 4),
              ),
            ],
          ),
          alignment: Alignment.center,
          child: Column(
            mainAxisSize: MainAxisSize.min,
            children: [
              Icon(icon, size: 40, color: Colors.white),
              const SizedBox(height: 12),
              Text(
                label,
                style: const TextStyle(
                  color: Colors.white,
                  fontSize: 17,
                  fontWeight: FontWeight.bold,
                  letterSpacing: 1.1,
                ),
                textAlign: TextAlign.center,
              ),
            ],
          ),
        ),
      ),
    );
  }
}