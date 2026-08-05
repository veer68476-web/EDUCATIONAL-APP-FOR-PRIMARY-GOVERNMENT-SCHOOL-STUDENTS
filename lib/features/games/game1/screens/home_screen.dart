import 'package:flutter/material.dart';
import '../widgets/puzzle_grid.dart';

class HomeScreen extends StatelessWidget {
  const HomeScreen({super.key});

  @override
  Widget build(BuildContext context) {
    return const Scaffold(
      backgroundColor: Colors.white,
      body: SafeArea(
        child: PuzzleGrid(),
      ),
    );
  }
}