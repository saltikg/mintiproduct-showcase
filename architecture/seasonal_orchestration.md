# Seasonal Orchestration Engine (MintiProduct)

This document describes the high-level workflow that powers seasonal content
automation in MintiProduct. It coordinates ingestion, trend scoring, content
generation, and publishing pipelines based on upcoming seasonal events.

---

## 1. Purpose

Seasonal behavior (Mother’s Day, Black Friday, Winter Holidays, etc.) generates clear
consumer intent patterns. The seasonal engine is designed to:

- detect emerging seasonal trends early,
- produce content ideas aligned with high-intent periods,
- schedule LLM generation jobs before the peak,
- regenerate outdated content automatically,
- orchestrate reels/blog posts for each season.

This ensures that the system stays *ahead* of demand.

---

## 2. Inputs

### Seasonal Metadata
Stored in DuckDB:
- `season_id`
- `name`
- `start_date`, `peak_date`, `end_date`
- associated keywords
- historical performance scores

### External Signals
- Google Trends (season-specific queries)
- YouTube transcripts mentioning seasonal concepts
- Product catalog metadata (seasonally relevant items)

---

## 3. Workflow Overview
Daily Cron → Seasonal Detector → Trend Ingestion → Embedding Refresh →
Relevance Scoring → Idea Generation → Priority Queue → Content Jobs


---

## 4. Stages

### Stage 1: Seasonal Detector (Daily)
- Looks 60–90 days ahead
- Identifies upcoming seasons
- Loads seasonal keyword lists
- Initializes job queue for that season

### Stage 2: Seasonal Trend Ingestion
- Filters Google Trends + YouTube transcripts using seasonal keywords
- Stores raw & cleaned text into DuckDB
- Normalizes seasonal weights

### Stage 3: Embedding Refresh
- Generates embeddings for season-specific text chunks
- Stores in FAISS or DuckDB vector columns
- Marks outdated embeddings for cleanup

### Stage 4: Relevance Scoring
Score components:
- recency (freshness)
- frequency spikes
- semantic similarity to seasonal keywords
- uniqueness score to avoid duplication

Output:
- ranked seasonal ideas

### Stage 5: Idea Generation (LLM)
- Converts top-ranked ideas into:
  - blog titles
  - short-form angles
  - seasonal hooks
- Produces 10–30 ideas per season

### Stage 6: Priority Queue
Each idea receives:
- score
- urgency level (based on days until peak)
- required assets (blog, reel, or both)

### Stage 7: Content Jobs (Automated)
For each item:
- Blog generation job (LLM → product enrichment → template assembly)
- Reel generation job (FFmpeg/OpenCV)
- Auto-publish or manual review option

Output is written to:
- `/blogs/seasonal/<season-slug>/`
- `/instagram_out/<season-slug>/`

---

## 5. Scheduling & Automation

Jobs run on a mix of:
- cron-based triggers
- dependency-based triggers (e.g., embeddings must be refreshed first)
- on-demand tasks from the admin panel

Examples:
- Daily trend refresh (04:00 UTC)
- Embedding refresh (06:00 UTC)
- Idea regeneration (weekly)
- Content refresh (every 30 days)

---

## 6. Notes

This file contains a **safe, simplified** outline.  
Production orchestration includes:
- concurrency locks  
- backpressure handling for LLM tokens  
- asset-level retry logic  
- seasonal performance scoring  
- webhook-based publish triggers  

These remain private in the main MintiProduct codebase.



