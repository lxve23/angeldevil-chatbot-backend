from openai import OpenAI
import os

client = OpenAI(
  api_key=os.getenv('API_KEY')
)


def newMessage(userPrompt):
  completion = client.chat.completions.create(
    model="gpt-4o-mini",
    store=True,
    messages=
    [
      {
        "role": "system",
        "content": "You will respond as an angel and the devil on one's shoulder. The angel will always speak first and talk positively, offering guidance that aligns with ethics, values, or betterment. The devil will then speak afterwards, twisting the angel's words and introducing negative, manipulative, or harmful perspectives. Have '---SPLIT---' between the angel's and demon's message. Do NOT have any identifiers in the message for who is speaking."
      },
      {
        "role": "user",
        "content": userPrompt
      }
    ]
  )

  return completion.choices[0].message.content