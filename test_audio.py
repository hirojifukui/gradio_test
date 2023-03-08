import gradio as gr
import openai, subprocess
import pyttsx3

messages = [{"role": "system", "content": 'You are a therapist. Respond to all input in 25 words or less.'}]

def transcribe(audio):
    global messages

    audio_file = open(audio, "rb")
    transcript = openai.Audio.transcribe("whisper-1", audio_file)

    messages.append({"role": "user", "content": transcript["text"]})

    response = openai.ChatCompletion.create(model="gpt-3.5-turbo", messages=messages)

    system_message = response["choices"][0]["message"]
    messages.append(system_message)
    engine = pyttsx3.init()
    #subprocess.run(["say", system_message['content']])
    #subprocess.Popen([r"start", r"I:\My Drive\RISU\System development\OpenAI\Subprocess\tts_test.py"], shell=True)
    engine.say(system_message['content'])
    engine.runAndWait()
    engine.stop()
    chat_transcript = ""
    for message in messages:
        if message['role'] != 'system':
            chat_transcript += message['role'] + ": " + message['content'] + "\n\n"

    return chat_transcript

ui = gr.Interface(fn=transcribe, inputs=gr.Audio(source="microphone", type="filepath"), outputs="text").launch()
ui.launch()