from pydantic import BaseModel, Field
from typing import List, Dict


class SimulationParams(BaseModel):
    """
    Input schema for simulation parameters
    """

    num_images: int = Field(..., description="Number of images to generate")
    substructure_type: str = Field(..., description="Type of substructure (none, subhalo, vortex)")
    resolution: int = Field(..., description="Image resolution (e.g., 64, 128)")
    redshift: float = Field(..., description="Redshift value")

    model_name: str = Field(
    default="Model_I",
    description="Model configuration to use"
)


class SimulationOutput(BaseModel):
    """
    Output schema returned by the agent
    """

    status: str
    model_used: str
    generated_images: List[str]
    metadata: Dict[str, str]