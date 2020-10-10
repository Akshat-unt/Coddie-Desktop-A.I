import pyttsx3  # pip install pyttsx3
import speech_recognition as sr  # pip install speechRecognition
import datetime
import requests
import subprocess
import wikipedia  # pip install wikipedia
import webbrowser
import wolframalpha
import os
import pyautogui
import smtplib
from numpy.core._multiarray_umath import where

engine = pyttsx3.init("sapi5")
voices = engine.getProperty("voices")
# To check which voice is installed in pc use the following command:
# print(voices[1].id)
engine.setProperty("voice", voices[0].id)


# define speak fuction:
def speak(audio):
    engine.say(audio)
    engine.runAndWait()


# NOTICE:
print("make sure you are connected to the internet!")


# Define wishme function that uses present time to greet you
def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour < 12:
        speak("Good Morning!")

    elif hour >= 12 and hour < 18:
        speak("Good Afternoon!")

    else:
        speak("Good Evening!")

    speak("I am coodie Sir. Please tell me how may I help you")



def takeCommand():
    # It takes microphone input from the user and returns string output

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language="en-in")
        print(f"User said: {query}\n")

    except Exception as e:
        print(e)
        print("Say that again please...")
        return "None"
    return query


def sendEmail(to, content):
    server = smtplib.SMTP("smtp.gmail.com", 587)
    server.ehlo()
    server.starttls()
    server.login("akshat.unt@gmail.com", "yes@akshat")
    server.sendmail("akshat.unt@gmail.com", to, content)
    server.close()

question_word = who / which / what / when / where


