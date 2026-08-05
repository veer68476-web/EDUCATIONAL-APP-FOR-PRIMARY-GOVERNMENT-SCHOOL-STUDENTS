import 'package:flutter/material.dart';
import 'package:http/http.dart' as http;
import 'dart:convert';
import 'login_page.dart'; // Make sure this exists
import 'package:skillplay/backend_config.dart';

class ForgetPasswordPage extends StatefulWidget {
  const ForgetPasswordPage({super.key});
  @override
  // ignore: library_private_types_in_public_api
  _ForgetPasswordPageState createState() => _ForgetPasswordPageState();
}

class _ForgetPasswordPageState extends State<ForgetPasswordPage> {
  final TextEditingController emailController = TextEditingController();
  final TextEditingController otpController = TextEditingController();
  final TextEditingController newPasswordController = TextEditingController();
  final TextEditingController confirmPasswordController = TextEditingController();

  bool otpSent = false;
  bool otpVerified = false;
  bool showNewPassword = false;
  bool showConfirmPassword = false;
  String errorMessage = '';

  Future<void> sendOtp() async {
    final email = emailController.text.trim();
    setState(() => errorMessage = '');

    final emailRegex = RegExp(r'^[\w-\.]+@([\w-]+\.)+[\w]{2,4}$');
    if (email.isEmpty || !emailRegex.hasMatch(email)) {
      setState(() => errorMessage = 'Please enter a valid email address');
      return;
    }

    try {
      final response = await http.post(
        Uri.parse('$backendBaseUrl/send-otp'),
        headers: {'Content-Type': 'application/json'},
        body: jsonEncode({'email': email}),
      );

      if (response.statusCode == 200) {
        setState(() => otpSent = true);
      } else {
        final data = jsonDecode(response.body);
        setState(() => errorMessage = data['error'] ?? 'Failed to send OTP');
      }
    } catch (e) {
      setState(() => errorMessage = 'Server error: $e');
    }
  }

  Future<void> verifyOtp() async {
    final email = emailController.text.trim();
    final otp = otpController.text.trim();
    setState(() => errorMessage = '');

    if (otp.isEmpty) {
      setState(() => errorMessage = 'Please enter the OTP');
      return;
    }

    try {
      final response = await http.post(
        Uri.parse('$backendBaseUrl/verify-otp'),
        headers: {'Content-Type': 'application/json'},
        body: jsonEncode({'email': email, 'otp': otp}),
      );

      if (response.statusCode == 200) {
        setState(() => otpVerified = true);
      } else {
        final data = jsonDecode(response.body);
        setState(() => errorMessage = data['error'] ?? 'Invalid OTP');
      }
    } catch (e) {
      setState(() => errorMessage = 'Server error: $e');
    }
  }

  Future<void> resetPassword() async {
    final email = emailController.text.trim();
    final newPassword = newPasswordController.text;
    final confirmPassword = confirmPasswordController.text;
    setState(() => errorMessage = '');

    if (newPassword != confirmPassword) {
      setState(() => errorMessage = 'Passwords do not match');
      return;
    }

    try {
      final response = await http.post(
        Uri.parse('$backendBaseUrl/reset-password'),
        headers: {'Content-Type': 'application/json'},
        body: jsonEncode({
          'email': email,
          'newPassword': newPassword,
          'confirmPassword': confirmPassword,
        }),
      );

      if (response.statusCode == 200) {
        if (mounted) {
          Navigator.pushReplacement(context, MaterialPageRoute(builder: (_) => LoginPage()));
        }
      } else {
        final data = jsonDecode(response.body);
        if (mounted) {
          setState(() => errorMessage = data['error'] ?? 'Failed to reset password');
        }
      }
    } catch (e) {
      setState(() => errorMessage = 'Server error: $e');
    }
  }

  void resendOtp() {
    sendOtp();
    ScaffoldMessenger.of(context).showSnackBar(SnackBar(content: Text('OTP resent')));
  }

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(title: Text('Reset Password'), automaticallyImplyLeading: false),
      body: Center(
        child: Container(
          padding: EdgeInsets.all(24),
          margin: EdgeInsets.symmetric(horizontal: 24),
          decoration: BoxDecoration(
            color: Colors.white,
            borderRadius: BorderRadius.circular(20),
            boxShadow: [BoxShadow(color: Colors.black26, blurRadius: 10)],
          ),
          child: Column(
            mainAxisSize: MainAxisSize.min,
            children: [
              if (errorMessage.isNotEmpty)
                Padding(
                  padding: const EdgeInsets.only(bottom: 12),
                  child: Text(errorMessage, style: TextStyle(color: Colors.red)),
                ),
              TextField(
                controller: emailController,
                decoration: InputDecoration(labelText: 'Email'),
                keyboardType: TextInputType.emailAddress,
              ),
              SizedBox(height: 16),
              if (!otpSent)
                ElevatedButton(onPressed: sendOtp, child: Text('Send OTP'))
              else if (!otpVerified) ...[
                TextField(
                  controller: otpController,
                  decoration: InputDecoration(labelText: 'Enter OTP'),
                ),
                SizedBox(height: 16),
                ElevatedButton(onPressed: verifyOtp, child: Text('Verify OTP')),
                TextButton(onPressed: resendOtp, child: Text('Resend OTP')),
              ] else ...[
                TextField(
                  controller: newPasswordController,
                  obscureText: !showNewPassword,
                  decoration: InputDecoration(
                    labelText: 'New Password',
                    suffixIcon: IconButton(
                      icon: Icon(showNewPassword ? Icons.visibility_off : Icons.visibility),
                      onPressed: () => setState(() => showNewPassword = !showNewPassword),
                    ),
                  ),
                ),
                SizedBox(height: 16),
                TextField(
                  controller: confirmPasswordController,
                  obscureText: !showConfirmPassword,
                  decoration: InputDecoration(
                    labelText: 'Confirm Password',
                    suffixIcon: IconButton(
                      icon: Icon(showConfirmPassword ? Icons.visibility_off : Icons.visibility),
                      onPressed: () => setState(() => showConfirmPassword = !showConfirmPassword),
                    ),
                  ),
                ),
                SizedBox(height: 20),
                ElevatedButton(onPressed: resetPassword, child: Text('Submit')),
              ],
            ],
          ),
        ),
      ),
    );
  }
}