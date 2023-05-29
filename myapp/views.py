# myapp/views.py
import os
import speech_recognition as sr
from gtts import gTTS
from django.shortcuts import render
from django.http import FileResponse
from playsound import playsound

def home(request):
    return render(request, 'home.html')

def ask_question(request):
    if request.method == 'POST':
        questions = ['તમારું નામ શું છે?', 'તમે ક્યાંથી છો?', 'તમારી ઉંમર કેટલી છે?']
        answers = []

        recognizer = sr.Recognizer()
        microphone = sr.Microphone()

        for question in questions:
            while True:
                tts = gTTS(text=question, lang='gu')
                tts.save('question.mp3')
                playsound('question.mp3')

                with microphone as source:
                    recognizer.adjust_for_ambient_noise(source)
                    audio = recognizer.listen(source)

                try:
                    answer = recognizer.recognize_google(audio, language='gu-IN')  # Set the language to Gujarati
                    if answer:
                        break  # loop tuti jase jo ene answer malse to
                except sr.UnknownValueError:
                    answer = "Sorry, I didn't catch that."
                except sr.RequestError:
                    answer = "Sorry, there was an issue with the speech recognition service."

            answers.append(answer)

        output_filename = os.path.join(os.path.dirname(__file__), 'output.txt')
        with open(output_filename, 'w', encoding='utf-8') as f:  # Set encoding to 'utf-8' for Gujarati characters
            for i in range(len(questions)):
                f.write(f"Question: {questions[i]}\n")
                f.write(f"Answer: {answers[i]}\n\n")

        return render(request, 'answers.html', {'answers': answers,'questions': questions})

    return render(request, 'question.html')

def download_output(request):
    output_filename = os.path.join(os.path.dirname(__file__), 'output.txt')
    response = FileResponse(open(output_filename, 'rb'))
    response['Content-Disposition'] = 'attachment; filename="output.txt"'
    return response

# # myapp/views.py
# import os
# import speech_recognition as sr
# from gtts import gTTS
# from django.shortcuts import render
# from django.http import FileResponse
# from playsound import playsound

# def home(request):
#     questions = ['તમારું નામ શું છે?', 'તમે ક્યાંથી છો?', 'તમારી ઉંમર કેટલી છે?']
#     answers = []

#     if request.method == 'POST':
#         recognizer = sr.Recognizer()
#         microphone = sr.Microphone()

#         for question in questions:
#             while True:
#                 tts = gTTS(text=question, lang='gu')
#                 tts.save('question.mp3')
#                 playsound('question.mp3')

#                 with microphone as source:
#                     recognizer.adjust_for_ambient_noise(source)
#                     audio = recognizer.listen(source)

#                 try:
#                     answer = recognizer.recognize_google(audio, language='gu-IN')  # Set the language to Gujarati
#                     if answer:
#                         break  # Break the loop if an answer is received
#                 except sr.UnknownValueError:
#                     answer = "Sorry, I didn't catch that."
#                 except sr.RequestError:
#                     answer = "Sorry, there was an issue with the speech recognition service."

#             answers.append(answer)

#         output_filename = os.path.join(os.path.dirname(__file__), 'output.txt')
#         with open(output_filename, 'w', encoding='utf-8') as f:  # Set encoding to 'utf-8' for Gujarati characters
#             for i in range(len(questions)):
#                 f.write(f"Question: {questions[i]}\n")
#                 f.write(f"Answer: {answers[i]}\n\n")

#     return render(request, 'home.html', {'questions': questions, 'answers': answers})

# def ask_question(request):
#     return render(request, 'ask_question.html')
