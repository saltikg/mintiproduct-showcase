"""
Date & Time Utilities (Safe Version)

Lightweight helpers for formatting, parsing, and normalizing timestamps.
Used across ingestion pipelines, scheduling logic, and content generation.

This is a simplified and safe subset of the production utilities.
"""

from datetime import datetime, timedelta
import pytz


def now_utc() -> datetime:
    """Return current UTC datetime."""
    return datetime.now(pytz.utc)


def to_iso(dt: datetime) -> str:
    """Convert datetime to ISO 8601 string."""
    return dt.astimezone(pytz.utc).isoformat()


def parse_iso(s: str) -> datetime:
    """Parse an ISO8601 timestamp."""
    return datetime.fromisoformat(s.replace("Z", "+00:00"))


def days_ago(days: int) -> datetime:
    """Get datetime of N days ago."""
    return now_utc() - timedelta(days=days)


def humanize(dt: datetime) -> str:
    """Return human-readable timing (e.g., '3 hours ago')."""
    delta = now_utc() - dt

    if delta.days > 0:
        return f"{delta.days} days ago"
    hours = delta.seconds // 3600
    if hours > 0:
        return f"{hours} hours ago"
    minutes = (delta.seconds % 3600) // 60
    return f"{minutes} minutes ago"
