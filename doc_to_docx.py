import os

# Specify the directory containing the .doc files
directory = 'output_documents'

# Iterate over all files in the directory
for filename in os.listdir(directory):

    # Check if the file ends with .doc
    if filename.endswith('.doc'):
        # Create the new filename by replacing .doc with .docx
        new_filename = filename[:-4] + '.docx'

        # Create full paths to the file
        old_file = os.path.join(directory, filename)
        new_file = os.path.join(directory, new_filename)

        # Rename the file
        os.rename(old_file, new_file)
        print(f'Renamed: {filename} to {new_filename}')

print("All .doc files have been renamed to .docx")
