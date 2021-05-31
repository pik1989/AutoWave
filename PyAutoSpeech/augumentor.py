import random
import soundfile as sf
import librosa
import numpy as np
import glob, os

def augumentOneFile(audioname,output_path,aug_times=10,noise=True,shift=True,stretch=True,pitch=True):
    print("Converting"+" "+audioname)
    formats_to_convert = ['.wav']  
    if audioname.endswith(tuple(formats_to_convert)):
        data,sr = librosa.core.load(audioname)
        for i in range(1,aug_times+1):
            #noise
            if noise==True and random.randint(0,5)>=3:
                wn = np.random.randn(len(data))
                data = data + 0.005*wn

            # Shifting the sound
            if shift==True and random.randint(0,5)>=3:
                data = np.roll(data, random.randint(100,200))

            #stretch
            if stretch==True and random.randint(0,5)>=3:
                data =librosa.effects.time_stretch(data, 1.2)

            #pitch
            if pitch==True and random.randint(0,5)>=3:
                data = librosa.effects.pitch_shift(data, sr, n_steps=random.randint(1,10),bins_per_octave=random.randint(10,200))

           

            sf.write(os.path.join(output_path,('{}'+audioname).format(i)), data, sr)
        print("Augmentation Completed")
    
    
    
    else:
        print('Please use .wav file')


    
def augumentFolderRate(input_path,output_path,aug_times=10,noise=True,shift=True,stretch=True,pitch=True):
    os.chdir( input_path)
    for file in glob.glob("*.wav"):
        print(file)
        augumentOneFile(file,output_path,aug_times,noise,shift,stretch,pitch)
    print("Augmentation Completed")
        
    
def augumentFolderItem(input_path,output_path,augumented_data=1000,noise=True,shift=True,stretch=True,pitch=True):
    os.chdir( input_path)
    aug_times=(augumented_data//len(glob.glob("*.wav")))+1
    for file in glob.glob("*.wav"):
        print(file)
        augumentOneFile(file,output_path,aug_times,noise,shift,stretch,pitch)
    print("Augmentation Completed")
    