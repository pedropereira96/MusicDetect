import sys, sox
from os import path, system, listdir, fsdecode


class Signatures:

    def __init__(self):
        command = "g++ -W -Wall -std=c++11 -o code/GetMaxFreqs/src/GetMaxFreqs code/GetMaxFreqs/src/GetMaxFreqs.cpp -lsndfile -lfftw3 -lm"
        system(command)


    def convert_type(self, dir, filename):
        """Convert file to .wav"""

        path = dir + "/" + filename  #old file
        new_filename = filename[:-3] + "wav"  #new name file

        #Execution commands
        system("mpg123 -w " + dir + "/" + new_filename + " " + path ) #create converted file from old file
        system("rm " + path) # remove old file
        
        return new_filename


    def convert_sample_rate(self, dir, filename):
        """ Convert file to 44100 Hz """
        path = dir + "/" + filename
        if filename.endswith(".wav"): 
            new_filename = filename[:-4] + "-temp.wav"
        else: 
            new_filename = filename[:-5] + "-temp.flac"
        
        #Create new file with 44100 Hz
        system("sox " + path + " -r 44100 " + dir + "/" + new_filename )
        #Remove old file
        system("rm " + path)

        new_filename_replaced = new_filename.replace("-temp","")

        #Remove temp from file name
        system("mv " + dir + "/" + new_filename + " " + dir + "/" + new_filename_replaced)
        
        return new_filename_replaced


    def calc_database_signatures(self):
        """Create the frequencies files for all files in database folder. Will store on signatures/database"""
        dir = "database"
        for file in listdir(dir):
            filename = fsdecode(file)
            if filename not in [".DS_Store", ".DS"]: #Macbook create this files "Desktop Services"
                
                signature_exists = False
                if path.exists("signatures/database/" + filename[:-3] + "freqs"): 
                    signature_exists = True 

                #Only create .freqs is file not exist
                if not signature_exists:
                    signature_path = self.create_freqs_file(filename, dir)



    def calc_file_signature(self, file_path ):
        """ Create the frequency file for the target file """

        filename = file_path[9:]
        
        signature_path = self.create_freqs_file(filename, dir = "segments")
        
        return signature_path


    def create_freqs_file(self,filename, dir):
        """ Create frequencies file """
        #check type of file
        if not (filename.endswith(".wav") or filename.endswith(".flac")):
            filename = self.convert_type(dir, filename)

        #check sample rate
        if sox.file_info.sample_rate(dir + "/" + filename) != 44100:    
            filename = self.convert_sample_rate(dir, filename)

        signature_path = "signatures/" + dir + "/" + filename[:-3] + "freqs"

        system("code/GetMaxFreqs/src/GetMaxFreqs -w " + signature_path  + " " + dir + "/" + filename)

        return signature_path






