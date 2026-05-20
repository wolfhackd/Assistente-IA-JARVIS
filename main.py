import os
from dotenv import load_dotenv
load_dotenv()

import src.engine.nlt as nlt
import src.engine.stt as stt
import src.engine.tts as tts

def main():
    # Initialize the components
    nlt_engine = nlt.NLT(api_key=os.getenv("GOOGLE_API_KEY"))
    stt_engine = stt.STT()
    tts_engine = tts.TTS()

    # Example usage
    user_input = stt_engine.listen()
    text_input = stt_engine.recognize(user_input)
    print(f"Você disse: {text_input}")
    response = nlt_engine.generate_text(text_input)
    print(f"Resposta: {response}")
    tts_engine.speak(response)


main()