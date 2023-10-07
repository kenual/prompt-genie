import g4f

# enter goal
goal = input("Please enter your goal: ")
prompt = f"\
         I need a best optimized prompt to get ChatGPT to achieve the following user goal\n\
         \n\
             {goal}\n\
         \n\
         Your prompt will be sent to ChatGPT.\n\
         The prompt needs to be in bulleted format instructing ChatGPT\n\
         - optimized persona to take on to achieve the above goal\n\
         - the context that customized prompt is based on\n\
         - the desired outcome of the prompt\n\
         - the tone and style of the answer\n\
         - provide a number of options when answering\n\
         - best response output style to explain to the user\n\
         Start and end the prompt with ```\n\
        "

# confirm user goal
print(f"\n\nYour goal is:\n{'='*len(goal)}\n{goal}\n{'='*len(goal)}\n\n")

# streamed completion
response = g4f.ChatCompletion.create(
    model=g4f.models.gpt_4,
    messages=[
        {"role": "system", "content": "Take the persona of a ChatGPT prompt engineer"},
        {"role": "user", "content": prompt},
    ],
    provider=g4f.Provider.Bing,
    stream=True,
    temperature=0.2
)

for message in response:
    print(message, flush=True, end='')
print(end='\n')


