"""
Unicode-Only Structural Charset Normalizer (USCN) Implementation

Implements isomorphic reduction principles from Section 4 of the 
OBINexus Cryptographic Interoperability Standard v1.0.
"""

import re
from typing import Dict, Pattern

# Encoding mappings for canonical normalization
ENCODING_MAPPINGS: Dict[str, str] = {
    # Case variations
    "_": "-",
    
    # Common delimiter standardization
    " ": "",
    "\t": "",
    "\n": "",
    
    # Hex prefix removal
    "0x": "",
    "0X": "",
}

def normalize_primitive_input(input_string: str) -> str:
    """
    Apply USCN normalization to eliminate encoding variations.
    
    Implements the canonical mapping function φ(ei) = c where all 
    semantically equivalent patterns reduce to a single canonical form.
    
    Args:
        input_string: Raw primitive input with potential encoding variations
        
    Returns:
        Normalized canonical form following OBINexus standard
    """
    if not input_string:
        return input_string
    
    normalized = input_string.strip()
    
    # Phase 1: Decode common encoding variations
    for encoding_variant, canonical in ENCODING_MAPPINGS.items():
        normalized = normalized.replace(encoding_variant, canonical)
    
    # Phase 2: Case normalization for algorithm names
    if ":" in normalized:
        algorithm, digest = normalized.split(":", 1)
        algorithm = algorithm.upper()
        
        # Phase 3: Hex string normalization
        if is_hex_string(digest):
            digest = digest.upper()
        
        normalized = f"{algorithm}:{digest}"
    
    # Phase 4: Delimiter standardization
    normalized = standardize_delimiters(normalized)
    
    return normalized

def is_hex_string(s: str) -> bool:
    """Check if string contains only hexadecimal characters."""
    if not s:
        return False
    return bool(re.match(r'^[a-fA-F0-9]+$', s))

def standardize_delimiters(s: str) -> str:
    """Standardize delimiter formatting for canonical representation."""
    # Ensure consistent hyphen usage in algorithm names
    s = re.sub(r'([A-Z]+)[-_]?(\d+)', r'\1-\2', s)
    return s
