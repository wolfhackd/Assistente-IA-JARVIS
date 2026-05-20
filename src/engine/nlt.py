from google import genai

class NLT:
    def __init__(self, api_key):
        self.client = genai.Client(api_key=api_key)

    def generate_text(self, prompt, model="gemini-3.5-flash"):
        response = self.client.models.generate_content(
            model=model,
            contents=prompt,
        )
        return response.text