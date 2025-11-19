# MintiProduct – Architecture Overview (Showcase)

This document provides a high-level, safe description of the overall system design of MintiProduct, 
a full-stack content automation engine built on Python, Flask, DuckDB, and multiple ML/LLM workflows.

---

## 1. System Goals

MintiProduct is designed to:
- detect trends from external data sources,
- generate shopping-oriented content using LLMs,
- assemble SEO-ready blogs automatically,
- create vertical Instagram Reels using FFmpeg,
- manage seasonal content pipelines,
- run efficiently on a lightweight cloud environment (AWS Lightsail).

All sensitive production code remains private. This is a non-sensitive architectural overview.

---

## 2. High-Level Architecture

External Data → Ingestion Pipeline → DuckDB Warehouse → ML/LLM Layer →
Content Generators → Admin Panel (Flask) → Publishing System


### Components:
- **Ingestion Services**  
  Fetch data from Google Trends, YouTube captions, and product sources.

- **Processing & Embeddings**  
  Clean text, chunk, embed using FAISS (vector search).

- **Trend Ranking Engine**  
  Scores trends by relevance, recency, and semantic similarity.

- **LLM Content Generator**  
  Produces draft blogs, product sections, and short-form variations.

- **Instagram Reel Generator**  
  Creates 1080x1920 MP4 reels using product images + background templates.

- **DuckDB Warehouse**  
  Stores:
  - raw ingestion tables  
  - cleaned text  
  - embeddings  
  - content metadata  
  - publishing logs  

- **Flask Admin Panel**  
  UI to trigger:
  - trend updates  
  - idea generation  
  - content creation  
  - reel generation  
  - seasonal orchestration  

- **Publishing Layer**  
  Generates pages, updates sitemaps, writes content to storage.

---

## 3. Data Storage

### DuckDB (primary warehouse)
Tables include:
- `trends_raw`
- `trends_clean`
- `trend_embeddings`
- `trend_ideas`
- `blogs`
- `products`
- `instagram_reels`

Features:
- columnar analytic performance  
- fast vector operations  
- zero-dependency storage  
- great for a one-machine content engine  

---

## 4. ML / LLM Layer

Functions:
- idea generation  
- similarity search  
- reranking  
- scrubbing hallucinations  
- assembling structured blog templates  

LLM prompts enforce:
- factual grounding  
- shopping-oriented outputs  
- tone consistency  
- modular sections  

---

## 5. Automation & Scheduling

Tasks:
- daily Google Trends pull  
- hourly YouTube transcript ingestion  
- seasonal content refresh  
- nightly embedding regeneration  
- expired content cleanup  
- sitemap rebuild  

All orchestrated via lightweight cron + Python jobs.

---

## 6. Deployment Model

- Hosted on **AWS Lightsail**
- Reverse-proxy using Nginx
- Flask app served via Gunicorn
- Static assets served directly by Nginx
- All code & data on a small but optimized instance

---

## 7. Security & Privacy Notes

This document is a **safe overview**.  
Production system includes:
- private API keys  
- concurrency locks  
- affiliate logic  
- embedding storage  
- admin authentication  
- rate-limited ingestion  

These are **not shared** in this public repo.

---



