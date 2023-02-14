import openai
import configparser


class NutritionPlan:
    def __init__(self, name, gender, age, height, food, sports):
        self.name = name
        self.gender = gender
        self.age = age
        self.height = height
        self.food = food
        self.sports = sports

    def generate_plan(self):
        config = configparser.ConfigParser()
        config.read("config.ini")
        openai.api_key = config["OPENAI"]["API_KEY"]
        openai.api_key = "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"
        input_text = f"I'm from india, my gender is {self.gender}, my age is {self.age}, my height is {self.height} cm my food preference is {self.food} can you share me a recommend nutrition plan if am a {self.sports} player breakfast, lunch, dinner"

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
        except Exception as ex:
            print(f"An error occurred: {ex}")
            return
        return response["choices"][0]["text"]

