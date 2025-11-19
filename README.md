# MintiProduct Showcase

This repository presents the high level architecture, workflows, and selected safe code samples from the MintiProduct system.

MintiProduct is a Python/Flask/DuckDB-based content automation platform that:
- fetches Google Trends and YouTube transcripts
- generates seasonal and affiliate-ready blog ideas using LLMs
- builds dynamic product blogs
- produces Instagram Reels using FFmpeg / OpenCV
- stores analytical data in DuckDB
- runs a full backend admin panel on Lightsail

## What's included in this repository

This showcase repo contains **safe** and **non-production** examples:

### Architecture
High-level diagrams and explanations of:
- Trend ingestion workflow
- Seasonal orchestration engine
- Content generation pipeline (LLM-based)
- Instagram Reel generation flow
- DuckDB analytical layer

### Examples
Lightweight and anonymized code samples for:
- YouTube transcript parsing (safe version)
- Simple FAISS embedding example
- Example trend ranking logic
- Sample blog idea scoring function

### Utils
Utility functions that do not expose production logic:
- text cleaning
- safe prompt templates
- date/time helpers

### Notebooks
Jupyter notebooks showing:
- exploratory analysis using DuckDB
- sample embedding workflows
- content idea generation demos

## Important Note
This repository **does not include** the private production code of MintiProduct.
All sensitive or proprietary components remain private.
