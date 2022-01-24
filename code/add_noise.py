import sys, sox
from os import path, system, listdir


def noise(file_path, noise):
    """Make some noise"""
    command = "sox " + file_path + " -p synth whitenoise vol " + str(noise) + " | sox -m " + file_path + " - segments/noised/" + file_path[9:-3]+"noise."+str(noise)+"."+file_path[-3:]
    r = system(command)
    return r, "segments/noised/" + file_path[9:-3]+"noise."+str(noise)+"."+file_path[-3:]



def convert_sample_rate(filename):
    """Convert Sample Rate to 44100 Hz"""
    path = filename
    if filename.endswith(".wav"): 
        new_filename = filename[:-4] + "-enc.wav"
    else: 
        new_filename = filename[:-5] + "-enc.flac"
    
    system("sox " + path + " -r 44100  " + new_filename )
    system("rm " + path)

    new_filename_replaced = new_filename.replace("-enc","")
    system("mv " + new_filename + " " + new_filename_replaced)
    
    return new_filename_replaced


def convert_type(filename):
    """Convert audio file to wav file"""
    new_filename = filename[:-3] + "wav"
    system("mpg123 -w "  + new_filename  + " " + filename )
    system("rm " + filename)
    return new_filename


def usage():
    print("\nUsage: python3 code/add_noise.py <file_name>  <noise>")


if __name__ == "__main__":  
    if len(sys.argv) != 3: 
        usage()
        sys.exit()
    elif not path.exists(sys.argv[1]):
        print("The file does not exist!")
        sys.exit()

    file = sys.argv[1]
    noiser = sys.argv[2]

    
    #Convert original file to wav
    if not (file.endswith(".wav") or file.endswith(".flac")):
        file = convert_type(file)
    
    #Check if file has 44100Hz
    if sox.file_info.sample_rate(file) != 44100:
        convert_sample_rate(file)

    #Create the noise file inside noised folder


    r , new_filename = noise(file, noiser)
    system("clear")
    print("\n\n")
    print("Noise added with success! \nPath: {}".format(new_filename) if r==0 else "Cannot create the file with noise!")
    print("\n\n")

