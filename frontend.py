import tkinter as tk
from tkinter import ttk
import backend

RESULT_FONT = ('Times', '12', 'bold italic')
STAT_FONT = ('Times', '12', 'bold')
TEXT_FONT = ('Times', '9', 'bold')
WIDGET_PADDING = '0.5c'


#Function to get statistics
def statistic_results():
    genres = [row[3] for row in backend.view()]
    #Page  stats
    if len(genres) > 0: 
        total_page = sum([row[4] if isinstance(row[4],int) else 0 for row in backend.view()])
        page_stat_text.set(f"{total_page} pages. ")
        #Author stats
        author_names = [row[2] for row in backend.view() if row[2] != ""]
        most_frequent_author = max(set(author_names), key = author_names.count)
        most_frequent_author_num = author_names.count(most_frequent_author)
        author_stat_text.set(f"You have read {most_frequent_author_num} books of {most_frequent_author}")
        #Book stats
        book_titles = [row[1] for row in backend.view() if row[1] != ""]
        book_stat_text.set(f"You have read {len(book_titles)} books so far.")
        #Genre stats
        genres = [row[3] for row in backend.view()]
        most_frequent_genre = max(set(genres), key = genres.count)
        genre_stat_text.set(f"You have mostly read {most_frequent_genre} books.")


#Function which shows the all elements on list_box  
def view_command():
    list_box.delete(0, tk.END) 
    for row in backend.view():
        list_box.insert(tk.END, row)

#Function to search on database and show them on list_box
def search_command():
    list_box.delete(0, tk.END)
    for row in backend.search(title_text.get().title(), 
                              author_text.get().title(), 
                              tkvar.get(),
                              page_text.get().title()):
        list_box.insert(tk.END, row)

#Function to add new elements on database
def add_command(): 
    backend.insert( title_text.get().title(), 
                    author_text.get().title(), 
                    tkvar.get(),
                    page_text.get().title())
    list_box.delete(0, tk.END)
    list_box.insert(tk.END, (title_text.get().title(), 
                    author_text.get().title(), 
                    tkvar.get(),
                    page_text.get().title()))
    statistic_results()

#Function to get selected rows on list box
def get_selected_row(event):
    try:
        global selected_tuple
        index = list_box.curselection()[0]
        selected_tuple = list_box.get(index)
        title_entry.delete(0, tk.END)
        title_entry.insert(tk.END, selected_tuple[1])
        author_entry.delete(0, tk.END)
        author_entry.insert(tk.END, selected_tuple[2])        
        page_entry.delete(0, tk.END)
        page_entry.insert(tk.END, selected_tuple[4])
    except IndexError:
        pass

#Function to delete elements on database
def delete_command():
    backend.delete(selected_tuple[0])
    view_command()
    statistic_results()

#Function to update selected element on list box and save on database
def update_command():
    backend.update(selected_tuple[0], 
                    title_text.get().title(), 
                    author_text.get().title(), 
                    tkvar.get(),
                    page_text.get().title())
    view_command()
    statistic_results()

#Genre list for dropdown menu.
genres_list = [
    "Action and Adventure",
    "Autobiography",
    "Biography", 
    "Classics", 
    "Comic Book", 
    "Cookbook", 
    "Detective and Mystery", 
    "Essays", 
    "Fantasy", 
    "Graphic Novel", 
    "Historical Fiction", 
    "History", 
    "Horror", 
    "Literary Fiction",
    "Memoir",
    "Poetry",
    "Romance",
    "Science Fiction",
    "Self-Help",
    "Short Stories",
    "Suspense and Thrillers",
    "True Crime",
    "Women's Fiction"
]

main_window = tk.Tk()
main_window.wm_title("Reading Tracker")

#Tkinter style
main_window.tk.call('source', 'breeze-dark.tcl')
style = ttk.Style()
style.theme_use('breeze-dark')

#Tabs
tab_control = ttk.Notebook(main_window, padding = WIDGET_PADDING)
tab1 = ttk.Frame(tab_control, padding = '0.5c')
tab2 = ttk.Frame(tab_control, padding = '0.5c')

tab_control.add(tab1, text ='Your Library')
tab_control.add(tab2, text ='Statistics')


tab_control.pack(expand = True, fill = tk.BOTH, side = tk.RIGHT)

