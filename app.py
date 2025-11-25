import streamlit as st
import requests
import subprocess
import os

st.title("Simple Game Generator")

game_name = st.text_input("Game Name", "snake")


URL = "https://chakravardhan06.app.n8n.cloud/webhook-test/2323bb11-348e-4d84-9825-e1c08be39984"


if st.button("Generate"):
    try:
        # Send only game name
        r = requests.post(URL, json={"game": game_name})
        data = r.json()

        # Handle list/dictionary response
        output = data[0]["output"] if isinstance(data, list) else data["output"]

        # Clean code
        code = (
            output.replace("```python", "")
                  .replace("```", "")
                  .strip()
        )

        file_name = f"{game_name}.py"

        with open(file_name, "w") as f:
            f.write(code)

        st.success(f"{file_name} created successfully!")

    except Exception as e:
        st.error(f"Error: {e}")

if st.button("Play"):
    file_name = f"{game_name}.py"

    if os.path.exists(file_name):
        subprocess.Popen([
            "osascript",
            "-e",
            f'tell application "Terminal" to do script "python3 \\"{os.path.abspath(file_name)}\\""'
        ])
        st.success("Game started!")
    else:
        st.error("Please generate the game first!")
