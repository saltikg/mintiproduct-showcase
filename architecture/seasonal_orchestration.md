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

