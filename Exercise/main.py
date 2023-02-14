import streamlit as st
from exercise import ExercisePlan


def main():
    st.title("Exercise Recommender 🧘")

    name = st.text_input("Name:", max_chars=50)
    age = st.number_input('Age:', min_value=1, max_value=100, step=1)
    height = st.number_input('Height(in cm):', min_value=1, max_value=300, step=1)
    gender = st.radio("Gender:", ('Male', 'Female'))
    sports = 'chess'

    # create button
    if st.button("Submit"):
        with st.spinner('Please wait...'):
            nutrition_plan = ExercisePlan(name, gender, age, height, sports)
            message = nutrition_plan.generate_plan()
            # update text area with message
            print(message)
            print("*"*20)
        st.success('Your report has been generated!!🥳🥳')
        msg = "1" + message.replace("?", "").partition("1")[2].lstrip()
        st.text_area("Exercise plan:", value=msg, height=500, max_chars=None, key=None,
                     help=None, on_change=None, args=None, kwargs=None, disabled=True)


if __name__ == "__main__":
    main()
