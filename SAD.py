import os

def menu():

    print(""" 
    ___       ___            ___       ___       ___        
   /\__\     /\  \          /\  \     /\  \     /\  \       
  /::L_L_   /::\  \        /::\  \   /::\  \   /::\  \      
 /:/L:\__\ /::\:\__\      /\:\:\__\ /::\:\__\ /:/\:\__\     
 \/_/:/  / \;:::/  /      \:\:\/__/ \/\::/  / \:\/:/  /     
   /:/  /   |:\/__/        \::/  /    /:/  /   \::/  /      
   \/__/     \|__|          \/__/     \/__/     \/__/       
-----------------------------------------------------
00. silahkan di pilih :'(                |
------------------------------------------
1. Install Nmap                          |
2. Install Hydra                         |
3. Install SQLMap                        |
4. Install Metasploit                    |
5. Install ngrok                         |
6. Install kali Nethunter                |
6. Install Kali Nethunter                |
7. Install angryFuzzer                   |
8. Install Red_Hawk                      |
9. Install Weeman                        |
10. Install IPGeoLocation                |
11. Install Ubuntu                       |
12. Install viSQL                        |
13. Install Hash-Buster                  |
14. Install routersploit                 |
------------------------------------------
00. Exit                                 |
------------------------------------------
""")


        print("--------------------------------")
        print("This will install: nmap, hydra, sqlmap, metasploit, ngrok, Kali Nethunter, angryFuzzer, red_hawk, weeman, IPGeoLocation, Hash-Buster, routersploit and viSQL with one click.")
        print("----------------")
        hm = input("[?] apakah kamu mau melanjutkan nya? (y/n): ")
        print("--------------------------------")
        if hm == "y":
		print("-----------------------------------------------------")
            print("[+] sabar gan :'(")
            print("waktunya lumayan lama :'(")
            print("-----------------------------------------------------")
            os.system("pkg update")
            os.system("pkg install -y git")
            os.system("pkg install -y python")
            os.system("pkg install -y python2")
            os.system("pkg install -y wget")
            os.sysetm("pkg install -y nmap")
            os.system("plg install -y hydra ")
            os.system("pkg update -y")
            os.system("pkg install -y git")
            os.system("pkg install python2")
            os.system("cd /data/data/com.termux/files/home && git clone https://github.com/sqlmapproject/sqlmap.git")
            os.system("cd /data/data/com.termux/files/home")
            os.system("pkg install wget")
            os.system("cd /data/data/com.termux/files/home && wget https://Auxilus.github.io/metasploit.sh")
            os.system("cd /data/data/com.termux/files/home && bash metasploit.sh")
            os.system("cd /data/data/com.termux/files/home && cd metasploit-framework")
            os.system("cd /data/data/com.termux/files/home && gem install bundle --pre")
            os.system("cd /data/data/com.termux/files/home && bundle config build.nokogiri --use-system-libraries")
            os.system("cd /data/data/com.termux/files/home && bundle install")
            os.system("cd /data/data/com.termux/files/home")
            os.system("pkg update -y")
            os.system("pkg install -y git")
            os.system("cd /data/data/com.termux/files/home && git clone https://github.com/themastersunil/ngrok.git")
            os.system("cd /data/data/com.termux/files/home")
            os.system("pkg update -y")
            os.system("pkg install -y git")
            os.system("pkg install -y python2")
            os.system("cd /data/data/com.termux/files/home && git clone https://github.com/ihebski/angryFuzzer.git")
            os.system("cd /data/data/com.termux/files/home && cd angryFuzzer")
            os.system("cd /data/data/com.termux/files/home && pip2 install -r requirements.txt")
            os.system("cd /data/data/com.termux/files/home && pip2 install requests")
            os.system("cd /data/data/com.termux/files/home")
            os.system("pkg update -y")
            os.system("pkg install -y git")
            os.system("pkg install -y php")
            os.system("cd /data/data/com.termux/files/home && git clone https://github.com/Tuhinshubhra/RED_HAWK")
            os.system("cd /data/data/com.termux/files/home")
            os.system("pkg update -y")
            os.system("pkg install -y python2")
            os.system("pkg install -y git")
            os.system("cd /data/data/com.termux/files/home && git clone https://github.com/evait-security/weeman.git")
            os.system("cd /data/data/com.termux/files/home && cd weeman")
            os.system("cd /data/data/com.termux/files/home && chmod +x weeman.py")
            os.system("cd /data/data/com.termux/files/home")
            os.system("pkg update -y")
            os.system("pkg install -y git")
            os.system("pkg install -y python")
            os.system("cd /data/data/com.termux/files/home && git clone https://github.com/maldevel/IPGeoLocation.git")
            os.system("cd /data/data/com.termux/files/home && cd IPGeoLocation")
            os.system("cd /data/data/com.termux/files/home && pip install -r requirements.txt")
            os.system("cd /data/data/com.termux/files/home")
            os.system("pkg update -y")
            os.system("pkg install -y git")
            os.system("pkg install -y python")
            os.system("cd /data/data/com.termux/files/home && git clone https://github.com/blackvkng/viSQL.git")
            os.system("pkg update -y")
            os.system("pkg install -y git")
            os.system("pkg install -y python2")
            os.system("cd /data/data/com.termux/files/home && git clone https://github.com/UltimateHackers/Hash-Buster.git")
            os.system("pkg update -y")
            os.system("pkg install -y git")
            os.system("pkg install -y python2")
            os.system("cd /data/data/com.termux/files/home && git clone https://github.com/reverse-shell/routersploit.git")
            os.system("cd /data/data/com.termux/files/home && cd routersploit")
            os.system("pip2 install -r requirements.txt")
            os.system("pip2 install -r requirements-dev.txt")
            os.system("pip2 install -r requests")
            os.system("clear")
            print("----------------------------------------")
            print("[+] selamat datang :'(")
            print("[+] silahkan di pilih")
            print("----------------------------------------")
        else:
            rmenu = input("[?] kembai ke menu? (y/n): ")
            if rmenu == "y":
                menu()
            else:
                break
				if what == "1":
        os.system("cd /data/data/com.termux/files/home")
        os.system("pkg update -y")
        os.system("pkg install -y nmap")
        os.system("cd /data/data/com.termux/files/home")
        print("------------------------------------")
        print("[+] nmap berhasil di install :'(")
        print("[+] ketik 'nmap' untuk menjalankan.")
        print("------------------------------------")
        rmenu = input("[?] kembali ke menu? (y/n): ")
        if rmenu == "y":
            menu()
        else:
            break
    elif what == "2":
        os.system("cd /data/data/com.termux/files/home")
        os.system("pkg update -y")
        os.system("pkg install -y hydra")
        os.system("cd /data/data/com.termux/files/home")
        print("------------------------------------")
        print("[+] hydra berhasil di install :'(")
        print("[+] ketik 'hydra' untuk menjalankan.")
        print("------------------------------------")
        rmenu = input("[?] kembai ke menu? (y/n): ")
        if rmenu == "y":
            menu()
        else:
            break
    elif what == "3":
        os.system("cd /data/data/com.termux/files/home")
        os.system("pkg update -y")
        os.system("pkg install -y git")
        os.system("pkg install python2")
        os.system("cd /data/data/com.termux/files/home && git clone https://github.com/sqlmapproject/sqlmap.git")
        os.system("cd /data/data/com.termux/files/home")
        print("------------------------------------")
        print("[+] SQLMap berhasil di install :'(")
        print("[+] pergi ke folder sqlmap dan ketik 'python2 sqlmap.py' untuk menjalankan.")
        print("------------------------------------")
        rmenu = input("[?] kembali ke menu? (y/n): ")
        if rmenu == "y":
            menu()
        else:
            break
    elif what == "4":
        os.system("pkg install -y wget")
        os.system("cd /data/data/com.termux/files/home && wget https://Auxilus.github.io/metasploit.sh")
        os.system("cd /data/data/com.termux/files/home && bash metasploit.sh")
        os.system("cd /data/data/com.termux/files/home && cd metasploit-framework")
        os.system("cd /data/data/com.termux/files/home && gem install bundle --pre")
        os.system("cd /data/data/com.termux/files/home && bundle config build.nokogiri --use-system-libraries")
        os.system("cd /data/data/com.termux/files/home && bundle install")
        os.system("cd /data/data/com.termux/files/home")
        print("------------------------------------")
        print("[+] Metasploit berhasil di install :'(")
        print("[+] ketik 'msfconsole' untuk menjalankan.")
        print("------------------------------------")
        rmenu = input("[?] kembali ke menu? (y/n): ")
        if rmenu == "y":
            menu()
        else:
            break
    elif what == "5":
        os.system("pkg update -y")
        os.system("pkg install -y git")
        os.system("cd /data/data/com.termux/files/home && git clone https://github.com/themastersunil/ngrok.git")
        os.system("cd /data/data/com.termux/files/home")
        print("------------------------------------")
        print("[+] ngrok berhasil di install :'(")
        print("[+] pergi ke folder ngrok dan ketik './ngrok http 80' untuk menjalankan.")
        print("------------------------------------")
        rmenu = input("[?] kembai ke manu? (y/n): ")
        if rmenu == "y":
            menu()
        else:
            break
    elif what == "6":
        os.system("pkg update -y")
        os.system("cd /data/data/com.termux/files/home && git clone https://github.com/Hax4us/Nethunter-In-Termux.git")
        os.system("cd /data/data/com.termux/files/home && cd Nethunter-In-Termux && chmod +x kalinethunter")
        os.system("cd /data/data/com.termux/files/home")
        print("------------------------------------")
        print("[+] Nethunter berhasil di install :'(")
        print("[+] pergi ke folder Nethunter di termux dan ketik './kalinethunter' untuk menjalankan.")
        print("------------------------------------")
        rmenu = input("[?] kembai ke menu? (y/n): ")
        if rmenu == "y":
            menu()
        else:
            break
    elif what == "7":
        os.system("pkg update -y")
        os.system("pkg install -y git")
        os.system("pkg install -y python2")
        os.system("cd /data/data/com.termux/files/home && git clone https://github.com/ihebski/angryFuzzer.git")
        os.system("cd /data/data/com.termux/files/home && cd angryFuzzer")
        os.system("cd /data/data/com.termux/files/home && pip2 install -r requirements.txt")
        os.system("cd /data/data/com.termux/files/home && pip2 install requests")
        os.system("cd /data/data/com.termux/files/home")
        print("------------------------------------")
        print("[+] angryFuzzer berhasil di install :'(")
        print("[+] pergi ke folder angryFuzzer dan ketik 'python2 angryFuzzer.py' untuk menjalankan.")
        print("------------------------------------")
        rmenu = input("[?] kembai ke menu? (y/n): ")
        if rmenu == "y":
            menu()
        else:
            break
    elif what == "8":
        os.system("pkg update -y")
        os.system("pkg install -y git")
        os.system("pkg install -y php")
        os.system("cd /data/data/com.termux/files/home && git clone https://github.com/Tuhinshubhra/RED_HAWK")
        os.system("cd /data/data/com.termux/files/home")
        print("------------------------------------")
        print("[+] RED_HAWK berhasil di install :'(")
        print("[+] pergi ke folder RED_HAWK dan ketik 'php rhawk.php' untuk menjalankan.")
        print("------------------------------------")
        rmenu = input("[?] kembai ke manu? (y/n): ")
        if rmenu == "y":
            menu()
        else:
            break
    elif what == "9":
        os.system("pkg update -y")
        os.system("pkg install -y python2")
        os.system("pkg install -y git")
        os.system("cd /data/data/com.termux/files/home && git clone https://github.com/evait-security/weeman.git")
        os.system("cd /data/data/com.termux/files/home && cd weeman")
        os.system("cd /data/data/com.termux/files/home && chmod +x weeman.py")
        os.system("cd /data/data/com.termux/files/home")
        print("------------------------------------")
        print("[+] weeman berhasil di install :'(")
        print("[+] pergi ke folder weeman dan ketik 'python2 weeman.py' untuk menjalankan.")
        print("------------------------------------")
        rmenu = input("[?] kembali ke manu? (y/n): ")
        if rmenu == "y":
            menu()
        else:
            break
    elif what == "10":
        os.system("pkg update -y")
        os.system("pkg install -y git")
        os.system("pkg install -y python")
        os.system("cd /data/data/com.termux/files/home && git clone https://github.com/maldevel/IPGeoLocation.git")
        os.system("cd /data/data/com.termux/files/home && cd IPGeoLocation")
        os.system("cd /data/data/com.termux/files/home && pip install -r requirements.txt")
        os.system("cd /data/data/com.termux/files/home")
        print("------------------------------------")
        print("[+] IPGeoLocation berhasil di install :'(")
        print("[+] pergi ke folder IPGeoLocation dan ketik 'python ipgeolocation.py' untuk menjalankan.")
        print("------------------------------------")
        rmenu = input("[?] kembali ke menu? (y/n): ")
        if rmenu == "y":
            menu()
        else:
            break
    elif what == "14":
        os.system("pkg update -y")
        os.system("pkg install -y git")
        os.system("cd /data/data/com.termux/files/home && git clone https://github.com/Neo-Oli/termux-ubuntu.git")
        os.system("cd /data/data/com.termux/files/home && cd termux-ubuntu && bash ubuntu.sh")
        print("------------------------------------")
        print("[+] Ubuntu berhasil di install :'(")
        print("[+] pergi ke folder termux-ubuntu dan ketik './start.sh' untuk menjalankan.")
        print("------------------------------------")
        rmenu = input("[?] kembali ke menu? (y/n): ")
        if rmenu == "y":
            menu()
        else:
            break
    elif what == "16":
        os.system("pkg update -y")
        os.system("pkg install -y git")
        os.system("pkg install -y python2")
        os.system("cd /data/data/com.termux/files/home && git clone https://github.com/blackvkng/viSQL.git")
        print("------------------------------------")
        print("[+] viSQL berhasil di install :'(")
        print("[+] pergi ke folder dan ketik 'python2 viSQL.py --help' untuk menjalankan.")
        print("------------------------------------")
        rmenu = input("[?] kembali ke menu? (y/n): ")
        if rmenu == "y":
            menu()
        else:
            break
    elif what == "17":
        os.system("pkg update -y")
        os.system("pkg install -y git")
        os.system("pkg install -y python2")
        os.system("cd /data/data/com.termux/files/home && git clone https://github.com/UltimateHackers/Hash-Buster.git")
        print("------------------------------------")
        print("[+] Hash-Buster berhasil di install :'(")
        print("[+] pergi ke folder Hash-Buster dan ketik 'python2 hash.py' untuk menjalankan.")
        print("------------------------------------")
        rmenu = input("[?] kembai ke manu? (y/n): ")
        if rmenu == "y":
            menu()
        else:
            break
            os.system("pkg update -y")
            os.system("pkg install -y git")
            os.system("pkg install -y python2")
            os.system("cd /data/data/com.termux/files/home && git clone https://github.com/reverse-shell/routersploit.git")
            os.system("cd /data/data/com.termux/files/home && cd routersploit")
            os.system("pip2 install -r requirements.txt")
            os.system("pip2 install -r requirements-dev.txt")
            os.system("pip2 install -r requests")
            print("------------------------------------")
            print("[+] routersploit berhasil di install :'(")
            print("[+] pergi ke routersploit folder dan ketik 'python2 rsf.py' untuk menjalankan.")
            print("------------------------------------")
            rmenu = input("[?] kembali ke menu? (y/n): ")
            if rmenu == "y":
                menu()
            else:
                break
    elif what == "00":
        print("sampai ketemu lagi :'(")
        break
