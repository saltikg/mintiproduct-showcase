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

