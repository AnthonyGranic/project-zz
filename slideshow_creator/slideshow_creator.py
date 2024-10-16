import os
import subprocess
import shlex


class videoConfig:

    def __init__(
        self,
        imagePaths: list[str],
        audioPath: str,
        outputPath: str,
        transitionLength=1,
        addZooms=True,
        addTransitions=True,
        frameLength=5,
        frameRate=30,
    ):
        self.imagePaths = imagePaths
        self.audioPath = audioPath
        self.outputPath = outputPath
        self.frameLength = frameLength
        self.frameRate = frameRate
        self.addZooms = addZooms
        self.addTransitions = addTransitions
        self.transitionLength = transitionLength


class videoCreator:

    def __init__(self, videoConfig: videoConfig, outputLogFiles=False):
        self.videoConfig = videoConfig
        self.outputLogFiles = outputLogFiles

    def createMp4(self):
        # create command
        command = self.__createCommand()
        print(command)
        self.__runCommand(command)
        return

    def __createCommand(self, printWarnings=False):
        cfg = self.videoConfig
        command = ["ffmpeg"]

        if not printWarnings:
            command.extend(["-loglevel", "error"])

        for imagePath in cfg.imagePaths:
            loopStr = f"-loop 1 -t {cfg.frameLength} -framerate {cfg.frameRate} -i {imagePath}"
            command.extend(shlex.split(loopStr))

        command.extend(shlex.split(f"-i {cfg.audioPath}"))
        filterComplex = self.__addFilterComplex()
        if filterComplex:
            command.extend(shlex.split(filterComplex))

        command.extend(
            shlex.split(
                f"-t {len(cfg.imagePaths) * cfg.frameLength - cfg.transitionLength}"
            )
        )

        command.extend(shlex.split("-c:v libx264 -pix_fmt yuv420p"))

        command.extend(shlex.split(cfg.outputPath))

        return command

    # little bit fucked up
    def __addFilterComplex(self):
        cfg = self.videoConfig
        addZooms = cfg.addZooms
        addTransitions = cfg.addTransitions
        if not addZooms and not addTransitions:
            return None

        filterComplex = '-filter_complex "'
        if addZooms:
            for i in range(len(cfg.imagePaths)):
                duration = cfg.frameRate * (cfg.frameLength + cfg.transitionLength)
                zoom = f"[{i}]scale=8000:-1,zoompan=z='zoom+0.001':x=iw/2-(iw/zoom/2):y=ih/2-(ih/zoom/2):d={duration}:s=576x1024:fps={cfg.frameRate}[s{i}]; "
                filterComplex += zoom

        if addTransitions:
            firstTransition = f"[s{0}][s{1}]xfade=transition=circleopen:duration={cfg.transitionLength}:offset={cfg.frameLength - cfg.transitionLength}[f0]; "
            filterComplex += firstTransition

            for i in range(1, len(cfg.imagePaths) - 1):
                offset = (cfg.frameLength) * (i + 1) - cfg.transitionLength
                if i != len(cfg.imagePaths) - 2:
                    transition = f"[f{i-1}][s{i+1}]xfade=transition=circleopen:duration={cfg.transitionLength}:offset={offset}[f{i}]; "
                else:
                    transition = f"[f{i-1}][s{i+1}]xfade=transition=circleopen:duration={cfg.transitionLength}:offset={offset}; "
                filterComplex += transition

        filterComplex += '"'
        return filterComplex

    def __runCommand(self, command: list[str]):
        # runs the command, shlex.split ensures we can run in linux
        subprocess.run(command)


def main():
    imagePaths = [
        "./images/image001.jpg",
        "./images/image002.jpg",
        "./images/image003.jpg",
        "./images/image004.jpg",
    ]
    config = videoConfig(
        imagePaths, "./images/audio.mp3", "plswork.mp4", transitionLength=3
    )

    creator = videoCreator(config)
    creator.createMp4()


if __name__ == "__main__":
    main()