#Labels
title_label = ttk.Label(tab1, text = "Title", font = TEXT_FONT, padding = WIDGET_PADDING)
title_label.grid(row = 0, column = 0)

book_stat = ttk.Label(tab2, text = "Total number of books: ", font = STAT_FONT, padding = WIDGET_PADDING)
book_stat.grid(row = 0, column = 0)

book_stat_text = tk.StringVar()
book_stat_result = ttk.Label(tab2, textvariable = book_stat_text, font = RESULT_FONT, padding = WIDGET_PADDING)
book_stat_result.grid(row = 0, column = 1)

page_stat = ttk.Label(tab2, text = "Total number of pages: ", font = STAT_FONT, padding = WIDGET_PADDING)
page_stat.grid(row = 1, column = 0)

page_stat_text = tk.StringVar()
page_stat_result = ttk.Label(tab2, textvariable = page_stat_text, font = RESULT_FONT, padding = WIDGET_PADDING)
page_stat_result.grid(row = 1, column = 1)

author_stat = ttk.Label(tab2, text = "Most read author: ", font = STAT_FONT, padding = WIDGET_PADDING)
author_stat.grid(row = 2, column = 0)

author_stat_text = tk.StringVar()
author_stat_result = ttk.Label(tab2, textvariable = author_stat_text, font = RESULT_FONT, padding = WIDGET_PADDING)
author_stat_result.grid(row = 2, column = 1)

genre_stat = ttk.Label(tab2, text = "Most read genre: ", font = STAT_FONT, padding = WIDGET_PADDING)
genre_stat.grid(row = 3, column = 0)

genre_stat_text = tk.StringVar()
genre_stat_result = ttk.Label(tab2, textvariable = genre_stat_text, font = RESULT_FONT, padding = WIDGET_PADDING)
genre_stat_result.grid(row = 3, column = 1)

author_label = ttk.Label(tab1, text = "Author", font = TEXT_FONT, padding = WIDGET_PADDING)
author_label.grid(row = 0, column = 2)

genres_label = ttk.Label(tab1, text = "Genres", font = TEXT_FONT, padding = WIDGET_PADDING)
genres_label.grid(row = 1, column = 0)

page_label = ttk.Label(tab1, text = "Number of Pages", font = TEXT_FONT, padding = WIDGET_PADDING)
page_label.grid(row = 1, column = 2)

#Entries
title_text = tk.StringVar()
title_entry = ttk.Entry(tab1, textvariable = title_text)
title_entry.grid(row = 0, column = 1)

author_text = tk.StringVar()
author_entry = ttk.Entry(tab1, textvariable = author_text)
author_entry.grid(row = 0, column = 3)

page_text = tk.StringVar()
page_entry = ttk.Entry(tab1, textvariable = page_text)
page_entry.grid(row = 1, column = 3)

#Option Menu
tkvar = tk.StringVar(tab1)
tkvar.set(genres_list[0])
genres_opt = ttk.OptionMenu(tab1,tkvar,*genres_list)
genres_opt.grid(row = 1, column = 1)

#List box 
list_box = tk.Listbox(tab1,height = 6, width = 50, font = TEXT_FONT)
list_box.grid(row = 2, column = 0, rowspan = 6, columnspan = 2)

scrow_bar = ttk.Scrollbar(tab1)
scrow_bar.grid(row = 2, column = 2, rowspan = 6)

list_box.configure(yscrollcommand = scrow_bar.set)
scrow_bar.configure(command = list_box.yview)

list_box.bind('<<ListboxSelect>>', get_selected_row)

#Buttons 

view_button = ttk.Button(tab1, text = "View All", width = 12, command = view_command)
view_button.grid(row = 2, column = 3)

search_button = ttk.Button(tab1, text = "Search", width = 12, command = search_command)
search_button.grid(row = 3, column = 3)

add_button = ttk.Button(tab1, text = "Add", width = 12, command = add_command)
add_button.grid(row = 4, column = 3)

update_button = ttk.Button(tab1, text = "Update Selected", width = 12, command = update_command)
update_button.grid(row = 5, column = 3)

delete_button = ttk.Button(tab1, text = "Delete Selected", width = 12, command = delete_command)
delete_button.grid(row = 6, column = 3)

close_button = tk.Button(tab1, text = "Close", width = 12, command = main_window.destroy)
close_button.grid(row = 7, column = 3)

statistic_results()  #To show statistics when program's first run

main_window.mainloop()