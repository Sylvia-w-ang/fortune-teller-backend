import random
from datetime import datetime

def get_zodiac_sign(birthday):
    # Replace period with forward slash if present
    birthday = birthday.replace('.', '/')
    month, day = map(int, birthday.split('/'))
    if (month == 3 and day >= 21) or (month == 4 and day <= 19):
        return "Aries"
    elif (month == 4 and day >= 20) or (month == 5 and day <= 20):
        return "Taurus"
    elif (month == 5 and day >= 21) or (month == 6 and day <= 20):
        return "Gemini"
    elif (month == 6 and day >= 21) or (month == 7 and day <= 22):
        return "Cancer"
    elif (month == 7 and day >= 23) or (month == 8 and day <= 22):
        return "Leo"
    elif (month == 8 and day >= 23) or (month == 9 and day <= 22):
        return "Virgo"
    elif (month == 9 and day >= 23) or (month == 10 and day <= 22):
        return "Libra"
    elif (month == 10 and day >= 23) or (month == 11 and day <= 21):
        return "Scorpio"
    elif (month == 11 and day >= 22) or (month == 12 and day <= 21):
        return "Sagittarius"
    elif (month == 12 and day >= 22) or (month == 1 and day <= 19):
        return "Capricorn"
    elif (month == 1 and day >= 20) or (month == 2 and day <= 18):
        return "Aquarius"
    else:
        return "Pisces"

def get_color_meaning(color):
    color_meanings = {
        "red": "passion and energy",
        "blue": "peace and tranquility",
        "green": "growth and harmony",
        "yellow": "happiness and optimism",
        "purple": "wisdom and creativity",
        "orange": "enthusiasm and adventure",
        "pink": "love and compassion",
        "black": "mystery and power",
        "white": "purity and clarity",
        "brown": "stability and reliability"
    }
    return color_meanings.get(color.lower(), "unique energy")

def get_zodiac_personality(zodiac_sign):
    personalities = {
        "Aries": "energetic and adventurous",
        "Taurus": "reliable and patient",
        "Gemini": "curious and adaptable",
        "Cancer": "caring and intuitive",
        "Leo": "confident and warm-hearted",
        "Virgo": "thoughtful and practical",
        "Libra": "fair-minded and sociable",
        "Scorpio": "determined and passionate",
        "Sagittarius": "optimistic and open-minded",
        "Capricorn": "disciplined and ambitious",
        "Aquarius": "innovative and friendly",
        "Pisces": "empathetic and creative"
    }
    return personalities.get(zodiac_sign, "unique and wonderful")

def get_color_personality(color):
    color_traits = {
        "red": "enthusiastic and bold",
        "blue": "calm and trustworthy",
        "green": "balanced and supportive",
        "yellow": "cheerful and inspiring",
        "purple": "imaginative and wise",
        "orange": "sociable and lively",
        "pink": "kind and caring",
        "black": "strong and thoughtful",
        "white": "honest and open-minded",
        "brown": "dependable and down-to-earth"
    }
    return color_traits.get(color.lower(), "uniquely expressive")

def generate_fortune(name, zodiac_sign, color, hobby):
    zodiac_personality = get_zodiac_personality(zodiac_sign)
    color_personality = get_color_personality(color)
    future_templates = [
        f"{name}, as someone who is {zodiac_personality} and {color_personality}, your passion for {hobby} will open up new opportunities for learning and connection this year.",
        f"Your {zodiac_personality} nature, combined with your {color_personality} outlook, means you'll find joy and growth in your {hobby}—and maybe even inspire others to join you!",
        f"With your {zodiac_personality} spirit and {color_personality} approach to life, {name}, your dedication to {hobby} will bring you both happiness and new friendships in the near future.",
        f"Being {zodiac_personality} and {color_personality}, you have a knack for making the most of your interests. Keep enjoying {hobby}, and you'll discover new strengths in yourself."
    ]
    return random.choice(future_templates)

def generate_response(name, birthday, color, hobby):
    zodiac_sign = get_zodiac_sign(birthday)
    zodiac_personality = get_zodiac_personality(zodiac_sign)
    color_personality = get_color_personality(color)
    feedback = (
        f"Here's a little about you, {name}:\n"
        f"- Zodiac Sign: {zodiac_sign} — {zodiac_personality}\n"
        f"- Color Personality: {color_personality}\n"
        f"- Favorite Hobby: {hobby}\n\n"
        f"Looking ahead: {generate_fortune(name, zodiac_sign, color, hobby)}"
    )
    return feedback

def main():
    print("Welcome! Let's learn a bit about you and your future.")
    print("----------------------------------------")
    
    name = input("What is your name? ")
    birthday = input("What is your birthday? (MM/DD): ")
    favorite_color = input("What is your favorite color? ")
    hobby = input("What is your favorite hobby? ")
    
    zodiac_sign = get_zodiac_sign(birthday)
    zodiac_personality = get_zodiac_personality(zodiac_sign)
    color_personality = get_color_personality(favorite_color)
    
    print("\nHere's a little about you:")
    print(f"Zodiac Sign: {zodiac_sign} — {zodiac_personality}")
    print(f"Color Personality: {color_personality}")
    print(f"Favorite Hobby: {hobby}")
    print("\nYour Friendly Forecast:")
    print(generate_fortune(name, zodiac_sign, favorite_color, hobby))
    print("\nWishing you a wonderful year ahead!")

if __name__ == "__main__":
    main() 
