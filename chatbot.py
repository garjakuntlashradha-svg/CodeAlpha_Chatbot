import random
import re
from datetime import datetime

# Memory for the current conversation
memory = {
    "name": "",
    "hobby": "",
    "favorite_subject": ""
}

# Different replies make conversations less repetitive
responses = {
    "greeting": [
        "Hey! 😊 How is your day going?",
        "Hello! What would you like to talk about?",
        "Hi there! I'm listening!"
    ],
    "feeling_good": [
        "That's wonderful! What made your day special?",
        "I'm glad to hear that! Tell me more.",
        "That sounds lovely! 😊"
    ],
    "feeling_bad": [
        "I'm sorry your day has been difficult.",
        "That sounds tough. Would you like to tell me more?",
        "I'm listening. Take your time."
    ],
    "study": [
        "What subject are you studying today?",
        "Try breaking your studies into small steps.",
        "Which topic would you like help understanding?"
    ],
    "hobby": [
        "That sounds interesting! How did you get into it?",
        "What do you enjoy most about your hobby?",
        "I'd love to hear more about what you like doing."
    ],
    "motivation": [
        "Small steps can lead to big progress. Keep going!",
        "You don't have to be perfect to make progress.",
        "Every new skill begins with learning something small."
    ],
    "joke": [
        "Why did the computer go to the doctor? "
        "Because it had a virus! 😂",
        "Why do programmers prefer dark mode? "
        "Because light attracts bugs! 😄",
        "What is a computer's favourite snack? Microchips!"
    ],
    "thanks": [
        "You're welcome! 😊",
        "Anytime! What else would you like to talk about?",
        "Happy to help!"
    ]
}


def reply(message):
    text = message.lower().strip()
    words = set(re.findall(r"[a-z0-9']+", text))

    if not text:
        return "I'm listening! Type something you'd like to discuss."

    # Exit the conversation
    if text in ["bye", "goodbye", "exit", "quit"]:
        return "It was nice chatting with you! Take care. 😊"

    # Remember the user's name
    match = re.match(
        r"^(?:my name is|i am|i'm|call me)\s+(.+)$",
        text
    )

    if match:
        name = match.group(1).strip(" .!?")
        if name:
            memory["name"] = name.title()
            return f"Nice to meet you, {memory['name']}! 😊"

    # Recall the user's name
    if "name" in words and any(
        phrase in text
        for phrase in ["my name", "what is my", "remember my"]
    ):
        if memory["name"]:
            return f"Your name is {memory['name']}!"
        return "You haven't told me your name yet."

    # Remember hobbies
    if text.startswith("my hobby is "):
        hobby = message.strip()[12:].strip(" .!?")
        if hobby:
            memory["hobby"] = hobby
            return f"{hobby.title()} sounds interesting! Tell me about it."

    if "hobby" in words and "my" in words:
        if memory["hobby"]:
            return f"Your hobby is {memory['hobby']}."
        return "What is your hobby? Tell me using 'My hobby is ...'."

    # Remember favourite subject
    if text.startswith("my favourite subject is "):
        subject = message.strip()[24:].strip(" .!?")
        if subject:
            memory["favorite_subject"] = subject
            return f"{subject.title()} is your favourite subject. Nice!"

    if "subject" in words and any(
        phrase in text
        for phrase in ["my favourite", "my favorite", "which is my"]
    ):
        if memory["favorite_subject"]:
            return (
                "Your favourite subject is "
                + memory["favorite_subject"] + "."
            )
        return "You haven't told me your favourite subject yet."

    # Greetings
    if words.intersection({"hello", "hi", "hey", "namaste"}):
        return random.choice(responses["greeting"])

    # Ask about the chatbot
    if "how are you" in text or "how are you doing" in text:
        return "I'm doing well! Thanks for asking. How are you?"

    if any(phrase in text for phrase in [
        "your name", "who are you", "what are you"
    ]):
        return "I'm your friendly offline Python chatbot! 🤖"

    # Time and date
    if "time" in words:
        return "The time on your computer is " + \
            datetime.now().strftime("%I:%M %p") + "."

    if "date" in words or "today's day" in text:
        return "Today's date is " + \
            datetime.now().strftime("%d %B %Y") + "."

    # Feelings
    if words.intersection({
        "sad", "upset", "lonely", "unhappy", "worried", "stressed"
    }):
        return random.choice(responses["feeling_bad"])

    if words.intersection({
        "happy", "excited", "wonderful", "great", "awesome"
    }):
        return random.choice(responses["feeling_good"])

    # Studies and hobbies
    if words.intersection({
        "study", "studying", "exam", "exams", "homework", "college"
    }):
        return random.choice(responses["study"])

    if words.intersection({
        "hobby", "hobbies", "drawing", "painting", "music", "singing",
        "reading", "dancing", "cricket", "football", "games"
    }):
        return random.choice(responses["hobby"])

    # Motivation
    if words.intersection({
        "motivate", "motivation", "confidence", "failure", "difficult"
    }):
        return random.choice(responses["motivation"])

    # Jokes
    if words.intersection({"joke", "jokes", "funny", "laugh"}):
        return random.choice(responses["joke"])

    # Gratitude
    if words.intersection({"thanks", "thank"}):
        return random.choice(responses["thanks"])

    # Simple conversation follow-ups
    if text.startswith(("because ", "actually ", "well ")):
        return "I see. Tell me a little more about that."

    if text.endswith("?"):
        return (
            "That's an interesting question! I don't know the answer "
            "to everything, but I can respond to topics I've been "
            "programmed for. Try asking about studies, hobbies, or time."
        )

    # General fallback
    fallback = [
        "Tell me more about that.",
        "I see! What happened next?",
        "That sounds interesting. How do you feel about it?",
        "I'm listening. Can you explain a little more?",
        "Thanks for sharing that with me."
    ]
    return random.choice(fallback)


def main():
    print("=" * 45)
    print("       FRIENDLY CHATBOT 🤖")
    print("=" * 45)
    print("Chat with me about your day, studies, hobbies")
    print("and more. Type 'bye' to end the conversation.")

    while True:
        message = input("\nYou: ")
        answer = reply(message)
        print("Bot:", answer)

        if message.lower().strip() in [
            "bye", "goodbye", "exit", "quit"
        ]:
            break


if __name__ == "__main__":
    main()