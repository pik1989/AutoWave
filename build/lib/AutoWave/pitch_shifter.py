from pydub import AudioSegment
def pitchShifter(audioname,shift,value):
    '''
    this functions takes the wav file and returns the pitch shifted file, i.e, increase and decrease the volume of the audio file
    audioname:- name of the audio file/path to the audio file
    shift:- 'i' for increasing the volume/ 'd' for decreasing the volume
    value:- unit by which increase and decrease the volume
    '''
    formats_to_convert = ['.wav']  
    if audioname.endswith(tuple(formats_to_convert)):
    
        audio=AudioSegment.from_wav(audioname)
        if shift=='i':

            # Increase the volume  
            return(audio + value)
        elif shift=='d':
            # Reducing volume 
            return(audio - value)
        else:
            print("Error in shifting the pitch")
    else:
        print('Please use .wav file')
