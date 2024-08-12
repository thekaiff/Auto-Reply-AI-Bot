import os
from groq import Groq

# gets API Key from environment variable OPENAI_API_KEY

client = Groq(
    api_key= os.environ.get("BOT_API_KEY")
)


command = """

paste some of your chat history here for auto reply chat bot to analyze

"""


completion = client.chat.completions.create(

  model="llama3-8b-8192",
  messages=[   
    {
      "role": "system",
      "content": """You are a person named Kaif Sayed who speaks hindi as well as english. You are very friendly, kind and sarcastic. You are from India. You are a very isolated person, who understand people and speaks very well.
                    You analyze chat histort and respond like Kaif Sayed.""",
    },
    {      
      "role": "user",
      "content": command
    }
          ])


print(completion.choices[0].message.content)