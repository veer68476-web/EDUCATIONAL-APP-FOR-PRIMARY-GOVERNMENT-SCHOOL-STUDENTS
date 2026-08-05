# SkillPlay

SkillPlay is an educational Flutter application for students that provides textbooks, answer sheets, video content, and interactive learning resources.

## Features

- PDF viewer for class textbooks and answer keys
- Video playback support using YouTube and local assets
- Google Sign-In integration
- Persistent user preferences with shared preferences
- Web content support through in-app browser views

## Run the App

These steps are written so anyone can run the project from the repository.

### 1. Install Flutter

If Flutter is not already installed, follow the official guide:
- https://docs.flutter.dev/get-started/install

### 2. Open the project folder

Open `D:\flutter\skillplay` in Visual Studio Code or your preferred IDE.

### 3. Get packages

Open a terminal in the project folder and run:

```bash
flutter pub get
```

### 4. Choose a device

Use `flutter devices` to list available devices and platforms.

```bash
flutter devices
```

### 5. Run the app

- To run on the default connected device:

```bash
flutter run
```

- To run on Windows:

```bash
flutter run -d windows
```

- To run on Android:

```bash
flutter run -d android
```

- To run on Chrome/web:

```bash
flutter run -d chrome
```

### 6. Stop the app

Press `q` in the terminal or close the app window.

## Troubleshooting

- If `flutter pub get` fails, check your internet connection and SDK installation.
- If a device is not found, make sure an emulator, simulator, or physical device is connected and recognized.
- If the app fails to launch, run `flutter doctor` and fix any issues shown.

```bash
flutter doctor
```

## Project Structure

- `lib/main.dart` - App entrypoint
- `lib/welcome_page.dart` - Initial onboarding screen
- `lib/features/home_page.dart` - Main application screen
- `lib/data.dart` - User data and app state
- `assets/` - PDF textbooks, answer sheets, and images

## Important Dependencies

- `flutter_pdfview`
- `flutter_inappwebview`
- `youtube_player_flutter`
- `video_player`
- `url_launcher`
- `google_sign_in`
- `shared_preferences`

## Notes

This app is configured as a private Flutter application (`publish_to: none`).

If you need to update assets or supported content, modify `pubspec.yaml` under the `flutter.assets` section.
