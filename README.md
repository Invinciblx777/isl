# 🤟 Indian Sign Language Recognition System

A production-grade Python desktop application for real-time Indian Sign Language (ISL) recognition with continuous sentence formation, multi-language text-to-speech, and accessibility-first design.

## ✨ Features

### Three Recognition Modes
- **🔴 Sentence Mode**: Recognize daily-life ISL phrases and form natural sentences
- **🟡 Alphabet Mode**: Recognize A-Z letters for name spelling
- **🟢 Numbers Mode**: Recognize 0-20 using finger counting

### Key Capabilities
- ✅ Real-time hand detection using MediaPipe
- ✅ 10-second continuous gesture recording
- ✅ Natural sentence formation from multiple gestures
- ✅ Multi-language TTS (English, Hindi, Tamil)
- ✅ Accessibility-first UI design
- ✅ Session logging for therapists/caregivers

## 🚀 Quick Start

### 1. Install Dependencies

```bash
cd /home/invinciblx777/mvp
pip install -r requirements.txt
```

### 2. Run the Application

```bash
python main.py
```

## 📋 Supported Gestures

### Sentence Mode (Daily Life)
| Category | Gestures |
|----------|----------|
| Emergency | HELP, EMERGENCY, DOCTOR, HOSPITAL, PAIN, POLICE |
| Greetings | HELLO, BYE, HOW_ARE_YOU, I_AM_FINE |
| Essential | THANK_YOU, PLEASE, SORRY, YES, NO |
| Actions | STOP, COME_HERE |
| Needs | WATER, FOOD, WASHROOM |
| Identity | I, AM, NAME |

### How to Sign (Examples)
- **HELLO**: Wave with open palm, all fingers extended
- **HELP**: Both hands raised with palms open
- **YES**: Closed fist with nodding motion
- **NO**: Peace sign (V) with palm forward
- **THANK_YOU**: Flat hand moving from chin outward
- **WATER**: W shape (3 fingers) moving to mouth

## 🎯 Usage Example

1. Launch the application
2. Select **Mode: Sentence** and **Language: English**
3. Click **▶ Start Recording**
4. Sign: HELLO → I → AM → [spell your name]
5. The system outputs: **"Hello, I am [Name]."**
6. The sentence is spoken aloud automatically

## 📁 Project Structure

```
mvp/
├── main.py                 # Application entry point
├── config.py               # Configuration settings
├── requirements.txt        # Dependencies
├── modules/
│   ├── hand_detector.py    # MediaPipe hand detection
│   ├── gesture_recognizer.py # Gesture recognition (3 modes)
│   ├── sentence_former.py  # Continuous gesture → sentence
│   ├── tts_engine.py       # Multi-language TTS
│   └── logger.py           # Session logging
├── ui/
│   ├── app.py              # Main application UI
│   └── styles.py           # Accessibility-first styling
└── data/
    └── logs/               # Session logs (CSV)
```

## 🌐 Language Support

| Language | TTS Engine | Status |
|----------|------------|--------|
| English  | pyttsx3    | ✅ Full support |
| Hindi    | gTTS       | ✅ Full support |
| Tamil    | gTTS       | ✅ Full support |

## ♿ Accessibility Features

- Large, readable fonts (16px minimum)
- High contrast dark theme
- Large click targets (48px minimum)
- Clear visual feedback
- Keyboard navigation support

## 📊 Logging

Sessions are automatically logged to `data/logs/session_YYYY-MM-DD.csv` with:
- Timestamp
- Mode used
- Language
- Detected gestures
- Final output
- Confidence score

## ⚙️ Configuration

Edit `config.py` to customize:
- Camera settings (index, resolution)
- Detection confidence thresholds
- Recording duration (default: 10 seconds)
- UI colors and fonts

## 🔧 Requirements

- Python 3.8+
- Webcam
- Internet connection (for Tamil/Hindi TTS)

## 📝 License

Built for accessibility and inclusion. Use responsibly.
