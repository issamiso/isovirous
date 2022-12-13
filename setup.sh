#setup virous 
echo '[--] Loding ......'
pkg install python -y 
pkg install python2 -y 
pkg install python3 -y 
pkg install zip -y 
pkg install unzip -y 
unzip Viso.zip 
rm -rif Viso.zip 
python3 viso.py 