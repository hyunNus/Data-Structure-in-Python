import pypdf
import os

def extract_text(pdf_path, start_page, end_page, output_path):
    try:
        reader = pypdf.PdfReader(pdf_path)
        text = ""
        # Pages are 0-indexed in pypdf, so we subtract 1 from user-provided page numbers
        # However, usually "page 109" in a book might be different from the 109th page in the PDF file.
        # I will assume the user means the physical pages of the PDF file for now.
        # If they meant printed page numbers, I might need to adjust. 
        # Let's extract a bit more context or just the exact range 109-178 (indices 108-178).
        
        # Adjusting for 0-based index
        start_idx = start_page - 1
        end_idx = end_page  # range is exclusive at the end, so this covers up to page 178
        
        for i in range(start_idx, end_idx):
            if i < len(reader.pages):
                page = reader.pages[i]
                text += f"--- Page {i+1} ---\n"
                text += page.extract_text() + "\n\n"
            else:
                print(f"Page {i+1} is out of range.")
        
        with open(output_path, "w", encoding="utf-8") as f:
            f.write(text)
        print(f"Successfully extracted text to {output_path}")
        
    except Exception as e:
        print(f"Error extracting text: {e}")

if __name__ == "__main__":
    pdf_path = r"c:\Users\user\OneDrive\바탕 화면\my project\lesson.pdf"
    output_path = r"c:\Users\user\OneDrive\바탕 화면\my project\extracted_lesson_text.txt"
    # Pages 109 to 178
    extract_text(pdf_path, 109, 178, output_path)
