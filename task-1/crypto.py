import os
import pyttsx3

print()

print("\t\t\t\t\tHi! I'm your personal voice assistant Crypto...")
print("\t\t\t\t\t```````````````````````````````````````````````")

pyttsx3.speak("Hi I'm crypto, your personal voice assistant! What can I do for you?")
pyttsx3.speak("Choose a method which you want to prefer to do these partiular tasks!")

print("""
Which method do you prefer:
1. Menu driven
2. Type yourself
3. Voice command
""")

method = input()

if int(method) == 1:
	while True:
		print("""
			Press 1: To show date.
			Press 2: To show time.
			Press 3: To open calculator.
			Press 4: To open WordPad.
			Press 5: To open Character Map.
			Press 6: To change the console of the color.
			Press 7: To open Google Chrome.
			Press 8: To go to Youtube.
			Press 9: To open Gmail.
			Press 10: Make Chrome your default browser
			Press 11: Make Opera your default browser
		""")

		print("Enter your choice:")
		ch = input()

		if int(ch) == 1:
			os.system("date")	#date
		elif int(ch) == 2:
			os.system("time")	#time
		elif int(ch) == 3:
			os.system("calc")	#calculator
		elif int(ch) == 4:
			os.system("write")	#wordpad
		elif int(ch) == 5:
			os.system("charmap")	#character-map
		elif int(ch) == 6:
			print("""
			What color do you want your console to look like?
			0: Black 						8: Gray
			1: Blue							9: Light Blue
			2: Green 						A: Light Green
			3: Aqua 						B: Light Aqua
			4: Red 							C: Light Red
			5: Purple						D: Light Purple
			6: Yellow						E: Light Yellow
			8: White						F: Bright White
			""")
			color = input()	#color_choice
			os.system("color {}".format(color))
		elif int(ch) == 7:
			os.system("chrome")	#chrome
		elif int(ch) == 8:
			os.system("start https://www.youtube.com")	#Youtube
		elif int(ch) == 9:
			os.system("start https://www.gmail.com")	#Gmail
		elif int(ch) == 10:
			os.system("chrome.exe --make-default-browser")	#ChromeDefaultBrowser
		elif int(ch) == 11:
			os.system("launcher.exe --make-default-browser")	#OperaDefaultBrowser	

elif int(method) == 2:
	while True:
		p = input("Enter:").lower()
		print(p)
		if (("run" in p) or ("open" in p) or ("launch" in p)) and ("chrome" in p):
			os.system("chrome")
		elif (("run" in p) or ("open" in p) or ("launch" in p)) and (("media player" in p) or ("player" in p)):
			os.system("wmplayer")
		elif (("run" in p) or ("open" in p) or ("launch" in p)) and (("notepad" in p) or ("text editor" in p) or ("editor" in p)):
			os.system("notepad")
		elif (("run" in p) or ("open" in p) or ("launch" in p)) and (("visual studio code" in p) or ("vs code" in p) or ("vs" in p)):
			os.system("code .")