Install nbgrader
================

Here we explain how to install nbgrader.

First of all we need a up-to-date python distribution. If you already have a
running python distribution, you can skip this step. We suggest to use
`Anaconda <https://www.continuum.io/downloads>`_. Instructions on how to
install Anaconda are available at the download page.

Now, use pip to install nbgrader. The output should look like:
```
$ pip install nbgrader
Collecting nbgrader
  Using cached nbgrader-0.2.2-py2.py3-none-any.whl
  Requirement already satisfied (use --upgrade to upgrade): jupyter-core in /home/ltmp/anaconda3/lib/python3.5/site-packages (from nbgrader)
  Requirement already satisfied (use --upgrade to upgrade): nbconvert in /home/ltmp/anaconda3/lib/python3.5/site-packages (from nbgrader)
  Requirement already satisfied (use --upgrade to upgrade): notebook in /home/ltmp/anaconda3/lib/python3.5/site-packages (from nbgrader)
  Requirement already satisfied (use --upgrade to upgrade): sqlalchemy in /home/ltmp/anaconda3/lib/python3.5/site-packages (from nbgrader)
  Requirement already satisfied (use --upgrade to upgrade): requests in /home/ltmp/anaconda3/lib/python3.5/site-packages (from nbgrader)
  Requirement already satisfied (use --upgrade to upgrade): Flask in /home/ltmp/anaconda3/lib/python3.5/site-packages (from nbgrader)
  Requirement already satisfied (use --upgrade to upgrade): traitlets in /home/ltmp/anaconda3/lib/python3.5/site-packages (from nbgrader)
  Requirement already satisfied (use --upgrade to upgrade): nbformat in /home/ltmp/anaconda3/lib/python3.5/site-packages (from nbgrader)
  Requirement already satisfied (use --upgrade to upgrade): tornado in /home/ltmp/anaconda3/lib/python3.5/site-packages (from nbgrader)
  Requirement already satisfied (use --upgrade to upgrade): six in /home/ltmp/anaconda3/lib/python3.5/site-packages (from nbgrader)
  Requirement already satisfied (use --upgrade to upgrade): python-dateutil in /home/ltmp/anaconda3/lib/python3.5/site-packages (from nbgrader)
  Installing collected packages: nbgrader
  Successfully installed nbgrader-0.2.2
```
The last line should state that nbgrader was installed successfully.

The last step is to activate the nbgrader toolbar extension for Jupyter
notebooks. You can use the nbgrader command line tool to activate the toolbar:
```
$ nbgrader extension activate
[ExtensionActivateApp | WARNING] Unrecognized JSON config file version, assuming version 1
[ExtensionActivateApp | INFO] Activating create_assignment nbextension
[ExtensionActivateApp | INFO] Activating assignment_list server extension
[ExtensionActivateApp | WARNING] Unrecognized JSON config file version, assuming version 1
[ExtensionActivateApp | INFO] Activating assignment_list nbextension
[ExtensionActivateApp | INFO] Done. You may need to restart the Jupyter notebook server for changes to take effect.
```
