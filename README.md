# Time Series with Python & MongoDB

Learn the fundamental techniques for analyzing time-series data with Python, MongoDB, PyMongo, Pandas, & Matplotlib

*References*
- Blog post *(coming soon)*
- Video *(coming soon)* 

*Prerequisites*
- Python 3.8+ Installed
- [Docker Desktop](https://www.docker.com/products/docker-desktop/) Installed (for local MongoDB instance)
- Terminal or PowerShell experience


## Getting Started

1. Make a project directory
```
mkdir -p ~/dev/ts-pymongo
cd ~/dev/ts-pymongo
```
2. Clone this repo:

```
git clone https://github.com/codingforentrepreneurs/time-series-mongodb-pymongo .
```

3. Make and activate a virtual environment:

```
python3.10 -m venv venv
```


*macOS/Linux activation*
```
source venv/bin/activate
```

*Windows activation*
```
./venv/Scripts/activate
```

4. Upgrade Virtual Environment Pip
```
(venv) python -m pip install pip --upgrade
```

5. Move `src/example.env` to `src/.env`
```
mv src/example.env src/.env
```

6. Change `MONGO_INITDB_ROOT_PASSWORD` in `.env`
Create a new password with:

```
(venv) python -c "import secrets;print(secrets.token_urlsafe(32))"
```

So `.env` looks like:

```
MONGO_INITDB_ROOT_USERNAME="root"
MONGO_INITDB_ROOT_PASSWORD="wlke0lL-v7FkGFn5Cl0brfxHJqhDPImBmg-MRfCIXx4" 
```

7. Install requirements

```
(venv) python -m pip install -r src/requirements.txt
```

8. Run Docker Compose
Don't have docker? Install [Docker Desktop](https://www.docker.com/products/docker-desktop/)

```
cd ~/dev/ts-pymongo
docker compose up
```


9. Checkout the Final Results
If you want to see the final code changes, checkout the `final` branch.
```
git checkout final
```
