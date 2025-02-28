# automate_chatwoot

## Overview
The `automate_chatwoot` project is a command-line interface (CLI) application designed to automate interactions with Chatwoot, an open-source customer support tool. This package provides a set of commands that can be executed from the terminal to streamline various tasks within Chatwoot.

## Installation
To install the `automate_chatwoot` package, follow these steps:

1. Clone the repository:
   ```
   mkdir /etc/scripts | cd /etc/scripts
   git clone https://github.com/brunobuzzeto/automate_chatwoot.git
   ```

2. Navigate to the project directory:
   ```
   cd /etc/scripts/automate_chatwoot
   ```

3. Install the package using pip:
   ```
   pip install .
   ```

## Usage
Once installed, you can use the CLI by running the following command in your terminal:

```
automate_chatwoot [command] [options]
```

### Commands
- `update_status`: Update client conversation status to solved

### Options
- `--db-url` : Postgres database url with password and database.


For more detailed information on each command, you can run:

```
automate_chatwoot [command] --help
```

## Contributing
Contributions are welcome! If you would like to contribute to the `automate_chatwoot` project, please fork the repository and submit a pull request.

## Virtual env

- Navigate to the project folder:

```
cd <your path>/automate_chatwoot
```

- Create your virtual env
```
python3 -m venv venv
```

- Activate the venv.

On linux or macOS:
```
source venv/bin/activate
```

On Windows:
```
.\venv\Scripts\activate
```

- Install the package
```
pip install .
```

## Testing for developmen
Every implementation on contribution must have a test, and still pass on our testbase

- Running the tests:

```bash
python -m unittest discover -s ./automate_chatwoot/src -p 'test_*.py'
```

## License
This project is licensed under the MIT License. See the LICENSE file for more details.
