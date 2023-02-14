import configparser
import openai


class ExercisePlan:
    def __init__(self, name, gender, age, height, sports):
        self.name = name
        self.gender = gender
        self.age = age
        self.height = height
        self.sports = sports

    def generate_plan(self):
        config = configparser.ConfigParser()
        config.read("config.ini")
        openai.api_key = config["OPENAI"]["API_KEY"]
        input_text = f"I'm from india, my gender is {self.gender}, my age is {self.age}, my height is {self.height} cm. Can you share me a recommend Yoga plan if am a {self.sports} player"

        try:
            response = openai.Completion.create(
                model="text-davinci-003",
                prompt=input_text,
                temperature=0.5,
                max_tokens=500,
                top_p=0.3,
                frequency_penalty=0.5,
                presence_penalty=0
            )
        except Exception as e:
            print(f"An error occurred: {e}")
            return "No nutrition plan could be generated."

        return response["choices"][0]["text"]

