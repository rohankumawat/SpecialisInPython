import os
import pyttsx3

print()

print("\t\t\t\t\tHi! I'm your personal voice assistant Crypto...")
print("\t\t\t\t\t```````````````````````````````````````````````")

pyttsx3.speak("Hi I'm crypto, your personal voice assistant! What can I for you?")

while True:
	p = input("Enter:").lower
	print(p)
	if ("run" in p or "open" in p or "launch" in p) and ("chrome" in p):
		os.system("chrome") 