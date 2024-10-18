from imageGenerators.IImageGenerator import IImageGetter
import os


class FakeImageGenerator(IImageGetter):
    def __init__(self):
        return

    # returns filepaths to images that were downloaded
    def getImages(self, numImages: int, prompt: str) -> list[str]:
        imagePaths = []
        for i in range(numImages):
            imagePaths.append(f"../images/image{i+1:003}.jpg")

        return imagePaths
