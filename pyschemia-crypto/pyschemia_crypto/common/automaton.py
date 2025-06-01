"""
Cryptographic Primitive Automaton Implementation

Implements the finite state automaton model defined in Section 4 
of the OBINexus Cryptographic Interoperability Standard v1.0.
"""

from enum import Enum
from abc import ABC, abstractmethod
from typing import Pattern, Set, Dict, Any
import re

class ValidationResult(Enum):
    """Validation results per OBINexus Standard Section 2.1."""
    ACCEPT_VALIDATED = "accept_validated"
    ACCEPT_SINGLE_MATCH = "accept_single_match"
    ACCEPT_CANONICAL_RESOLUTION = "accept_canonical_resolution"
    ACCEPT_LEGACY_CONTEXT = "accept_legacy_context"
    REJECT_UNKNOWN_PATTERN = "reject_unknown_pattern"
    REJECT_DEPRECATED_SECURITY = "reject_deprecated_security"
    REJECT_CONTEXT_VIOLATION = "reject_context_violation"
    REJECT_INCOMPATIBLE_VERSION = "reject_incompatible_version"

class PatternEnforcer(ABC):
    """
    Abstract base class for cryptographic pattern enforcement.
    
    Implements mandatory if/else control logic per OBINexus Section 2.1.
    """
    
    @abstractmethod
    def enforce_primitive_pattern(self, 
                                primitive_digest: str, 
                                context: str) -> ValidationResult:
        """
        Mandatory pattern enforcement for cryptographic primitives.
        
        Args:
            primitive_digest: Raw primitive digest string
            context: Operational context for validation
            
        Returns:
            ValidationResult indicating acceptance or rejection
        """
        pass
    
    @abstractmethod
    def get_canonical_pattern(self) -> Pattern:
        """Return canonical regex pattern for this primitive."""
        pass
    
    @abstractmethod
    def get_security_level(self) -> str:
        """Return security level: legacy, stable, or experimental."""
        pass
