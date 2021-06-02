from pydub.playback import play
from pydub import AudioSegment
def AudioPlayer(audioname):
    audio=AudioSegment.from_wav(audioname)
    play(audio)