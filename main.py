from config.model_config import response_agent

response = response_agent.run_sync("What is the currency value of Taka?")
print(response.output)