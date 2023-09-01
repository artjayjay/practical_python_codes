import os
import docx
import PyPDF2
import stegoveritas as stego
from PIL import Image

def sanitize_file(file_path):
    """
    Sanitizes a file by removing active content and steganography.
    :param file_path: Path to the file to sanitize.
    """
    _, file_ext = os.path.splitext(file_path)
    
    if file_ext.lower() == ".docx":
        # Sanitize a Microsoft Word document
        doc = docx.Document(file_path)
        for vba_part in doc.part.vba_parts:
            vba_part.clear()
        doc.core_properties.clear()
        doc.extended_properties.clear()
        sanitized_path = os.path.splitext(file_path)[0] + "_clean" + file_ext
        doc.save(sanitized_path)
        
    elif file_ext.lower() == ".pdf":
        # Sanitize a PDF file
        with open(file_path, "rb") as f:
            pdf_reader = PyPDF2.PdfFileReader(f)
            pdf_writer = PyPDF2.PdfFileWriter()
            for page_num in range(pdf_reader.getNumPages()):
                page = pdf_reader.getPage(page_num)
                page.stripAnnots()
                pdf_writer.addPage(page)
            pdf_writer.removeJavaScript()
            pdf_writer.removeMetadata()
            sanitized_path = os.path.splitext(file_path)[0] + "_clean" + file_ext
            with open(sanitized_path, "wb") as out:
                pdf_writer.write(out)
                
    elif file_ext.lower() in [".jpg", ".jpeg", ".png", ".bmp"]:
        # Sanitize an image file
        result = stego.StegAnalysis(file_path)
        if result["steganography_detected"]:
            stego.unhide(file_path, output_path=os.path.splitext(file_path)[0] + "_clean" + file_ext)
        else:
            sanitized_path = file_path
            print("No steganography detected in", file_path)
    else:
        # Unsupported file format
        print("Unsupported file format:", file_ext)
        return
    
    # Remove original file
    os.remove(file_path)
    print("Sanitized file saved to", sanitized_path)

# Example usage
sanitize_file("example.docx")
sanitize_file("example.pdf")
sanitize_file("example.jpg")

# this is from chat gpt