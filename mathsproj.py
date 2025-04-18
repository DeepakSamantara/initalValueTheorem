from sympy import symbols, limit, sympify, simplify

# Define the symbolic variable
z = symbols('z')

# Take Z-transform expression from user
user_input = input("Enter the Z-transform expression X(z) in terms of z (e.g., z/(z - 3)): ")

try:
    # Convert input string to symbolic expression
    X_z = sympify(user_input)

    # Compute the initial value using the Initial Value Theorem
    x_0 = limit(X_z, z, float('inf'))

    # Display results
    print("\nZ-transform X(z):", simplify(X_z))
    print("Initial value x[0] using IVT:", x_0)

except Exception as e:
    print("Error in expression:", e)
