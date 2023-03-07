from gradio.components import Textbox
import gradio as gr
import openai
import subprocess

def prop(code):
  process = subprocess.Popen(['python', '-c', code], stderr=subprocess.PIPE, stdout=subprocess.PIPE)
  output, error = process.communicate()

  if error:
    return code + "\n\n" + error.decode()
  else:
    return output.decode()

ui = gr.Interface(fn=prop, 
                  inputs=gr.Textbox(lines = 10, placeholder="Enter code"),
                  outputs = Textbox(lines=10),)

ui.launch()