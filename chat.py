from langchain.chat_models import ChatOpenAI
from langchain.agents import create_json_agent
from langchain.agents.agent_toolkits import JsonToolkit
from langchain.tools.json.tool import JsonSpec
import json

file = "details.json"
with open(file, "r") as f1:
    data = json.load(f1)

OPENAI_API_KEY = "api_key"

spec = JsonSpec(dict_=data, max_value_length=4000)
toolkit = JsonToolkit(spec=spec)

agent = create_json_agent(llm=ChatOpenAI(openai_api_key=OPENAI_API_KEY, temperature=0, model="gpt-3.5-turbo"), toolkit=toolkit, max_iterations=1000, verbose=True)

while True:
    user_input = input("Enter question (type 'exit' to quit): ")
    
    if user_input.lower() == 'exit':
        break

    response = agent.run(user_input)
    print("Response:", response)
