import 'dart:io';
import 'package:flutter/material.dart';
import 'package:flutter/services.dart';
import 'package:flutter_pdfview/flutter_pdfview.dart';
import 'package:path_provider/path_provider.dart';

class FlutterPDFView extends StatefulWidget {
  final String assetPath;

  const FlutterPDFView({required this.assetPath, super.key});

  @override
  // ignore: library_private_types_in_public_api
  _FlutterPDFViewState createState() => _FlutterPDFViewState();
}

class _FlutterPDFViewState extends State<FlutterPDFView> {
  String? localPDFPath;
  int? pages = 0;
  int? currentPage = 0;
  bool isReady = false;
  late PDFViewController pdfViewController;

  @override
  void initState() {
    super.initState();
    preparePDF();
  }

  Future<void> preparePDF() async {
    try {
      final ByteData bytes = await rootBundle.load(widget.assetPath);
      final Uint8List list = bytes.buffer.asUint8List();

      final tempDir = await getTemporaryDirectory();
      final fileName = widget.assetPath.split('/').last;
      final file = File('${tempDir.path}/$fileName');

      await file.writeAsBytes(list, flush: true);
      setState(() {
        localPDFPath = file.path;
      });
    } catch (e) {
      if (!mounted) return;
      ScaffoldMessenger.of(context).showSnackBar(
        SnackBar(content: Text('Failed to load PDF: $e')),
      );
    }
  }

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        title: const Text(
          'PDF Viewer',
          style: TextStyle(color: Colors.white), // ✅ Title text color
        ),
        backgroundColor: Colors.deepPurple.shade700,
        iconTheme: const IconThemeData(color: Colors.white), // ✅ Back arrow color
      ),
      body: localPDFPath == null
          ? const Center(child: CircularProgressIndicator())
          : PDFView(
              filePath: localPDFPath!,
              enableSwipe: true,
              swipeHorizontal: true,
              autoSpacing: true,
              pageFling: true,
              onRender: (pagesCount) {
                setState(() {
                  pages = pagesCount;
                  isReady = true;
                });
              },
              onViewCreated: (PDFViewController vc) {
                pdfViewController = vc;
              },
              onPageChanged: (int? page, int? total) {
                setState(() {
                  currentPage = page;
                });
              },
              onError: (error) {
                // Error loading PDF
              },
              onPageError: (page, error) {
                // Error on page
              },
            ),
      floatingActionButton: isReady
          ? FloatingActionButton.extended(
              label: Text('Page ${currentPage! + 1}/$pages'),
              icon: const Icon(Icons.navigate_next),
              onPressed: () async {
                if (pages != null) {
                  final nextPage = (currentPage! + 1) % pages!;
                  await pdfViewController.setPage(nextPage);
                }
              },
            )
          : null,
    );
  }
}