import 'dart:math';
import 'package:flutter/material.dart';
import 'package:flutter/services.dart';
import 'package:image/image.dart' as img;
import 'package:flutter/foundation.dart';

class PuzzlePiece {
  final Uint8List image;
  final int correctRow;
  final int correctCol;

  PuzzlePiece({
    required this.image,
    required this.correctRow,
    required this.correctCol,
  });
}

class DraggedPiece {
  final PuzzlePiece piece;
  final int? fromRow;
  final int? fromCol;

  DraggedPiece({required this.piece, this.fromRow, this.fromCol});
}

class GameplayScreen extends StatefulWidget {
  final String imagePath;
  final int pieceCount;

  const GameplayScreen({
    super.key,
    required this.imagePath,
    required this.pieceCount,
  });

  @override
  State<GameplayScreen> createState() => _GameplayScreenState();
}

class _GameplayScreenState extends State<GameplayScreen> {
  bool showImage = false;
  bool isLoading = true;
  List<PuzzlePiece> trayPieces = [];
  late List<List<PuzzlePiece?>> placedPieces;
  late List<List<PuzzlePiece?>> fullImagePieces;
  int imageWidth = 0;
  int imageHeight = 0;
  int gridSize = 0;

  @override
  void initState() {
    super.initState();
    loadPieces();
  }

  Future<void> loadPieces() async {
    setState(() => isLoading = true);

    final byteData = await rootBundle.load(widget.imagePath);
    final imageBytes = byteData.buffer.asUint8List();

    final result = await compute(sliceImage, {
      'imageBytes': imageBytes,
      'pieceCount': widget.pieceCount,
    });

    setState(() {
      trayPieces = result['pieces'];
      imageWidth = result['width'];
      imageHeight = result['height'];
      gridSize = result['gridSize'];
      placedPieces = List.generate(
        gridSize,
        (_) => List.filled(gridSize, null),
      );
      fullImagePieces = List.generate(
        gridSize,
        (_) => List.filled(gridSize, null),
      );

      for (final piece in result['pieces']) {
        fullImagePieces[piece.correctRow][piece.correctCol] = PuzzlePiece(
          image: piece.image,
          correctRow: piece.correctRow,
          correctCol: piece.correctCol,
        );
      }

      isLoading = false;
    });
  }

  void _handleEyePress(bool isPressed) {
    setState(() {
      showImage = isPressed;
    });
  }

  void _checkCompletion() {
    for (int row = 0; row < gridSize; row++) {
      for (int col = 0; col < gridSize; col++) {
        final piece = placedPieces[row][col];
        if (piece == null ||
            piece.correctRow != row ||
            piece.correctCol != col) {
          return;
        }
      }
    }

    Future.delayed(const Duration(milliseconds: 300), () {
      if (mounted) {
        showDialog(
          context: context,
          barrierDismissible: false,
          builder: (_) => AlertDialog(
            title: const Text('🎉 Congratulations!'),
            content: const Text('You have completed the puzzle.'),
            actions: [
            TextButton(
              onPressed: () {
                Navigator.pop(context);
                Navigator.pop(context);
              },
              child: const Text('Done'),
            ),
          ],
        ),
      );
      }
    });
  }

