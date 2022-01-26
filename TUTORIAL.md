# TUTORIAL

first of all this tool is for educational purposes  only!
> i suggest you to don't use it on a stranger's website or servers and use it on your servers or server you got premission to attack.
## cloning repo:

first thing you need to do is is cloning my tool!
you can type 
"git clone https://github.com/Pastlecry/Lemonade-Tool/"
for it

# How to attack:

#DoS:
first of all go to Lemonade Tool's dictionary by typing
cd Lemonade-Tool
than you need to run the python script by typing
python dos.py
you can get help by typing this in console
python dos.py --h
now what you need to set in attack setup?
let me show you

first you need to set your Attack's Trget IP:
"python dos.py --T [Target website or server's ip]" for example "python dos.py --T 127.0.0.1"

then you need to insert port that you want to attack with:
"python dos.py --P [Port that you want to connect to the server with it(default=80)]" for example "python dos.py --P 80"

after that you need to set Transport Protocol you want to attack with it:
"python dos.py --O [Transport Protocol{UDP, TCP} (default=UDP]" for example "python dos.py --O TCP"

for a quick attack, all you need to do is just inserting Target IP
"python dos.py --T 127.0.0.1"

but for an attack fully customized you can type:
"python dos.py --T 127.0.0.1 --P 80 --O TCP"
