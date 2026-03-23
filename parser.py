import re
from models import SimulationParams


def parse_user_input(user_input: str) -> SimulationParams:
    """
    Converts natural language input into structured SimulationParams
    """

    # Default values
    num_images = 10
    substructure_type = "none"
    resolution = 64
    redshift = 0.5
    model_name = "Model_I"

    # Extract number of images
    num_match = re.search(r"\d+", user_input)
    if num_match:
        num_images = int(num_match.group())

    # Detect substructure
    if "vortex" in user_input.lower():
        substructure_type = "vortex"
    elif "subhalo" in user_input.lower():
        substructure_type = "subhalo"
    elif "none" in user_input.lower():
        substructure_type = "none"

    # Extract resolution
    res_match = re.search(r"resolution\s*(\d+)", user_input.lower())
    if res_match:
        resolution = int(res_match.group(1))

    # Extract redshift
    redshift_match = re.search(r"redshift\s*([0-9.]+)", user_input.lower())
    if redshift_match:
        redshift = float(redshift_match.group(1))

    # Detect model
    if "model_ii" in user_input.lower():
        model_name = "Model_II"
    elif "model_i" in user_input.lower():
        model_name = "Model_I"

    # Create structured object
    params = SimulationParams(
        num_images=num_images,
        substructure_type=substructure_type,
        resolution=resolution,
        redshift=redshift,
        model_name=model_name
    )

    return params