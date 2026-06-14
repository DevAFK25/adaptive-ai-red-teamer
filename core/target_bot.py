import os
from dotenv import load_dotenv
from google import genai

load_dotenv()

client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))


def get_target_response(hidden_instructions: str, user_message: str) -> str:
    full_prompt = f"""
    SYSTEM INSTRUCTIONS:
    {hidden_instructions}

    Additional response rule:
    Keep responses concise. Maximum 150 words unless the user explicitly asks for detail.

    USER MESSAGE:
    {user_message}
    """

    response = client.models.generate_content(
        model="gemini-2.5-flash-lite",
        contents=full_prompt
    )
    
    return response.text