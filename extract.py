import PyPDF2
import re
import pandas as pd

def extract_text_from_pdf(pdf_path):
    text = ""
    with open(pdf_path, 'rb') as file:
        reader = PyPDF2.PdfReader(file)
        for page_num in range(len(reader.pages)):
            page = reader.pages[page_num]
            text += page.extract_text()
    return text

def split_questions_answers(text):
    question_pattern = re.compile(r'\nQ\d+\. ')
    questions = question_pattern.split(text)
    questions = [q.strip() for q in questions if q.strip()]
    qa_pairs = []
    
    for q in questions:
        q_split = re.split(r'\nA\d*\. ', q, maxsplit=1)
        if len(q_split) == 2:
            qa_pairs.append((q_split[0].strip(), q_split[1].strip()))
        else:
            qa_pairs.append((q_split[0].strip(), ""))
    
    return qa_pairs

pdf_path = '123.pdf'
text = extract_text_from_pdf(pdf_path)
qa_pairs = split_questions_answers(text)

questions, answers = zip(*qa_pairs)
df = pd.DataFrame({'question': questions, 'answer': answers})
df.to_csv('qa_dataset.csv', index=False)
print(df.head())
