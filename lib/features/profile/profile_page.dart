import 'package:flutter/material.dart';
import 'package:http/http.dart' as http;
import 'dart:convert';
import 'package:skillplay/auth/screens/login_page.dart'; // Adjust path if needed
import 'package:skillplay/data.dart';
import 'package:skillplay/backend_config.dart';

const Color accentColor = Color(0xFF008080); // Teal
const Color lightColor = Colors.white;

class ProfilePage extends StatefulWidget {
  final String email;

  const ProfilePage({super.key, required this.email});

  @override
  State<ProfilePage> createState() => _ProfilePageState();
}

class _ProfilePageState extends State<ProfilePage> {
  String name = '';
  String phone = '';
  int badgeCount = 0;
  bool isLoading = true;
  String errorMessage = '';

  @override
  void initState() {
    super.initState();
    fetchUserProfile();
  }

  Future<void> fetchUserProfile() async {
    try {
      final response = await http.get(Uri.parse('$backendBaseUrl/profile?email=${widget.email}'));
      if (response.statusCode == 200) {
        final data = jsonDecode(response.body);
        setState(() {
          name = data['name'] ?? '';
          phone = data['phone'] ?? '';
          badgeCount = data['count'] ?? 0;
          isLoading = false;
        });
      } else {
        setState(() {
          errorMessage = 'User not found';
          isLoading = false;
        });
      }
    } catch (e) {
      setState(() {
        errorMessage = 'Error fetching profile: $e';
        isLoading = false;
      });
    }
  }

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      backgroundColor: lightColor,
      appBar: AppBar(
        backgroundColor: accentColor,
        title: Text('Profile', style: TextStyle(color: lightColor)),
        iconTheme: IconThemeData(color: lightColor),
      ),
      body: isLoading
          ? Center(child: CircularProgressIndicator())
          : errorMessage.isNotEmpty
              ? Center(child: Text(errorMessage, style: TextStyle(color: Colors.red)))
              : Padding(
                  padding: const EdgeInsets.symmetric(horizontal: 20, vertical: 24),
                  child: Column(
                    crossAxisAlignment: CrossAxisAlignment.center,
                    children: [
                      CircleAvatar(
                        radius: 50,
                        backgroundColor: Colors.grey.shade300,
                        child: Icon(Icons.person, size: 50, color: Colors.grey.shade700),
                      ),
                      const SizedBox(height: 16),
                      Text(name, style: const TextStyle(fontSize: 20, fontWeight: FontWeight.bold)),
                      Text('@${widget.email.split('@')[0]}', style: TextStyle(color: Colors.grey)),
                      const SizedBox(height: 24),
                      _buildInfoRow('Email', widget.email),
                      _buildInfoRow('Phone', phone),
                      _buildBadgeSection(),
                      const Spacer(),
                      TextButton(
                        onPressed: () {
                          UserData.reset();
                          Navigator.pushAndRemoveUntil(
                            context,
                            MaterialPageRoute(builder: (_) => LoginPage()),
                            (route) => false,
                          );
                        },
                        child: const Text('LOG OUT', style: TextStyle(color: Colors.blue, fontSize: 16)),
                      ),
                    ],
                  ),
                ),
    );
  }

  Widget _buildInfoRow(String label, String value) {
    return Padding(
      padding: const EdgeInsets.symmetric(vertical: 8),
      child: Row(
        children: [
          Text('$label:', style: TextStyle(fontSize: 16, fontWeight: FontWeight.bold)),
          SizedBox(width: 8),
          Expanded(child: Text(value, style: TextStyle(fontSize: 16))),
        ],
      ),
    );
  }

  Widget _buildBadgeSection() {
    return Row(
      children: [
        const Icon(Icons.verified, color: Colors.orange),
        const SizedBox(width: 8),
        const Text('Badge', style: TextStyle(fontSize: 16)),
        const Spacer(),
        Container(
          padding: const EdgeInsets.symmetric(horizontal: 12, vertical: 6),
          decoration: BoxDecoration(
            color: Colors.orange.shade100,
            borderRadius: BorderRadius.circular(12),
          ),
          child: Text('$badgeCount', style: const TextStyle(fontSize: 14, fontWeight: FontWeight.bold)),
        ),
      ],
    );
  }
}