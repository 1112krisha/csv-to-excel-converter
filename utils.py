def detect_intent(user_input):
    user_input = user_input.lower()
    if "admission" in user_input:
        return "admissions"
    elif "philosophy" in user_input or "teaching" in user_input:
        return "philosophy"
    elif "fee" in user_input or "fees" in user_input:
        return "fees"
    elif "visit" in user_input or "tour" in user_input:
        return "visit"
    elif "contact" in user_input or "reach" in user_input:
        return "contact"
    else:
        return None
