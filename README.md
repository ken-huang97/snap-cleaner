# snap-cleaner
Remove grey label and text from snapchat photos

If it says No module named 'PIL' you need to install the requirements
## Set up virtual environment
Read [virtualenvwrapper-win](https://pypi.org/project/virtualenvwrapper-win/) to learn more.

If using Jupyter, this will not apply.

### Python on Windows:
  - If already set up, run `workon snap-cleaner` to activate the venv. 
- Install [virtualenvwrapper-win](https://pypi.org/project/virtualenvwrapper-win/)
- run `mkvirtualenv snap-cleaner` in cmd
  - should now say (snap-cleaner) in every line of cmd
- Download/clone the repo
- run `pip install -r requirements.txt`

## Running the program
- In cmd, run `python snap-cleaner.py`
- Use `python snap-cleaner.py -h` for help with running with non-default arguments
  - e.g. `python snap-clenaer.py 100 200 -i test_images/bird.jpg -o new_bird.jpg`
