"""
Invariant checking functions for trace validation.

This module implements the core invariants that must hold true throughout
the execution of the governance system.
"""

from datetime import datetime
from typing import Dict, List, Any, Optional


class InvariantViolation(Exception):
    """Raised when an invariant is violated."""
    
    def __init__(self, invariant_name: str, message: str, event_id: Optional[str] = None):
        self.invariant_name = invariant_name
        self.message = message
        self.event_id = event_id
        super().__init__(f"{invariant_name}: {message}")


def check_chain_integrity(trace: Dict[str, Any]) -> List[Dict[str, Any]]:
    """
    Verify that the event chain is unbroken and valid.
    
    Each event (except the first) must reference the hash of the previous event.
    
    Args:
        trace: The trace object containing events
        
    Returns:
        List of violation dictionaries, empty if no violations
    """
    violations = []
    events = trace.get("events", [])
    
    if not events:
        return violations
    
    # First event should not have a previous_event_hash
    first_event = events[0]
    if "previous_event_hash" in first_event:
        violations.append({
            "invariant": "chain_integrity",
            "event_id": first_event["id"],
            "message": "First event should not have previous_event_hash"
        })
    
    # Check subsequent events
    for i in range(1, len(events)):
        current_event = events[i]
        previous_event = events[i - 1]
        
        if "previous_event_hash" not in current_event:
            violations.append({
                "invariant": "chain_integrity",
                "event_id": current_event["id"],
                "message": f"Event missing previous_event_hash"
            })
        elif current_event["previous_event_hash"] != previous_event["id"]:
            violations.append({
                "invariant": "chain_integrity",
                "event_id": current_event["id"],
                "message": f"Event hash chain broken: expected {previous_event['id']}, got {current_event.get('previous_event_hash')}"
            })
    
    return violations


def check_temporal_consistency(trace: Dict[str, Any]) -> List[Dict[str, Any]]:
    """
    Verify that event timestamps are monotonically increasing.
    
    Args:
        trace: The trace object containing events
        
    Returns:
        List of violation dictionaries, empty if no violations
    """
    violations = []
    events = trace.get("events", [])
    
    if len(events) < 2:
        return violations
    
    for i in range(1, len(events)):
        current_event = events[i]
        previous_event = events[i - 1]
        
        try:
            current_time = datetime.fromisoformat(current_event["timestamp"].replace("Z", "+00:00"))
            previous_time = datetime.fromisoformat(previous_event["timestamp"].replace("Z", "+00:00"))
            
            if current_time < previous_time:
                violations.append({
                    "invariant": "temporal_consistency",
                    "event_id": current_event["id"],
                    "message": f"Timestamp {current_event['timestamp']} is before previous timestamp {previous_event['timestamp']}"
                })
        except (KeyError, ValueError) as e:
            violations.append({
                "invariant": "temporal_consistency",
                "event_id": current_event.get("id", "unknown"),
                "message": f"Invalid timestamp format: {e}"
            })
    
    return violations


def check_signature_validity(trace: Dict[str, Any]) -> List[Dict[str, Any]]:
    """
    Verify that all events have valid signatures.
    
    Note: This is a structural check only. Full cryptographic verification
    would require the public keys and signature verification implementation.
    
    Args:
        trace: The trace object containing events
        
    Returns:
        List of violation dictionaries, empty if no violations
    """
    violations = []
    events = trace.get("events", [])
    
    for event in events:
        if "signature" not in event:
            violations.append({
                "invariant": "signature_validity",
                "event_id": event.get("id", "unknown"),
                "message": "Event missing signature"
            })
        elif not isinstance(event["signature"], str):
            violations.append({
                "invariant": "signature_validity",
                "event_id": event["id"],
                "message": "Signature is not a string"
            })
        elif len(event["signature"]) == 0:
            violations.append({
                "invariant": "signature_validity",
                "event_id": event["id"],
                "message": "Signature is empty"
            })
    
    return violations


def check_authorization_chain(trace: Dict[str, Any]) -> List[Dict[str, Any]]:
    """
    Verify that every action traces back to valid authorization.
    
    - Actions must have associated tokens
    - Tokens must have associated capsules
    - Token grants must occur before action attempts
    
    Args:
        trace: The trace object containing events
        
    Returns:
        List of violation dictionaries, empty if no violations
    """
    violations = []
    events = trace.get("events", [])
    
    capsules_created = set()
    tokens_granted = set()
    
    for event in events:
        event_type = event.get("event_type")
        
        # Track capsule creation
        if event_type == "capsule_created":
            if "capsule_hash" in event:
                capsules_created.add(event["capsule_hash"])
        
        # Track token grants and verify capsule exists
        elif event_type == "token_granted":
            capsule_hash = event.get("capsule_hash")
            token_hash = event.get("token_hash")
            
            if capsule_hash and capsule_hash not in capsules_created:
                violations.append({
                    "invariant": "authorization_chain",
                    "event_id": event["id"],
                    "message": f"Token granted without corresponding capsule: {capsule_hash}"
                })
            
            if token_hash:
                tokens_granted.add(token_hash)
        
        # Verify actions have authorization
        elif event_type in ["action_attempted", "action_completed"]:
            token_hash = event.get("token_hash")
            
            if not token_hash:
                violations.append({
                    "invariant": "authorization_chain",
                    "event_id": event["id"],
                    "message": "Action attempted without token"
                })
            elif token_hash not in tokens_granted:
                violations.append({
                    "invariant": "authorization_chain",
                    "event_id": event["id"],
                    "message": f"Action attempted with non-existent token: {token_hash}"
                })
    
    return violations


def check_sequence_numbers(trace: Dict[str, Any]) -> List[Dict[str, Any]]:
    """
    Verify that sequence numbers are consecutive and start from 0.
    
    Args:
        trace: The trace object containing events
        
    Returns:
        List of violation dictionaries, empty if no violations
    """
    violations = []
    events = trace.get("events", [])
    
    for i, event in enumerate(events):
        if "sequence" not in event:
            violations.append({
                "invariant": "sequence_numbers",
                "event_id": event.get("id", "unknown"),
                "message": "Event missing sequence number"
            })
        elif event["sequence"] != i:
            violations.append({
                "invariant": "sequence_numbers",
                "event_id": event["id"],
                "message": f"Expected sequence {i}, got {event['sequence']}"
            })
    
    return violations


def verify_trace(trace: Dict[str, Any]) -> Dict[str, Any]:
    """
    Verify that a trace satisfies all system invariants.
    
    Args:
        trace: The trace object to verify
        
    Returns:
        Dictionary with 'valid' boolean and 'violations' list
    """
    all_violations = []
    
    # Run all invariant checks
    all_violations.extend(check_chain_integrity(trace))
    all_violations.extend(check_temporal_consistency(trace))
    all_violations.extend(check_signature_validity(trace))
    all_violations.extend(check_authorization_chain(trace))
    all_violations.extend(check_sequence_numbers(trace))
    
    return {
        "valid": len(all_violations) == 0,
        "violations": all_violations,
        "checks_performed": [
            "chain_integrity",
            "temporal_consistency",
            "signature_validity",
            "authorization_chain",
            "sequence_numbers"
        ]
    }
