import openai

class AIAgent:
    """
    AIAgent is a class for interacting with OpenAI's API to generate responses
    based on user-provided prompts.

    Attributes:
        model (str): The OpenAI model to use for generating responses.
        temperature (float): The temperature setting for the response generation.
    """

    def __init__(self, model: str = "text-davinci-003", temperature: float = 0.7):
        """
        Initializes the AIAgent with the specified model and temperature.

        Args:
            model (str): The OpenAI model to use (default is "text-davinci-003").
            temperature (float): Controls the randomness of the output (default is 0.7).
        """
        self.model = model
        self.temperature = temperature

    def generate_response(self, prompt: str) -> str:
        """
        Generate a response based on the given prompt.

        Args:
            prompt (str): The input text to generate a response for.

        Returns:
            str: The generated response from the OpenAI API.
        """
        try:
            response = openai.Completion.create(
                engine=self.model,
                prompt=prompt,
                temperature=self.temperature,
                max_tokens=150,
            )
            return response.choices[0].text.strip()
        except Exception as e:
            return f"Error: {e}"
