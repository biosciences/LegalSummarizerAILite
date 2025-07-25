# LegalSummarizerAI Lite

Streamlit app to summarise NSW residential tenancy agreements using GPT-4.1.

## 📄 Project Links
- 📂 [Source Code](https://github.com/biosciences/LegalSummarizerAILite): Explore the full repository
- 🔗 [Live Report](https://biosciences.github.io/LegalSummarizerAILite/index.html): View the interactive HTML output

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
