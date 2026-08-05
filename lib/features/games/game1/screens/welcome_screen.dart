import 'package:flutter/material.dart';
import 'home_screen.dart'; // Ensure this exists

class WelcomeScreen extends StatefulWidget {
  const WelcomeScreen({super.key});

  @override
  State<WelcomeScreen> createState() => _WelcomeScreenState();
}

class _WelcomeScreenState extends State<WelcomeScreen> {
  @override
  void initState() {
    super.initState();
    Future.delayed(const Duration(seconds: 1), () {
      if (mounted) {
        Navigator.pushReplacement(
          context,
          MaterialPageRoute(builder: (context) => const HomeScreen()),
        );
      }
    });
  }

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      backgroundColor: Colors.white,
      body: const Center(
        child: Text(
          'Jigsawsapes',
          textAlign: TextAlign.center,
          style: TextStyle(
            fontSize: 48,
            fontWeight: FontWeight.w900,
            color: Colors.purple,
            fontFamily: 'Cursive',
            letterSpacing: 2,
            shadows: [
              Shadow(
                blurRadius: 4,
                color: Colors.grey,
                offset: Offset(2, 2),
              ),
            ],
          ),
        ),
      ),
    );
  }
}