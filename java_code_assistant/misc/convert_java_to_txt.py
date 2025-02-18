import os

# Define paths
java_project_dir = "../airline_reservation_system/Project"  # Your Java project directory
output_dir = "./java_code_assistant/outputs"  # Desired output directory
output_file = os.path.join(output_dir, "java_files.txt")

# Create the outputs directory if it doesn't exist
os.makedirs(output_dir, exist_ok=True)

# Function to concatenate Java files
def concatenate_java_files(directory, output_file):
    with open(output_file, "w", encoding="utf-8") as outfile:
        for root, _, files in os.walk(directory):
            for file in files:
                if file.endswith(".java"):
                    file_path = os.path.join(root, file)
                    with open(file_path, "r", encoding="utf-8") as infile:
                        outfile.write(f"// File: {file_path}\n")
                        outfile.write(infile.read())
                        outfile.write("\n\n")  # Add spacing between files

# Run the function
concatenate_java_files(java_project_dir, output_file)
print(f"All Java files have been concatenated into {output_file}")
