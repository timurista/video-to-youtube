from moviepy.editor import *

ic_1 = ImageClip('./test_images/paw-patrol-2.jpeg').set_duration(2)
ic_2 = ImageClip('./test_images/paw-patrol-3.jpg').set_duration(1)

video = concatenate([ic_1, ic_2], method="compose")
audioclip = AudioFileClip("song.mp3")
video.set_audio(audioclip)
video.write_videofile('test.mp4', fps=24)
