from config.model_config import response_agent

response = response_agent.run_sync("can u check my gmail if there's any important email.")
print(response.output)