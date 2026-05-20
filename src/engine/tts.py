#  Texto Para Audio / Text to Speech

import pyttsx3

class TTS:
    def __init__(self):
        self.engine = pyttsx3.init()

    def speak(self, text):
        self.engine.say(text)
        self.engine.runAndWait()

# OBS: Voz robotizada/ Melhoria de voz

# Teste do módulo TTS

if __name__ == "__main__":

    assistente = TTS()

    assistente.speak("Olá, tudo bem?")