S3 Auto Uploader
==========================
Library to monitoring a specific folder for a new file and send it to a Amazon S3 bucket

Usage
-----
    1. Check a folder for changes (New files)
    2. Send file found to a S3 bucket

Requirements
^^^^^^^^^^^^

    * Python 3.5 or earlier
    * PIP (Python Instaler Package) - https://pypi.python.org/pypi/pip
    * AWS credentials (to access sqs/sns at least)
    * Check the requirements folder at the project root.


Installation
------------
Clone de repository
::

    $ git clone git@github.com:solidarium/s3-auto-uploader.git

    You must have a ssh key to make the clone from this way
    
    $ cd  s3-auto-uploader
    $ python setup.py install

Use
-----
::

    In [1]: import s3_auto_uploader
    In [2]: s3_auto_uploader.auto_uploader('/full/path', 'bucket', 'folder key')
