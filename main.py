from config.model_config import response_agent

response = response_agent.run_sync("give me the summary of the linux log file")
print(response.output)