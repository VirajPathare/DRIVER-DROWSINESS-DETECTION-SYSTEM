import pytest
from src.detector import DrowsinessDetector

def test_calculate_ear():
    detector = DrowsinessDetector()
    # Mocking eye coordinates (normal open eye)
    eye = [(0, 0), (1, 2), (2, 2), (3, 0), (2, -2), (1, -2)]
    ear = detector.calculate_ear(eye)
    assert ear > 0.2  # Should be open

def test_calculate_mar():
    detector = DrowsinessDetector()
    # Mocking mouth coordinates (closed mouth)
    mouth = [(0, 0), (1, 0), (2, 0), (3, 0), (4, 0), (5, 0), (6, 0), (7, 0)]
    mar = detector.calculate_mar(mouth)
    assert mar < 0.5  # Should be closed
