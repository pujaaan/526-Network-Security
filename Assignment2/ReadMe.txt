CPSC 526 Assignment 2:
Pujan Bhatta 10162769
Tutorial 1
Mohammed Albaiti
How to run it:
  python3 backdoor.py <port> 

How to connect to it:
  nc localhost <port>
  * Make sure to use the same port as Server

Handshake:
  When prompted for the password enter “password” as password
  If anything else then it disconnects

Supported Commands:
  pwd, cd, cwd, ls, cp, rm, mv, cat, snap, diff, off, who, ps


All of the command works. The snap and the diff command works recursively. The code has been documented and cleaned up.

Summary:
  This code listens in a port, takes command and executes them.