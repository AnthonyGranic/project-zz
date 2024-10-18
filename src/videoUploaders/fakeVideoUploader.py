from videoUploaders.IVideoUploader import IVideoUploader


class FakeVideoUploader(IVideoUploader):
    def __init__(self):
        return

    def uploadVideo(self, videoFilePath=str) -> bool:
        return True
