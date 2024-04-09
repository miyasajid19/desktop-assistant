from tkinter import *
import pyttsx3
import speech_recognition as sp
import datetime
import subprocess
import cv2
import os
import requests
import wikipedia
import webbrowser
import pywhatkit
import smtplib as s
import sys
import pyautogui
import time
import wmi
import math
from ctypes import cast, POINTER
from comtypes import CLSCTX_ALL
from pycaw.pycaw import AudioUtilities, IAudioEndpointVolume
import platform
import psutil
from PyPDF2 import PdfReader
import ctypes

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def firstconfig(a):
    firstcontent.config(text=a)

def secondconfig(a):
    secondcontent.config(text=a, fg="#407432", font="roman 14 ", anchor="sw")

def thirdconfig(a):
    thirdcontent.config(text=a, fg="#407432", font="roman 14 ", anchor="sw")

def open_notepad():
    npath = "C:\\Windows\\System32\\notepad.exe"
    subprocess.Popen(npath)

def open_command_prompt():
    subprocess.Popen(['start', 'cmd'], shell=True)

def open_camera():
    try:
        capture = cv2.VideoCapture(0)
        while True:
            ret, img = capture.read()
            cv2.imshow('webcam', img)
            k = cv2.waitKey(50)
            if k == 27:
                break
        capture.release()
        cv2.destroyAllWindows()
    except Exception as e:
        speak("not supported in your system")

def play_music():
    musicdirs = r"C:\\Users\\ACER\\OneDrive\\Desktop\\Positive Vibes Music 🍀 English Songs Love Playlist _ Tiktok Songs 2023 With Lyrics.mp3"
    os.startfile(musicdirs)

def ip_address():
    ip = requests.get("https://api.ipify.org").text
    p
    speak(f"your ip address is : {ip}")

def swikipedia():
    speak("searching wikipedia")
    
    query = take()  # Assuming take() function retrieves user input
    query = query.replace("wikipedia", "")
    results = wikipedia.summary(query, sentences=5)
    speak("according to wikipedia")
    
    firstcontent.config(text=f"according to wikipedia"+results) 
    
    speak(results)
    


def open_youtube():
    webbrowser.open("www.youtube.com")

def facebook():
    webbrowser.open("www.facebook.com")

def w3schools():
    webbrowser.open("www.w3schools.com")

def Google():
    speak("what do you want to search?")
    search_query = take().lower()
    print(search_query)
    webbrowser.open(f"https://www.google.com/search?q={search_query}")

def Whatsapp():
    speak("what you want send??")
    message1 = take()
    cmin = datetime.datetime.today().minute
    chr = datetime.datetime.today().hour
    pywhatkit.sendwhatmsg("sender number with country code", f"{message1}", chr, cmin + 2)

def Syoutube():
    speak("title??")
    search_query = take().lower()
    pywhatkit.playonyt(search_query)

def sendmail(message1):
    server = s.SMTP('smtp.gmail.com', 587)
    server.starttls()
    try:
        # Use the application-specific password generated from your Google Account
        server.login('your mail', 'your password')
    except Exception as e:
        print(e)
    subjecttext = 'From Jarvis'
    message = f"Subject: {subjecttext}\n\n{message1}"
    try:
        server.sendmail('your mail', 'reciever mail', message)
        speak("Successfully mail was sent")
    except Exception as e:
        speak(f"error in sending mail due to {e}")
    server.quit()

def Sendmail():
    speak("what's the message?")
    message1 = take()
    sendmail(message1)

def shutdown():
    os.system("shutdown /s /t 1")

def restart():
    os.system("shutdown /r /t 1")

def sleep1():
    os.system("rundll32.exe powrprof.dll,SetSuspendState 0,1,0")

def nothanks():
    a = "thank you for using me.\nyou can can be any time you want. Have a good day. \n bye"
    firstcontent.config(text=a)
    speak(a)
    sys.exit()

def close_notepad():
    os.system("taskkill /f /im notepad.exe")
    speak("Notepad closed successfully.")

def close_command_prompt():
    os.system("taskkill /f /im cmd.exe")
    speak("Command prompt closed successfully.")

def close_youtube():
    # Use pyautogui to simulate key presses for closing the browser tab or window
    pyautogui.hotkey('ctrl', 'w')  # Close the current tab/window
    speak("YouTube closed successfully.")

def nextvid():
    pyautogui.hotkey('shift', 'n')  # Next video
    speak("Playing next video.")

def previousvideo():
    pyautogui.hotkey('shift', 'p')  # Previous video
    speak("Playing previous video.")

