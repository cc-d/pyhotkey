import json
import os
from typing import List, Dict, Any, Optional, Union, Tuple, Set


# Determine the path of combos.json relative to the location of this utils.py file
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
COMBOS_PATH = os.path.join(BASE_DIR, "combos.json")

def load_combos(file_path: str = COMBOS_PATH) -> Dict[str, str]:
    """
    Load the combos from a JSON file.

    Parameters:
    - file_path (str): The path to the JSON file containing combos. Defaults to the path relative to this utils file.

    Returns:
    - Dict[str, str]: A dictionary mapping hotkey combinations to text.
    """
    with open(file_path, 'r') as f:
        return json.load(f)

def write_combos(combos: Dict[str, str], file_path: str = COMBOS_PATH) -> None:
    """
    Write the combos to a JSON file in a pretty format.

    Parameters:
    - combos (Dict[str, str]): The dictionary mapping hotkey combinations to text.
    - file_path (str): The path to the JSON file where combos will be written. Defaults to the path relative to this utils file.
    """
    with open(file_path, 'w') as f:
        json.dump(combos, f, indent=4)
