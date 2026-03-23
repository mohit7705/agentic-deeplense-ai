from typing import Dict


MODEL_CONFIGS: Dict[str, Dict[str, str]] = {
    "Model_I": {
        "default_resolution": "64",
        "description": "Basic lensing model"
    },
    "Model_II": {
        "default_resolution": "128",
        "description": "Higher resolution lensing model"
    }
}