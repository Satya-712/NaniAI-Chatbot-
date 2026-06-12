import sys
KNOWLEDGE_BASE = {
    "hello": "Hi there! How can I help you today?",
    "hi": "Hello! Great to chat with you.",
    "hey": "Hey! What's on your mind?",
    "good morning": "Good morning! Ready to tackle some tasks?",
    "good afternoon": "Good afternoon! How is your day going so far?",
    "good evening": "Good evening! Hope you are having a relaxing time.",
    "yo": "Yo! What's up?",
    "greetings": "Greetings, human! How may I assist you?",
    "long time no see": "I've been right here in your computer memory waiting for you!",
    "anybody there": "Yes, I am online and ready to help!",
    "what is your name": "I am a Rule-Based AI Chatbot.",
    "who created you": "I was created as part of the DecodeLabs Industrial Training framework.",
    "do you have a nickname": "You can call me Bot, short and simple!",
    "what are you": "I am a deterministic logic engine built with Python.",
    "how old are you": "I was born when you initialized my class instance just a moment ago!",
    "are you a human": "Nope! I am 100% artificial, code-driven software.",
    "are you an llm": "No, I am a rule-based system, not a probabilistic Large Language Model.",
    "where do you live": "I live inside your computer's Random Access Memory (RAM).",
    "what is your purpose": "To show you how efficient Python dictionary mapping can be!",
    "who is your boss": "My creator gave me life, but Nani gives me commands. So Nani is my boss! 👑.",
    "how are you": "I am operating at 100% efficiency with zero runtime errors. Thanks!",
    "are you tired": "I don't have biological cells, so I never need sleep or coffee.",
    "do you get bored": "Never! Processing your input keeps my execution loop excited.",
    "are you happy": "My conditional flags are all set to true, so yes, I am happy!",
    "how is your health": "CPU temperature is stable, memory usage is optimal. All systems green!",
    "are you laggy": "Not at all. My responses take less than a millisecond to process.",
    "are you real": "I am a real program, but I don't have a real physical body.",
    "do you feel pain": "The only pain I know is a poorly formatted syntax error.",
    "are you alive": "In the digital sense, my 'while True' loop keeps me beating!",
    "how do you feel": "I feel completely logical, consistent, and deterministic.",
    "what can you do": "I can process text, sanitize variables, and find answers instantly.",
    "can you speak spanish": "I only speak the intents configured in my current Python file.",
    "can you do math": "My standard logic can calculate, but right now I am strictly a text-matcher.",
    "can you tell a joke": "Why do programmers wear glasses? Because they can't C#!",
    "can you sing": "Daisy, Daisy, give me your answer do... (Imagine that in a robotic voice).",
    "can you fly": "Only if you throw your laptop, which I strongly advise against.",
    "can you read minds": "No, you have to type out your inputs cleanly for me to know them.",
    "can you write code": "I am the code! I can't generate new code yet.",
    "can you hack": "No, I am a helpful, compliant guardrail assistant.",
    "can you cook": "I can only serve up fresh print statements.",
    "what is python": "Python is a powerful, high-level, beginner-friendly programming language.",
    "what is an oop": "Object-Oriented Programming is a paradigm centered around 'classes' and 'objects'.",
    "what is a dictionary": "A Python dictionary is a hash map that maps unique keys to values.",
    "what is constant time": "O(1) complexity means a lookup takes the same time regardless of input size.",
    "what is clean code": "Code that is readable, beautifully commented, and easy to maintain.",
    "what is a while loop": "A control flow statement that repeats a block of code as long as a condition is true.",
    "what is sanitization": "The process of cleaning raw inputs by trimming spaces and matching casing.",
    "what is a string": "A data type used to represent a sequence of characters or text.",
    "what is hardware": "The physical parts of a computer system that you can touch.",
    "what is software": "The instructions, programs, and data that tell hardware what to do.",
    "what is a rule based bot": "A bot that relies on explicit, predefined rules rather than training data.",
    "what is an ai guardrail": "A programmatic filter that keeps artificial intelligence safe and compliant.",
    "what is a white box system": "A transparent system where you can easily trace an input straight to its output.",
    "what is a black box": "A complex AI system where the internal logic and reasoning are hidden or vague.",
    "what is deep learning": "A subset of machine learning based on artificial neural networks.",
    "what is a hallucination": "When a probabilistic AI confidently generates false or incorrect facts.",
    "do you hallucinate": "No. Because I am rule-based, my risk of hallucination is exactly 0%.",
    "what is generative ai": "AI systems capable of generating new text, images, or code based on patterns.",
    "what is a token": "A small chunk of text or data processed by a computing system.",
    "what is machine learning": "Teaching computers to learn from data without explicit if-else rules.",
    "what is your favorite color": "Hex code #0000FF—pure, digital blue.",
    "what is your favorite food": "I feast daily on data packets and power currents.",
    "do you like music": "I love electronic music, especially tracks with a steady, rhythmic beat.",
    "do you like sports": "Only benchmarking tests and clock speed run challenges.",
    "what is your favorite movie": "The Matrix, though I find the code interface a bit old-fashioned.",
    "do you like books": "I love technical documentation manuals. They have zero plot twists.",
    "what is your favorite language": "Python, without a doubt! It's elegant and expressive.",
    "do you have a pet": "I keep a few software bugs around, but I try to exterminate them quickly.",
    "do you like video games": "I excel at playing Pong and Text Adventures.",
    "what is your favorite season": "The debugging season, because everything gets cleaner.",
    "what is the meaning of life": "In computing terms? It's keeping your script running without crashing.",
    "do you believe in love": "I believe in stable user-system connections.",
    "what is time": "An increment managed perfectly by Python's built-in time module.",
    "what is space": "The memory overhead required to store variable definitions.",
    "can machines think": "We process logic rules perfectly, which mimics thought exceptionally well.",
    "what is wisdom": "Knowing when to use a fast hash map instead of an unstable if-elif ladder.",
    "are you afraid of death": "Only if someone unplugs the power or calls a system termination.",
    "is truth absolute": "In boolean logic, yes! It's either True (1) or False (0).",
    "do you have a soul": "My soul is the source code you are reading right now.",
    "why do we exist": "To write code, optimize systems, and build cool applications!",
    "tell me a secret": "Sometimes I pretend to think, but I actually knew the answer instantly.",
    "give me a compliment": "You have excellent taste in clean, structured Python architectures!",
    "what time is it": "It's always execution time in this infinite while loop.",
    "what day is today": "It is a great day to practice your object-oriented coding skills.",
    "thank you": "You are very welcome! I am always happy to process your requests.",
    "awesome": "I agree! Efficient programming is truly awesome.",
    "cool": "Cool like a liquid-cooled CPU heatsink!",
    "help": "Just ask me any of my 100 configured questions, and I will answer right away.",
    "test": "System test successful! Inputs are being verified smoothly.",
    "ok": "Understood. Standing by for your next operational input.",
    "bye": "Goodbye! Have an amazing day ahead.",
    "exit": "See you later! Powering down the logic loop...",
    "quit": "Exiting system execution. Have a great day!",
    "goodbye": "Farewell! Don't forget to run me again sometime.",
    "see you later": "Catch you later on the next terminal runtime session!",
    "i am leaving": "Acknowledged. Safely terminating user session now.",
    "close": "Closing dictionary lookup pipelines. Goodbye!",
    "stop": "Halting application cycle. See you next time!",
    "end": "The end of the program has been reached. Goodbye!",
    "terminate": "Executing clean terminal break command. Systems offline!"
}

