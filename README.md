# Chief - Code Assignment
### Developer Notes
I cannot afford to spend more time on this challenge, please note:
- Tests pending
- Tasks and users are not persisted

I worked on the assignment as I had committed to doing so. However, as we discussed in our meeting, I believe it would be best for you to consider other candidates whose skill sets are more closely aligned with your current needs.

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
cd ./backend

python3 -m pip install -r requirements.txt
```

Run the service 

```bash
python3 main.py
```

## Starting the frontend

Run the project:

```bash
cd ./frontend

yarn dev
```

Open [http://localhost:8080](http://localhost:8080) with your browser to see the result.
