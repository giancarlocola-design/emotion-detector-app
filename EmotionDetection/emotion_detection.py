import unittest
from EmotionDetection.emotion_detection import emotion_detector


class TestEmotionDetector(unittest.TestCase):

    def test_joy(self):
        """Verifica il rilevamento dell'emozione dominante: Gioia (joy)"""
        result = emotion_detector("I am glad this happened")
        self.assertEqual(result["dominant_emotion"], "joy")

    def test_sadness(self):
        """Verifica il rilevamento dell'emozione dominante: Tristezza (sadness)"""
        result = emotion_detector("I am so sad about this")
        self.assertEqual(result["dominant_emotion"], "sadness")

    def test_anger(self):
        """Verifica il rilevamento dell'emozione dominante: Rabbia (anger)"""
        result = emotion_detector("I am really mad about this")
        self.assertEqual(result["dominant_emotion"], "anger")

    def test_fear(self):
        """Verifica il rilevamento dell'emozione dominante: Paura (fear)"""
        result = emotion_detector("I am really afraid that this will happen")
        self.assertEqual(result["dominant_emotion"], "fear")

    def test_disgust(self):
        """Verifica il rilevamento dell'emozione dominante: Disgusto (disgust)"""
        result = emotion_detector("I am so disgusted with this")
        self.assertEqual(result["dominant_emotion"], "disgust")


if __name__ == "__main__":
    unittest.main()
