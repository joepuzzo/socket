# Socket Example

This project an example of how to make js and python clients talk to a js soket server or python socket server. You would do this when you had some master controller that you want multiple services to subscribe to ( some running in js and some in python ).

## Installation

Its reccomended that you set up a viruall python envirnment. Note, in this example we use 3.10 of python

Run the following in the root of the project.

```bash
python3.10 -m venv venv
```

The above will set up a virtual envirnment directory. Next you simply activate it.

```bash
source venv/bin/activate
```

This will activate the virtual envirnment. Now all thats left is to install the dependencies

```bash
python -m pip install -r requirements.txt
```

## Testing our first program

With the virtual env activated we can now run the following to start the two clients and the control server

```bash
npm start
```

By default this will run with the js server. In order to run with the python server you can run the following command:

```bash
npm start -- --controller=py
```

Under the hood this is simply running the `start.sh` bash script which can take a `--controller` argument.
