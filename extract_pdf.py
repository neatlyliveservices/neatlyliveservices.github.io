import PyPDF2
try:
    with open('NeatlyLive_Terms_and_Conditions.pdf', 'rb') as file:
        reader = PyPDF2.PdfReader(file)
        text = ""
        for page in reader.pages:
            text += page.extract_text() + "\n"
        print(text)
except Exception as e:
    print(f"Error: {e}")
