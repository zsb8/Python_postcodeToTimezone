# postcode_timezone
Find the time zone through Post Code.
# 1. How to install this private package through original code from Github?
## (1). One way: use GIT to download and install package from Github.
This test in Ubuntu, you need to get personal token from Github first because it forbit you use really password when you down load.
### How to set your personal token of Github?
https://docs.github.com/en/authentication/keeping-your-account-and-data-secure/creating-a-personal-access-token    
If you have personal token, you can clone or download code from Github on Linux because Linux will ask you input your personal token during the install process.
So you should get a personal token before you install package on Linux. If you have github personal token already, you can pass this step that creathing personal token on Github. 

If you have you personal token, you can type this command on Linux:   
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
![image](https://user-images.githubusercontent.com/75282285/179817348-3ff6ba22-55b1-496a-ab2c-47b7f6e64cc1.png)

Then you will find a new version package in the `/dist/`
![image](https://user-images.githubusercontent.com/75282285/179817480-8e2821aa-3862-41e0-b75f-e31ba663ff4a.png)

Then you can pip install it as others.
![image](https://user-images.githubusercontent.com/75282285/179817725-b80d2fe5-c01e-46bb-94fe-600d921150f5.png)

## (3). pip install directly
You can download the .tar.gz from this repository /dist/*.tar.gz, then you can pip install it on your local.
Such as
~~~
pip install postcode_timezone-1.3.tar.gz
~~~

# 2. How to run this pyhton personal package?
If you install the package already, you can run it, such as:      
Input is a Post Code, output will be a JSON result.
~~~python
from pctz import timezone
timezone.get_time_zone("H9H 5J1")
~~~
You will get the result such as below:
~~~jason
'{"Result": "Success", "Time_zone": -4, "Daylight saving time": "Yes", "Region": "Montreal Metropolitan", "Remark": "This time_zone means the hours before UTC time. If on the second Sunday of March or on the first Sunday in November, diff DST effect today in diff time zone"}'
~~~
If the "Daylight saving time" is Yes, it means the Time_zone is Daylight saving time zone.    
Such as above result, the "H9H 5J1" has dst, so the loca time of "H9H 5J1" will be UTC time minus 4 hours. If UTC is '2022-07-25 <b>08</b>:27:52.000000', the loca time of "H9H 5J1" will be '2022-07-25 <b>04</b>:27:52.000000'. But UTC is '2022-12-25 <b>08</b>:27:52.000000', the loca time of "H9H 5J1" will be '2022-12-25 <b>03</b>:27:52.000000' because not in daylight savting time. 
