## Örnek Çıktılar

Input: a2b1t4r7p1prtbac1x0xcm2m  
Output:  
c  
_x  
m  
​a  
_b  
__t  
___r  
____p  
  
Input: a2ab3f1fg2gb  
Output:  
a  
b  
_f  
_g  

Input: a2b1t4r7p1prtbac1x0xcm2f5fu5um  
Output:  
c  
_x  
m  
_u  
_f  
a  
_b  
__t  
___r  
____p 

Input: g3a2b1t4r7p1prtbac1x0xcm2f5fu5umg  
Output:  
g  
_c  
__x  
_m  
__u  
__f  
_a  
__b  
___t  
____r  
_____p  

## Çok Bir Şey Anlatılmayan Basit Açıklama
Verilen Input serialized olmuş bir  XML veya JSON 
(nested) tarzı bir veri yapısını temsil ediyor, 
Output ise bu veri yapısının sort edilmiş ve 
node derinliğini belirten bir şekilde indent edilmiş halini temsil ediyor. 

Varsayımlar:
Her harf (a-z) sadece bir kere kullanılır
Sayı değerleri (0-9) tek basamaklıdır

## Benim Anladığım
Bir harf gördüğümde o harfi tekrar görene kadar bir döngüdeyim gibi düşündüm.
her sayı gördüğümde harfle sayıyı bir bütün olarak hesapladım. 
Tekrar eden bir harf görünce döngüden çıktığımı hayal ettim.  
En zor kısmı aynı seviyedekileri sıralamak oldu, döngü mantığı ile zaten deep'leri bulmak çok kolaydı.
orada da 1. örnek bana çok yardımcı oldu, çünkü a ve m değerlerinin valueları eşit olduğu halde m daha önce yazılıyordu.

Bir file tree mantığı ile gitmek hoşuma giden bir şey, aslında ilk yazdığımda arraylist şeklinde yapmıştım ama onu beğenmedim.
Benzer projeleri çoğaltabiliriz, mesela hesap makinasında benzer mantık kullanılıyor, parentez aç kapa ve işlem öncelikleri 
yapılırken benzer tree ve stack yapısından faydalanılıyor diye hatırlıyorum.


### Proje Notları
PyCharm 2018.3.1 (Professional Edition)  
Build #PY-183.4588.64, built on December 4, 2018  
JRE: 1.8.0_152-release-1343-b16 x86_64  
JVM: OpenJDK 64-Bit Server VM by JetBrains s.r.o  
macOS 10.16  
python 3.6.7 venv