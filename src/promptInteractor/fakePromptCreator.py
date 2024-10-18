from promptInteractor.IPromptCreator import IPromptCreator


class FakePromptCreator(IPromptCreator):
    def __init__(self):
        return

    def getPromptForImageCreations(self, channelDescription: str) -> str:
        return channelDescription
