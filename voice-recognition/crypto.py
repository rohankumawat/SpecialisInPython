import os
import pyttsx3
import speech_recognition as sr
import pyaudio as audio


print()

print("\t\t\t\t\t```````````````````````````````````````````````")
print("\t\t\t\t\tHi! I'm Crypto, your personal voice assistant...")
print("\t\t\t\t\t```````````````````````````````````````````````")

pyttsx3.speak("Hi I'm crypto, your personal voice assistant! What can I do for you?")

while True:
	pyttsx3.speak("Choose a method which you want to prefer to do these particular tasks!")
	
	print("""
	Which method do you prefer:
	1. Menu driven
	2. Type yourself
	3. Give command using your voice
	4. Exit
	""")
	
	method = input("Method you want: ")
	
	if int(method) == 1:
		
		print("\t\t\t\t\t``````````````````````````````````")
		print("\t\t\t\t\tWelcome to the One-Click Palace..!")
		print("\t\t\t\t\t``````````````````````````````````")

		pyttsx3.speak("Oh well! Welcome to the palace of Crypto where you just have to press one button and then press enter and have your daily tasks in one click!!")
		
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
				Press 10: Make Chrome your default browser.
				Press 11: Make Opera your default browser.
				Press 12: To open Spotify.
				Press 13: Go to the previous menu.
			""")

			ch = input("Enter your choice: ")

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
				os.system("cls")
				print("""
				Want to customise?
				0: Black 						8: Gray
				1: Blue							9: Light Blue
				2: Green 						A: Light Green
				3: Aqua 						B: Light Aqua
				4: Red 							C: Light Red
				5: Purple						D: Light Purple
				6: Yellow						E: Light Yellow
				8: White						F: Bright White
				What do you want to do right now?
				-> Change the color of the text only: Only give 1 input like, "1" or "2" or "a" and so...
				-> Change the color of the background too: Give 2 character input like, "1a" or "fc" or "3e" and so...
				""")
				pyttsx3.speak("You're going to enter the Color playground. To exit type 'exit' and then press enter.")
				while True:
					color = input("Play with colors or enter exit: ")	#color_choice
					if color == "exit":
						break
					else:
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
			elif int(ch) == 12:
				os.system("spotify") #spotify-app
			elif int(ch) == 13:
				pyttsx3.speak("With an 'enter' away from your tasks, there's nothing to worry about being slow eh!")
				break
			else:
				print("Please enter the commands which are already here! I'll update my menu soon...")
				pyttsx3.speak("Wrong Command!!")

			pyttsx3.speak("What do you want to do next..?")
			os.system("cls")

	elif int(method) == 2:
		while True:
			pyttsx3.speak("What next..?")
			p = input("Enter:").lower()
			print(p)
			# Open Chrome
			if (("run" in p) or ("open" in p) or ("launch" in p)) and ("chrome" in p):
				pyttsx3.speak("Launching Chrome for you!")
				os.system("chrome")
			# Open Windows Media Player
			elif (("run" in p) or ("open" in p) or ("launch" in p)) and (("media player" in p) or ("player" in p)):
				pyttsx3.speak("Launching Windows Media Player for you!")
				os.system("wmplayer")
			# Open text editor
			elif (("run" in p) or ("open" in p) or ("launch" in p)) and (("notepad" in p) or ("text editor" in p) or ("editor" in p)):
				pyttsx3.speak("Opening Text Editor for you!")
				os.system("notepad")
			# Open VS code
			elif (("run" in p) or ("open" in p) or ("launch" in p)) and (("visual studio code" in p) or ("vs code" in p) or ("vs" in p)):
				pyttsx3.speak("Opening Visual Studio Code for you!")
				os.system("code .")
			# CMD color
			elif ("change" in p) and ("color" in p) and (("command prompt" in p) or ("cmd" in p)):
				pyttsx3.speak("In which colour do you want to see your command prompt text to look like??")
				color = input().lower()
				if color == "black":
					os.system("color 0")
				elif color == "blue":
					os.system("color 1")
				elif color == "green":
					os.system("color 2")
				elif color == "aqua":
					os.system("color 3")
				elif color == "red":
					os.system("color 4")
				elif color == "purple":
					os.system("color 5")
				elif color == "yellow":
					os.system("color 6")
				elif color == "white":
					os.system("color 7")
				elif color == "gray":
					os.system("color 8")
				elif color == "light blue":
					os.system("color 9")
				elif color == "light green":
					os.system("color A")
				elif color == "light aqua":
					os.system("color B")
				elif color == "light red":
					os.system("color C")
				elif color == "light purple":
					os.system("color D")
				elif color == "light yellow":
					os.system("color E")
				elif color == "bright white":
					os.system("color F")
				else:
					pyttsx3.speak("There's no such color available in Command Prompt!!")
			# Open Youtube
			elif (("open" in p) or ("launch" in p)) and ("youtube" in p):
				pyttsx3.speak("Opening Youtube for you!")
				os.system("start https://www.youtube.com")
			# Open Gmail
			elif ("open" in p) and (("g-mail" in p) or ("mail" in p) or ("e-mail" in p)):
				pyttsx3.speak("Opening G-mail for you!")
				os.system("start https://www.gmail.com")
			# Open WordPad
			elif (("run" in p) or ("open" in p) or ("launch" in p)) and (("wordpad" in p) or ("word pad" in p)):
				pyttsx3.speak("Opening WordPad for you!")
				os.system("write")
			# make chrome default browser
			elif ("make" in p) and (("google chrome" in p) or ("chrome" in p)) and ("default browser" in p):
				pyttsx3.speak("Making Chrome your default browser!")
				os.system("chrome.exe --make-default-browser")
			# make opera default browser
			elif ("make" in p) and ("opera" in p) and ("default browser" in p):
				pyttsx3.speak("Opening Opera GX Browser for you!")
				os.system("launcher.exe --make-default-browser")
			# Open spotify app
			elif (("listen" in p) or ("open" in p) or ("play" in p)) and ("spotify" in p):
				pyttsx3.speak("Launching spotify for you!")
				os.system("spotify")
			elif (("show" in p) or ("tell" in p)) and ("date" in p):
				os.system("date")
			# to go back to previous menu
			elif (("take" in p) or ("go in p")) and ("previous" in p) and ("menu" in p):
				pyttsx3.speak("They'll never catch you!")
				break
			# if the command is not understandable
			else:
				pyttsx3.speak("I cannot understand this command. What do you mean to say? And yes, I'll keep on updating my system soon...")
			os.system("cls")
			
	elif int(method) == 3:
		while True:
			r = sr.Recognizer()
			with sr.Microphone() as source:
				pyttsx3.speak("Say something!!")
				audio = r.listen(source)
			p = r.recognize_google(audio)
			print(p)
			# Open Chrome
			if (("run" in p) or ("open" in p) or ("launch" in p)) and ("chrome" in p):
				pyttsx3.speak("Launching Chrome for you!")
				os.system("chrome")
			# Open Windows Media Player
			elif (("run" in p) or ("open" in p) or ("launch" in p)) and (("media player" in p) or ("player" in p)):
				pyttsx3.speak("Launching Windows Media Player for you!")
				os.system("wmplayer")
			# Open text editor
			elif (("run" in p) or ("open" in p) or ("launch" in p)) and (("notepad" in p) or ("text editor" in p) or ("editor" in p)):
				pyttsx3.speak("Opening Text Editor for you!")
				os.system("notepad")
			# Open VS code
			elif (("run" in p) or ("open" in p) or ("launch" in p)) and (("visual studio code" in p) or ("vs code" in p) or ("vs" in p)):
				pyttsx3.speak("Opening Visual Studio Code for you!")
				os.system("code .")
			# Open Youtube
			elif (("open" in p) or ("launch" in p)) and ("youtube" in p):
				pyttsx3.speak("Opening Youtube for you!")
				os.system("start https://www.youtube.com")
			# Open Gmail
			elif ("open" in p) and (("g-mail" in p) or ("mail" in p) or ("e-mail" in p)):
				pyttsx3.speak("Opening G-mail for you!")
				os.system("start https://www.gmail.com")
			# Open WordPad
			elif (("run" in p) or ("open" in p) or ("launch" in p)) and (("wordpad" in p) or ("word pad" in p)):
				pyttsx3.speak("Opening WordPad for you!")
				os.system("write")
			# make chrome default browser
			elif ("make" in p) and (("google chrome" in p) or ("chrome" in p)) and ("default browser" in p):
				pyttsx3.speak("Making Chrome your default browser!")
				os.system("chrome.exe --make-default-browser")
			# make opera default browser
			elif ("make" in p) and ("opera" in p) and ("default browser" in p):
				pyttsx3.speak("Opening Opera GX Browser for you!")
				os.system("launcher.exe --make-default-browser")
			# Open spotify app
			elif (("listen" in p) or ("open" in p) or ("play" in p)) and ("spotify" in p):
				pyttsx3.speak("Launching spotify for you!")
				os.system("spotify")
			elif (("show" in p) or ("tell" in p)) and ("date" in p):
				os.system("date")
			# to go back to previous menu
			elif (("take" in p) or ("go in p")) and ("previous" in p) and ("menu" in p):
				pyttsx3.speak("They'll never catch you!")
				break
			# if the command is not understandable
			else:
				pyttsx3.speak("I cannot understand this command. What do you mean to say? And yes, I'll keep on updating my system soon...")
			os.system("cls")
			
            

	elif int(method) == 4: #to exit permanently out of this code
		break