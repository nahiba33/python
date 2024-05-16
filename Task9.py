with open("File.txt", encoding="utf-8", mode="w" ) as text: #taskın 1.tələbi
  setrler = ['Şavaş barışdır', '\nAzadlıq köləlikdir', "\nCahillik gücdür"]
  text.writelines(setrler)
with open("File.txt", encoding="utf-8", mode="r") as text: # taskın 2.tələbi
  ilk_setr = text.readline().upper()
with open("F_File.txt", encoding="utf-8", mode="w") as text: #taskın 3.tələbi
  text.write(ilk_setr)
