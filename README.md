# PyHotkey

A hotkey combination listener that outputs text after keypress combo listener is activated.

## Installation

This was created under the assumption of python version 3.11

To install PyHotkey, run the following command:

```bash
pip install pyhotkey
```

## Usage

To activate the PyHotkey hotkey combination listener, use:

```bash
pyhotkey
```

### Virtual Env

Run `. ./use-venv.sh` to switch to python3.11 using python and activate/create the virtual environment.


## Features

- Activate and deactivate the hotkey combination listener using a PyHotkey modifier key.
- Define your custom hotkey combinations and their corresponding actions in `combos.json`.

## Configuration

Edit `combos.json` to define your hotkey combinations and the text that should be output when each combination is activated.

Example:

```json
{
  "ctrl+alt+a": "Text for ctrl+alt+a",
  "ctrl+alt+b": "Text for ctrl+alt+b"
}
```

## Tests

To run tests, run the following command:

```bash
python -m unittest tests.py
```

## Contribution

Contributions are welcome! Please read the [contribution guidelines](CONTRIBUTING.md) first.

## License

MIT

## Author

Cary Carter
Email: ccarterdev@gmail.com
GitHub: [cc-d](https://github.com/cc-d)