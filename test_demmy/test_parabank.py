import pytest

from recording_hook.client import record_activity
from utils.fakeuser_details import generate_random_user_for_registration


class Test_Para_Bank:

    @pytest.mark.usefixtures("setup")
    @pytest.mark.asyncio
    async def test_register(self,setup):
        agent, commontask, results = setup
        username = generate_random_user_for_registration()
        task = ("Click on register button"
                f"Register with Fake Details with different username {username}"
                "Click on Logout"
                "Use the same register details for login"
                "after Register Click on find transaction")

        agent.add_new_task(new_task=task)
        history = await agent.run()
        results.set_results_history(history)

# on_step_start=record_activity