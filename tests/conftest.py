import os
import pytest
from browser_use import Controller, Agent
from langchain_google_genai import ChatGoogleGenerativeAI
from pydantic import SecretStr
from utils.Posts import Posts
from utils.results_history import Results

@pytest.fixture(scope='function')
@pytest.mark.asyncio  # Ensure that the fixture itself works in an async context
async def setup(request):
    os.environ['GEMINI_API_KEY'] = "add gemini api key"
    api_key = os.environ['GEMINI_API_KEY']
    llm = ChatGoogleGenerativeAI(model='gemini-2.0-flash-exp', api_key=SecretStr(api_key))

    controller = Controller(output_model=Posts)

    results = Results()

    task = ('Open Chrome browser along with website url "https://parabank.parasoft.com/parabank/index.htm"'
            'Wait for the next steps prompt')

    # Your agent initialization
    agent = Agent(llm=llm, task=task, use_vision=True, controller = controller)
    yield agent, controller, results
    results.result_history()
    await agent.close()

