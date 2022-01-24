import sys

class NCD:

    def __init__(self, compressor:str):

        #Choose the compress engine to import and use
        if compressor == "gzip": 
            from gzip import compress
        elif compressor == "bzip2": 
            from bz2 import compress
        elif compressor == "lzma": 
            from lzma import compress 
        elif compressor == "lz4":
            from lz4.frame import compress 

        self.compress = compress
    
    def calc_NCD(self, segment, complete_music):
        """Return the NCD value """
        music_unknown = self.compress(segment)  
        music_known = self.compress(complete_music)  
        booth = self.compress(segment + complete_music)
        return (len(booth) - min(len(music_unknown), len(music_known))) / max(len(music_unknown), len(music_known))