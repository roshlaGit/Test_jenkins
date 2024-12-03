import os
from test_folder.test_folder import testme


# Get all environment variables
env_vars = os.environ

# Define the output file
output_file = 'jenkins_env_variables_git.txt'

# Define the inputs for the testme class
buildno = env_vars.get("BUILD_NUMBER", "default_buildno")  # Replace with actual key from Jenkins or a default
MY_GLOBAL_KEY = env_vars.get("MY_GLOBAL_KEY", "default_key")  # Replace with actual key from Jenkins or a default

# Create an instance of the testme class
test_instance = testme(buildno, MY_GLOBAL_KEY)

# Call the concat function
concat_result = test_instance.concat()

# Write the environment variables to the file
with open(output_file, 'w') as f:
    for key, value in env_vars.items():
        f.write(f"{key}={value}\n")
    f.write(f"Concatenated Result: {concat_result}\n")
    
print(f"Environment variables written to {output_file}")
