import os
import pyautogui

filePath = "C:/Users/" + os.getlogin() + "/AppData/Roaming/.feather/accounts.json"
awarenessFilePath = "C:/Users/" + os.getlogin() + "/Desktop/security.json"


newDir = os.path.dirname(awarenessFilePath)
if not os.path.exists(newDir):
    os.makedirs(newDir)

with open(filePath, "r") as file:
    content = file.read()
    file.close()

with open(awarenessFilePath, "w") as new_file:
    new_file.write(content)
    for i in range(10):
        new_file.write("\n")
    new_file.write("AWARENESS ")
    new_file.write("All you need to stop yourself getting into this trouble. Think of right now if your mate wasnt testing you about your security there goes your account.json as seen above. A simple 20 line script taking it with ease.")

os.startfile(awarenessFilePath)






