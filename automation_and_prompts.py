# Automation Script & Comprehensive Prompt Library

import json

def generate_alt_text_prompt(image_description, target_audience="screen reader users"):
    """Automates alt-text prompt draft creation for educational images."""
    prompt = (
        f"Act as an accessibility expert. Generate a concise, pedagogically relevant alt-text "
        f"description (under 150 characters) tailored for {target_audience}. "
        f"Image Details: {image_description}"
    )
    return prompt

PROMPT_LIBRARY = {
    "alt_text_generation": "Act as an accessibility expert. Create concise, descriptive alt-text for screen readers.",
    "wcag_summarization": "Summarize this WCAG standard into 3 clear, actionable bullet points for educators.",
    "hallucination_verification": "Verify the following AI-generated description against standard W3C guidelines and highlight any errors.",
    "caption_formatting": "Clean up this raw lecture transcript by adding punctuation, line breaks, and speaker labels."
}

if __name__ == "__main__":
    print("==================================================")
    print("--- Capstone 78 Automation & Prompt Engine ---")
    print("==================================================")
    
    print("\n[1] Loaded Prompt Library:")
    for key, val in PROMPT_LIBRARY.items():
        print(f"  * {key}: {val}")
    
    print("\n[2] Executing Automation Workflow Demo:")
    sample_image = "A biology professor explaining a DNA double helix diagram on a digital screen."
    generated_prompt = generate_alt_text_prompt(sample_image)
    
    print("  Input Image Context:", sample_image)
    print("  Generated AI Prompt:", generated_prompt)
    print("\n==================================================")
    print("--- Demo Execution Completed Successfully ---")
    print("==================================================")
