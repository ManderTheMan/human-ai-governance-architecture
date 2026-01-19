"""
Tests for trace validation using example traces.
"""

import json
import os
from pathlib import Path
import pytest

from oracle.invariants import (
    verify_trace,
    check_chain_integrity,
    check_temporal_consistency,
    check_signature_validity,
    check_authorization_chain,
    check_sequence_numbers
)


# Get the examples directory
EXAMPLES_DIR = Path(__file__).parent.parent / "examples"


def load_example(filename: str):
    """Load an example trace file."""
    filepath = EXAMPLES_DIR / filename
    with open(filepath, 'r') as f:
        return json.load(f)


class TestGoldenPath:
    """Test the golden path example."""
    
    def test_golden_path_valid(self):
        trace = load_example("golden-path.json")
        result = verify_trace(trace)
        assert result["valid"], f"Golden path should be valid, violations: {result['violations']}"
    
    def test_golden_path_chain_integrity(self):
        trace = load_example("golden-path.json")
        violations = check_chain_integrity(trace)
        assert len(violations) == 0, f"Chain integrity violations: {violations}"
    
    def test_golden_path_temporal_consistency(self):
        trace = load_example("golden-path.json")
        violations = check_temporal_consistency(trace)
        assert len(violations) == 0, f"Temporal consistency violations: {violations}"


class TestWET1Trace:
    """Test the WET-1 trace example."""
    
    def test_wet1_valid(self):
        trace = load_example("wet-1-trace.json")
        result = verify_trace(trace)
        assert result["valid"], f"WET-1 should be valid, violations: {result['violations']}"
    
    def test_wet1_authorization_chain(self):
        trace = load_example("wet-1-trace.json")
        violations = check_authorization_chain(trace)
        assert len(violations) == 0, f"Authorization chain violations: {violations}"
    
    def test_wet1_sequence_numbers(self):
        trace = load_example("wet-1-trace.json")
        violations = check_sequence_numbers(trace)
        assert len(violations) == 0, f"Sequence number violations: {violations}"


class TestHeartBlock:
    """Test the heart block example."""
    
    def test_heart_block_valid(self):
        trace = load_example("heart-block.json")
        result = verify_trace(trace)
        assert result["valid"], f"Heart block should be valid, violations: {result['violations']}"
    
    def test_heart_block_ends_in_blocked_state(self):
        trace = load_example("heart-block.json")
        assert trace["metadata"]["final_state"] == "Blocked"
    
    def test_heart_block_has_heart_block_event(self):
        trace = load_example("heart-block.json")
        event_types = [e["event_type"] for e in trace["events"]]
        assert "heart_block" in event_types


class TestGutVeto:
    """Test the gut veto example."""
    
    def test_gut_veto_valid(self):
        trace = load_example("gut-veto.json")
        result = verify_trace(trace)
        assert result["valid"], f"Gut veto should be valid, violations: {result['violations']}"
    
    def test_gut_veto_ends_in_blocked_state(self):
        trace = load_example("gut-veto.json")
        assert trace["metadata"]["final_state"] == "Blocked"
    
    def test_gut_veto_has_gut_veto_event(self):
        trace = load_example("gut-veto.json")
        event_types = [e["event_type"] for e in trace["events"]]
        assert "gut_veto" in event_types


class TestGateDeny:
    """Test the gate deny example."""
    
    def test_gate_deny_valid(self):
        trace = load_example("gate-deny.json")
        result = verify_trace(trace)
        assert result["valid"], f"Gate deny should be valid, violations: {result['violations']}"
    
    def test_gate_deny_ends_in_denied_state(self):
        trace = load_example("gate-deny.json")
        assert trace["metadata"]["final_state"] == "Denied"
    
    def test_gate_deny_has_gate_deny_event(self):
        trace = load_example("gate-deny.json")
        event_types = [e["event_type"] for e in trace["events"]]
        assert "gate_deny" in event_types
    
    def test_gate_deny_no_execution(self):
        trace = load_example("gate-deny.json")
        assert trace["metadata"]["execution_never_started"] == True


class TestInvariantChecks:
    """Test individual invariant checking functions."""
    
    def test_chain_integrity_detects_broken_chain(self):
        """Test that broken chains are detected."""
        trace = {
            "events": [
                {
                    "id": "0001",
                    "timestamp": "2026-01-19T00:00:00.000Z",
                    "signature": "sig1"
                },
                {
                    "id": "0002",
                    "timestamp": "2026-01-19T00:00:01.000Z",
                    "previous_event_hash": "0099",  # Wrong hash
                    "signature": "sig2"
                }
            ]
        }
        violations = check_chain_integrity(trace)
        assert len(violations) > 0
        assert violations[0]["invariant"] == "chain_integrity"
    
    def test_temporal_consistency_detects_time_reversal(self):
        """Test that timestamp reversals are detected."""
        trace = {
            "events": [
                {
                    "id": "0001",
                    "timestamp": "2026-01-19T00:00:01.000Z",
                    "signature": "sig1"
                },
                {
                    "id": "0002",
                    "timestamp": "2026-01-19T00:00:00.000Z",  # Earlier than previous
                    "previous_event_hash": "0001",
                    "signature": "sig2"
                }
            ]
        }
        violations = check_temporal_consistency(trace)
        assert len(violations) > 0
        assert violations[0]["invariant"] == "temporal_consistency"
    
    def test_signature_validity_detects_missing_signature(self):
        """Test that missing signatures are detected."""
        trace = {
            "events": [
                {
                    "id": "0001",
                    "timestamp": "2026-01-19T00:00:00.000Z"
                    # Missing signature
                }
            ]
        }
        violations = check_signature_validity(trace)
        assert len(violations) > 0
        assert violations[0]["invariant"] == "signature_validity"


if __name__ == "__main__":
    pytest.main([__file__, "-v"])
