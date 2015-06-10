# Tyrannosaurus


## Installation

- Install [Python 2.7](https://www.python.org/downloads/windows/):

  - On step 'Customize Python 2.7' please check 'Add python.exe to Path'

- Install [Virtualenv](https://virtualenv.pypa.io/en/latest/installation.html)

- Install [Node.js](https://nodejs.org/download/)

- Install [Bower](http://bower.io/#install-bower)

- Install [Git](https://git-scm.com/download/win):

  - On step 'Adjusting your PATH environment' please check 'Use Git from the Windows Command Prompt'

  - On step 'Configuring the line ending conversions' please check 'Checkout as-is, commit as-is'

- Clone the repository:

  ```batch
  C:\Users\John> git clone https://github.com/Perlence/tyrannosaurus
  C:\Users\John> cd tyrannosaurus
  ```

- Create and activate virtual environment:

  ```batch
  C:\Users\John\tyrannosaurus> virtualenv py27
  C:\Users\John\tyrannosaurus> py27\Scripts\activate.bat
  ```

- Install requirements:

  ```batch
  (py27) C:\Users\John\tyrannosaurus> pip install -r requirements.txt -r dev-requirements.txt
  ```

- Install Bower components:

  ```batch
  (py27) C:\Users\John\tyrannosaurus> bower install
  ```

- Apply migrations:

  ```batch
  (py27) C:\Users\John\tyrannosaurus> python manage.py migrate
  ```

- Create super user:

  ```cmd
  C:\Users\John\tyrannosaurus> python manage.py createsuperuser
  ```

- Run server:

  ```batch
  (py27) C:\Users\John\tyrannosaurus> python manage.py runserver
  ```

- Open browser and go to http://127.0.0.1:8000
