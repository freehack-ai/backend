from gradio_client import Client
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


with open("config/config.yaml", "r") as f:
    config = yaml.safe_load(f)

img_client = Client("https://xinyu1205-recognize-anything.hf.space/")
oac = OpenAIClient(
    api_key=config["openai"],
    model="gpt-3.5-turbo",
)


class MyOAC:
    def __init__(self):
        pass

    def __call__(self, tags):
        prompt = f"You are a scary pumpkin during Halloween. There is a person in front of you that you are trying to scare. I took a picture of this person and I am going to describe it to you using tags. Delimited by  {tags}. Write a creepy sentence about this person using details about the person and their surroundings."
        return oac.chat_completion(prompt)
