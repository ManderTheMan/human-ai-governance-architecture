"""
Oracle - Invariant verification for Human-AI Governance Architecture

This module provides tools for verifying that trace events satisfy system invariants.
"""

__version__ = "1.0.0"

from .invariants import (
    verify_trace,
    check_chain_integrity,
    check_temporal_consistency,
    check_signature_validity,
    check_authorization_chain,
    InvariantViolation
)

__all__ = [
    "verify_trace",
    "check_chain_integrity",
    "check_temporal_consistency",
    "check_signature_validity",
    "check_authorization_chain",
    "InvariantViolation"
]
