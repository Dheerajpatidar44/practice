"""
=============================================================================
Phase 8: Practical Project Implementation
Topic: Validating AI / LLM Output & LangGraph Integration Pattern
=============================================================================
LLMs (OpenAI GPT-4, Claude, Gemini) aksar JSON return karte waqt:
1. Markdown code fences add kar dete hain (```json ... ```).
2. Kabhi kabhi fields miss ya galat format me bhej dete hain.
Is file me hum dekhenge ki LangGraph / Agentic pipelines me LLM ke raw output
ko Pydantic se robustly kaise clean aur validate kiya jata hai.
"""

import json
import re
from pydantic import BaseModel, Field, ValidationError

# AI Generated Prompt Model
class VideoPromptOutput(BaseModel):
    positive_prompt: str = Field(min_length=20, description="Detailed scene description for video generator")
    negative_prompt: str = Field(default="blurry, distorted, low quality, artifacts, watermark")
    camera_angle: str = Field(pattern="^(eye_level|low_angle|high_angle|overhead)$")
    motion_speed: float = Field(ge=0.1, le=2.0, default=1.0)
    suggested_fps: int = Field(default=24)

# Robust parser function (used in LangGraph nodes)
def clean_and_parse_llm_json(raw_llm_text: str) -> VideoPromptOutput:
    """
    Step 1: Markdown code fences (```json ... ```) hatata hai.
    Step 2: Pydantic se validate karta hai.
    """
    # Regex se code block me se raw JSON extract karna
    match = re.search(r"```(?:json)?\s*([\s\S]*?)\s*```", raw_llm_text)
    clean_text = match.group(1) if match else raw_llm_text.strip()
    
    # Pydantic validation
    return VideoPromptOutput.model_validate_json(clean_text)


if __name__ == "__main__":
    print("=" * 60)
    print("1. Simulating RAW LLM Response (With Markdown Code Fences)")
    print("=" * 60)

    raw_ai_response = """
    Here is the video prompt you requested:
    ```json
    {
        "positive_prompt": "Cinematic slow motion shot of an astronaut looking at Earth from the Moon surface, hyper-realistic, 8k resolution",
        "negative_prompt": "blurry, dark, low quality",
        "camera_angle": "low_angle",
        "motion_speed": 0.5,
        "suggested_fps": 30
    }
    ```
    Hope this helps!
    """

    print("Raw LLM Output received:\n", raw_ai_response)
    
    # Parse and Validate:
    validated_prompt = clean_and_parse_llm_json(raw_ai_response)
    print("\nSuccessfully Parsed & Validated:")
    print(f"Positive Prompt : {validated_prompt.positive_prompt}")
    print(f"Camera Angle    : {validated_prompt.camera_angle}")
    print(f"Motion Speed    : {validated_prompt.motion_speed}x")
    print(f"FPS             : {validated_prompt.suggested_fps}")


    print("\n" + "=" * 60)
    print("2. Simulating Hallucinated / Invalid LLM Output")
    print("=" * 60)

    bad_ai_response = """
    ```json
    {
        "positive_prompt": "too short",
        "camera_angle": "crazy_angle_45_degrees",
        "motion_speed": 10.5
    }
    ```
    """

    try:
        clean_and_parse_llm_json(bad_ai_response)
    except ValidationError as e:
        print("LangGraph Agent catches this error and automatically sends a correction prompt to the LLM:")
        for err in e.errors():
            print(f"  - Issue with '{err['loc'][0]}': {err['msg']}")
