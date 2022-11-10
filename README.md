# python-ssh

The python script that create connection using ssh and perform any action on remoe system.

In this script, I mentioned how to create text file and paste content in it to remote server.

## How to run the Script?
Create and activate virtual enviornment.

```bash
python -m venv venv
```

```bash
venv\Scripts\activate
```

Install the paramiko package

```bash
pip install paramiko
```

To run the script
- Specify the IP Address, Username, Password and path to the folder where file is being created then run below command.

```bash
python main.py
```