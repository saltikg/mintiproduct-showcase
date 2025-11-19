# Content Generation Pipeline (MintiProduct)

This document describes the high-level design of the content creation pipeline 
that converts trend signals into full affiliate-ready blog posts, short-form reels, 
and seasonal content pieces.

---

## 1. Inputs

### Trend Signals
- Google Trends (hourly)
- YouTube transcripts
- Seasonal keywords
- Product catalogs (affiliate sources)

### Metadata
- Category & subcategory
- Seasonal context (Winter, Black Friday, Mother's Day)
- Ranking scores
- Deduplication signals

---

## 2. Pipeline Overview

The flow consists of several stages:
Trend Signal → Preprocessing → Embedding → Relevance Scoring →
Idea Generation → Draft Creation → Blog Assembly → Publish


---

## 3. Stage Details

### Stage 1: Preprocessing
- Clean text
- Remove noise
- Standardize structure
- Optional: merge related signals

### Stage 2: Embedding & Retrieval
- Convert text chunks into embeddings
- Use FAISS (production) or DuckDB vectors (light mode)
- Retrieve top-k relevant chunks

### Stage 3: Idea Generation (LLM)
- Prompt templates:
  - intent: "create a shopping-oriented angle"
  - constraints: "no hallucination", "based on chunks only"
- Output:
  - idea title
  - angle/insight summary
  - category tag  

### Stage 4: Draft Creation (LLM)
- Structured prompt producing:
  - intro paragraph
  - 3–7 product card sections
  - optional short-form version for reels
- Style control:
  - SEO friendly
  - high-engagement tone
  - short sentences

### Stage 5: Product Enrichment
- Query affiliate API (eBay, Amazon)
- Select 5 top products
- Add:
  - title
  - price
  - short bullet descriptions
  - CTA links

### Stage 6: Blog Assembly
- Jinja2 template in Flask
- HTML + CSS
- Responsive product grid
- Automatic table of contents
- Schema markup (SEO)

### Stage 7: Publishing
- Write to database
- Generate unique slug
- Add to sitemap
- Upload images
- Clear any caches

---

## 4. Safety & Privacy Notes

This document includes *safe* descriptions only.  
Production features not included here:
- concurrency locks
- full prompt templates
- affiliate monetization layer
- YouTube API rate control
- embedding storage system
- seasonal orchestration logic

These remain in the private repository.

---

