from audioGetters.IAudioGetter import IAudioGetter


class FakeAudioGetter(IAudioGetter):
    def __init__(self):
        return

    # returns filepath to audio file
    def getAudio(self) -> str:
        audioPath = "../audio/audio.mp3"
        return audioPath
