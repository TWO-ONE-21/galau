#hanya untuk hiburan bro, jgn baper :voss
import os,time

class warna():
    merah = '\033[31m'
    hijau = '\033[32m'
    kuning = '\033[33m'
    biru = '\033[34m'

print '\n'+'\033[1;41mProgram Konsultasi Hati | By Ardo Rianda\033[1;m'+'\n'

nama = raw_input(warna.biru+'[#]Siapakah Nama Anda? '+warna.kuning)
dia = raw_input(warna.biru+'[#]Siapa nama orang yang anda suka? '+warna.kuning)

def main():
    print '\n'+warna.biru + '[*]Selamat Datang '+warna.merah+ nama + warna.biru + ' Mohon pilih salah satu dari pilihan berikut:'
    print warna.kuning + '==> 1. Mencoba mendapatkan hati si ' + warna.merah + dia
    print warna.kuning + '==> 2. Membiarkan dia bahagia bersama orang lain'

    pilihan = input(warna.merah+'[Pilih Nomor] : '+warna.kuning)

    if pilihan == 1:
        cinta = raw_input(warna.biru+'Apakah kamu mencintainya? '+warna.merah+'[YA/gak] '+warna.hijau)
        cinta = cinta.lower()
        if cinta == 'ya':
            os.system('clear')
            print warna.hijau+nama.upper()+warna.merah+'! KENAPA LU MASIH MENCINTAI DIA?\nDIA AJA GAK ADA PERASAAN SAMA LU.'
            time.sleep(5)
            os.system('clear')
            print warna.merah+'LU ITU BUKAN TIPE DIA\nHARUSNYA LU SADAR BRO!!'
            time.sleep(5)
            os.system('clear')
            print warna.merah+'SAINGAN LU GAK CUMAN SATU DUA AJA.\nTAPI BANYAK BRO, MEREKA LEBIH KAYA DAN LEBIH BISA BAHAGIAIN SI '+warna.hijau+dia.upper()+warna.merah+' ITU :"")'
            time.sleep(7)
            os.system('clear')
            print warna.merah+'MUNDUR BROO, MUNDUR... RELAKAN DIA DENGAN YANG LAIN. :")'
            time.sleep(5)
            os.system('clear')
            kembali = raw_input(warna.hijau+'Apakah anda ingin mencoba pilihan yang lain? '+warna.merah+'[YA/gak] '+warna.kuning)
            kembali = kembali.lower()
            if kembali == 'ya':
                os.system('clear')
                return main()
            else:
                os.system('exit')
                
    else:
        os.system('clear')
        print warna.kuning+nama+warna.hijau+'! KAMU MEMILIH PILIHAN YANG BENAR :)'
        time.sleep(3)
        os.system('clear')
        print warna.hijau+'LEBIH BAIK RELAKAN DIA SAMA YANG LAIN :)'
        time.sleep(4)
        os.system('clear')
        print warna.merah+'JANGAN LEMAH, BANGKIT BRO. CEWE GAK CUMAN SATU AJA.\nMASIH BANYAK YANG LAIN, YANG LEBIH BAIK DAN LEBIH CANTIK DARI DIA :")'
        time.sleep(5)
        os.system('clear')
        print warna.merah+'JANGAN GOBLOK HANYA KARNA CINTA!! :")'
        time.sleep(5)
        os.system('clear')
        print warna.hijau+'AYO BUKTIKAN KALO LU BISA DAPETIN YANG LEBIH DARI DIA :)'
        time.sleep(4)
        os.system('clear')
        print warna.merah+'S U A T U  S A A T  L U  B A K A L  L I A T  D I A  J A L A N  B A R E N G  P A C A R  B A R U N Y A  P A K E '+warna.hijau+ ' L A M B O R G H I N I,'
        time.sleep(3)
        print warna.kuning+'\nD A N  L U  C U M A  B I S A  M E L I H A T  M E R E K A  D A R I  A T A S  '+warna.merah+'H E L I K O P T E R '+warna.kuning+' LU\n'
        time.sleep(7)
        os.system('clear')
        
main()
def penutup():
    a = raw_input(warna.merah+nama.upper()+warna.kuning+', APAKAH ANDA MASIH MENGINGINKAN DIA?? '+warna.merah+'[ya/GAK] '+warna.hijau)
    a = a.lower()
    if a == 'gak':
        print warna.hijau+'Jawaban yang sangat tepat :)'
        os.system('exit')
    elif a != 'ya' and a != 'gak':
        print warna.merah+"HARAP PILIH "+warna.hijau+"'YA'"+warna.merah+' ATAU'+warna.hijau+"'GAK'"
        return penutup()
    else:
        print warna.merah+'Sumpah gobloknya murni pemberian tuhan'
        os.system('exit')
penutup()
