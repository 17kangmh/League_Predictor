import streamlit as st
import pickle
import numpy as np


def load_model():
    loaded_model = pickle.load(open("lol_pred_model.pkl", "rb"))
    return loaded_model


loaded_model = load_model()


def show_page():
    st.title("League of Legends Win Prediction (In the First Ten Minutes)")

    blueKills = st.slider("Number of Blue Side Kills", 0, 15, 0, 1)
    redKills = st.slider("Number of Red Side Kills", 0, 15, 0, 1)
    blueTowersDestroyed = st.slider("Number of Blue Towers Destroyed", 0, 2, 0, 1)
    blueDragonKills = st.slider("Numbers of Blue Side Dragon Kills", 0, 2, 0, 1)

    calculate = st.button("Calculate Win Percentage")
    if calculate:
        data = np.array([[blueKills, redKills, blueTowersDestroyed, blueDragonKills]])

        blueWinChance = loaded_model.predict(data)
        st.subheader(
            f"The Predicted Win Percentage of Blue Side is {blueWinChance[0]:.2%}"
        )
