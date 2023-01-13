import streamlit as st
import numpy as np
import matplotlib.pyplot as plt

st.set_page_config(layout="wide")

SAMPLE_RATE = 44_100

# Helper function so we can play np.ndarray as audio
def convert_to_audio(y):
    y *= 32767 / np.max(np.abs(y))
    y = y.astype(np.int16)
    return y
    

st.title("Synthesizer")
col1, col2, col3, col4 = st.columns(4)

with col1:
    st.header("Oscillator")
    # TODO: Allow users to select a different signal
    # Later on this will be used to generate audio
    waveform = st.radio("Waveform", options=[])

    # TODO: Let users select a different base_frequency
    base_frequency = st.radio("Base Frequency", options=[220.])

    y = ...

    # TODO: Plot the waveform

# Helper function to plot the amplifier envelope
def plot_adsr_envelope(amp: np.ndarray) -> None:
    amp_duration = len(amp) / SAMPLE_RATE
    t = np.linspace(0, amp_duration, int(amp_duration * SAMPLE_RATE), endpoint=False)
    fig = plt.figure()

    plt.plot(t, amp)
    plt.yticks([])
    st.pyplot(fig)


with col2:
    st.header("Amplifier Envelope")

    # TODO: Implement sliders to get envelope durations (seconds) for the ADSR parameters
    attack = st.slider("Attack")
    decay = ...
    sustain = ...
    release = ...

    # TODO: Implement ADSR amplification over time
    attack_amp = np.array([0.01])
    decay_amp = np.array([2])
    sustain_amp = np.array([0.5, 0.5])
    release_amp = np.array([0])

    # TODO: Combine ADSR signals into one array
    # This will create one single volume envelope
    amp = np.concatenate(
        [
            np.array([])
        ]
    )

    plot_adsr_envelope(amp)

    # TODO: Apply ADSR envelope to our signal
    y = np.array([0.])



with col3:
    st.header("Filter")
    # TODO: Apply a filter to the signal
    # Use https://docs.scipy.org/doc/scipy/reference/generated/scipy.signal.butter.html#scipy-signal-butter

    cutoff = st.slider("Cutoff")


with col4:
    st.header("Output")

    fig = plt.figure()
    plt.plot(y)
    st.pyplot(fig)

    audio = convert_to_audio(y)

    st.audio(audio, sample_rate=SAMPLE_RATE)
