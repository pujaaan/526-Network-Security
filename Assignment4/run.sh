#! /bin/bash

clear

echo "Write null 1KB"
time python3 Client.py write a.txt localhost:$1 null pass < 1KB.bin

echo "\n\nWrite null 1MB"
time python3 Client.py write a.txt localhost:$1 null pass < 1MB.bin

echo "\n\nWrite null 1GB"
time python3 Client.py write a.txt localhost:$1 null pass < 1GB.bin

echo "\n\nWrite aes128 1KB"
time python3 Client.py write a.txt localhost:$1 aes128 pass < 1KB.bin

echo "\n\nWrite aes128 1MB"
time python3 Client.py write a.txt localhost:$1 aes128 pass < 1MB.bin

echo "\n\nWrite aes128 1GB"
time python3 Client.py write a.txt localhost:$1 aes128 pass < 1GB.bin

echo "\n\nWrite aes256 1KB"
time python3 Client.py write a.txt localhost:$1 aes256 pass < 1KB.bin

echo "\n\nWrite aes256 1MB"
time python3 Client.py write a.txt localhost:$1 aes256 pass < 1MB.bin

echo "\n\nWrite aes256 1GB"
time python3 Client.py write a.txt localhost:$1 aes256 pass < 1GB.bin


echo "\n\nRead null 1KB"
time python3 Client.py read a.txt localhost:$1 null pass > scrap.txt
echo "\n\nRead null 1MB"
time python3 Client.py read a.txt localhost:$1 null pass > scrap.txt
echo "\n\nRead null 1GB"
time python3 Client.py read a.txt localhost:$1 null pass > scrap.txt
echo "\n\nRead aes128 1KB"
time python3 Client.py read a.txt localhost:$1 aes128 pass > scrap.txt
echo "\n\nRead aes128 1MB"
time python3 Client.py read a.txt localhost:$1 aes128 pass > scrap.txt
echo "\n\nRead aes128 1GB"
time python3 Client.py read a.txt localhost:$1 aes128 pass > scrap.txt
echo "\n\nRead aes256 1KB"
time python3 Client.py read a.txt localhost:$1 aes256 pass > scrap.txt
echo "\n\nRead aes256 1MB"
time python3 Client.py read a.txt localhost:$1 aes256 pass > scrap.txt
echo "\n\nRead aes265 1GB"
time python3 Client.py read a.txt localhost:$1 aes256 pass > scrap.txt
