import 'package:flutter/material.dart';
import 'package:flutter_pdfview/flutter_pdfview.dart';

class FlutterPDFView extends StatefulWidget {
  final String assetPath; // This is now a local file path

  const FlutterPDFView({required this.assetPath, super.key});

  @override
  // ignore: library_private_types_in_public_api
  _FlutterPDFViewState createState() => _FlutterPDFViewState();
}

class _FlutterPDFViewState extends State<FlutterPDFView> {
  int? pages = 0;
  int? currentPage = 0;
  bool isReady = false;
  late PDFViewController pdfViewController;

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        title: const Text('PDF Viewer', style: TextStyle(color: Colors.white)),
        backgroundColor: Colors.deepPurple.shade700,
        iconTheme: const IconThemeData(color: Colors.white),
      ),
      body: PDFView(
        filePath: widget.assetPath, // ✅ Use the local file path directly
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