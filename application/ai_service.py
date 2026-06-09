"""AI Text Generation Service using OpenAI API."""

from openai import OpenAI
import os


def get_ai_client():
    """Initialize OpenAI client with API key from environment variable."""
    api_key = os.getenv("OPENAI_API_KEY")
    if not api_key:
        raise ValueError("OPENAI_API_KEY environment variable is not set.")
    return OpenAI(api_key=api_key)


def generate_text(prompt: str, model: str = "gpt-4o-mini", max_tokens: int = 500) -> str:
    """
    Generate text using OpenAI API.
    
    Args:
        prompt: The input prompt for text generation
        model: The model to use (default: gpt-4o-mini)
        max_tokens: Maximum tokens in the response (default: 500)
    
    Returns:
        Generated text from the API
    """
    try:
        client = get_ai_client()
        
        response = client.chat.completions.create(
            model=model,
            messages=[
                {"role": "user", "content": prompt}
            ],
            max_tokens=max_tokens,
            temperature=0.7
        )
        
        return response.choices[0].message.content
    
    except Exception as error:
        print(f"ERROR! Failed to generate text: {error}.")
        return f"Error: Unable to generate text. {str(error)}"
