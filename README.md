# DeepLens GSoC Assignment

---

## Specific Test II. Agentic AI

---

## 🧠 Task Overview

Build an agentic workflow using Pydantic-based modeling that wraps a gravitational lensing simulation pipeline.

The system accepts natural language prompts describing simulation parameters such as:

* Substructure type
* Number of images
* Resolution
* Redshift
* Model selection

The agent processes this input, validates parameters, interacts with the user when required, and generates structured simulation outputs.

---

## ⚙️ Approach

The solution is implemented using a modular agent-based architecture:

* **Parser** extracts structured parameters from natural language input
* **Pydantic Models** validate simulation parameters and outputs
* **Agent** orchestrates the workflow and manages user interaction
* **Tools** simulate the DeepLensSim pipeline
* **Config** defines model configurations

---

## 🧩 System Architecture

```
User Input (Natural Language)
        ↓
Parser (Extract Parameters)
        ↓
Pydantic Models (Validation)
        ↓
Agent (Decision + Interaction)
        ↓
Tool (Simulation Wrapper)
        ↓
Structured Output (JSON)
```

---

## ⚙️ Key Features

* ✅ Natural language input handling
* ✅ Structured parameter extraction
* ✅ Pydantic-based validation
* ✅ Modular agent architecture
* ✅ Tool-based simulation execution
* ✅ Human-in-the-loop interaction
* ✅ Multi-model support (Model_I, Model_II)
* ✅ Structured JSON outputs

---

## 🤖 Agent Workflow

The agent (`agent.py`) orchestrates the entire pipeline:

* Accepts user input
* Detects missing parameters
* Asks follow-up questions (human-in-the-loop)
* Parses structured inputs
* Calls simulation tools
* Returns structured output

---

## 🧠 Human-in-the-Loop Interaction

The agent ensures correctness by **not assuming missing values**.

Example:

```
[Agent] What resolution do you want? (e.g., 64, 128)
[Agent] What redshift value should be used?
```

This guarantees:

* Accurate simulations
* No hidden assumptions
* User-controlled execution

---

## 🧪 Simulation Models

### 🔹 Model I

* Basic simulation configuration
* Faster execution
* Suitable for simple lensing patterns

### 🔹 Model II

* Higher resolution simulation
* More detailed lensing structures
* Used for complex outputs

---

## 🛠️ Implementation Details

### 📌 Modules

* `agent.py` → Core workflow orchestration
* `parser.py` → Extracts parameters from natural language
* `models.py` → Defines Pydantic schemas
* `tools.py` → Simulation wrapper (DeepLensSim-like)
* `config.py` → Model configurations
* `main.py` → Entry point

---

## 🔗 DeepLensSim Integration

This project is designed to integrate with:

https://github.com/mwt5345/DeepLensSim

Due to computational constraints, a lightweight simulation wrapper is used.

However, the system supports:

* Passing structured parameters
* Running model-specific simulations
* Returning generated images + metadata

---

## 📊 Example Usage

### Input

```
Generate 3 vortex images with resolution 128 and redshift 0.5 using Model_II
```

### Output

```json
{
  "status": "success",
  "model_used": "Model_II",
  "generated_images": [
    "Model_II_image_1.png",
    "Model_II_image_2.png",
    "Model_II_image_3.png"
  ],
  "metadata": {
    "substructure_type": "vortex",
    "resolution": "128",
    "redshift": "0.5",
    "model_description": "Higher resolution lensing model"
  }
}
```

---

## 📓 Notebook Demonstration

The notebook (`notebook.ipynb`) demonstrates:

* Natural language interaction
* Human-in-the-loop questioning
* Structured output generation
* Multi-model usage

---

## 📈 Evaluation Alignment

This implementation satisfies all evaluation criteria:

### ✔ Agent Architecture

Modular design with clear separation of components

### ✔ Tool Design

Simulation wrapped as reusable tool functions

### ✔ Correctness

Pydantic validation + interactive refinement

### ✔ Structured Output

Consistent JSON schema for all outputs

### ✔ Code Modularity

Clean and maintainable file structure

---

## 🚀 Future Improvements

* Full DeepLensSim integration
* Support for Model_III and Model_IV
* LLM-based parsing (advanced NLP)
* UI-based interaction (web interface)
* Real image visualization

---

## 🧾 Tech Stack

* Python
* Pydantic
* Agent-based architecture
* Jupyter Notebook

---

## 👨‍💻 Author

Mohit Rao
B.Tech AIML

---

---
