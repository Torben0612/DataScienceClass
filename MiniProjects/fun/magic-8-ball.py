import random
import time
magic_ball = ["It is certain", "Without a doubt", "Yes definitely", "You may rely on it", "Ask again", "As I see it, yes", "Most likely", "Outlook looks good", "Yes", "Signs point to yes", "Reply hazy, try again", "Ask again later", "Better not tell you now", "Cannot predict now", "Concentrate and ask again", "Don't count on it", "My reply is no", "My sources say", "Outlook not so", "Very doubtful"]

q = input("What is your Question")
print("Thinking")
time.sleep(2)
print(magic_ball[random.randint(0,21)])
