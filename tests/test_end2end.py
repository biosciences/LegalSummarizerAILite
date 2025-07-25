import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from core import pdf_parser, prompt_template, summarizer

def test_summarization_pipeline():
    with open("samples/NSW_residential_tenancy_agreement_sample.pdf", "rb") as f:
        text = pdf_parser.extract_text(f)
    prompt = prompt_template.build_user_prompt(text)
    summary = summarizer.generate_summary(prompt)
    print("\\n🔍 Generated Summary:")
    print(summary)
    assert "Parties Involved" in summary
