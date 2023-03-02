import streamlit as st
from exercise import generate_exercise_plan
from nutrition import generate_nutrition_plan
from streamlit_option_menu import option_menu

st.set_page_config(
    page_title="Chessensei",
    page_icon=""
)
hide_streamlit_style = """
            <style>
            #MainMenu {visibility: hidden;}
            footer {visibility: hidden;}
            </style>
            """
st.markdown(hide_streamlit_style, unsafe_allow_html=True)


def main():

    # with st.sidebar:
    selected = option_menu(
        menu_title="Chessensei Recommendation Tools",
        options=["Exercise", "Nutrition"],
        icons=["bicycle", "clipboard"],
        menu_icon="magic",
        default_index=0,
        orientation="horizontal",
        styles={
            "menu-title": {"text-align": "center"}
        }
    )

    if selected == "Exercise":
        st.title("Exercise Planner 🧘")

        name = st.text_input("Name:", max_chars=50)
        age = st.number_input('Age:', min_value=1, max_value=100, step=1, key="eage")
        height = st.number_input('Height(in cm):', min_value=1, max_value=300, step=1)
        gender = st.radio("Gender:", ('Male', 'Female'))
        sports = 'chess'

        # create button
        if st.button("Submit"):
            with st.spinner('Please wait...'):
                message = generate_exercise_plan(name, gender, age, height, sports)
                # update text area with message
                print(message)
                print("*" * 20)
            st.success('Your report has been generated!!🥳🥳')
            msg = "1" + message.replace("?", "").partition("1")[2].lstrip()
            st.text_area("Exercise plan:", value=msg, height=500, max_chars=None, key=None,
                         help=None, on_change=None, args=None, kwargs=None, disabled=True)

    if selected == "Nutrition":
        st.title("Nutrition Planner 🍛")

        name = st.text_input("Name:", max_chars=100)
        age = st.number_input('Age:', min_value=1, max_value=100, step=1, key="nage")
        height = st.number_input('Height(in cm):', min_value=1, max_value=300, step=1)
        gender = st.radio("Gender:", ('Male', 'Female'))
        food = st.radio("Food Preferences:", ('Veg', 'Non-veg'))
        sports = 'chess'

        # create button
        if st.button("Submit"):
            with st.spinner('Please wait...'):
                message = generate_nutrition_plan(name, gender, age, height, food, sports)
                # update text area with message
                print("*" * 20)
                print(message)
                print("*" * 20)
            st.success('Your report has been generated!🥳🥳')
            breakfast_data = message.partition("Lunch")[0].partition("Breakfast:")[2].rstrip().lstrip().replace("-",
                                                                                                                "- ")
            lunch_data = message.partition("Dinner:")[0].partition("Lunch:")[2].rstrip().lstrip().replace("-", "- ")
            dinner_data = message.partition("Dinner:")[2].partition("Snacks")[0].rstrip().lstrip().replace("-", "- ")

            st.text_area("Nutrition plan (Breakfast):", value=breakfast_data, height=None, max_chars=None, key=None,
                         help=None, on_change=None, args=None, kwargs=None, disabled=True)
            st.text_area("Nutrition plan (Lunch):", value=lunch_data, height=None, max_chars=None, key=None, help=None,
                         on_change=None, args=None, kwargs=None, disabled=True)
            st.text_area("Nutrition plan (Dinner):", value=dinner_data, height=None, max_chars=None, key=None,
                         help=None,
                         on_change=None, args=None, kwargs=None, disabled=True)


if __name__ == "__main__":
    main()

