from app.config import llm
from app.prompts.system_prompt import EXTRACTION_PROMPT_TEMPLATE, DIET_PROMPT_TEMPLATE

def analyze_blood_work(blood_report: str) -> tuple[str, str]:
    """Executes the two-stage LLM pipeline dynamically on button click."""
    
    # Stage 1: Extract and flag abnormal values
    extraction_prompt = EXTRACTION_PROMPT_TEMPLATE.format(blood_report=blood_report)
    extraction_response = llm.invoke(extraction_prompt)
    extracted_values = extraction_response.content 

    # Stage 2: Health summary and Indian diet plan
    diet_prompt = DIET_PROMPT_TEMPLATE.format(extracted_values=extracted_values)
    diet_response = llm.invoke(diet_prompt)
    full_response = diet_response.content

    # Dynamic parsing logic
    if "SECTION 2" in full_response:
        parts = full_response.split("SECTION 2")
        health_summary = parts[0].replace("SECTION 1 - HEALTH SUMMARY:", "").replace("SECTION 1", "").strip()
        diet_plan = ("SECTION 2" + parts[1]).replace("SECTION 2 - INDIAN DIET PLAN:", "").replace("SECTION 2", "").strip()
    else:
        health_summary = full_response
        diet_plan = ""
        
    return health_summary, diet_plan