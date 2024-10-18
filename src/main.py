from videoCreator.videoCreator import VideoCreator, VideoConfig
from audioGetters.fakeAudioGetter import FakeAudioGetter
from imageGenerators.fakeImageGenerator import FakeImageGenerator


def main():
    imageGenerator = FakeImageGenerator()
    imagePaths = imageGenerator.getImages(4, "prompt")

    audioGetter = FakeAudioGetter()
    audioPath = audioGetter.getAudio()

    outputPath = "../outputs/SZDFC.mp4"

    config = VideoConfig(imagePaths, audioPath, outputPath, transitionLength=3)

    creator = VideoCreator(config)

    creator.createMp4()


if __name__ == "__main__":
    main()
