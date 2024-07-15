import os

def combine_jsx_files(source_dir, output_file):
    with open(output_file, 'w', encoding='utf-8') as outfile:
        for root, _, files in os.walk(source_dir):
            for file in files:
                if file.endswith('.jsx'):import os

def combine_jsx_files(source_dir, output_file):
    with open(output_file, 'w', encoding='utf-8') as outfile:
        for root, _, files in os.walk(source_dir):
            for file in files:
                if file.endswith('.jsx'):
                    file_path = os.path.join(root, file)
                    with open(file_path, 'r', encoding='utf-8') as infile:
                        outfile.write(f"// {file_path}\n")
                        outfile.write(infile.read())
                        outfile.write("\n\n")

if __name__ == "__main__":
    source_directory = "/home/ubuntu/wscrm/src"  # Replace with the path to your main folder
    output_file_path = "/home/ubuntu/wscrm/src/combined_code.txt"  # Replace with your desired output file name and path
    combine_jsx_files(source_directory, output_file_path)
    print(f"Combined code saved to {output_file_path}")
                    file_path = os.path.join(root, file)
                    with open(file_path, 'r', encoding='utf-8') as infile:
                        outfile.write(f"// {file_path}\n")
                        outfile.write(infile.read())
                        outfile.write("\n\n")

if __name__ == "__main__ ":
    source_directory = "/home/ubuntu/wscrm/src"  # Replace with the path to your main folder
    output_file_path = "/home/ubuntu/wscrm/src/combined_code.txt"  # Replace with your desired output file name and path
    combine_jsx_files(source_directory, output_file_path)
    print(f"Combined code saved to {output_file_path}")
