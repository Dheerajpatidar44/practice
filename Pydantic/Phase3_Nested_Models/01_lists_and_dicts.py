"""
=============================================================================
Phase 3: Lists, Dictionaries & Nested Models
Topic: Lists, Dictionaries, Sets & Tuples in Models
=============================================================================
Pydantic standard Python collections ko deeply validate karta hai:
- list[str]: Har element string hona zaroori hai.
- dict[str, float]: Keys string aur values float honi chahiye.
- set[str]: Duplicates automatically remove ho jate hain.
"""

from pydantic import BaseModel, Field

class DeveloperProfile(BaseModel):
    name: str
    skills: list[str] = Field(default_factory=list)
    project_scores: dict[str, float] = Field(default_factory=dict)
    certifications: set[str] = Field(default_factory=set)

print("=" * 60)
print("1. Valid Developer Profile with Collections")
print("=" * 60)

raw_data = {
    "name": "Dheeraj",
    "skills": ["Python", "OpenCV", "Pydantic", "FastAPI"],
    "project_scores": {
        "Phase1_OpenCV": 95.5,
        "Phase8_FaceDetection": 98.0
    },
    # Set me duplicate "AWS" pass kiya -> Pydantic automatic unique karega
    "certifications": ["AWS", "Docker", "AWS"]
}

dev = DeveloperProfile(**raw_data)
print("Developer:", dev)
print(f"Skills Count: {len(dev.skills)}")
print(f"Unique Certifications: {dev.certifications}")
print(f"OpenCV Score: {dev.project_scores['Phase1_OpenCV']}")


print("\n" + "=" * 60)
print("2. Type Coercion Inside Lists & Dicts")
print("=" * 60)

# Notice: scores me string numbers diye hain ("90", "88.5")
# Pydantic list aur dict ke har item ko float me coerce karega!
dev2 = DeveloperProfile(
    name="Rahul",
    skills=["HTML", "CSS"],
    project_scores={"frontend": "90", "backend": "88.5"}
)

print("Developer 2 project_scores:", dev2.project_scores)
print("frontend score type:", type(dev2.project_scores["frontend"]))
