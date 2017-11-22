Task 1- The exploit
The vulnerability of the code exists when we are reading from the Client. The code will work perfectly while the Client inputs less than 31 and the 32nd index will be set to /0. Which is just an null value and indicates the termination of the string. A longer input will make it such that the password will be over written. When the Client input length is 32, the password is overwritten by /0. If the Client input is more than the buffer size then the password will be over written by the input after the 32nd index. 
This is caused by a bug called buffer overflow. There is a stack where memory is allocated in a Last in First Out manner. So when we defined the struct in the code secretServer.c, it was such that the buffer was initialized before password. The password is defined from the command line argument. Then when a client connects, they give an input and if it matches with the password defined in the Server then we can get the secret message but because the input buffer was defined before the password, if the input is longer than the buffer size the password will get over written.
We created a bash which first initializes a file will buffer_size + 1 ‘a’s and then connect to the Server using nc and redirecting the file. Then create another file with only one a and then connect to the Server again with the new file containing the overwritten password. 

To run the code: 
1) Make sure the server is started in one terminal. 
2) Edit Exploit.sh such that the port number which is 1234 by default matches up with the        
   Server’s port (Not needed if Server port is 1234)
3) You can define the length of the password by just changing the number which is 32 by      
   default to any size. Best way is to make it the same value as the buffer size. Then in
   the next line you can define the new password to be whatever you want. The password
   is “overwritten” by default. Then you create another file which holds the new password.  
   It is also “overwritten” by default. Make sure the input matches the new password you
   set it to.
4) Open another Terminal and type sh Exploit.sh a

