
# Trend Ingestion Flow (MintiProduct)

This document describes the high-level workflow for collecting and transforming 
trend signals from external sources such as Google Trends and YouTube video transcripts.

---

## 1. Sources

### Google Trends
- Hourly interest-over-time data
- Query list comes from seasonal topics and evergreen categories
- Fetched via the `pytrends` API
- Stored as raw JSON for reproducibility

### YouTube Transcripts
- Fetched using the YouTube Data API
- Captions parsed into structured text
- Noise removed (music tags, timestamps, repeated words)

---

## 2. Ingestion Pipeline

### Step 1: Fetch
- A scheduler (cron or Python job) fetches new data
- API responses logged and timestamped
- Rate limits handled with exponential backoff

### Step 2: Clean & Normalize
- Standardize text
- Remove stopwords and repetition
- Normalize casing and unicode characters

### Step 3: Chunking
- Split long transcripts into semantic chunks
- Prepare for embeddings and content generation

### Step 4: Embedding (Safe Example)
- Convert chunks to vector embeddings (FAISS in production)
- Store in DuckDB for fast retrieval

### Step 5: Ranking & Scoring
- Lightweight scoring based on:
  - recency
  - frequency
  - semantic relevance to seasonal topics
  - uniqueness

### Step 6: Write to DuckDB
Tables include:
- `trends_raw`
- `trends_clean`
- `trend_embeddings`
- `trend_ideas`

---

## 3. Output

- A ranked list of trend ideas
- Ready to be used by:
  - seasonal idea generators
  - blog generation agents
  - Instagram reel scripts
  - YouTube product inspiration workflows

---

## 4. Notes

This document is a **safe showcase** version.  
The production implementation includes:
- concurrency control
- full embedding pipeline
- duplicate idea prevention
- private affiliate logic
and remains in the private repository.