def toggle():
    pyautogui.hotkey('k')  # Play/pause toggle
    speak("Playback toggled.")

def mute():
    pyautogui.hotkey('shift', 'm')  # Mute/unmute
    speak("Mute toggled.")

def speed():
    pyautogui.hotkey('shift', '>')  # Increase playback speed
    speak("Speed increased.")

def dspeed():
    pyautogui.hotkey('shift', '<')  # Decrease playback speed
    speak("Speed decreased.")

def space():
    pyautogui.hotkey('space')  # Press spacebar
    speak("Spacebar pressed.")

def get_brightness():
    c = wmi.WMI(namespace='wmi')
    brightness = c.WmiMonitorBrightness()[0]
    return brightness.CurrentBrightness

def set_brightness(level):
    c = wmi.WMI(namespace='wmi')
    try:
        methods = c.WmiMonitorBrightnessMethods()[0]
        methods.WmiSetBrightness(level, 0)
    except:
        firstcontent.config(text="sorry to perform")

def increase_brightness():
    current_brightness = get_brightness()
    new_brightness = min(100, current_brightness + 25)  # Increase brightness by 25%, capped at 100
    set_brightness(new_brightness)
    firstcontent.config(text="Brightness increased successfully.")

def decrease_brightness():
    current_brightness = get_brightness()
    new_brightness = min(100, current_brightness - 25)  # Increase brightness by 25%, capped at 100
    set_brightness(new_brightness)
    firstcontent.config(text="Brightness decreased successfully.")

def get_volume():
    devices = AudioUtilities.GetSpeakers()
    interface = devices.Activate(IAudioEndpointVolume._iid_, CLSCTX_ALL, None)
    volume = cast(interface, POINTER(IAudioEndpointVolume))
    return volume.GetMasterVolumeLevelScalar() * 100

def set_volume(volume_level):
    devices = AudioUtilities.GetSpeakers()
    interface = devices.Activate(IAudioEndpointVolume._iid_, CLSCTX_ALL, None)
    volume = cast(interface, POINTER(IAudioEndpointVolume))
    volume.SetMasterVolumeLevelScalar(volume_level, None)

def increase_volume():
    current_volume = get_volume()
    new_volume = min(100, current_volume + 25)  # Increase volume by 25%, capped at 100
    set_volume(new_volume / 100)  # Volume level should be in the range [0.0, 1.0]
    firstcontent.config(text="Volume increased successfully.")

def decrease_volume():
    current_volume = get_volume()
    new_volume = min(100, current_volume - 25)  # Increase volume by 25%, capped at 100
    set_volume(new_volume / 100)  # Volume level should be in the range [0.0, 1.0]
    firstcontent.config(text="Volume decreased successfully.")

def open_access():
    access_path = "C:\\ProgramData\\Microsoft\\Windows\\Start Menu\\Programs\\Access.lnk"
    os.startfile(access_path)

def open_powerpoint():
    powerpoint_path = "C:\\ProgramData\\Microsoft\\Windows\\Start Menu\\Programs\\PowerPoint.lnk"
    os.startfile(powerpoint_path)

def open_excel():
    excel_path = "C:\\ProgramData\\Microsoft\\Windows\\Start Menu\\Programs\\Excel.lnk"
    os.startfile(excel_path)

def open_word():
    word_path = "C:\\ProgramData\\Microsoft\\Windows\\Start Menu\\Programs\\Word.lnk"
    os.startfile(word_path)

def close_access():
    access_path = "C:\\ProgramData\\Microsoft\\Windows\\Start Menu\\Programs\\Access.lnk"
    if os.path.exists(access_path):
        pyautogui.hotkey("alt", "f4")
        os.remove(access_path)
        speak("Microsoft Access closed.")
    else:
        speak("Microsoft Access is not currently open.")

def close_powerpoint():
    powerpoint_path = "C:\\ProgramData\\Microsoft\\Windows\\Start Menu\\Programs\\PowerPoint.lnk"
    if os.path.exists(powerpoint_path):
        pyautogui.hotkey("alt", "f4")
        os.remove(powerpoint_path)
        speak("Microsoft PowerPoint closed.")
    else:
        speak("Microsoft PowerPoint is not currently open.")

def close_excel():
    pyautogui.hotkey("alt", "f4")

def close_word():
    word_path = "C:\\ProgramData\\Microsoft\\Windows\\Start Menu\\Programs\\Word.lnk"
    if os.path.exists(word_path):
        os.remove(word_path)
        speak("Microsoft Word closed.")
    else:
        speak("Microsoft Word is not currently open.")

def open_this_pc():
    os.startfile("explorer")

