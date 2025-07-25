# LegalSummarizerAI Lite

🧠 An AI-powered assistant to summarise legal documents into clear, structured summaries, with built-in clause risk detection and multilingual support.

## 📄 Project Links
- 📂 [Source Code](https://github.com/biosciences/LegalSummarizerAILite): Explore the full repository
- 🔗 [Live Report](https://biosciences.github.io/LegalSummarizerAILite/index.html): View the interactive HTML output

## Features

✅ Upload residential tenancy PDFs  
✅ Summarises key clauses: rent, dates, pets, bond, responsibilities  
✅ Detects common legal risk patterns ⚠️  
✅ Generates Word, PDF, and HTML reports  
✅ Auto language detection  
✅ Ready for deployment via Streamlit / Render / GitHub Pages  

## Env
Set your OpenAI API key:
```
export OPENAI_API_KEY=sk-xxxxx
```

## Setup
```
pip install -r requirements.txt
streamlit run app/app.py
```

## Features
- Extracts key clauses from rental agreements
- Outputs summaries to Word / PDF
- Uses GPT-4o with structured prompts
```
