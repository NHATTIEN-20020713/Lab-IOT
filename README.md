# Introduction to WSL, set up WSL for Python-programming 
For more information about how to install WSL (Windows Subsystem for Linux), you can watch some tutorial videos below:

https://www.youtube.com/watch?v=ypvjxw5qBK0

https://www.youtube.com/watch?v=aIYhaeJa90g&t=399s

https://www.youtube.com/watch?v=Y1Yr10qrOjg

Commands used for setting up WSL: <br>
cls, clear, exit <br>
wsl --install: use to install the wsl <br>
wsl --set-default-version 2: use to set the version 2 for wsl because it also has version 1 <br> 
wsl --list --verbose: list all distribution <br>
wsl --set-version Ubuntu-18.04 2 <br>
sudo update -y <br>
sudo apt update -y <br>
sudo apt upgrade -y <br>
ubuntu config --default-user name: name is the name you set <br>

Commands used for setting up Python to compile and run in WSL: <br>
sudo apt upgrade python3 <br>
sudo apt install python3-pip: set up pip <br>
sudo apt install python3-venv: set up virtual environment <br>
sudo add-apt-repository ppa:deadsnakes/ppa: set up multiple python versions <br>
sudo apt install python3.number: install the python version that you want instead of default version <br>
python3 --version: check the default version <br>
python3.num --version: check the installed version (num can be 7, 8, 9, 10, 11, 12,...) <br>
python3 -m pip install package_name: install package with default python version <br>
python3.num -m pip install package_name: install package with the python version you want <br>
python3 or python3.num before run code to make sure the version you want to use

On Windows, you can set up the virtual environment as follow: <br>
python or py -m venv any_name (any_name can be: myenv, virtualenv,...) <br>
any_name\Scripts\activate: to activate the environment
