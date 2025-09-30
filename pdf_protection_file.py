from pypdf import PdfReader, PdfWriter
import sys

def create_password_protected_pdf(input_pdf, output_pdf, password):
    try:
        pdf_reader = PdfReader(input_pdf)
        pdf_writer = PdfWriter()

        for page in pdf_reader.pages:
            pdf_writer.add_page(page)

        pdf_writer.encrypt(user_password=password)
        with open(output_pdf, "wb") as f:
            pdf_writer.write(f)

        print(f"Password-protected PDF saved as: {output_pdf}")

    except FileNotFoundError:
        print(f"The file {input_pdf} was not found.")
    except Exception as e:
        print(f"Error: {e}")

def main():
    if len(sys.argv) == 4:
        create_password_protected_pdf(sys.argv[1], sys.argv[2], sys.argv[3])
    else:
        print("Use: python pdf_protection_file.py <input_pdf> <output_pdf> <password>")

if __name__ == "__main__":
    main()
