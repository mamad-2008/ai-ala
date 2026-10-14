"""
College Helpdesk Rule-Based Chatbot
Course: DETCE15213 - Artificial Intelligence
Purpose: Demonstrate a simple rule-based chatbot using Python if-elif-else.
Run: python college_chatbot.py
"""

def get_response(user_input):
    """Return a response based on keyword/rule matching."""
    message = user_input.lower().strip()

    if message in {"hi", "hello", "hey", "good morning", "good afternoon"}:
        return "Hello! Welcome to the College Helpdesk Chatbot. How can I help you?"
    elif "your name" in message or "who are you" in message:
        return "I am the College Helpdesk Chatbot, a simple rule-based assistant."
    elif "admission" in message or "apply" in message:
        return "For admission, check the college admission office or official portal for eligibility, documents, and deadlines."
    elif "fee" in message or "fees" in message or "payment" in message:
        return "For fee details or payment confirmation, contact the accounts department and keep your receipt."
    elif "timetable" in message or "schedule" in message or "time table" in message:
        return "Please check the latest timetable shared by your department or on the college portal."
    elif "exam" in message or "hall ticket" in message:
        return "For exam dates, hall tickets, and exam rules, check the official student portal or contact the exam cell."
    elif "library" in message or "book" in message:
        return "The library can help you find books and study resources. Ask the librarian about issue and return dates."
    elif "attendance" in message or "present" in message:
        return "For attendance records or corrections, contact your subject faculty or department office."
    elif "result" in message or "marks" in message or "grade" in message:
        return "Check the official student portal for results. If something looks incorrect, contact the exam cell."
    elif "certificate" in message or "bonafide" in message or "transcript" in message:
        return "Contact the student section to learn the application process and required documents for certificates."
    elif "contact" in message or "phone" in message or "email" in message:
        return "Please use the contact information published on your college's official website or student portal."
    elif "thank" in message:
        return "You're welcome! Good luck with your studies."
    elif "bye" in message or "exit" in message or "quit" in message:
        return "Goodbye! Have a great day."
    else:
        return "Sorry, I don't have a rule for that question yet. Try asking about admissions, fees, timetable, exams, library, attendance, or results."


def main():
    print("=" * 56)
    print("       COLLEGE HELPDESK RULE-BASED CHATBOT")
    print("Type 'bye' or 'exit' to end the conversation.")
    print("=" * 56)

    while True:
        user_input = input("You: ").strip()
        if not user_input:
            print("Bot: Please type a question.")
            continue

        response = get_response(user_input)
        print("Bot:", response)

        if user_input.lower().strip() in {"bye", "exit", "quit"}:
            break


if __name__ == "__main__":
    main()
