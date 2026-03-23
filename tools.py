from models import SimulationParams, SimulationOutput
from config import MODEL_CONFIGS


def generate_lens_images(params: SimulationParams) -> SimulationOutput:
    """
    Simulates the generation of gravitational lensing images
    """

    # Get model config
    model_config = MODEL_CONFIGS.get(params.model_name, MODEL_CONFIGS["Model_I"])

    # Use model-specific resolution if needed
    resolution = params.resolution or model_config["default_resolution"]

    # Fake image generation
    images = [f"{params.model_name}_image_{i}.png" for i in range(1, params.num_images + 1)]

    # Metadata
    metadata = {
        "substructure_type": params.substructure_type,
        "resolution": str(resolution),
        "redshift": str(params.redshift),
        "model_description": model_config["description"]
    }

    result = SimulationOutput(
        status="success",
        model_used=params.model_name,
        generated_images=images,
        metadata=metadata
    )

    return result