def open_c_drive():
    os.startfile("C:\\")

def open_e_drive():
    os.startfile("E:\\")

def close_explorer():
    os.system("taskkill /f /im explorer.exe")
    speak("File Explorer closed.")

def hide_file(file_path):
    try:
        if os.path.exists(file_path):
            os.rename(file_path, file_path + ".hidden")
            speak("File hidden successfully.")
            return True
        else:
            speak("Error: File not found or unable to hide.")
            return False
    except Exception as e:
        speak(f"Error: {str(e)}")
        return False

def display_hidden_file(file_path):
    try:
        hidden_file_path = file_path + ".hidden"
        if os.path.exists(hidden_file_path):
            os.rename(hidden_file_path, file_path)
            speak("Hidden file displayed successfully.")
            return True
        else:
            speak("Error: Hidden file not found or unable to display.")
            return False
    except Exception as e:
        speak(f"Error: {str(e)}")
        return False

def take_screenshot():
    try:
        screenshot = pyautogui.screenshot()
        screenshot.save("screenshot.png")
        speak("Screenshot saved as screenshot.png")
    except Exception as e:
        speak(f"An error occurred while taking the screenshot: {str(e)}")

def system_information():
    system_info = {}
    system_info['Operating System'] = platform.system()
    system_info['OS Version'] = platform.version()
    system_info['Processor'] = platform.processor()
    system_info['Memory'] = str(round(psutil.virtual_memory().total / (1024.0 ** 3), 2)) + " GB"
    a = f"operating system : {system_info['Operating System']}\nos version : {system_info['OS Version']}\nsystem processor : {system_info['Processor']}\n memory : {system_info['Memory']}"
    firstcontent.config(text=a)
    speak(a)

def get_date_time():
    now = datetime.datetime.now()
    return now.strftime("%A, %d %B %Y %I:%M:%S %p")

def current_date_time():
    current_date_time = get_date_time()
    speak(f"The current date and time is {current_date_time}.")

def read_pdf(pdf_path):
    try:
        with open(pdf_path, 'rb') as file:
            reader = PdfReader(file)
            text = ''
            for page in reader.pages:
                text += page.extract_text()
            return text
    except Exception as e:
        print(f"Error reading PDF: {e}")
        return None

def reading_pdf():
    text = read_pdf(pdf_path)
    if text:
        speak("Here is the text from the PDF:")
        speak(text)
    else:
        speak("Sorry, I couldn't read the PDF file.")

def perform(query):
    if query is None:
        take()

    actions = {
        "open notepad": open_notepad,
        "open command prompt": open_command_prompt,
        "close notepad": close_notepad,
        "close command prompt": close_command_prompt,
        "close youtube": close_youtube,
        "open youtube": open_youtube,
        "next": nextvid,
        "previous": previousvideo,
        "increase speed": speed,
        "decrease speed": dspeed,
        "play": toggle,
        "pause": toggle,
        "mute": mute,
        "space": space,
        "screenshot": take_screenshot,
        "open access": open_access,
        "open powerpoint": open_powerpoint,
        "open excel": open_excel,
        "open word": open_word,
        "close access": close_access,
        "close powerpoint": close_powerpoint,
        "close excel": close_excel,
        "close word": close_word,
        "open this pc": open_this_pc,
        "open c drive": open_c_drive,
        "open e drive": open_e_drive,
        "close explorer": close_explorer,
        "increase brightness": increase_brightness,
        "decrease brightness": decrease_brightness,
        "increase volume": increase_volume,
        "decrease volume": decrease_volume,
        "system information": system_information,
        "current date and time": current_date_time,
        "read pdf": read_pdf,
        "hide file": hide_file,
        "display hidden file": display_hidden_file,
        "send mail": sendmail,
        "whatsapp": Whatsapp,
        "search youtube": Syoutube,
        "shutdown": shutdown,
        "restart": restart,
        "sleep": sleep1,
        "hibernate": sleep1,
        "no thanks": nothanks,
        "wikipedia":swikipedia
    }

    for key, action in actions.items():
        try:
            if key in query:
                action()
                break
        except Exception as e:
            print(e)

def wish():
    c_hour = int(datetime.datetime.now().hour)
    if c_hour < 12:
        a = "Good morning sir."
    elif 12 <= c_hour < 16:
        a = "Good afternoon sir."
    else:
        a = "Good evening sir."
    a = a + "\nI am Jarvis,\nyour personal assistant.\nHow can I assist you today??"
    firstconfig(a)
    speak(a)
    thirdconfig("")

