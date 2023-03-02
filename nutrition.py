import openai
import configparser
import streamlit as st


@st.cache_data(show_spinner=False)
def generate_nutrition_plan(name, gender, age, height, food, sports):
    config = configparser.ConfigParser()
    config.read("config.ini")
    openai.api_key = config["OPENAI"]["API_KEY"]
    openai.api_key = "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"
    input_text = f"I'm from india, my gender is {gender}, my age is {age}, my height is {height} cm my food preference is {food} can you share me a recommend nutrition plan if am a {sports} player breakfast, lunch, dinner"

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

