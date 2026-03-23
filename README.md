# Agentic AI for Autonomous Gravitational Lensing Simulation

## 🚀 Overview
This project implements an **agentic AI workflow** that wraps the DeepLenseSim simulation pipeline to generate strong gravitational lensing images using natural language interaction.

The system allows users to describe simulation parameters (such as substructure type, number of images, resolution, and redshift) in plain English. The agent processes this input, validates parameters, and orchestrates simulation execution.

---

## 🧠 Key Features

- ✅ Natural Language Interaction  
- ✅ Pydantic-based Structured Parameter Modeling  
- ✅ Modular Agent Architecture  
- ✅ Tool-based Simulation Execution  
- ✅ Human-in-the-Loop Interaction (interactive prompts for missing inputs)  
- ✅ Support for Multiple Models (Model_I, Model_II)  
- ✅ Structured JSON Output  

---

## 🏗️ Architecture


User Input
↓
Parser (Natural Language → Structured Data)
↓
Agent (Validation + Decision Making)
↓
Tool (Simulation Wrapper)
↓
Structured Output (JSON)


---

## ⚙️ Approach

### 1. Agent Design
A modular agent (`agent.py`) orchestrates the entire workflow:
- Accepts user input
- Detects missing parameters
- Interactively asks follow-up questions (human-in-the-loop)
- Calls simulation tools

### 2. Natural Language Parsing
The `parser.py` module extracts structured parameters from user prompts:
- Number of images  
- Substructure type (vortex, subhalo, none)  
- Resolution  
- Redshift  
- Model selection  

### 3. Pydantic Models
Defined in `models.py`:
- `SimulationParams` for input validation  
- `SimulationOutput` for structured results  

### 4. Tool Abstraction
The `tools.py` module simulates the DeepLenseSim pipeline:
- Generates mock outputs
- Returns structured metadata
- Designed for easy integration with real simulation code  

### 5. Model Configuration
The `config.py` module supports:
- Model_I (basic simulation)
- Model_II (higher resolution simulation)

---

## 🔗 DeepLenseSim Integration

This project is designed to wrap the DeepLenseSim repository:

https://github.com/mwt5345/DeepLenseSim

Due to computational and dependency constraints, a lightweight simulation wrapper is used. However, the architecture supports real integration by:

- Calling simulation scripts from Model_I / Model_II  
- Passing structured parameters from the agent  
- Returning generated images and metadata  

---

## 🧪 Example Usage

### Input:

Generate 2 vortex images


### Interaction:

[Agent] What resolution do you want? (e.g., 64, 128): 128  
[Agent] What redshift value should be used? (e.g., 0.5): 0.8  
[Agent] Which model do you want? (Model_I / Model_II): Model_I



### Output:
```json
{
    "status": "success",
    "model_used": "Model_I",
    "generated_images": [
        "Model_I_image_1.png",
        "Model_I_image_2.png"
    ],
    "metadata": {
        "substructure_type": "vortex",
        "resolution": "128",
        "redshift": "0.8",
        "model_description": "Basic lensing model"
    }
}

### 📊 Notebook Demonstration

The notebook.ipynb file demonstrates:

Natural language input handling
Human-in-the-loop interaction
Simulation output generation
🛠️ Tech Stack
Python
Pydantic
Modular Agent Design
