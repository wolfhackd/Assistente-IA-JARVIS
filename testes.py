import src.engine.stt as stt
import src.engine.tts as tts

assistente_stt = stt.STT()
assistente_tts = tts.TTS()

audio_gravado = assistente_stt.listen()
texto = assistente_stt.recognize(audio_gravado)

assistente_tts.speak(f"Você disse: {texto}")