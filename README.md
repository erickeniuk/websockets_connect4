# Websockets (in Python)

A demonstration of Python websockets...

@erickeniuk

https://websockets.readthedocs.io/en/stable/intro/tutorial1.html

### To Install

```
git clone https://github.com/erickeniuk/websockets_connect4.git
```

### To Run

Open a terminal and on the command line:
```
python -m http.server
```

Open another terminal. Enter the `websockets/` dir, and then on the command line:
```
cd websockets/
python app.py
```

Open one more terminal (3rd) and on the command line:
```
python -m websockets ws://localhost:8001/
```