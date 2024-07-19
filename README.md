# FEM_truss_analysis
Finite Element Analysis of a 1 D truss element
# Finite Element Analysis of a 1D Truss Element

## Overview
This repository contains a Python implementation of a finite element analysis (FEA) for a 1D truss element. The code is designed to model and analyze the mechanical behavior of truss structures under various loading conditions.

## Features
- **Element Stiffness Matrix**: Calculate the stiffness matrix for a 1D truss element.
- **Global Stiffness Matrix Assembly**: Assemble the global stiffness matrix from individual element stiffness matrices.
- **Boundary Conditions and External Forces**: Apply boundary conditions and external forces to the truss.
- **Displacement and Force Calculation**: Solve for nodal displacements and extract forces in the truss.
- **Results Output**: Display the displacement at 2 meters and the force on the free end of the truss.

## Getting Started

### Prerequisites
- Python 3.x
- NumPy
- SciPy

### Installation
1. Clone the repository:
    ```bash
    git clone https://github.com/yourusername/1d-truss-finite-element-analysis.git
    cd 1d-truss-finite-element-analysis
    ```
2. Install the required Python packages:
    ```bash
    pip install numpy scipy
    ```

### Usage
1. Run the analysis:
    ```bash
    python truss.py
    ```