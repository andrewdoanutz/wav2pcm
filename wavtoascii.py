import wave
import struct

def pcm_channels(wave_file):
    stream = wave.open(wave_file,"rb")

    num_channels = stream.getnchannels()
    sample_rate = stream.getframerate()
    sample_width = stream.getsampwidth()
    num_frames = stream.getnframes()
    print(num_channels)
    print(sample_rate)
    print(sample_width)
    raw_data = stream.readframes( num_frames )
    stream.close()

    total_samples = num_frames * num_channels

    if sample_width == 1:
        fmt = "%iB" % total_samples
    elif sample_width == 2:
        fmt = "%ih" % total_samples
    else:
        raise ValueError("Only supports 8 and 16 bit audio formats.")

    integer_data = struct.unpack(fmt, raw_data)
    del raw_data

    #channels = [ [] for time in range(num_channels) ]
    channels=[]
    for index, value in enumerate(integer_data):
        #bucket = index % num_channels
        #channels[bucket].append(value)
        channels.append(value)
    return channels



header=[82,73,70,70,202,119,0,0,87,65,86,69,102,109,116,32,
18,0,0,0,1,0,1,0,64,31,0,0,64,31,0,0,
1,0,8,0,0,0,100,97,116,97,164,119]
'''
with open("result.txt","w") as f:
    for num in temp:
        f.write("%s\n" % num)


    my_list=pcm_channels('8kmono.wav')
    for item in my_list:
        f.write("%s\n" % item)
'''
filename="igotanidea8k16"
my_list=pcm_channels(filename+'.wav')

with open(filename+".txt","w") as f:
    f.write(str(header+my_list))