import json
from parser import parse_user_input
from tools import generate_lens_images


def run_agent(user_input: str):
    """
    Agent workflow with REAL human-in-the-loop interaction
    """

    print("\n[Agent] Processing user input...")

    # Ask for missing resolution
    if "resolution" not in user_input.lower():
        resolution = input("[Agent] What resolution do you want? (e.g., 64, 128): ")
        user_input += f" resolution {resolution}"

    # Ask for missing redshift
    if "redshift" not in user_input.lower():
        redshift = input("[Agent] What redshift value should be used? (e.g., 0.5): ")
        user_input += f" redshift {redshift}"

    # Ask for missing model
    if "model" not in user_input.lower():
        model = input("[Agent] Which model do you want? (Model_I / Model_II): ")
        user_input += f" using {model}"

    try:
        params = parse_user_input(user_input)
        print(f"[Agent] Parsed Params: {params}")

        result = generate_lens_images(params)

        print("[Agent] Simulation completed.\n")

        return result.model_dump()

    except Exception as e:
        return json.dumps({
            "status": "error",
            "message": str(e)
        }, indent=4)