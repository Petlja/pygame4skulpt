@for /f %%p in ('pipenv --venv') do call %%p\Scripts\activate.bat
@echo If an environment is activated succesfuly you can use the "deactivate" command to deactivate it