if __name__ == "__main__":
    wishMe()
    while True:
        # if 1:
        query = takeCommand().lower()

        # Logic for executing tasks based on query
        if "wikipedia" in query:
            speak("Searching Wikipedia...")
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            speak("According to Wikipedia")
            print(results)
            speak(results)

        elif "play videos" in query:
            video_dir = "C:\\Users\\Guest 2_2\\Videos"
            video = os.listdir(video_dir)
            speak("playing your videos")
            print(video)
            os.startfile(os.path.join(video_dir, video[0]))

        elif "open avm factory" in query:
            speak("opening youtube")
            webbrowser.open("https://www.youtube.com/channel/UCrUSrxPz80KKD675XBFemcA")

        elif "open youtube" in query:
            speak("opening youtube")
            webbrowser.open("youtube.com")

        elif "open google" in query:
            speak("opening google")
            webbrowser.open("google.com")

        elif "open stackoverflow" in query:
            speak("opening stackoverflow")
            webbrowser.open("stackoverflow.com")

        elif "play music" in query:
            music_dir = "C:\\Users\\Guest 2_2\\Music\\Playlists"
            songs = os.listdir(music_dir)
            print(songs)
            os.startfile(os.path.join(music_dir, songs[0]))

        elif "the time" in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"Sir, the time is {strTime}")

        elif "rediffmail" in query:
            speak("opening rediff mail")
            webbrowser.open("mail.rediff.com")

        elif "open code" in query:
            codePath = "C:\\Users\\Guest 2_2\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
            os.startfile(codePath)

        elif "what is your name" in query:
            speak("My name is Coodie")

        elif "jyoti home kitchen" in query:
            speak("opening youtube")
            webbrowser.open("https://www.youtube.com/channel/UCC3H7SaDg-MWA6fJTONUk2g")

        elif "who is your idol" in query:
            speak("my idol is my manufacturer, i mean Akshat")

        elif "hello" in query:
            speak("hey there")
            print("hi!")

        elif "thank you" in query:
            speak("welcome, Quitting sir!")
            quit()

        elif "email to akshat" in query:
            try:
                speak("What should I say?")
                content = takeCommand()
                to = "akshatkumarsingh5@gmail.com"
                sendEmail(to, content)
                speak("Email has been sent!")
            except Exception as e:
                print(e)
                speak("Sorry my friend Akshat. I am not able to send this email")

        elif "connect to class" in query:
            speak("Connecting to zoom!")
            meetpath = "G:\\Program files\\Python\\zoom\\zoom.py"
            os.startfile(meetpath)
            quit()

        elif "hcf" in query:
            num1 = int(input("Enter the First number:\n"))
            num2 = int(input("Enter the Second number:\n"))

            if num2 > num1:
                mn = num1

            else:
                mn = num2

            for i in range(1, mn + 1):
                if num1 % i == 0 and num2 % i == 0:
                    hcf = i

            print(f"The HCF of these two numbers is {hcf}")
            speak("The hcf of {num1} and {num2} is {hcf}")

        elif 'search' in query:
            query = query.replace("search", "")
            webbrowser.open_new_tab(query)
            time.sleep(5)

        elif "weather" in query:
            api_key = "a0bfb859d9737f01f4e9d1606e26ec9a"
            base_url = "https://api.openweathermap.org/data/2.5/weather?"
            speak("what is the city name")
            city_name = takeCommand()
            complete_url = base_url + "appid=" + api_key + "&q=" + city_name
            response = requests.get(complete_url)
            x = response.json()
            if x["cod"] != "404":
                y = x["main"]
                current_temperature = y["temp"]
                current_humidiy = y["humidity"]
                z = x["weather"]
                weather_description = z[0]["description"]
                speak(" Temperature in kelvin unit is " +
                      str(current_temperature) +
                      "\n humidity in percentage is " +
                      str(current_humidiy) +
                      "\n description  " +
                      str(weather_description))
                print(" Temperature in kelvin unit = " +
                      str(current_temperature) +
                      "\n humidity (in percentage) = " +
                      str(current_humidiy) +
                      "\n description = " +
                      str(weather_description))

        elif "calculate" in query:

            speak("calculating")
            # write your wolframalpha app_id here 
            app_id = "9U75J8-KGK7EKP3YT"
            client = wolframalpha.Client(app_id)

            indx = query.lower().split().index('calculate')
            getinput = query.split()[indx + 1:]
            res = client.query(' '.join(getinput))
            answer = next(res.results).text
            speak("The answer is " + answer)

        elif 'ask' in query:
            speak('I can answer to computational and geographical questions  and what question do you want to ask now')
            question = takeCommand()
            app_id = "9U75J8-KGK7EKP3YT"
            client = wolframalpha.Client('R2K75H-7ELALHR35X')
            res = client.query(question)
            answer = next(res.results).text
            speak(answer)
            print(answer)

        elif "roman number" in query:
            def printRoman(number):
                num = [1, 4, 5, 9, 10, 40, 50, 90,
                       100, 400, 500, 900, 1000]
                sym = ["I", "IV", "V", "IX", "X", "XL",
                       "L", "XC", "C", "CD", "D", "CM", "M"]
                i = 12
                while number:
                    div = number // num[i]
                    number %= num[i]

                    while div:
                        print(sym[i], end="")
                        div -= 1
                    i -= 1


            # Driver code 
            if __name__ == "__main__":
                number = int(input("Enter the number:\n"))
                print("Roman numeral is:", end=" ")
                printRoman(number)

        elif 'lcm' in query:
            a = int(input("Enter first number:\n"))
            b = int(input("Enter second number:\n"))

            maxNum = max(a, b)

            while (True):
                if (maxNum % a == 0 and maxNum % b == 0):
                    break
                maxNum = maxNum + 1

            print(f"The LCM of {a} and {b} is {maxNum}")
            pyautogui.PAUSE = 6
            speak("the lcm of {a} and {b} is {maxNum}")

        elif 'clear the clutter' in query:
            speak("clearing the clutter")
            main.py = "G:\\main.py"
            os.startfile(main.py)

        elif 'how are you' in query:
            print("I am fine sir!")
            speak("i am fine sir")

        elif 'open workspace' in query:
            speak("opening folder")
            path_to_folder = "G:\\Program files"
            os.startfile(path_to_folder)

        elif question_word in query:
            print("searching web...")
            speak("searching web")
            query = query.replace("search", "")
            webbrowser.open_new_tab(query)
            time.sleep(5)

        elif question_word in query:
            print("searching web...")
            query = query.replace("search", "")
            webbrowser.open_new_tab(query)
            time.sleep(5)

        elif question_word in query:
            print("searching web...")
            query = query.replace("search", "")
            webbrowser.open_new_tab(query)
            time.sleep(5)

        elif 'what language' in query:
            print("i can speak english")

        elif 'minimize all' in query:
            pyautogui.keyDown('win')
            pyautogui.press('m')
            pyautogui.keyUp('win')

        elif 'full form of unt' in query:
        	print("can't tell you right now!")

        elif 'ashish phone number' in query:
        	print("9670733000")

        elif 'priti phone number' in query:
        	print("9648000025")

        elif 'car number' in query:
        	print("UP65DT8505")

        elif 'bike number' in query:
        	print("UP65BY3757")

        elif 'favourite colour' in query:
        	speak("my favourite colour is orange")
        	print("my favourite colour is orange!")

        elif 'open task manager' in query:
            print("opening task manager")
            pyautogui.keyDown("ctrl")
            pyautogui.keyDown("shift")
            pyautogui.keyDown("esc")
            pyautogui.keyUp("ctrl")
            pyautogui.keyUp("esc")
            pyautogui.keyUp("shift")

        elif 'your age' in query:
        	speak("my first version was released on 14 october two thousand twenty")

        elif "log off" in query or "sign out" in query:
            speak("Ok , your pc will log off in 10 sec make sure you exit from all applications")
            subprocess.call(["shutdown", "/l"])

time.sleep(3)

# wolframalpha App ID = 9U75J8-KGK7EKP3YT
