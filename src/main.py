from promptInteractor.fakePromptCreator import FakePromptCreator
from videoCreator.videoCreator import VideoCreator, VideoConfig
from audioGetters.fakeAudioGetter import FakeAudioGetter
from imageGenerators.fakeImageGenerator import FakeImageGenerator
from videoUploaders.fakeVideoUploader import FakeVideoUploader


def main():
    imageGenerator = FakeImageGenerator()
    audioGetter = FakeAudioGetter()
    videoUploader = FakeVideoUploader()
    promptCreator = FakePromptCreator()

    prompt = promptCreator.getPromptForImageCreations("channel description")
    imagePaths = imageGenerator.getImages(4, prompt)
    audioPath = audioGetter.getAudio()

    outputPath = "../outputs/SZDFC.mp4"

    config = VideoConfig(imagePaths, audioPath, outputPath, transitionLength=3)
    creator = VideoCreator(config)

    creator.createMp4()

    videoUploadSuccessful = videoUploader.uploadVideo(outputPath)


if __name__ == "__main__":
    main()
