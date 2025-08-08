# Import required libraries
import PyPDF2
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize

# Download necessary NLTK resources (only needed once)
nltk.download('punkt_tab')
nltk.download('stopwords')

# Function to extract text from a PDF file
def extract_text_from_pdf(pdf_path):
    with open(pdf_path, 'rb') as file:
        reader = PyPDF2.PdfReader(file)  # Initialize PDF reader
        text = ''
        for page in reader.pages:
            text += page.extract_text()  # Extract text from each page
        return text

# Function to clean and tokenize text
def clean_text(text):
    tokens = word_tokenize(text.lower())  # Convert text to lowercase and tokenize into words
    stop_words = set(stopwords.words('english'))  # Load English stopwords
    # Keep only alphabetic tokens and remove stopwords
    cleaned = [word for word in tokens if word.isalpha() and word not in stop_words]
    return set(cleaned)  # Convert list to set for comparison

# Load and extract text from resume and job description PDFs
resume_text = extract_text_from_pdf(r"C:\Users\Ajay\Downloads\HARSHITH MUNAKALA.pdf")
jd_text = extract_text_from_pdf(r"C:\Users\Ajay\Downloads\JD.pdf")

# Clean and extract keywords from both documents
resume_words = clean_text(resume_text)
jd_words = clean_text(jd_text)

# Compare keywords to find matched and missing skills
matched_skills = resume_words & jd_words  # Set intersection: common skills
missing_skills = jd_words - resume_words  # Set difference: skills required but not in resume

# Calculate the match percentage
match_percentage = round(len(matched_skills) / len(jd_words) * 100, 2) if jd_words else 0

# Print the final skill match report
print("📄 Resume-JD Skill Match Report")
print("=" * 40)
print(f"✅ Matched Skills: {matched_skills}")
print(f"❌ Missing Skills: {missing_skills}")
print(f"📊 Match Percentage: {match_percentage}%")