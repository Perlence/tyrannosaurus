# Tyrannosaurus


## Installation

1.  Install [Python 2.7](https://www.python.org/downloads/windows/):

    - On step 'Customize Python 2.7' please check 'Add python.exe to Path'

2.  Install [Virtualenv](https://virtualenv.pypa.io/en/latest/installation.html)

3.  Install [Node.js](https://nodejs.org/download/)

4.  Install [Bower](http://bower.io/#install-bower)

5.  Install [Git](https://git-scm.com/download/win):

    - On step 'Adjusting your PATH environment' please check 'Use Git from the Windows Command Prompt'

    - On step 'Configuring the line ending conversions' please check 'Checkout as-is, commit as-is'

6.  Clone the repository:

    ```batch
    C:\Users\John> git clone https://github.com/Perlence/tyrannosaurus
    C:\Users\John> cd tyrannosaurus
    ```

7.  Create virtual environment:

    ```batch
    C:\Users\John\tyrannosaurus> virtualenv py27
    ```

8.  Activate virtual environment:

    ```batch
    C:\Users\John\tyrannosaurus> py27\Scripts\activate.bat
    ```

9.  Install requirements:

    ```batch
    (py27) C:\Users\John\tyrannosaurus> pip install -r requirements.txt -r dev-requirements.txt
    ```

10.  Install Bower components:

    ```batch
    (py27) C:\Users\John\tyrannosaurus> bower install
    ```

11. Apply migrations:

    ```batch
    (py27) C:\Users\John\tyrannosaurus> python manage.py migrate
    ```

12. Create super user:

    ```cmd
    (py27) C:\Users\John\tyrannosaurus> python manage.py createsuperuser
    ```

13. Run server:

    ```batch
    (py27) C:\Users\John\tyrannosaurus> python manage.py runserver
    ```

14. Open browser and go to http://127.0.0.1:8000
