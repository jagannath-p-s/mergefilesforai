import os

def combine_jsx_files(directory):
    """
    Combines all .jsx files in the specified directory into a single file.
    
    Args:
        directory (str): The path to the directory containing the .jsx files.
    """
    # Create a list to store the contents of each .jsx file
    jsx_contents = []
    
    # Loop through all files in the directory
    for filename in os.listdir(directory):
        # Check if the file has a .jsx extension
        if filename.endswith(".jsx"):
            # Open the file and read its contents
            with open(os.path.join(directory, filename), "r") as file:
                content = file.read()
                jsx_contents.append(content)
    
    # Combine all the .jsx file contents into a single string
    combined_content = "\n\n".join(jsx_contents)
    
    # Write the combined content to a new file
    output_filename = os.path.join(directory, "combined.jsx")
    with open(output_filename, "w") as file:
        file.write(combined_content)
    
    print(f"Combined .jsx files saved to: {output_filename}")

# Example usage
combine_jsx_files("/path/to/directory/containing/jsx/files")
