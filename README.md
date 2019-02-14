# ptvsd-flask-reload

demoing an issue when flask app is run with reloading

raises exception on repeat calls to `ptvsd.enable_attach`:

```
OSError(10048, 'Only one usage of each socket address (protocol/network address/port) is normally permitted', None, 10048, None)
```

afterwards attaching to debugger works but does not work properly (breakpoints stop getting caught)


## Getting Started
Run this to start the flask app
```
./run.sh
```

## Attaching to Debugger from VSCode Editor
the file `.vscode/launch.json` contains the launch config we'll use to attach, simply press `F5` to make run it.