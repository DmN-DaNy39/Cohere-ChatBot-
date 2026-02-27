import speech_recognition as sr
import pyttsx3
import cohere
#initialising cohere API key
co = cohere.ClientV2("#ADD COHERE API KEY :)")

#Send prompt to cohere through API 
def chat(prompt):
    response = co.chat(
        model="command-a-03-2025",
        messages=[
            {
                "role": "user",
                "content": prompt,
            }
        ],
    )

    reply = response.message.content[0].text.strip()
    tts(reply)

#Listen to the user and return what the user said
def speechRecog():
    recognizer = sr.Recognizer()
    try:
        with sr.Microphone() as mic:
            recognizer.adjust_for_ambient_noise(mic, duration=0.2)
            audio = recognizer.listen(mic)

            text = recognizer.recognize_google(audio)
            text = text.lower()

            print(f"User: {text}")
            return text

    except sr.UnknownValueError:
        return ""

#creating the text to speech engine to say the ai response
def tts(text):
    print(f"CPU: {text}")
    engine = pyttsx3.init(driverName='sapi5')
    engine.setProperty('rate', 150)
    engine.say(text)
    engine.runAndWait()
    engine.stop()
    del engine


while True:
    user_input = speechRecog()
    if user_input.lower() in ["quit", "exit", "bye"]:
        break
    else:
        chat(user_input)

    