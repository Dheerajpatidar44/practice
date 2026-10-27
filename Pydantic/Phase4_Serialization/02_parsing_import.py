"""
=============================================================================
Phase 4: Model Serialization & Deserialization
Topic: Parsing Data with model_validate() and model_validate_json()
=============================================================================
External data ko Pydantic model me load karne ke liye:
- Model.model_validate(obj): Python dictionary ya object ko validate karke model banata hai.
- Model.model_validate_json(json_str): Direct raw JSON STRING ko validate karke model banata hai
  (Ye json.loads() se bohot zyada fast aur optimized hota hai).
"""

from pydantic import BaseModel

class VideoMetadata(BaseModel):
    video_id: str
    title: str
    duration_seconds: int
    resolution: str
    views: int = 0

print("=" * 60)
print("1. model_validate() from Python Dictionary")
print("=" * 60)

db_record = {
    "video_id": "VID_2026_01",
    "title": "OpenCV & Computer Vision Masterclass",
    "duration_seconds": 1250,
    "resolution": "1920x1080",
    "views": 4500
}

video_1 = VideoMetadata.model_validate(db_record)
print("Validated from Dict:", video_1)
print(f"Title: {video_1.title}, Duration: {video_1.duration_seconds}s")


print("\n" + "=" * 60)
print("2. model_validate_json() from Raw JSON String")
print("=" * 60)

# Maan lijiye ye string kisi external REST API ya LLM se aayi hai:
raw_json_string = """
{
    "video_id": "VID_2026_02",
    "title": "Pydantic V2 Complete Guide",
    "duration_seconds": 780,
    "resolution": "3840x2160",
    "views": 8200
}
"""

video_2 = VideoMetadata.model_validate_json(raw_json_string)
print("Validated from JSON String:", video_2)
print(f"Title: {video_2.title}, Resolution: {video_2.resolution}")
