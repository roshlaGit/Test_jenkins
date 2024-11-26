import os

# Get all environment variables
env_vars = os.environ

# Define the output file
output_file = 'jenkins_env_variables_git.txt'

# Write the environment variables to the file
with open(output_file, 'w') as f:
    for key, value in env_vars.items():
        f.write(f"{key}={value}\n")

print(f"Environment variables written to {output_file}")
