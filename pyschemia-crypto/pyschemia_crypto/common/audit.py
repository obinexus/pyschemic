"""
Secure Audit Trail Implementation

Implements Section 6 of the OBINexus Cryptographic Interoperability 
Standard v1.0 for secure pattern hash references and audit compliance.
"""

import hashlib
from datetime import datetime
from dataclasses import dataclass
from typing import Dict, Any, Optional

@dataclass
class SecureAuditNode:
    """
    Secure audit trail node for primitive operations.
    
    Prevents information disclosure while maintaining audit integrity 
    per OBINexus Section 6.1.
    """
    
    timestamp: datetime
    primitive_hash: str
    pattern_hash: str
    operation_context: str
    compliance_level: str = "OBINexus-v1.0"
    
    @classmethod
    def create_audit_entry(cls, 
                          primitive_digest: str, 
                          pattern: str,
                          context: str) -> 'SecureAuditNode':
        """
        Create audit entry with secure hash references.
        
        Args:
            primitive_digest: Raw primitive digest (never stored)
            pattern: Regex pattern (never stored)
            context: Operational context
            
        Returns:
            SecureAuditNode with hashed references
        """
        primitive_hash = hashlib.sha256(primitive_digest.encode()).hexdigest()[:16]
        pattern_hash = hashlib.sha256(pattern.encode()).hexdigest()[:16]
        
        return cls(
            timestamp=datetime.utcnow(),
            primitive_hash=f"PRIM_{primitive_hash}",
            pattern_hash=f"PAT_{pattern_hash}",
            operation_context=context
        )
    
    def to_audit_record(self) -> Dict[str, Any]:
        """
        Generate compliant audit record per OBINexus Section 6.2.
        
        Returns:
            Dictionary conforming to mandatory audit record format
        """
        return {
            "timestamp": self.timestamp.isoformat(),
            "primitive_ref": self.primitive_hash,
            "pattern_ref": self.pattern_hash,
            "context": self.operation_context,
            "compliance_level": self.compliance_level
        }
    
    def verify_integrity(self, 
                        original_digest: str, 
                        original_pattern: str) -> bool:
        """
        Verify audit trail integrity against original values.
        
        Args:
            original_digest: Original primitive digest for verification
            original_pattern: Original pattern for verification
            
        Returns:
            True if audit hashes match original values
        """
        expected_primitive = f"PRIM_{hashlib.sha256(original_digest.encode()).hexdigest()[:16]}"
        expected_pattern = f"PAT_{hashlib.sha256(original_pattern.encode()).hexdigest()[:16]}"
        
        return (self.primitive_hash == expected_primitive and 
                self.pattern_hash == expected_pattern)
