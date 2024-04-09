Desktop Assistant named as----->J.A.R.V.I.S.

J.A.R.V.I.S. (Just A Rather Very Intelligent System) is a Python-based personal assistant inspired by Tony Stark's assistant in the Marvel Cinematic Universe. Although this program is limited in its code and efficiency, it serves as an excellent project for beginners. It's capable of performing various tasks such as opening applications, browsing the web, sending emails, controlling media playback, and providing system information, all through voice commands. While it currently supports only 44 commands, it can still be quite useful for smaller tasks like shutdown, sleep, adjusting brightness and volume, searching and playing YouTube videos, and controlling playback speed. Integrating different APIs like OpenAI could further enhance its productivity and usefulness.

Features

  1. Voice Recognition: Utilizes the speech_recognition library to recognize voice commands.
    
  2. Text-to-Speech: Employs the pyttsx3 library to convert text to speech for providing feedback to the user.
    
  3. Task Automation: Performs a wide range of tasks including opening applications, controlling media playback, sending emails, etc.
    
  4. Web Interaction: Can perform web searches using Wikipedia, Google, YouTube, and more.
    
  5. System Control: Provides system information, shuts down or restarts the system, and adjusts volume and brightness.
    
  6. GUI Interface: Features a graphical user interface built using Tkinter for user interaction.



Prerequisites

  1. Python 3.x
  2. modules: 

          pip install pyttsx3
          pip install SpeechRecognition
          pip install opencv-python
          pip install wikipedia
          pip install pywhatkit
          pip install pyautogui
          pip install wmi
          pip install psutil
          pip install comtypes
          pip install PyPDF2
      
  3.Microsoft Windows operating system (some functionalities may not be supported on other operating systems)


Converting  .py file to .exe file

      pyinstaller --onefile --noconsole main.py

Interface:
        ![Screenshot 2024-04-10 035355](https://github.com/miyasajid19/desktop-assistant/assets/166320427/dd48287a-86be-4548-9133-8195aa462ccc)



Contributing

  Contributions are welcome! If you have any ideas for improving J.A.R.V.I.S. or adding new features, feel free to open an issue or submit a pull request.
