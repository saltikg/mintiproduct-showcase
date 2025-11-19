# Instagram Reels Generation Flow (MintiProduct)

This document describes the high-level workflow responsible for 
automatically generating vertical 1080x1920 Instagram Reels using product images, 
a background template, and text overlays.

---

## 1. Inputs

### Product Data
- 5 product images per reel
- Titles and pricing info
- CTA text (e.g., “Tap to Shop”)
- Affiliate URLs (not included here)

### Background Assets
- Static background image (1920x1080 or 1080x1920)
- Optional logo or watermark
- Color theme depending on season

### Settings
- Duration per image (2–3 seconds)
- Transition type
- FPS (typically 30)
- Output format: MP4 (H.264)

---

## 2. Pipeline Overview

Select Products → Prepare Assets → Resize & Crop → Overlay Text →
Assemble Clips → Add Transitions → Export MP4


---

## 3. Stages

### Stage 1: Prepare Assets
- Download product images
- Convert to RGB
- Uniform sizing for vertical ratio (1080x1920)
- Handle aspect ratios via:
  - letterboxing
  - background blur
  - centered cropping

### Stage 2: Text Overlay
- Add:
  - title
  - price
  - CTA button
- Use PIL or OpenCV
- Apply safe fonts (no license issues)
- Ensure readability on bright/dark products

### Stage 3: Clip Assembly
- Combine frames into short video clips
- Add transitions (crossfade or slide)
- Use FFmpeg filters:
  - `fade=t=in`
  - `xfade=transition`

### Stage 4: Final Rendering
- Combine all clips into a single vertical 1080x1920 video
- Add music track (optional)
- Encode using:

ffmpeg -i input -vf scale=1080:1920 -r 30 -preset veryfast -c:v libx264 output.mp4


### Stage 5: Save & Upload
- Write file into `instagram_out/`
- Mark video as generated in DuckDB
- Optionally upload using Instagram Graph API (Production only)

---

## 4. Notes

This document provides a **safe and simplified** overview.  
The real implementation includes:
- job orchestration
- FFmpeg concurrency controls
- auto product ranking
- image quality scoring
- retry logic
- Instagram upload pipeline

These remain private in the production repo.





