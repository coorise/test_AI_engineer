from agents import Agent, Runner, OpenAIChatCompletionsModel, AsyncOpenAI

# Configure the model
model = OpenAIChatCompletionsModel( 
    model="auto",
    openai_client=AsyncOpenAI(base_url="http://localhost:8000/v1"),
    api_key="1234"
)

# Create the agent
agent = Agent(
    name="Assistant",
    instructions="You are a helpful assistant",
    model=model
)

# Run the agent synchronously
result = Runner.run_sync(agent, "Create a meal plan for a week.")
print(result.final_output)