import 'package:flutter/material.dart';
import 'data.dart';
import 'welcome_page.dart';
import 'features/home_page.dart';

void main() async {
  WidgetsFlutterBinding.ensureInitialized();
  runApp(const SkillPlay());
}

class SkillPlay extends StatelessWidget {
  const SkillPlay({super.key});

  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      title: 'Educational App',
      debugShowCheckedModeBanner: false,
      home: UserData.choice == 0
          ? WelcomePage()
          : HomePage(email: UserData.email),
    );
  }
}