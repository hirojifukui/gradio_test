from gradio.components import Textbox
import gradio as gr
import openai
import subprocess

def m_construct(prompt):
    ms1 = """You are AI programming trainner.
         ### Explain what are wrong in the below Python code for the given challenge below.
         ### Then, provide the bug fixed code.
         Give xList = [1,2,3], print out all elements.
         
        xList = [1,2,3]
        for x in xList
          print(x)

        File "<string>", line 2
        for x in xList
                 ^
        AI: for loop requires : at the end.
        xList = [1,2,3]
        for x in xList:
          print(x)

        ### Explain what are wrong in the below Python code for the given challenge below.
        """
    return ms1 + prompt

def ai(prompt, temp):
  return openai.Completion.create(
                engine="text-davinci-002",
                prompt=prompt,
                max_tokens=1024,
                n=1,
                stop=None,
                temperature=temp,
            )["choices"][0]["text"].strip()

def prop(code):
  process = subprocess.Popen(['python', '-c', code], stderr=subprocess.PIPE, stdout=subprocess.PIPE)
  output, error = process.communicate()

  if error:
    prompt = code + "\n\n" + error.decode()
    message = m_construct(prompt)
    return prompt + ai(message, 0)
  else:
    return output.decode()

with gr.Blocks() as ui:
  challenge = "Give xList = [1,2,3], print out all elements."
  gr.Markdown(
    """
    #Study Python Coding
    
    """ + challenge
  )
  code = gr.Textbox(lines = 10, placeholder="Enter code")
  output = gr.Textbox(lines=10)
  btn = gr.Button("Run")
  btn.click(fn=prop, inputs=code, outputs=output)

ui.launch()