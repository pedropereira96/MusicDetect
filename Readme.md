# Lab Work 3

Projeto desenvolvido para a unidade curricular Teoria Algoritmica da Informação.

O objetivo principal deste trabalho, consistem em desenvolver e testar a congiguração do NCD para identificação automática das músicas, utilizando pequenos excertos de músicas


# Instalar os requisitos
```
pip install -r requirements.txt
```

# Executar geração de ruído em músicas
```python
python3 code/add_noise.py database/<musica> <nível_de_ruido>

python3 code/add_noise.py database/AC_DC-Thunderstruck.wav 10
```


# Executar deteção de música
Pode-se utilizar um dos seguintes 4 compressores "gzip", "bzip2", "lzma", ou "lz4"
```python
python3 code/main.py segments/<musica> <nível_de_ruido>

# Compressor gzip para Coldplay - Fix You
python3 code/main.py segements/Coldplay-Fix_You.wav gzip

# Compressor bzip2 para AC DC - TNT com ruído gerado de nível 10
python3 code/main.py ssegments/noised/AC_DC-TNT.noise.10.0.wav bzip2

```