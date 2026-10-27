"""
=============================================================================
Phase 8: Practical Project Implementation
Topic: Script Analysis, Scene & Shot Models for AI Video Generation
=============================================================================
AI Video Generation pipelines (jaise Video Prompt Agents) me script ko analyze
karke scenes aur camera shots me break kiya jata hai.
Pydantic models ensure karte hain ki AI/LLM ka generated data strictly
structured aur valid ho.
"""

from enum import Enum
from typing import Optional
from pydantic import BaseModel, Field

# 1. Enums for Allowed Values (Strict Choices)
class ShotType(str, Enum):
    WIDE = "wide_shot"
    MEDIUM = "medium_shot"
    CLOSE_UP = "close_up"
    EXTREME_CLOSE_UP = "extreme_close_up"

class CameraMovement(str, Enum):
    STATIC = "static"
    PAN = "pan"
    TILT = "tilt"
    ZOOM = "zoom"
    TRACKING = "tracking"

# 2. Shot Model (Har individual camera shot)
class ShotModel(BaseModel):
    shot_id: int
    shot_type: ShotType
    camera_movement: CameraMovement = CameraMovement.STATIC
    prompt_description: str = Field(min_length=10, description="AI video generator (Runway/Sora) prompt")
    duration_seconds: float = Field(gt=0, le=30.0, description="Shot duration (max 30s)")

# 3. Scene Model (Ek scene jisme multiple shots hote hain)
class SceneModel(BaseModel):
    scene_number: int
    location: str
    time_of_day: str  # "Day", "Night", "Golden Hour"
    mood: str
    shots: list[ShotModel] = Field(min_length=1, description="Scene me kam se kam 1 shot hona chahiye")

    @property
    def scene_duration(self) -> float:
        return sum(shot.duration_seconds for shot in self.shots)

# 4. Top-Level Script Analysis Model
class ScriptAnalysis(BaseModel):
    project_title: str
    genre: str
    target_aspect_ratio: str = Field(default="16:9")
    scenes: list[SceneModel] = Field(min_length=1)

    @property
    def total_shots(self) -> int:
        return sum(len(scene.shots) for scene in self.scenes)

    @property
    def total_runtime_seconds(self) -> float:
        return sum(scene.scene_duration for scene in self.scenes)


# ---------------------------------------------------------------------------
# Demonstration
# ---------------------------------------------------------------------------
if __name__ == "__main__":
    print("=" * 60)
    print("Parsing Complete AI Video Production Script")
    print("=" * 60)

    ai_generated_script_data = {
        "project_title": "Cyberpunk Detective: The Missing Code",
        "genre": "Sci-Fi Noir",
        "target_aspect_ratio": "16:9",
        "scenes": [
            {
                "scene_number": 1,
                "location": "Rainy Neon Alleyway, Neo-Tokyo",
                "time_of_day": "Night",
                "mood": "Mysterious & Gritty",
                "shots": [
                    {
                        "shot_id": 1,
                        "shot_type": "wide_shot",
                        "camera_movement": "tracking",
                        "prompt_description": "Cinematic wide shot of a detective walking slowly down a rain-soaked neon alley, puddles reflecting magenta and cyan signs, 4k ultra-detailed.",
                        "duration_seconds": 4.5
                    },
                    {
                        "shot_id": 2,
                        "shot_type": "close_up",
                        "camera_movement": "static",
                        "prompt_description": "Extreme close-up on detective's wet mechanical cybernetic eye flickering with data, shallow depth of field.",
                        "duration_seconds": 3.0
                    }
                ]
            },
            {
                "scene_number": 2,
                "location": "High-tech Underground Server Room",
                "time_of_day": "Night",
                "mood": "Tense & Suspenseful",
                "shots": [
                    {
                        "shot_id": 3,
                        "shot_type": "medium_shot",
                        "camera_movement": "zoom",
                        "prompt_description": "Slow zoom in on an open server rack with glowing blue optical cables being unplugged by an unseen figure.",
                        "duration_seconds": 5.0
                    }
                ]
            }
        ]
    }

    script = ScriptAnalysis.model_validate(ai_generated_script_data)

    print(f"Project Title  : {script.project_title}")
    print(f"Genre          : {script.genre}")
    print(f"Aspect Ratio   : {script.target_aspect_ratio}")
    print(f"Total Scenes   : {len(script.scenes)}")
    print(f"Total Shots    : {script.total_shots}")
    print(f"Total Duration : {script.total_runtime_seconds} seconds")
    print("-" * 60)

    for scene in script.scenes:
        print(f"\n[Scene {scene.scene_number}] - {scene.location} ({scene.time_of_day}) | Mood: {scene.mood}")
        for shot in scene.shots:
            print(f"  * Shot {shot.shot_id} ({shot.shot_type.value}, {shot.camera_movement.value}, {shot.duration_seconds}s):")
            print(f"    Prompt: {shot.prompt_description}")
