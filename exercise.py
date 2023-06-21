import configparser
import openai
import streamlit as st


@st.cache_data(show_spinner=False)
def generate_exercise_plan(name, gender, age, height, sports):
    # config = configparser.ConfigParser()
    # config.read("config.ini")
    # openai.api_key = config["OPENAI"]["API_KEY"]
    openai.api_key = "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"
    input_text = f"I'm from india, my gender is {gender}, my age is {age}, my height is {height} cm. Can you share me a recommend Yoga plan if am a {sports} player"

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

