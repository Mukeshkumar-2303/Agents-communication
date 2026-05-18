from memory import sessions
from utils import generate_content


def process_message(session_id, user_message):

    # Create session if not exists
    if session_id not in sessions:

        sessions[session_id] = {
            "task": None,
            "tone": None,
            "length": None,
            "step": 0
        }

    session = sessions[session_id]

    # STEP 1 → Save task
    if session["step"] == 0:

        session["task"] = user_message
        session["step"] = 1

        return {
            "type": "question",
            "message": "What tone would you like? (formal/casual)"
        }

    # STEP 2 → Save tone
    elif session["step"] == 1:

        session["tone"] = user_message.lower()
        session["step"] = 2

        return {
            "type": "question",
            "message": "What length should the content be? (short/medium)"
        }

    # STEP 3 → Save length and generate output
    elif session["step"] == 2:

        session["length"] = user_message.lower()

        task = session["task"]
        tone = session["tone"]
        length = session["length"]

        final_output = generate_content(
            task,
            tone,
            length
        )

        # Reset session after completion
        sessions[session_id] = {
            "task": None,
            "tone": None,
            "length": None,
            "step": 0
        }

        return {
            "type": "final",
            "message": final_output
        }