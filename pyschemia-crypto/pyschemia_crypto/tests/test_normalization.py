"""
Unicode Normalization Testing

Validates USCN implementation per OBINexus Standard v1.0 Section 4.
"""

import pytest
from pyschemia_crypto.common.normalize import normalize_primitive_input

class TestNormalization:
    """Test isomorphic reduction implementation."""
    
    @pytest.mark.parametrize("input_variant,expected_canonical", [
        ("rsa-3072:abc123", "RSA-3072:ABC123"),
        ("RSA_3072:abc123", "RSA-3072:ABC123"), 
        ("rsa3072:abc123", "RSA-3072:ABC123"),
        ("RSA-3072:0xabc123", "RSA-3072:ABC123"),
        ("  rsa-3072:abc123  ", "RSA-3072:ABC123"),
    ])
    def test_canonical_normalization(self, input_variant, expected_canonical):
        """Test canonical mapping function φ(ei) = c."""
        result = normalize_primitive_input(input_variant)
        assert result == expected_canonical
    
    def test_security_invariant(self):
        """Test security invariant: validate(normalize(s)) ≡ validate(canonical(s))."""
        from pyschemia_crypto.stable.rsa_3072.pattern import PatternEnforcer
        
        enforcer = PatternEnforcer()
        
        # Test with encoding variations
        variants = [
            "RSA-3072:" + "a" * 768,
            "rsa-3072:" + "a" * 768,
            "RSA_3072:" + "a" * 768,
        ]
        
        results = []
        for variant in variants:
            normalized = normalize_primitive_input(variant)
            result = enforcer.enforce_primitive_pattern(normalized, "audit_verification")
            results.append(result)
        
        # All variants should produce identical results
        assert len(set(results)) == 1
        assert results[0] == ValidationResult.ACCEPT_VALIDATED
