import yaml

import openai


class OpenAIClient:
    def __init__(self, api_key, **kwargs):
        """
        Initialize the OpenAI client with specific parameters.

        :param api_key: Your OpenAI API key.
        :**kwargs: Additional parameters to pass to the OpenAI API.
        """
        self.api_key = api_key
        self.params = kwargs
        openai.api_key = self.api_key

    def chat_completion(self, prompt):
        """
        Send a query to the OpenAI API.

        :param prompt: The input text to generate responses from.
        :return: The generated text response from the API.
        """
        message = {"role": "system", "content": prompt}
        try:
            response = openai.ChatCompletion.create(
                model=self.params.get("model", "gpt-3.5-turbo"),
                messages=[message],
            )
            return response["choices"][0]["message"]["content"]
        except Exception as e:
            print(f"An error occurred: {e}")
            return None
