import os
import datetime
import wikipedia
import pyttsx3
import pywhatkit
import pyjokes
import random

# 💬 Chatbot imports
from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer


class VirtualAssistant:
    def __init__(self):
        # Voice setup
        self.engine = pyttsx3.init()
        self.engine.setProperty('rate', 175)
        self.engine.setProperty('volume', 1.0)
        self.balance = 0
        self.name = ""
        self.speak("Welcome to your all-in-one Virtual Assistant!")

    # ---------- Utility ----------
    def speak(self, text):
        print(text)
        self.engine.say(text)
        self.engine.runAndWait()

    # ---------- Greeting ----------
    def greet_user(self):
        self.name = input("Enter your name: ")
        hour = datetime.datetime.now().hour

        if 5 <= hour < 12:
            greeting = f"Good Morning, {self.name}! ☀️"
        elif 12 <= hour < 17:
            greeting = f"Good Afternoon, {self.name}! 🌤️"
        elif 17 <= hour < 21:
            greeting = f"Good Evening, {self.name}! 🌇"
        else:
            greeting = f"Hello, {self.name}! 🌙 You’re up late, huh?"

        self.speak(greeting)
        self.speak("Welcome to your personal App Launcher, Calculator, and Wikipedia Assistant!")

    # ---------- App Launcher ----------
    def open_app(self):
        while True:
            print("\n=== Choose which app you want to open ===")
            print("1. Notepad")
            print("2. Chrome")
            print("3. Exit")

            app = input("Enter your choice (1-3): ")

            if app == '1':
                self.speak("Opening Notepad")
                os.startfile("notepad.exe")
            elif app == '2':
                self.speak("Opening Google Chrome")
                os.startfile("C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe")
            elif app == '3':
                self.speak("Exiting App Launcher")
                break
            else:
                self.speak("Invalid input. Please enter 1, 2, or 3.")

    # ---------- Calculator ----------
    def calculator(self):
        self.speak("Welcome to OOP-Based Simple Calculator.")
        while True:
            print("\n==== Choose Operation ====")
            print("1. Addition (+)")
            print("2. Subtraction (-)")
            print("3. Multiplication (*)")
            print("4. Division (/)")
            print("5. Exit")

            choice = input("\nEnter your choice (1-5): ")

            if choice == '5':
                self.speak("Exiting Calculator.")
                break

            if choice not in ['1', '2', '3', '4']:
                self.speak("Invalid choice. Please enter between 1 and 5.")
                continue

            try:
                a = float(input("\nEnter number a: "))
                b = float(input("Enter number b: "))
            except ValueError:
                self.speak("Invalid input! Please enter numeric values.")
                continue

            if choice == '1':
                result = a + b
                self.speak(f"The sum of {a} and {b} is {result}.")
            elif choice == '2':
                result = a - b
                self.speak(f"The difference between {a} and {b} is {result}.")
            elif choice == '3':
                result = a * b
                self.speak(f"The product of {a} and {b} is {result}.")
            elif choice == '4':
                if b == 0:
                    result = "Error: Division by zero!"
                else:
                    result = a / b
                self.speak(f"The division of {a} by {b} gives {result}.")

            print(f"Result: {result}")

    # ---------- Wikipedia Search ----------
    def search_wikipedia(self):
        while True:
            print("\n=== Wikipedia Search ===")
            topic = input("Enter a topic to search (or type 'exit' to go back): ").strip()

            if topic.lower() == 'exit':
                self.speak("Exiting Wikipedia Search.")
                break

            try:
                summary = wikipedia.summary(topic, sentences=3)
                print("\n🧠 Here's what I found:\n")
                print(summary)
                self.speak(f"According to Wikipedia, {summary}")
            except wikipedia.exceptions.DisambiguationError as e:
                self.speak("The topic is too broad. Try being more specific.")
                print("Some suggestions:", e.options[:5])
            except wikipedia.exceptions.PageError:
                self.speak("Sorry, no page found for that topic.")
            except Exception as e:
                self.speak(f"An error occurred: {e}")

    # ---------- Daily Quotes ----------
    def daily_quotes(self):
        quotes = [
            "The only way to do great work is to love what you do. 💌",
            "Innovation distinguishes between a leader and a follower. 🚀",
            "The future belongs to those who believe in the beauty of their dreams. ✨",
            "Success is not final, failure is not fatal: it is the courage to continue that counts. 💪",
            "The only impossible journey is the one you never begin. 🌟"
        ]
        quote = random.choice(quotes)
        print(f"\n💫 Daily Motivation: {quote}")
        self.speak("Here's your daily motivation!")
        self.speak(quote)

    # ---------- YouTube ----------
    def youtube(self):
        while True:
            print("\n=== YouTube Options ===")
            print("1. Search on YouTube")
            print("2. Play a Song")
            print("3. Exit YouTube")

            choice = input("Enter your choice (1-3): ")

            if choice == '1':
                query = input("What would you like to search on YouTube? ")
                if query:
                    self.speak(f"Searching YouTube for {query}")
                    pywhatkit.playonyt(query)
                else:
                    self.speak("Please enter a valid search query.")
            elif choice == '2':
                song = input("Which song would you like to play? ")
                if song:
                    self.speak(f"Playing {song} on YouTube")
                    pywhatkit.playonyt(song + " song")
                else:
                    self.speak("Please enter a song name.")
            elif choice == '3':
                self.speak("Exiting YouTube")
                break
            else:
                self.speak("Invalid choice. Please enter 1, 2, or 3.")

    # ---------- Time & Date ----------
    def get_time_date(self):
        now = datetime.datetime.now()
        current_time = now.strftime("%I:%M %p")
        current_date = now.strftime("%A, %B %d, %Y")

        time_info = f"""
🕒 Current Time: {current_time}
📅 Current Date: {current_date}
        """
        print(time_info)
        self.speak(f"The current time is {current_time} and today is {current_date}")

    # ---------- Joke Teller ----------
    def tell_joke(self):
        print("\n" + "=" * 30)
        print("😂 JOKE TELLER")
        print("=" * 30)
        try:
            joke = pyjokes.get_joke()
            print(f"🎭 {joke}")
            self.speak("Here's a joke for you!")
            self.speak(joke)
        except Exception as e:
            self.speak("I'm out of jokes right now!")
            print(f"Error: {e}")
        
        

    # ---------- Banking System ----------
    def bank_menu(self):
        while True:
            print("\nChoose an option:")
            print("1. Check Balance")
            print("2. Add Cash")
            print("3. Withdraw Cash")
            print("4. Exit Bank")

            choice = input("Enter your choice: ")

            if choice == "1":
                print(f"Your bank balance is ₹{self.balance}")
                self.speak(f"Your current balance is {self.balance} rupees")
            elif choice == "2":
                try:
                    amount = float(input("Enter the amount to add: ₹"))
                    self.balance += amount
                    print(f"₹{amount} added successfully! New balance: ₹{self.balance}")
                    self.speak(f"{amount} rupees added successfully")
                except ValueError:
                    self.speak("Please enter a valid amount.")
            elif choice == "3":
                try:
                    amount = float(input("Enter the amount to withdraw: ₹"))
                    if amount > self.balance:
                        print("Insufficient balance!")
                        self.speak("Insufficient balance!")
                    else:
                        self.balance -= amount
                        print(f"₹{amount} withdrawn successfully! Remaining balance: ₹{self.balance}")
                        self.speak(f"{amount} rupees withdrawn successfully")
                except ValueError:
                    self.speak("Please enter a valid amount.")
            elif choice == "4":
                self.speak("Exiting Virtual Bank.")
                break
            else:
                print("Invalid choice! Please try again.")

    # 💬 ---------- CHATBOT MODE ----------
    def chatbot_mode(self):
        self.speak("Chatbot mode activated! You can chat with me now.")
        chatbot = ChatBot("VirtualAssistantBot")
        trainer = ChatterBotCorpusTrainer(chatbot)
        trainer.train("chatterbot.corpus.english")

        print("\nType 'exit' to leave chat mode.\n")
        while True:
            user_input = input("You: ")
            if user_input.lower() in ["exit", "quit", "bye"]:
                self.speak("Goodbye! Exiting chat mode.")
                break
            response = chatbot.get_response(user_input)
            print("Awara:", response)
            self.speak(str(response))

    # ---------- Main Menu ----------
    def run(self):
        self.greet_user()
        self.daily_quotes()

        while True:
            print("\n==== Main Menu ====")
            print("1. Open Application")
            print("2. Calculator")
            print("3. Virtual Banking System")
            print("4. Wikipedia Search")
            print("5. Youtube")
            print("6. Date and Time")
            print("7. Tell a Joke")
            print("8. Chatbot Mode 💬")
            print("9. Exit")

            main_choice = input("Enter your choice (1-9): ")

            if main_choice == '1':
                self.open_app()
            elif main_choice == '2':
                self.calculator()
            elif main_choice == '3':
                self.bank_menu()
            elif main_choice == '4':
                self.search_wikipedia()
            elif main_choice == '5':
                self.youtube()
            elif main_choice == '6':
                self.get_time_date()
            elif main_choice == '7':
                self.tell_joke()
            elif main_choice == '8':
                self.chatbot_mode()
            elif main_choice == '9':
                self.speak("Exiting the program. Goodbye!")
                break
            else:
                self.speak("Invalid input. Please enter between 1 and 9.")


# ---------- Run Program ----------
if __name__ == "__main__":
    assistant = VirtualAssistant()
    assistant.run()