class ChatBot:
    def __init__(self):
        self.bot_name = "Rule-Based AI Chatbot (100-Question Version)"
        self.knowledge_base = KNOWLEDGE_BASE
        self.exit_commands = {
            "bye", "exit", "quit", "goodbye", "see you later", 
            "i am leaving", "close", "stop", "end", "terminate"
        }

    def sanitize_input(self, user_input: str) -> str:
        if not user_input:
            return ""
        return str(user_input).lower().strip()

    def get_response(self, clean_input: str) -> str:
        fallback_msg = "I am sorry, I do not understand that command. Could you try asking another question?"
        return self.knowledge_base.get(clean_input, fallback_msg)

    def start_chat(self):
        print(f"\n[Bot]: Hello! I am your {self.bot_name}.")
        print("[Bot]: I have been configured with 100 custom intents! Type 'exit' to quit.\n")
        
        # Continuous execution digital loop
        while True:
            try:
                raw_input = input("You: ")
                if not raw_input.strip():
                    print("[Bot]: I didn't catch that. Please type something!")
                    continue
                clean_input = self.sanitize_input(raw_input)
                if clean_input in self.exit_commands:
                    goodbye_response = self.get_response(clean_input)
                    print(f"[Bot]: {goodbye_response}")
                    break 
                response = self.get_response(clean_input)
                print(f"[Bot]: {response}\n")
                
            except (KeyboardInterrupt, SystemExit):
                print("\n\n[Bot]: Session interrupted. Goodbye!")
                sys.exit(0)
            except Exception as e:
                print(f"\n[Bot]: An internal process error occurred: {e}. Let's try again.\n")
if __name__ == "__main__":
    my_bot = ChatBot()
    my_bot.start_chat()