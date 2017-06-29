import wave

wavfile = wave.open("ksample2.wav")
framerate = wavfile.getframerate()
nframes = wavfile.getnframes()

oneminute = framerate*60
sliceSize = oneminute
slicedSoFar = 0

# print out file properties
print "framerate: "+str(framerate)
print "channels: "+str(nframes)
print "n of frames: "+str(wavfile.getnframes())
print "length: "+str(float(wavfile.getnframes())/float(wavfile.getframerate()))+" seconds"
print "a minute is: "+str(oneminute)+" frames"


frames = []

def writeFile(fname):
    newWavFile = wave.open(fname, "w")

    nchannels = 1
    sampwidth = 2
    comptype = "NONE"
    compname = "not compressed"

    newWavFile.setparams((nchannels, sampwidth, framerate, sliceSize,
        comptype, compname))

    for s in frames:
        # write the audio frames to file
        newWavFile.writeframes(s)

    newWavFile.close()

def sliceMeDaddy():
    while(nframes-slicedSoFar<oneminute):
        slicedSoFar+=1
        frames.append(wavfile.readframes(i+slicedSoFar))
# if we're slicing less than we need
if(nframes-slicedSoFar<oneminute):
    sliceSize = nframes

for i in range(nframes):
    slicedSoFar+=1
    frames.append(wavfile.readframes(i))

writeFile("newfile")
