## Starting the python service

Set up a virtual environment (do this on initial set-up)

```bash
# Create a directory for your virtual environments (if none exists)
mkdir ~/my_env

# Create a new virtual environment
python3 -m venv ~/my_env/next
```

Activate the virtual environment (do this for every new Terminal window)

```bash
source ~/my_env/next/bin/activate
```

Install dependencies 

```bash
cd ./python

python3 -m pip install -r requirements.txt
```

Run the service 

```bash
python3 main.py
```
