import requests

class PaddleSpeechTTSEngine:

    def __init__(self, url: str):
        self._url = url

    def get_tts(self, text: str):
        """ Makes request to OpenAI TTS engine to convert text into audio"""
        data: dict = {
            "text": text,
        }
        return requests.post(self._url, json=data)

    @staticmethod
    def get_supported_langs() -> list:
        """Returns list of supported languages. Note: the model determines the provides language automatically."""
        return ["zh"]