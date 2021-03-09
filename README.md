# Book Tracker GUI

Used Libraries: 
* Tkinter - It's used to create GUI.
* SQLite3 - It's used for database. 

For Tkinter.ttk theme, breeze-dark theme whose author is Bartek Jasicki is used. The theme's github link: https://github.com/thindil/tkBreeze

In this project, a program that allows the user to store information about books and shows statistics of given informations is built. 

This program was built mainly with Tkinter which is a graphical user interface library and the SQLite3 library which is a library to interact with SQLite database. You have 3 entries where can eter a new book record and also 1 dropdown menu to choose genre of the book. By clicking view all button, you are able to see all the books that have been added to the program. Every record is stored in a table inside the book.db database. You are able to search, update and delete entries also. 

![library](https://user-images.githubusercontent.com/78566362/110482478-c2e60a80-80f9-11eb-85ea-c6f63f3a0f78.png)

For statistics, different tab is created as it shown below. It is possible to see number of pages and books have read, the most read author and genre. 

![statistics](https://user-images.githubusercontent.com/78566362/110482495-c5e0fb00-80f9-11eb-8ecb-0885fc8b9b50.png)

# How to make an executable file 

To make an executable file pyinstaller library is needed. 
* You can install it by using "pip install pyinstaller" command on your PowerShell
* And then call pyinstaller and your main script.  "pyinstaller --onefile --windowed frontend.py "
* --onefile parameter will create a single executable file. 
* If you do not want a terminal, a command line displayed on the background of your GUI, specify another parameter called --windowed

This is valid for Mac users as well. 
