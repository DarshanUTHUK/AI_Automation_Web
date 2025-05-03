import os
import pathlib
from typing import Optional

from utils.Posts import Posts

class Results:

    def __init__(self):
        self.history = None

    def set_results_history(self, history : Optional):
        self.history = history
        return history

    def result_history(self):
        poject_path = pathlib.Path(__file__).parent.parent
        result_path = os.path.join(poject_path,"results/agentresults.json")
        self.history.save_to_file(result_path)
        result = self.history.final_result()
        if result:
            parsed: Posts = Posts.model_validate_json(result)

            for post in parsed.posts:
                print(f"{post}")