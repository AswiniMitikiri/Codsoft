import re
from datetime import datetime, timedelta
import math
import time

def get_current_date():
    # Get the current date in the format: Month Day, Year
    return datetime.now().strftime("%B %d, %Y")

def get_current_day():
    # Get the current day of the week
    return datetime.now().strftime("%A")

def perform_math_operation(math_expression):
    try:
        # Allow square roots and exponents
        math_expression = math_expression.replace('^', '**')
        result = eval(math_expression)
        return f"The result of {math_expression} is {result}."
    except Exception as e:
        return f"Error: {str(e)}"

def set_alarm(alarm_time_str):
    try:
        # Parse the time from the user input
        alarm_time = datetime.strptime(alarm_time_str, '%H:%M')
        
        # Get the current time
        current_time = datetime.now()

        # Calculate the time difference for the alarm
        time_difference = (alarm_time - current_time).total_seconds()

        # Set the alarm if the specified time is in the future
        if time_difference > 0:
            time.sleep(time_difference)
            return f"Alarm! It's {alarm_time_str} now."
        else:
            return "Sorry, the specified alarm time has already passed."

    except ValueError:
        return "Invalid time format. Please use HH:MM."

def simple_chatbot(user_input):
    # Convert user input to lowercase for case-insensitivity
    user_input = user_input.lower()

    # Define rules and responses
    greetings = ['hello', 'hi', 'hey', 'howdy']
    goodbye_patterns = ['bye', 'goodbye', 'see you', 'farewell']
    about_bot_patterns = ['who are you', 'what are you', 'your name']
    weather_patterns = ['weather', 'how is the weather today', 'forecast']
    compliment_patterns = ['good job', 'well done', 'nice']
    generic_patterns = ['how are you', 'what is this', 'tell me something']
    date_patterns = ['date', 'today\'s date', 'current date']
    day_patterns = ['day', 'today\'s day', 'current day']
    math_patterns = ['+', '-', '*', '/', '^', 'sqrt']
    alarm_patterns = ['set alarm', 'alarm at']

    # Check user input against predefined patterns
    if any(greeting in user_input for greeting in greetings):
        return "Hello! How can I help you today?"

    elif any(pattern in user_input for pattern in goodbye_patterns):
        return "Goodbye! Have a great day."

    elif any(pattern in user_input for pattern in about_bot_patterns):
        return "I am a simple rule-based chatbot. My purpose is to assist you with basic queries."

    elif any(pattern in user_input for pattern in weather_patterns):
        return "I'm sorry, I don't have real-time weather information. You can check a weather website or app for the latest updates."

    elif any(pattern in user_input for pattern in compliment_patterns):
        return "Thank you! I appreciate the compliment."

    elif any(pattern in user_input for pattern in date_patterns):
        return f"The current date is {get_current_date()}."

    elif any(pattern in user_input for pattern in day_patterns):
        return f"Today is {get_current_day()}."

    elif any(pattern in user_input for pattern in generic_patterns):
        return "I'm here to assist you. If you have any specific questions, feel free to ask."

    elif any(pattern in user_input for pattern in math_patterns):
        # Check if the user input contains mathematical operations
        return perform_math_operation(user_input)

    elif any(pattern in user_input for pattern in alarm_patterns):
        # Check if the user wants to set an alarm
        if 'set alarm' in user_input:
            # Extract the time from the user input
            time_match = re.search(r'\d{1,2}:\d{2}', user_input)
            if time_match:
                alarm_time = time_match.group()
                return set_alarm(alarm_time)
            else:
                return "Please specify the time for the alarm in HH:MM format."

    else:
        return "I'm sorry, I didn't understand that. Can you please rephrase or ask something else?"

# Main loop for chatting
def main():
    print("Simple Chatbot: Hello! Type 'exit' to end the conversation.")
    
    while True:
        user_input = input("User: ")
        
        if user_input.lower() == 'exit':
            print("Simple Chatbot: Goodbye! Have a great day.")
            break

        response = simple_chatbot(user_input)
        print("Simple Chatbot:", response)

if __name__ == "__main__":
    main()
