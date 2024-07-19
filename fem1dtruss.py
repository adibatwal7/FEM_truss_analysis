import numpy as np
from scipy.linalg import solve

# Truss properties
E = 210e9  # Young's modulus in Pa
A = 0.0004 # Cross-sectional area in m^2
displacement_at_free_end = 0.025 # Displacement at the free end in meters
L = 2 # Length of each truss element in meters
force_applied = -10.0  # Force applied in kN

# Element stiffness matrix for a 1D truss element
def element_stiffness_matrix(E, A, L):
    k = E * A / L
    return np.array([[k, -k], [-k, k]])

# Global stiffness matrix assembly
def assemble_global_matrix(k_element):
    K_global = np.zeros((4, 4))
    K_global[0:2, 0:2] += k_element
    K_global[2:4, 2:4] += k_element
    return K_global

# Apply boundary conditions and external forces
def apply_boundary_conditions(K_global, displacement_at_free_end, force_applied):
    # Fixed displacement at one end
    K_global[0, :] = 0
    K_global[0, 0] = 1

    # Apply displacement at the free end
    K_global[-2, -1] = 1
    K_global[-1, -2] = 1

    # Adjust right-hand side for the prescribed displacement and applied force
    F = np.zeros(4)
    F[-2] = displacement_at_free_end
    F[-1] = force_applied * 1000  # Convert force to N

    return K_global, F

# Solve for displacements and forces
def solve_system(K_global, F):
    # Solve for displacements
    try:
        displacements = solve(K_global, F)
    except np.linalg.LinAlgError:
        print("Error: Singular matrix encountered. Check input values or system stability.")
        exit()

    # Extract forces
    forces = np.dot(K_global, displacements)

    return displacements, forces

# Main function
def main():
    # Element stiffness matrix
    k_element = element_stiffness_matrix(E, A, L)

    # Global stiffness matrix
    K_global = assemble_global_matrix(k_element)

    # Apply boundary conditions and external forces
    K_global, F = apply_boundary_conditions(K_global, displacement_at_free_end, force_applied)

    # Solve the system
    displacements, forces = solve_system(K_global, F)

    # Extract the displacement at 2m of the truss and the force on the free end
    displacement_at_2m = displacements[2]
    force_on_free_end = forces[-1]

    # Print results
    print("\nResults:")
    print("Displacement at 2m:", displacement_at_2m, "m")
    print("Force on the free end:", force_on_free_end, "N")

if __name__ == "__main__":
    main()
