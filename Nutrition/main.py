import streamlit as st
from nutrition import NutritionPlan


def main():
    st.title("Nutrition Plan Recommender 🍛")

    name = st.text_input("Name:", max_chars=100)
    age = st.number_input('Age:', min_value=1, max_value=100, step=1)
    height = st.number_input('Height(in cm):', min_value=1, max_value=300, step=1)
    gender = st.radio("Gender:", ('Male', 'Female'))
    food = st.radio("Food Preferences:", ('Veg', 'Non-veg'))
    sports = 'chess'

    # create button
    if st.button("Submit"):
        with st.spinner('Please wait...'):
            nutrition_plan = NutritionPlan(name, gender, age, height, food, sports)
            message = nutrition_plan.generate_plan()
            # update text area with message
            print("*" * 20)
            print(message)
            print("*"*20)
        st.success('Your report has been generated!🥳🥳')
        breakfast_data = message.partition("Lunch")[0].partition("Breakfast:")[2].rstrip().lstrip().replace("-", "- ")
        lunch_data = message.partition("Dinner:")[0].partition("Lunch:")[2].rstrip().lstrip().replace("-", "- ")
        dinner_data = message.partition("Dinner:")[2].partition("Snacks")[0].rstrip().lstrip().replace("-", "- ")

        st.text_area("Nutrition plan (Breakfast):", value=breakfast_data, height=None, max_chars=None, key=None,
                     help=None, on_change=None, args=None, kwargs=None, disabled=True)
        st.text_area("Nutrition plan (Lunch):", value=lunch_data, height=None, max_chars=None, key=None, help=None,
                     on_change=None, args=None, kwargs=None, disabled=True)
        st.text_area("Nutrition plan (Dinner):", value=dinner_data, height=None, max_chars=None, key=None, help=None,
                     on_change=None, args=None, kwargs=None, disabled=True)


if __name__ == "__main__":
    main()
