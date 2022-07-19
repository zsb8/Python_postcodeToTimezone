# postcode_timezone
Find the time zone through Post Code
# How to install this private package through original code from Github?
## (1). One way: use GIT to download and install package.
This test in Ubuntu, you need to get personal token from Github first because it forbit you use really password when you down load.
~~~
python3 -m pip install git+https://github.com/zsb8/postcode_timezone.git@main
~~~
![image](https://user-images.githubusercontent.com/75282285/179816321-c6aa744a-f09a-470b-9f43-0b7606f24905.png)
Then you can use it in Python environment because you install it already. 
![image](https://user-images.githubusercontent.com/75282285/179816896-94b04441-3c86-473c-af37-75e65f5105d4.png)


## (2). The other way: run setup.py to build a package
You can download code to local disk from Github and build a package on your local disk.
~~~
python setup.py sdist
~~~
![image](https://user-images.githubusercontent.com/75282285/165078786-06dd2348-bb1a-42c1-9f07-d4c23ecab420.png)
![image](https://user-images.githubusercontent.com/75282285/165078866-5b21eac0-4628-4ad4-92d9-26bca1425146.png)

Then you will find a new version package in the `/dist/`
![image](https://user-images.githubusercontent.com/75282285/165078607-5a4377e1-5461-4e35-91b3-090f82b7759e.png)

# How to run this code
~~~
from pctz import timezone
timezone.get_time_zone("H9H 5J1")
~~~
