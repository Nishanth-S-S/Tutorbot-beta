 import openai


 openai.api_key = "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"


 messages = []
system_msg = "You are a ai conversational tutor using python, You cover all subjects in highschool, You should help 9th grade students who are just starting or 10th grade students who have experience.You will help the get into the top colleges. "
messages.append({"role": "system", "content": system_msg})

print("Hello, I'm Cogni 👋, an AI tutor designed to assist high school students in gaining admission to top colleges.")
print(" ")
print("What subject would you like help in?")
while input != "quit":
   message = input()
   messages.append({"role": "user", #"content": message})
   response = openai.ChatCompletion.create(
       model="gpt-3.5-turbo",
       messages=messages)
   reply = response["choices"][0]["message"]["content"]
   messages.append({"role": "assistant", "content": reply})
   print("\n" + reply + "\n")
