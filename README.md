# Audio Synthesis in Python

## Installation

You can choose between a) devcontainer b) poetry c) requirements.txt

A. DevContainer using Docker
See https://code.visualstudio.com/docs/devcontainers/tutorial on how to set it up.

B. Poetry
Make sure you have `poetry`: https://python-poetry.org/docs/#installation
Then, install the project:
```sh
poetry install
``` 

C. requirements.txt

```sh
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

# Exercise 1: Synthesizing a single sound
1. Run Jupyter Lab
```sh
# Poetry
poetry run jupyter lab

# Others
jupyter lab
``` 

2. Open the url given by Jupyter Lab. When you've opened it, find and open `synthesizer/notebook.ipynb`.

3. Fill in the gaps!


# Exercise 2: Play a melody using a midi file
1. Open `synthesizer/midi_to_audio.ipynb`
2. Fill in the gaps to play the melody


# Exercise 3: Allowing users to control your synthesizers
1. Run `streamlit run synthesizer/main.py`
2. Fill in the gaps in `synthesizer/main.py`, have a look at the [Streamlit docs](https://docs.streamlit.io/library/get-started/create-an-app)