def take():
    
    r = sp.Recognizer()
    with sp.Microphone() as source:
        thirdconfig("Listening...")
        print("Listening...")
        root.update()
        r.adjust_for_ambient_noise(source)  # Adjust for ambient noise
        r.pause_threshold = 1
        try:
            audio = r.listen(source, timeout=0, phrase_time_limit=5)  # Increase timeout and phrase time limit
        except sp.WaitTimeoutError:
            speak("Sorry, I didn't catch that. Please speak louder or more clearly.")
            return 'a'

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language="en")
        query = query.lower()
        print(f"User said: {query}")
        secondconfig(query)
        firstconfig(f"performing on {query}")
        speak(f"performing on {query}")  # Clear first label when user speaks
        # Schedule the update of the status label after 1 second
        root.after(1000, lambda: thirdconfig("Recognizing..."))
    except Exception as e:
        speak(str(e))
        return None
    return query

root = Tk()
root.title("J.A.R.V.I.S")
root.configure(bg="#FDF0D1")

Label(root, text="J.A.R.V.I.S.", fg="#5FBDFF", font="stencil 70 bold").grid(row=0, sticky=N, columnspan=4)

first = Label(root, text="Jarvis", fg="#FB5660", bg="#FDF0D1", font="stencil 20 bold")
first.grid(row=1, column=0)
firstcontent = Label(root, text="", fg="#407432", bg="#FDF0D1", font="roman 14 ", anchor="sw")
firstcontent.grid(row=1, column=1, columnspan=3)

second = Label(root, text="User", fg="#FB5660", bg="#FDF0D1", font="stencil 20 bold")
second.grid(row=2, column=0)
secondcontent = Label(root, text="", fg="#407432", bg="#FDF0D1", font="roman 14 ", anchor="sw")
secondcontent.grid(row=2, column=1, columnspan=3)

third = Label(root, text="Status", fg="#FB5660", bg="#FDF0D1", font="stencil 20 bold")
third.grid(row=3, column=0)
thirdcontent = Label(root, text="Listening...", fg="#407432", bg="#FDF0D1", font="roman 14 ", anchor="sw")
thirdcontent.grid(row=3, column=1, columnspan=3)
frame1=LabelFrame(root,bg="#FDF0D1")
frame1.grid(row=4,column=0,columnspan=4)
fourth = Label(frame1, text="Command J.A.R.V.I.S. understands", fg="#FB5660", bg="#FDF0D1", font="stencil 20 bold")
fourth.grid(row=4, column=0, columnspan=4)

cont4 = ['open notepad', 'close notepad', 'open command prompt',
         'close command prompt','wikipedia' , 'open youtube','search youtube','close youtube',
         'next', 'previous', 'play', 'pause','mute','space',
         'increase speed', 'decrease speed',
           'screenshot',
         'open access', 'close access', 'open powerpoint','close powerpoint', 'open excel',
          
         'close excel', 'open word','close word', 'open this pc',
         'open C/E  drive',
         'close explorer', 'increase brightness', 'decrease brightness',
         'increase volume', 'decrease volume', 'system information',
         'current date and time', 'read pdf', 'hide file',
         'display hidden file', 'send mail', 'whatsapp',
          'shutdown', 'sleep', 'restart', 'hibernate', 'no thanks']

# Split the list into sublists of 11 items each
sublists = [cont4[i:i+11] for i in range(0, len(cont4), 11)]

# Create Labels for each item in the sublists and organize them into 4 columns
row_index = 5  # Start from row 5 to avoid overlapping with the title
column_index = 0
for sublist in sublists:
    for index, item in enumerate(sublist):
        label = Label(frame1, text=f"{index + 1}. {item}", fg="#407432", bg="#FDF0D1", font="roman 14 ", anchor="w")
        label.grid(row=row_index, column=column_index, sticky="ew", padx=5, pady=2)
        row_index += 1
    column_index += 1
    row_index = 5  # Reset row index for the next c
root.iconbitmap(r"E:\vscode\python\PYTHON FILES\J.A.R.V.I.S.H\file_type_ai_icon_130757.ico")

## Starting the engine ###
engine = pyttsx3.init("sapi5")
voices = engine.getProperty("voices")
print(engine.setProperty('voice', voices[0].id))



global pdf_path
pdf_path=r"E:\Downloads\I-Was-Never-Broken-Sara-Sheehan-Samantha-Stone-1-2018-Createspace-Independent-Publishing-Platform-9781719105088-f24a9381755bc0d49aee5e36deadb592-Annas-Archive.pdf"#replace with your pdf
wish()
while True:
    perform(take())
    root.update()

root.mainloop()
