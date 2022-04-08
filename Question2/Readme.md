# Question 2 solution
<img src="https://raw.githubusercontent.com/devicons/devicon/master/icons/python/python-original.svg" width="auto" height="80"/>

## Run the project 
Install the depandencies in a virtual environment 


```
python3 -m venv diffrence
source diffrence/bin/activate
pip install -r requirements.txt
```
Run script against the data
```
python3 diffrences.py -f Lists.xlsx
```

### Available arguments 
```
$ python3 diffrences.py -h
usage: diffrences.py [-h] [-f FILE_XLS] [-l1 LIST1_SHEET] [-l2 LIST2_SHEET] [-c COLUMN]

Find the differences between the 2 lists by generating a 3rd list which contains only those elements from every list.

optional arguments:
  -h, --help            show this help message and exit
  -f FILE_XLS, --file-xls FILE_XLS
                        supply challenge xlsfile
  -l1 LIST1_SHEET, --list1-sheet LIST1_SHEET
                        the name of the sheet 1 in the xlsx file
  -l2 LIST2_SHEET, --list2-sheet LIST2_SHEET
                        the name of sheet 2 in the xlsx file
  -c COLUMN, --column COLUMN
                        column name in xlsx file
```