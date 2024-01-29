# Websockets (in Python)

### Summary

A demonstration of Python websockets...

@erickeniuk

![Connect4](/Connect4.png)

Tutorial here:
https://websockets.readthedocs.io/en/stable/intro/tutorial1.html

### To Clone

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

### To Play

Open a browser and go to:
```
http://localhost:8000/
```

### To Push to Git

Commit new changes and provide a commit message:
```
git commit -am "Your commit message here"
```

Add the remote if not added:
```
git remote add origin https://github.com/erickeniuk/websockets_connect4.git
```

For the first push, you may need:
```
git push --set-upstream origin main
```

Otherwise, a simple...
```
git push
```

should suffice.