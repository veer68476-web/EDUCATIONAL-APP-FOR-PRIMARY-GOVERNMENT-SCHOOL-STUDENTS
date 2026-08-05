import 'package:flutter/material.dart';
import '../screens/puzzle_detail_screen.dart';
import 'package:skillplay/features/games/games_page.dart'; // ✅ Adjust path if needed

class PuzzleGrid extends StatelessWidget {
  const PuzzleGrid({super.key});

  @override
  Widget build(BuildContext context) {
    final puzzles = List.generate(10, (i) => 'assets/puzzle_$i.jpg');

    return Scaffold(
      appBar: AppBar(
        title: const Text('Choose a Puzzle'),
        leading: IconButton(
          icon: const Icon(Icons.arrow_back),
          onPressed: () {
            Navigator.pushReplacement(
              context,
              MaterialPageRoute(builder: (_) => GamesPage()),
            );
          },
        ),
        backgroundColor: Colors.deepPurple.shade700,
        foregroundColor: Colors.white,
        elevation: 4,
      ),
      body: GridView.builder(
        padding: const EdgeInsets.all(12),
        gridDelegate: const SliverGridDelegateWithFixedCrossAxisCount(
          crossAxisCount: 2,
          mainAxisSpacing: 12,
          crossAxisSpacing: 12,
          childAspectRatio: 0.75,
        ),
        itemCount: puzzles.length,
        itemBuilder: (context, index) {
          return GestureDetector(
            onTap: () {
              Navigator.push(
                context,
                MaterialPageRoute(
                  builder: (context) => PuzzleDetailScreen(imagePath: puzzles[index]),
                ),
              );
            },
            child: ClipRRect(
              borderRadius: BorderRadius.circular(12),
              child: Image.asset(puzzles[index], fit: BoxFit.cover),
            ),
          );
        },
      ),
    );
  }
}