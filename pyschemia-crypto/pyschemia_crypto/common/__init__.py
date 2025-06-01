"""
Common cryptographic infrastructure components.
"""

from .automaton import ValidationResult, PatternEnforcer
from .normalize import normalize_primitive_input
from .audit import SecureAuditNode

__all__ = [
    "ValidationResult",
    "PatternEnforcer", 
    "normalize_primitive_input",
    "SecureAuditNode"
]
