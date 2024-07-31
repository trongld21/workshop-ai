from openai import OpenAI

client = OpenAI(
    api_key='your-api-key'
)

user_input = input("Hãy nhập câu văn tiếng Anh của bạn để chấm điểm: ")

completion = client.chat.completions.create(
  model="gpt-3.5-turbo",
  temperature=0.7,
  messages=[
    {"role": "system", "content": "Bạn là giám khảo chấm điểm ngữ pháp tiếng Anh. Tôi sẽ cung cấp cho bạn một câu văn hãy chấm điểm trên thang điểm 9, đưa ra nhận xét và góp ý để tôi cải thiện ngữ pháp của mình."},
    {"role": "user", "content": user_input}
  ]
)

print(completion.choices[0].message.content)


