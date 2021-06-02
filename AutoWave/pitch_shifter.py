from pydub import AudioSegment
def pitchShifter(audioname,shift,value):
    formats_to_convert = ['.wav']  
    if audioname.endswith(tuple(formats_to_convert)):
    
        audio=AudioSegment.from_wav(audioname)
        if shift=='i':

            # Increase the volume by 10 dB 
            return(audio + value)
        elif shift=='d':
            # Reducing volume by 5
            return(audio - value)
        else:
            print("Error in shifting the pitch")
    else:
        print('Please use .wav file')
