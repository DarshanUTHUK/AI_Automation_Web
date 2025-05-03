from fastapi import FastAPI


class ApiInstance:
    def __init__(self):
        self._api  = FastAPI()

    def app(self):
        return self._api