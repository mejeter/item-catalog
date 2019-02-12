# Movie Genre Catalog


### Source code for displaying information and altering a catalog for authorized users.
This program displays a database of movie and genre information. Authorized
users can perform CRUD operations on the database information once logged in. One can use the Google or Facebook third party logins.

This program allows for users with proper permissions to add, edit, or delete movies and their genres. All users can view the details of the genres and movies.

This program utilizes:
* HTML
* CSS
* JavaScript
* JSON
* Python
* SQL Alchemy
* Flask
* Google OAuth API

The `database_setup.py` file configures the database and defines the classes. The `movies.py` file populates the tables and columns of the database. The `project.py` file includes functionality for login, third party oauth integration, and user registration. The `templates` folder contains formatting, functionality, and forms for the different pages of the program. The `static` folder contains the CSS styling and images.


#### Documentation
1. Install [Git Bash](https://git-scm.com/downloads).
2. Install the appropriate platform package of [VirtualBox](https://www.virtualbox.org/wiki/Download_Old_Builds_5_2).
3. Install the [Vagrant](https://www.vagrantup.com/downloads.html) software.
4. Start the virtual machine by running `vagrant up` in Git Bash.
5. Log in to the virtual machine by running `vagrant ssh` in Git Bash.
6. Fork the GitHub [repository](https://github.com/mejeter/item-catalog.git).
7. Change to desired directory in Git Bash and type `git clone https://github.com/YOUR-USERNAME/YOUR-REPOSITORY`.
8. After you have `cd` into the directory, run `database_setup.py` in the terminal to initialize the database.
9. Type `python movies.py` in the terminal to populate the database.
10. Run `python project.py` in the terminal and open a page in your web browser to **http://localhost:8000**.


#### JSON Endpoints
**/genre/JSON**

Returns JSON to view all genres.

**/genre/<int:genre_id>/movie/JSON**

Returns JSON to view all movies within a given genre.


#### Acknowledgements
* The poster images are fair use from Wikipedia, hosted on Wikimedia Foundation servers.
* Bootstrap boiler template was used.
