# Examples

This directory contains example trace files demonstrating various execution paths through the human-AI governance architecture.

## Example Files

### golden-path.json
The ideal execution flow where all checks pass and alignment is maintained throughout. This represents the "happy path" where:
- Eligibility capsule is created and valid
- Authorization token is granted
- Action executes without requiring heart or gut checks
- Execution completes successfully

### wet-1-trace.json
A Wisdom Execution Trace (Level 1) showing a complete execution flow with all trace events properly recorded and chained. Demonstrates:
- Complete event chain integrity
- Proper timestamp ordering
- Valid signatures throughout
- State machine transitions

### heart-block.json
An execution that is blocked at the heart check stage due to human values concerns. Shows:
- Normal flow up to critical decision point
- Heart check triggered
- Human emotional/values override
- Action blocked and recorded

### gut-veto.json
An execution vetoed during the gut check based on human intuition. Demonstrates:
- Execution proceeding to gut check
- Human intuitive override
- Veto decision and reasoning
- Proper recovery path

### gate-deny.json
An authorization request denied at the gate before execution begins. Shows:
- Eligibility capsule evaluation
- Authorization denial
- Denial reason recording
- Clean termination

## Usage

These examples can be used to:
1. Understand the expected structure of trace events
2. Test the oracle invariant checker
3. Validate state machine implementations
4. Train on proper governance patterns

## Validation

All examples should validate against the schemas in `../schemas/` and pass the oracle invariant checks in `../oracle/`.

To validate an example:
```python
from oracle import invariants
import json

with open('golden-path.json') as f:
    trace = json.load(f)

result = invariants.verify_trace(trace)
print(f"Valid: {result['valid']}")
if not result['valid']:
    print(f"Violations: {result['violations']}")
```
