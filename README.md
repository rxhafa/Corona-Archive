# SE-Sprint01-Team41

<h2>Contributors</h2>
<h3>Sprint 1<h3>

* Rajdeep Bastakoti

* Robert Xhafa

<H2>About the project</H2>
<p>Corona Archive is a web service for Corona disease management which
enables digital tracking of citizens which enter certain places and keeping the records in case of a
Covid infection spread.</p>

<h3>Built with:</h3>

1. flask
2. python3
3. html
4. css

## Using the App in your Machine
Follow these instructions to run the app in your device
### Prerequisites
Mysql
Flask
Sqlite3
Virtual Env
 
### Installation Guide
#### Clone the repo. The following code:
#### git clone https://github.com/Magrawal17/SE-Sprint01-Team41.git

#### Install virtual env
sudo pip3 install virtualenv

#### Create virtual environment
$ virtualenv env

#### Start virtual environment
$ source env/bin/activate

#### Install required dependencies like so:
$ pip install flask
$ pip install sqlite3

#### Run python server for the app like so:
$ python3 run.py

#### Go to the app in your browser using following URL
##### https://localhost:5000



<h1>Sprint 1 Progress</h1>

<h2>Frontend</h2>
1.	Created the main page where the user chooses his status and identity as a user. (whether he is a visitor, place owner, agent or hospital)<br>
2.	Created a login form for the visitor (email or phone number  and password to log in)<br>
3.	Created a registration form for the visitor (name, address, City, email and or phone, password etc..)<br>
4.	Created a login form for the place owner<br>
5.	Created a registration form for the place owner<br>

<h2>Backend</h2>
1.	Store the registered visitors and place owners in the data base<br>
2.	Login Authentication for the visitors and place owners that enter the right credentials  that match<br>
