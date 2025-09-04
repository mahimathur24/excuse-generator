import streamlit as st
import random
import datetime

st.set_page_config(page_title="Excuse Generator", layout="centered")

st.markdown(
    """
    <style>
    body {background-color: #ffeef8;}
    [data-testid="stSidebar"] {background-color: #fff0f6;}
    .stButton>button {
        background-color: #ff6fb5;
        color: white;
        border: none;
        border-radius: 8px;
        padding: 8px 16px;
    }
    .stButton>button:hover {opacity: 0.9;}
    h1 {color: #c2185b;}
    </style>
    """,
    unsafe_allow_html=True
)

st.title("🌸 Simple Excuse Generator")
st.write("Type your situation and generate a polite excuse.")

scenario = st.selectbox("Choose a scenario", ["Work", "School", "Social", "Family", "Other"])
tone = st.selectbox("Choose a tone", ["Formal", "Casual", "Apologetic"])
situation = st.text_area("Describe your situation:")

templates = {
    "Work": [
        "I won't be able to attend work {when} because {reason}. I’ll make sure to catch up soon.",
        "I need to take some time off on {when} due to {reason}. Thank you for understanding."
    ],
    "School": [
        "I couldn't attend class {when} because {reason}. I'll complete the missed work.",
        "I need more time for the assignment due {when} because {reason}. Thanks for understanding."
    ],
    "Social": [
        "I'm really sorry, I can’t join {when} because {reason}. Can we reschedule?",
        "I won’t be able to come to {event} because {reason}. Hope you all have fun!"
    ],
    "Family": [
        "I need to be with family {when} because {reason}. I hope you understand.",
        "There’s a family matter {when}, so I can’t make it. Sorry for the inconvenience."
    ],
    "Other": [
        "I won’t be available {when} because {reason}. Thanks for understanding."
    ]
}

if st.button("Generate Excuse"):
    if not situation.strip():
        st.warning("Please describe your situation first.")
    else:
        reason = situation
        when = "today"
        template = random.choice(templates.get(scenario, templates["Other"]))
        excuse = template.format(reason=reason, when=when, event="the event")
        
        if tone == "Apologetic":
            excuse = "I sincerely apologize. " + excuse
        elif tone == "Formal":
            excuse = "Dear Sir/Madam, " + excuse
        
        st.subheader("Generated Excuse:")
        st.write(excuse)
        
        st.download_button(
            label="Download Excuse",
            data=excuse,
            file_name=f"excuse_{datetime.datetime.now().strftime('%Y%m%d_%H%M%S')}.txt"
        )
