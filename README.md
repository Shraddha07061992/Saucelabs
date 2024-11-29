Used Pytest and python langauge for automation of task 
Install python 
$ brew install python 
install pytest 
$ pip3 install pytest 
Framework structure 
Webapp >> saulabs >> 
Assertions >> validation.py(validation checks added here)
Generic >> base.py (added setup and tear down in this file)
pages >> cart.py, login.py and checkoutprocess.py (added pagewise methods added here)
tests >> test_checkoutprocess.py (actual positive test case added here)
Added flow 
login with username and password 
selected random three items 
checked added cart
checkout process 
verified order placed or not 
