# postcode_timezone
Find the time zone through Post Code
# How to install this private package through original code from Github?
## (1). One way: use GIT to download and install package.
This test in Ubuntu, you need to get personal token from Github first because it forbit you use really password when you down load.
~~~
python3 -m pip install git+https://github.com/waybase-data-analytics/data-tools.git@first_refactor
~~~
![image](https://user-images.githubusercontent.com/75282285/153072035-794da8a0-1e52-470a-81cd-d3b417edd652.png)
Then you can use it in Python environment because you install it already. 

## (2). The other way: run setup.py to build a package
You can download code to local disk from Github and build a package on your local disk.
~~~
python setup.py sdist
~~~
![image](https://user-images.githubusercontent.com/75282285/165078786-06dd2348-bb1a-42c1-9f07-d4c23ecab420.png)
![image](https://user-images.githubusercontent.com/75282285/165078866-5b21eac0-4628-4ad4-92d9-26bca1425146.png)

Then you will find a new version package in the `/dist/`
![image](https://user-images.githubusercontent.com/75282285/165078607-5a4377e1-5461-4e35-91b3-090f82b7759e.png)
