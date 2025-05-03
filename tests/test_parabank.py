import pytest

# Mark the class or method as async
class Test_Para_Bank:

    @pytest.mark.usefixtures("setup")
    @pytest.mark.asyncio
    async def test_register(self,setup):
        agent, controller, results = setup

        task = ("Click on register button"
                "Register with Fake Details"
                "Click on Logout"
                "Use the same register details for login")

        agent.add_new_task(new_task=task)
        history = await agent.run()
        results.set_results_history(history)
