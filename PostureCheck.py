from playsound import playsound
import time

print("Posture Checker has started")
minutesAsString = input("After how many minutes should you be reminded to check your posture? ")
userInputIsInvalid = True

while userInputIsInvalid:
    try:
        minutes = int(minutesAsString)
    except:
        print("The user input was not a valid integer, please try again.")
        minutesAsString = input("After how many minutes should you be reminded to check your posture? ")
    else:
        minutes = abs(minutes)
        soundIntervalSeconds = minutes * 60
        userInputIsInvalid = False

start = time.time()
elapsedMinutes = 0

while True:
    end = time.time()
    elapsedSeconds = end - start

    if elapsedSeconds > soundIntervalSeconds:
        playsound('./alert.wav')
        start = time.time()
        elapsedMinutes = elapsedMinutes + minutes
        print(str(elapsedMinutes) + " minutes have passed.")
    
    time.sleep(1)
