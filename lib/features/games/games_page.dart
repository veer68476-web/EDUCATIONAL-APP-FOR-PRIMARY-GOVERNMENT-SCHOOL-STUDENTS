import 'package:flutter/material.dart';
import 'game1/screens/welcome_screen.dart'; // ✅ Adjust path as needed

class GamesPage extends StatelessWidget {
  GamesPage({super.key});

  final Color backgroundColor = Colors.white;
  final Color buttonColor = Colors.deepPurple.shade700;

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      backgroundColor: backgroundColor,
      appBar: AppBar(
        title: const Text('Select a Game'),
        backgroundColor: buttonColor,
        foregroundColor: Colors.white,
        elevation: 4,
      ),
      body: Center(
        child: Container(
          padding: const EdgeInsets.all(24),
          child: Material(
            color: Colors.transparent,
            child: InkWell(
              onTap: () {
                Navigator.push(
                  context,
                  MaterialPageRoute(builder: (_) => const WelcomeScreen()),
                );
              },
              splashColor: buttonColor.withValues(alpha: 0.3),
              highlightColor: buttonColor.withValues(alpha: 0.15),
              borderRadius: BorderRadius.circular(20),
              child: Container(
                padding: const EdgeInsets.symmetric(horizontal: 24, vertical: 32),
                decoration: BoxDecoration(
                  color: buttonColor,
                  borderRadius: BorderRadius.circular(20),
                  boxShadow: [
                    BoxShadow(
                      color: buttonColor.withValues(alpha: 0.4),
                      blurRadius: 8,
                      offset: const Offset(0, 4),
                    ),
                  ],
                ),
                child: Column(
                  mainAxisSize: MainAxisSize.min,
                  children: const [
                    Icon(Icons.extension, size: 40, color: Colors.white), // puzzle icon
                    SizedBox(height: 12),
                    Text(
                      'JIGSAWSCAPES',
                      style: TextStyle(
                        color: Colors.white,
                        fontSize: 18,
                        fontWeight: FontWeight.bold,
                        letterSpacing: 1.2,
                      ),
                    ),
                  ],
                ),
              ),
            ),
          ),
        ),
      ),
    );
  }
}