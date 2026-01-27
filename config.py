"""
Configuration settings for ISL Recognition System
"""

import os

# Application Info
APP_NAME = "ISL Recognition System"
APP_VERSION = "1.0.0"

# Paths
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DATA_DIR = os.path.join(BASE_DIR, "data")
LOGS_DIR = os.path.join(DATA_DIR, "logs")
ASSETS_DIR = os.path.join(BASE_DIR, "assets")

# Ensure directories exist
os.makedirs(LOGS_DIR, exist_ok=True)
os.makedirs(ASSETS_DIR, exist_ok=True)

# Camera Settings
CAMERA_INDEX = 0
CAMERA_WIDTH = 640
CAMERA_HEIGHT = 480
CAMERA_FPS = 30
FRAME_SKIP = 1  # Process every frame for smoother detection

# Hand Detection Settings
MAX_HANDS = 2
MIN_DETECTION_CONFIDENCE = 0.65
MIN_TRACKING_CONFIDENCE = 0.55
LANDMARK_SMOOTHING_FACTOR = 0.6  # Higher = smoother, lower = more responsive

# Gesture Recognition Settings
GESTURE_BUFFER_DURATION = 10.0  # seconds
GESTURE_HOLD_TIME = 0.3  # seconds to hold gesture for recognition (faster)
PAUSE_THRESHOLD = 0.6  # seconds of stillness to detect pause
MOTION_THRESHOLD = 0.02  # normalized motion threshold

# Recognition Modes
MODE_SENTENCE = "sentence"
MODE_ALPHABET = "alphabet"
MODE_NUMBERS = "numbers"

# Supported Languages
LANGUAGES = {
    "English": "en",
    "Hindi": "hi",
    "Tamil": "ta"
}

# UI Settings
WINDOW_WIDTH = 1200
WINDOW_HEIGHT = 750
FONT_FAMILY = "Segoe UI"
FONT_SIZE_NORMAL = 14
FONT_SIZE_LARGE = 18
FONT_SIZE_HEADER = 24
FONT_SIZE_OUTPUT = 28

# Colors (Accessibility-focused high contrast)
COLORS = {
    "bg_dark": "#1a1a2e",
    "bg_medium": "#16213e",
    "bg_light": "#0f3460",
    "accent": "#e94560",
    "accent_hover": "#ff6b6b",
    "text_primary": "#ffffff",
    "text_secondary": "#b8b8b8",
    "success": "#4ecca3",
    "warning": "#ffc107",
    "error": "#ff4757"
}

# =============================================================================
# BIS COMPLIANCE SETTINGS (IS 13252 & IS 16333)
# =============================================================================

# Compliance Version
BIS_COMPLIANCE_VERSION = "1.0.0"

# IS 13252 - IT Equipment Safety Settings
IS_13252_SETTINGS = {
    "enabled": True,
    "input_validation": True,
    "error_monitoring": True,
    "resource_tracking": True,
    "audit_logging": True,
    "max_error_threshold": 100,  # Max errors before degraded mode
    "health_check_interval": 60,  # Seconds between health checks
}

# IS 16333 - Camera System Safety Settings  
IS_16333_SETTINGS = {
    "enabled": True,
    "camera_validation": True,
    "frame_quality_check": True,
    "min_brightness": 30,
    "max_brightness": 225,
    "min_contrast": 20,
    "privacy_mode": False,  # Enable to prevent frame storage
    "max_error_frames": 50,  # Max consecutive error frames before warning
}

# Safety Logging Settings
SAFETY_LOG_FILE = os.path.join(LOGS_DIR, "safety_audit.log")
SAFETY_LOG_MAX_SIZE = 10 * 1024 * 1024  # 10 MB
SAFETY_LOG_BACKUP_COUNT = 5

# Compliance Metadata
COMPLIANCE_STANDARDS = [
    "IS 13252 - Information Technology Equipment Safety",
    "IS 16333 - Camera-based Systems for Assistive Technology (Ready)"
]
