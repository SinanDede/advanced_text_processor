"""
Subpackage: data_tools

Contains dataset-level utilities built using only Python built-ins.
These modules extend the base text processing library with:
- Statistical summarization
- Fuzzy dataset merging
- Class-balanced splitting
- Versioned dataset storage
- Anomaly detection
"""

from .summarize import summarize_table
from .fuzzy_merge import fuzzy_merge
from .balanced_split import balanced_split
from .versioned_manager import save_version, load_version
from .anomalies import detect_anomalies

__all__ = [
    "summarize_table",
    "fuzzy_merge",
    "balanced_split",
    "save_version",
    "load_version",
    "detect_anomalies",
]

