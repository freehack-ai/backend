job_description = input(
    "This agent can do logo design from project description on a website. Do you have any particular condition for the choice of the project? Can be a keyword, a price range, a deadline, etc. "
)

# query the mongodb db using the user's answer

name_of_task = "design project"

# call the agent to perform the task

# save the result and print it

result = "img"

print(f"The agent has completed the task {name_of_task}. Here is the result: {result}")
