"""AI Text and Image Generation Service using OpenAI API."""

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


def generate_image(prompt: str, model: str = "dall-e-3", size: str = "1024x1024", quality: str = "standard") -> str:
    """
    Generate image using OpenAI DALL-E API.
    
    Args:
        prompt: The input prompt for image generation
        model: The model to use (default: dall-e-3)
        size: Image size - "1024x1024", "1024x1792", "1792x1024" (default: 1024x1024)
        quality: Image quality - "standard" or "hd" (default: standard)
    
    Returns:
        Base64 encoded image data or error message
    """
    try:
        client = get_ai_client()
        
        response = client.images.generate(
            model=model,
            prompt=prompt,
            size=size,
            quality=quality,
            n=1,
            response_format="b64_json"
        )
        
        # Return base64 encoded image
        image_base64 = response.data[0].b64_json
        return f"data:image/png;base64,{image_base64}"
    
    except Exception as error:
        print(f"ERROR! Failed to generate image: {error}.")
        return f"Error: Unable to generate image. {str(error)}"
