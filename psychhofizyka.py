import time as t
import msvcrt
import sys, os
import playsound
import datetime
from mutagen.mp3 import MP3
from msvcrt import getch



def count_down(duration):
	for i in range(duration,0,-1):
		print(str(i)+' ', end="\r")
		sys.stdout.flush()
		t.sleep(1)

#urrentDT = datetime.datetime.now()
#outputFile  = "wyniki_"+str(currentDT.hour)+"_"+str(currentDT.minute)+".txt"
#print(outputFile)
outputFile="wyniki.txt"
OutputFile=open(outputFile,'w')



if os.path.isdir(".\\beats"):
    arr =os.listdir(".\\beats")
else:
	print("Folder 'beats' musi byc w tej samej lokalizacji co plik .exe")
	exit()

n=len(arr)-1
print("\nBadanie sklada sie z 2 czesci po", n,"zadan. \nW kazdym zadaniu uslyszysz 8 udezen w pewnym tempie. \nTwoim zadaniem jest powtorzenie 8 uderzen w takim samym tempie. Do wystukania rytmu uzyj SPACJI\nPo uslyszeniu 8 uderzen zostanie wyswietlone slowo 'start', nie sugeruj sie nim, informuje ono tylko, ze nagranie sie skonczylo i teraz Twoja kolej. \nMiedzy czesciami zrob min. 5min przerwy. \nPrzed rozpoczeciem uslyszysz dzwiek probny")
input("\nAby przejsc do dzwieku probnego wcisnij Enter")

#dzwiek probny
flag = False;
print("\n\nTo jest dzwiek probny, ustaw odpowienia glosnosc w swoim komputerze.\nAby przejsc do czesci wlasciwej wcisnij SPACJA")
while((True)):


	audioFile = MP3("beats\\00.mp3")
	audio_info = audioFile.info
	playsound.playsound("beats\\00.mp3", True)
	length_in_secs = int(audio_info.length)

	t.sleep(length_in_secs)

	if msvcrt.kbhit():
		if (msvcrt.getwche()==chr(32)):
			#print ("OK")
			break


#badanie wlasciwe - wszytkie dzwieki powtorzone dwokrotnie z 5min przerwa
del arr[0]

a=' '


print("\nUslyszysz 8 uderzen w pewnym tempie. \nNastepnie urzywajac SPACJI wystukaj kolejne 8 uderzen w tym samym tempie.")
input("\nKliknij Enter aby zaczac...")


for it in range(0,2):
	OutputFile=open(outputFile,'a')
	OutputFile.write("proba "+str(it+1)+"\n")
	print("Czesc ",(it+1))
	if(it>0):
		print("Uslyszysz ponownie",n,"przykladow po 8 uderzen metronomu w kazdym. \nNastepnie urzywajac SPACJI wystukaj kolejne 8 uderzen w tym samym tempie.")
		input("\nKliknij Enter aby zaczac...")
	i=0;
	for beat in arr:
		filename="beats\\"+beat

		#wylicza czas miedzy uderzeniami
		audioFile = MP3(filename)
		audio_info = audioFile.info
		length_in_secs = int(audio_info.length)
		rate=length_in_secs/8
		#print(rate)
		OutputFile.write(filename+"\n")
		i+=1
		count = 0
		if(i==0): input("Kliknij Enter aby zaczac...")
		print("Przyklad"+str(i))
		time = 0
		playsound.playsound(filename, False)
		#play_obj.wait_done()
		# script exit
		ch = 0

		#numerowanie uderzen z nagrania
		while(time<length_in_secs):
			ch+=1
			print(ch, end="\r")
			t.sleep(rate)
			time+=rate

		print("start", flush=True)
		start = t.time()


		#mierzenie czasu minedzy spacjami
		while((count < 8 )):#and(a.isspace()) == True):


			a=getch()
			if(a.isspace()):
				end = t.time()

				count +=1

				print(count)
				#print((count%4),end=" ")if (count%4!=0) else print("4",end=" ")#print(count%4, (end - start))if (count%4!=0) else print("4",(end - start))
				if(count!=1): OutputFile.write(str((end - start))+"\n")
				start = t.time()

			#else:print("to nie spacja", flush=False)









		input("Kilknij Enter, aby kontynuowac...\n")
	OutputFile.close()
	if(it==0):
		print("\nKoniec czesci ",(it+1), "\nPrzed przejsciem do kolejnej zrob min. 5 min przerwy:")
		count_down(300)
		input("Kilknij Enter, aby kontynuowac...\n")

print("Dziekuje, badanie zakonczone. Wyniki zapisane w pliku:", outputFile)
print("Plik", outputFile,"przeslij mailem na mz.fajerabend@gmail.com, przez Messenger lub Teams")
t.sleep(2)
input("\nAby wyjsc wcisnij ENTER")
