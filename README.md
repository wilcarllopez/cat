# :cat2: "cat" Functionality Python Script
A python script of Linux' cat functionalities using  *argparse* . 

## What is cat?
The cat (short for "**concatenate**") command is one of the most frequently used command in Linux/Unix like operating systems.
cat command allows to create single or multiple files, view contain of file, concatenate files and redirect output in terminal or files.

## Usage
First, download or clone the repository. After which, run the script in a terminal.
```bash
python <directory>/cat.py
```
Using -h will show the list of argparse command for the script.
```python
positional arguments:
  texts            Filename of the text file/s

optional arguments:
  -h, --help       Show this help message and exit
  -r, --read       Read the text file
  -c, --create     Create a text file
  -w, --write      Write content for the text file
  -cat, --concat   Concatenate files and save it to another text file
  -app, --append   Append content to the end of file chosen
  -prp, --prepend  Prepend content at the start of file chosen
```

## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

Please make sure to update tests as appropriate. :+1:
