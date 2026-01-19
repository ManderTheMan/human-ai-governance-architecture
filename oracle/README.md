# Oracle

The Oracle module provides invariant verification for the Human-AI Governance Architecture.

## Purpose

The Oracle verifies that trace events satisfy system invariants, ensuring the integrity and correctness of governance flows.

## Features

- **Chain Integrity**: Verifies event chain is unbroken
- **Temporal Consistency**: Ensures monotonically increasing timestamps
- **Signature Validity**: Checks all events have valid signatures
- **Authorization Chain**: Verifies actions trace back to valid authorization
- **Sequence Numbers**: Validates consecutive sequence numbering

## Usage

### Basic Verification

```python
from oracle import verify_trace
import json

# Load a trace
with open('examples/golden-path.json') as f:
    trace = json.load(f)

# Verify the trace
result = verify_trace(trace)

if result['valid']:
    print("Trace is valid!")
else:
    print("Violations found:")
    for violation in result['violations']:
        print(f"  - {violation['invariant']}: {violation['message']}")
```

### Individual Invariant Checks

```python
from oracle.invariants import (
    check_chain_integrity,
    check_temporal_consistency,
    check_authorization_chain
)

# Check specific invariants
chain_violations = check_chain_integrity(trace)
temporal_violations = check_temporal_consistency(trace)
auth_violations = check_authorization_chain(trace)
```

## Running Tests

The test suite validates the Oracle against example traces:

```bash
# Install pytest if needed
pip install pytest

# Run tests
python -m pytest oracle/test_traces.py -v

# Run specific test class
python -m pytest oracle/test_traces.py::TestGoldenPath -v
```

## Invariants

### Chain Integrity
Every event (except the first) must reference the hash of the previous event, creating an unbreakable chain.

### Temporal Consistency
Event timestamps must be monotonically increasing - time cannot go backwards.

### Signature Validity
All events must have valid cryptographic signatures (structural check only in this implementation).

### Authorization Chain
- Actions must have associated tokens
- Tokens must have associated capsules
- Token grants must occur before action attempts

### Sequence Numbers
Events must have consecutive sequence numbers starting from 0.

## Extending the Oracle

To add new invariants:

1. Implement a check function in `invariants.py`:
```python
def check_new_invariant(trace: Dict[str, Any]) -> List[Dict[str, Any]]:
    violations = []
    # ... check logic ...
    return violations
```

2. Add the check to `verify_trace()`:
```python
def verify_trace(trace: Dict[str, Any]) -> Dict[str, Any]:
    all_violations = []
    all_violations.extend(check_new_invariant(trace))
    # ... other checks ...
```

3. Add tests in `test_traces.py`

## Integration

The Oracle can be integrated into:
- CI/CD pipelines to validate traces
- Runtime monitoring systems
- Recovery procedures to verify system state
- Development tools for trace validation
