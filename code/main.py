import sys
from os import listdir, fsdecode, system, path
import collections


from signature import Signatures
from NCD import NCD

def main(file, compressor):

    #CALCULAR FAZER GERAÇAO DA BASE DE DADOS
    results = {} 
    signatures = Signatures()
    ncd = NCD(compressor)

    # CREATE THE SIGNATURES:
    signatures.calc_database_signatures()
    segment_signature_path = signatures.calc_file_signature(file)
    segment_signature = read_file(segment_signature_path)

    for file in listdir("signatures/database"):
        if file not in [".DS_Store", ".DS"] :
            filename = fsdecode(file) 
            music_signature = read_file("signatures/database/" + filename)
            value = ncd.calc_NCD(segment_signature, music_signature) # Normalized Comprehension Distance between that music and the segment
            results[filename[:-6]] = value


    results = dict(sorted(results.items(), key=lambda item: item[1]))
    music_recognized = list(results.keys())[0]
    system("clear")
    print("\n\n")
    print("Music detected: {}".format(music_recognized))
    print("\n\n")


def read_file(file_path:str):
    # Reads the content of the signature file
    content = ""
    try:
        file = open(file_path, mode='rb')
    except OSError:
        print("Could not open/read file: ", file_path)
        sys.exit()
    content = file.read()    
    return content    


def usage():
    print("\nUsage: python3 bin/Recognizer.py segments/<file_name> <compressor> <noise>\n\nFile type: wav, flac or mp3\nCompressors: gzip, bzip2, lzma or lz4")
        

if __name__ == "__main__":  
    if len(sys.argv) < 3 or len(sys.argv) > 4: 
        usage()
        sys.exit()
    elif not path.exists(sys.argv[1]):
        print("The file does not exist!")
        sys.exit()
    elif sys.argv[2] not in ["gzip", "bzip2", "lzma", "lz4"]:
        print("Invalid type of compressor! Must be 'gzip', 'bzip2' or 'lzma' or 'lz4'")
        sys.exit()

    main(sys.argv[1], sys.argv[2])
