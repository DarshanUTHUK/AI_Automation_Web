import os
from browser_use import Agent
from langchain_google_genai import ChatGoogleGenerativeAI
from pydantic import SecretStr
from tasks.common_task import CommonTask
from utils.results_history import Results
import pytest


@pytest.fixture(scope='function')
@pytest.mark.asyncio  # Ensure that the fixture itself works in an async context
async def setup(request):
    os.environ['GEMINI_API_KEY'] = "Add gemini api key"
    api_key = os.environ['GEMINI_API_KEY']
    llm = ChatGoogleGenerativeAI(model='gemini-2.0-flash-exp', api_key=SecretStr(api_key))
    results = Results()
    commontask = CommonTask()
    controller = commontask.controller
    task = commontask.task
    # Your agent initialization
    agent = Agent(llm=llm, task=task, use_vision=True, controller = controller )
    yield agent, commontask, results
    await agent.log_completion()
    results.result_history()
    await agent.close()
