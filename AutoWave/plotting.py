import pandas as pd
from datetime import datetime
from os import scandir
import os
import matplotlib.pyplot as plt
from scipy.io import wavfile as wav
from scipy.fftpack import fft
import numpy as np

class plotOneFile():
    
    def time_freq_domain(filename):  
        rate, data = wav.read(filename)
        fft_out = fft(data)
        duration = len(data)/rate
        time = np.arange(0,duration,1/rate) #time vector
        fig, axes = plt.subplots(nrows=1, ncols=2, figsize=(10, 5))
        axes[0].plot(data, np.abs(fft_out))
        axes[1].plot(time,data)
        axes[0].set_xlabel('Frequency Domain')
        axes[1].set_xlabel('Time Domain')
        fig.suptitle('Frequency and Time Domain'+' '+filename)
        fig.tight_layout()
        
    def freq_domain(filename):
        rate, data = wav.read(filename)
        fft_out = fft(data)
        plt.figure(figsize=(10, 5))
        plt.plot(data, np.abs(fft_out))
        plt.title('Frequency Domain'+' '+filename)
    
    def time_domain(filename):
        rate, data = wav.read(filename)
        duration = len(data)/rate
        time = np.arange(0,duration,1/rate)
        plt.figure(figsize=(10, 5))
        plt.plot(time,data)
        plt.title('Time Domain'+' '+filename)

    
class plotMultipleFile():
    
    def time_freq_domain(path,number_of_plots):
        for dirpath, dirnames, files in os.walk(path):
            for i in range(number_of_plots):
                rate, data = wav.read(dirpath + "//"+ files[i])
                fft_out = fft(data)
                duration = len(data)/rate
                time = np.arange(0,duration,1/rate) #time vector
                fig, axes = plt.subplots(nrows=1, ncols=2, figsize=(10, 5))
                axes[0].plot(data, np.abs(fft_out))
                axes[1].plot(time,data)
                axes[0].set_xlabel('Frequency Domain')
                axes[1].set_xlabel('Time Domain')
                fig.suptitle('Frequency and Time Domain'+' '+files[i])
                fig.tight_layout()
    
    
    def time_domain(path,number_of_plots):
        for dirpath, dirnames, files in os.walk(path):
            for i in range(number_of_plots):
                rate, data = wav.read(dirpath + "//"+ files[i])
                duration = len(data)/rate
                time = np.arange(0,duration,1/rate)
                plt.figure(figsize=(10, 5))
                plt.plot(time,data)
                plt.title('Time Domain'+' '+files[i])
                
    def freq_domain(path,number_of_plots):
        for dirpath, dirnames, files in os.walk(path):
            for i in range(number_of_plots):
                rate, data = wav.read(dirpath + "//"+ files[i])
                fft_out = fft(data)
                plt.figure(figsize=(10, 5))
                plt.plot(data, np.abs(fft_out))
                plt.title('Frequency Domain'+' '+files[i])
