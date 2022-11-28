import glob

from pyfiglet import Figlet
import ffmpeg

print(Figlet(font="slant").renderText("Audio Converter"))
print("""
1: file to wav 2: file to mp3
""", end="\n")


def choice():
    choice = input("Enter Number>> ")
    return int(choice)
def main():
    select_num = choice()
    input_audio_list = glob.glob("./file/" + "*")
    if select_num == 1:
       for input_audio in input_audio_list:
         in_audio = ffmpeg.input(input_audio)
         in_audio = ffmpeg.output(in_audio, "{}-output.wav".format(input_audio))
         ffmpeg.run(in_audio)
    elif select_num == 2:
        for input_audio in input_audio_list:
            in_audio = ffmpeg.input(input_audio)
            in_audio = ffmpeg.output(in_audio, "{}-output.mp3".format(input_audio))
            ffmpeg.run(in_audio)
if __name__ == '__main__':
   
       main()