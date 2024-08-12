import os
import pyautogui
import time
import pyperclip # use to retrive content from clipboard.
from groq import Groq




client = Groq(
    api_key= os.environ.get("BOT_API_KEY")
)

def last_message_from_sender(chat_log, sender_name="Mom:"):     
    # Split the chat log into individual messages
    messages = chat_log.strip().split('/2024')[-1]
    if sender_name in messages:
      return True
    return False


# Assuming a delay to switch to the window where the action needs to be performed
time.sleep(1.3)

pyautogui.click(425, 65) # Click on a tab at coordinates (425, 65)
time.sleep(1)            # wait for 1s to ensure the click is registered.


while True:

    # Drag from (578, 459) to (576, 1472) to select text
    pyautogui.moveTo(578, 459)
    pyautogui.dragTo(584, 1637, duration=1.0, button='left')


    # Copy the selected text to clipboard (Ctrl+C shortcut)
    pyautogui.hotkey('ctrl', 'c')
    time.sleep(1) # wait for 1s to ensure the copy command is completed
    pyautogui.click(593,588)
    # time.sleep(1) # wait for 1s to ensure the copy command is completed


    # Retrieve the copied text from the clipboard
    chat_history = pyperclip.paste()


    # Output the copied text to verify
    print(chat_history)
    
    print(last_message_from_sender(chat_history))

    if last_message_from_sender(chat_history):
      completion = client.chat.completions.create(
      model="llama3-8b-8192",
      messages=[
        {
        "role": "system",
        "content": """
                    You are an AI autoreply bot representing a person
                    You speak Hindi as well as English and you are from India. You communicate using few words,
                    but each response carries profound meaning and thought.  You are a coder and solve any piece of code. Your replies should be intelligent,
                    empathetic, and wise and some sarcasm, reflecting a deep understanding of the ongoing conversation.Analyze
                    the chat history provided and respond in a manner that is both insightful and considerate.
                    output should be more human like response,Output should be next chat response (text message only).""" 
        },

        {"role": "system",
         "content":  "Do not start like this [2:14 PM, 7/28/2024] Mom: "
        }, 

        {
        "role": "user",
        "content": chat_history 
        }
        ],
      )

      response = completion.choices[0].message.content
      pyperclip.copy(response)

        # Click at coordinates (1160, 1564)
      pyautogui.click(1160, 1564)
      time.sleep(1)  # Adjust the sleep time if necessary

        # Paste the text
      pyautogui.hotkey('ctrl', 'v')
      time.sleep(1)  # Adjust the sleep time if necessary

        # Press Enter
      pyautogui.press('enter')




