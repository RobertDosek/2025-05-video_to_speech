import os
from docx import Document

# Directory containing the .docx files
directory = 'output_documents'

# Create a new Document object for the final output
final_document = Document()

# Iterate through the files in the directory
for filename in os.listdir(directory):
    if filename.endswith('.docx'):
        # Define the full file path
        file_path = os.path.join(directory, filename)

        # Open the existing .docx file
        doc = Document(file_path)

        # Add the file name (without extension) as a header
        final_document.add_heading(filename[:-5], level=1)
        # Add an empty line
        final_document.add_paragraph("")

        # Copy the content from each paragraph in the doc
        for para in doc.paragraphs:
            final_document.add_paragraph(para.text)


# Save the compiled document
final_document.save('vsechno_v_jednom.docx')
