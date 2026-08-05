import 'package:flutter/material.dart';
import 'package:http/http.dart' as http;
import 'dart:convert';
import 'package:skillplay/features/home_page.dart';
import 'register_page.dart';
import 'forget_password_page.dart';
import 'package:skillplay/data.dart';
import 'package:skillplay/backend_config.dart';

class LoginPage extends StatefulWidget {
  const LoginPage({super.key});
  @override
  State<LoginPage> createState() => _LoginPageState();
}

class _LoginPageState extends State<LoginPage> {
  final TextEditingController emailController = TextEditingController();
  final TextEditingController passwordController = TextEditingController();

  bool showPassword = false;
  String errorMessage = '';

  Future<void> loginUser() async {
    final email = emailController.text.trim();
    final password = passwordController.text;
    final currentContext = context;

    setState(() {
      errorMessage = '';
    });

    if (email.isEmpty || password.isEmpty) {
      setState(() {
        errorMessage = 'Please enter both email and password';
      });
      return;
    }

    final emailRegex = RegExp(r'^[\w-\.]+@([\w-]+\.)+[\w]{2,4}$');
    if (!emailRegex.hasMatch(email)) {
      setState(() {
        errorMessage = 'Please enter a valid email address';
      });
      return;
    }

    try {
      final response = await http.post(
        Uri.parse('$backendBaseUrl/login'),
        headers: {'Content-Type': 'application/json'},
        body: jsonEncode({
          'email': email,
          'password': password,
        }),
      );

      if (response.statusCode == 200) {
        UserData.setUser(email);
        if (mounted) {
          // ignore: use_build_context_synchronously
          Navigator.push(
            currentContext, // ignore: use_build_context_synchronously
            MaterialPageRoute(builder: (_) => HomePage(email: email)),
          );
        }
      } else {
        final data = jsonDecode(response.body);
        if (mounted) {
          setState(() {
            errorMessage = data['error'] ?? 'Login failed';
          });
        }
      }
    } catch (e) {
      if (!mounted) return;
      setState(() {
        errorMessage = 'Error connecting to server: $e';
      });
    }
  }

  void _navigateToRegister(BuildContext context) {
    Navigator.push(context, MaterialPageRoute(builder: (_) => RegisterPage()));
  }

  void _navigateToForgotPassword(BuildContext context) {
    Navigator.push(context, MaterialPageRoute(builder: (_) => ForgetPasswordPage()));
  }

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(title: Text('Login'), automaticallyImplyLeading: false),
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
                  child: Text(
                    errorMessage,
                    style: TextStyle(color: Colors.red, fontWeight: FontWeight.bold),
                  ),
                ),
              TextField(
                controller: emailController,
                decoration: InputDecoration(labelText: 'Email'),
                keyboardType: TextInputType.emailAddress,
              ),
              SizedBox(height: 16),
              TextField(
                controller: passwordController,
                obscureText: !showPassword,
                decoration: InputDecoration(
                  labelText: 'Password',
                  suffixIcon: IconButton(
                    icon: Icon(showPassword ? Icons.visibility_off : Icons.visibility),
                    onPressed: () {
                      setState(() {
                        showPassword = !showPassword;
                      });
                    },
                  ),
                ),
              ),
              SizedBox(height: 20),
              ElevatedButton(
                onPressed: () => loginUser(),
                child: Text('Login'),
              ),
              TextButton(
                onPressed: () => _navigateToForgotPassword(context),
                child: Text('Forgot password?'),
              ),
              SizedBox(height: 10),
              Row(
                mainAxisAlignment: MainAxisAlignment.center,
                children: [
                  Text("Don't have an account? "),
                  GestureDetector(
                    onTap: () => _navigateToRegister(context),
                    child: Text('Register', style: TextStyle(color: Colors.blue)),
                  ),
                ],
              ),
            ],
          ),
        ),
      ),
    );
  }
}