# Audio Para texto / Speech to Text

import speech_recognition as sr

class STT:
    def __init__(self):
        self.recognizer = sr.Recognizer()

    def listen(self):
        with sr.Microphone() as source:
            print("Listening...")
            audio = self.recognizer.listen(source)
        return audio

    def recognize(self, audio):
        try:
            text = self.recognizer.recognize_google(audio, language='pt-BR')
            return text
        except sr.UnknownValueError:
            print("Could not understand audio")
        except sr.RequestError as e:
            print(f"Could not request results; {e}")


# Teste do módulo STT
# if __name__ == "__main__":

#     assistente = STT()

#     audio_gravado = assistente.listen()
#     texto = assistente.recognize(audio_gravado)

#     print(f"Você disse: {texto}")