  @override
  Widget build(BuildContext context) {
    final pieceWidth = gridSize > 0 ? imageWidth ~/ gridSize : 1;
    final pieceHeight = gridSize > 0 ? imageHeight ~/ gridSize : 1;

    return Scaffold(
      backgroundColor: Colors.grey[200],
      body: Column(
        children: [
          // Top toolbar with styled icons
          Container(
            padding: const EdgeInsets.symmetric(horizontal: 12, vertical: 8),
            color: Colors.white,
            child: Row(
              mainAxisAlignment: MainAxisAlignment.spaceBetween,
              children: [
                Container(
                  padding: const EdgeInsets.all(6),
                  margin: const EdgeInsets.only(top: 3),
                  decoration: const BoxDecoration(
                    color: Colors.white,
                    shape: BoxShape.circle,
                  ),
                  child: IconButton(
                    iconSize: 30,
                    icon: const Icon(Icons.arrow_back),
                    onPressed: () => Navigator.pop(context),
                  ),
                ),
                Container(
                  padding: const EdgeInsets.all(6),
                  margin: const EdgeInsets.only(top: 3),
                  decoration: const BoxDecoration(
                    color: Colors.white,
                    shape: BoxShape.circle,
                  ),
                  child: GestureDetector(
                    onTapDown: (_) => _handleEyePress(true),
                    onTapUp: (_) => _handleEyePress(false),
                    onTapCancel: () => _handleEyePress(false),
                    child: const Icon(Icons.remove_red_eye, size: 30),
                  ),
                ),
              ],
            ),
          ),

          // Puzzle board
          if (imageWidth > 0 && imageHeight > 0)
            Expanded(
              child: Center(
                child: SizedBox(
                  width: imageWidth.toDouble(),
                  height: imageHeight.toDouble(),
                  child: GridView.builder(
                    physics: const NeverScrollableScrollPhysics(),
                    gridDelegate: SliverGridDelegateWithFixedCrossAxisCount(
                      crossAxisCount: gridSize,
                      childAspectRatio: pieceWidth / pieceHeight,
                    ),
                    itemCount: gridSize * gridSize,
                    itemBuilder: (context, index) {
                      final row = index ~/ gridSize;
                      final col = index % gridSize;
                      final placed = placedPieces[row][col];
                      final fullPiece = fullImagePieces[row][col];

                      return DragTarget<DraggedPiece>(
                        builder: (context, candidateData, rejectedData) {
                          return Container(
                            decoration: BoxDecoration(
                              border: Border.all(color: Colors.black),
                            ),
                            child: showImage
                                ? Image.memory(
                                    fullPiece!.image,
                                    fit: BoxFit.fill,
                                  )
                                : placed != null
                                ? Draggable<DraggedPiece>(
                                    data: DraggedPiece(
                                      piece: placed,
                                      fromRow: row,
                                      fromCol: col,
                                    ),
                                    feedback: Material(
                                      child: Image.memory(
                                        placed.image,
                                        width: 60,
                                        height: 60,
                                      ),
                                    ),
                                    childWhenDragging: Container(
                                      color: Colors.transparent,
                                    ),
                                    child: Image.memory(
                                      placed.image,
                                      fit: BoxFit.fill,
                                    ),
                                  )
                                : Container(color: Colors.transparent),
                          );
                        },
                        onWillAcceptWithDetails: (details) => true,
                        onAcceptWithDetails: (details) {
                          final dragged = details.data;
                          setState(() {
                            final incoming = dragged.piece;
                            final fromRow = dragged.fromRow;
                            final fromCol = dragged.fromCol;

                            trayPieces.remove(incoming);
                            if (fromRow != null && fromCol != null) {
                              placedPieces[fromRow][fromCol] = null;
                            }

                            final existing = placedPieces[row][col];
                            if (existing != null) {
                              if (fromRow != null && fromCol != null) {
                                placedPieces[fromRow][fromCol] = existing;
                              } else {
                                trayPieces.add(existing);
                              }
                            }

                            placedPieces[row][col] = incoming;
                          });

                          _checkCompletion();
                        },
                      );
                    },
                  ),
                ),
              ),
            )
          else
            const Expanded(child: Center(child: CircularProgressIndicator())),

          // Piece tray
          Container(
            height: 100,
            padding: const EdgeInsets.symmetric(horizontal: 12),
            color: Colors.white,
            child: isLoading
                ? const Center(child: CircularProgressIndicator())
                : trayPieces.isEmpty
                ? const Center(child: Text('All pieces placed!'))
                : ListView.builder(
                    scrollDirection: Axis.horizontal,
                    itemCount: trayPieces.length,
                    itemBuilder: (context, index) {
                      final piece = trayPieces[index];
                      return Draggable<DraggedPiece>(
                        data: DraggedPiece(piece: piece),
                        feedback: Material(
                          child: Image.memory(
                            piece.image,
                            width: 60,
                            height: 60,
                          ),
                        ),
                        childWhenDragging: SizedBox(width: 60, height: 60),
                        child: Container(
                          margin: const EdgeInsets.symmetric(
                            horizontal: 8,
                            vertical: 12,
                          ),
                          width: 60,
                          height: 60,
                          decoration: BoxDecoration(
                            color: Colors.grey[300],
                            border: Border.all(color: Colors.black26),
                          ),
                          child: Image.memory(piece.image, fit: BoxFit.cover),
                        ),
                      );
                    },
                  ),
          ),
        ],
      ),
    );
  }
}

// ✅ Slicing function with shuffle
Map<String, dynamic> sliceImage(Map<String, dynamic> args) {
  final image = img.decodeImage(args['imageBytes'])!;
  final pieceCount = args['pieceCount'];

  final root = sqrt(pieceCount);
  if (root != root.floorToDouble()) {
    throw Exception('pieceCount must be a perfect square');
  }

  final gridSize = root.toInt();
  final pieceWidth = image.width ~/ gridSize;
  final pieceHeight = image.height ~/ gridSize;

  final pieces = <PuzzlePiece>[];

  for (int y = 0; y < gridSize; y++) {
    for (int x = 0; x < gridSize; x++) {
      final cropped = img.copyCrop(
        image,
        x * pieceWidth,
        y * pieceHeight,
        pieceWidth,
        pieceHeight,
      );
      pieces.add(
        PuzzlePiece(
          image: Uint8List.fromList(img.encodePng(cropped)),
          correctRow: y,
          correctCol: x,
        ),
      );
    }
  }

  pieces.shuffle(Random());

  return {
    'pieces': pieces,
    'width': image.width,
    'height': image.height,
    'gridSize': gridSize,
  };
}
