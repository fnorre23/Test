
# Deleting what was previously in the file

# Reading the files
file = open('DearDiary.txt', 'r+') # ORV - r+ indikerer vi både må læse og skrive i filen, i stedet for kun 1 ad gangen
print('1')

# absolute file positioning 
file.seek(0) # 0 specifiserer hvilken byte der skal kigges på. Så 10 f.eks. ville være 10th byte
print('2')

# Den her linje slette dataen 
file.truncate() 
# Den virker ved at bestemme størrelsen af filen. f.eks. 20 som input argument
# så ville den truncate filen til 20 bytes. Til 0, så sletter du al indholdet,
# da det jo så sætter filen til at fylde 0 bytes.

print('3')

# Lukker filen
file.close()
print('4')

# NÅR MAN ÅBNER I 'w' MODE OVERSKRIVER MAN FAKTISK HVAD DER VAR FØR, SÅ DET HER
# ER SLET IKKE NØDVENDIGT.

################################################################

# Creating txt file
file = open('DearDiary.txt', 'w')
print('5')

# Writing to txt file
file.write('Dear Diary') # \n skal placeres der hvor der skal opstå linje skift, så enten bag linjen der skal skiftes fra, eller før linjen der skal skiftes til
file.write('\nToday i learned to make this file and write in it.')

print('6')