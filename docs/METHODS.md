# Methods

## Implementation Methods

### 1. Eligibility Capsule Creation

#### Purpose
Create a cryptographically sealed authorization context for an action.

#### Method
```python
def create_eligibility_capsule(action, context, constraints):
    capsule = {
        "action": action,
        "context": context,
        "constraints": constraints,
        "timestamp": current_timestamp(),
        "signature": sign(action, context, constraints)
    }
    validate_schema(capsule, "eligibility-capsule.schema.json")
    return capsule
```

#### Validation
- Schema conformance
- Cryptographic signature verification
- Constraint consistency checks

### 2. Authorization Token Generation

#### Purpose
Generate a token representing granted permission for a specific action.

#### Method
```python
def generate_authorization_token(capsule, approver):
    token = {
        "capsule_hash": hash(capsule),
        "approver": approver,
        "granted_at": current_timestamp(),
        "expires_at": calculate_expiry(capsule.constraints),
        "signature": sign_with_key(approver.private_key)
    }
    validate_schema(token, "authorization-token.schema.json")
    return token
```

#### Validation
- Approver authority verification
- Expiry time validation
- Signature verification

### 3. Trace Event Recording

#### Purpose
Create an immutable record of a decision-making event.

#### Method
```python
def record_trace_event(event_type, data, capsule, token):
    event = {
        "event_type": event_type,
        "timestamp": current_timestamp(),
        "data": data,
        "capsule_hash": hash(capsule),
        "token_hash": hash(token),
        "previous_event_hash": get_last_event_hash(),
        "signature": sign(event_data)
    }
    validate_schema(event, "trace-event.schema.json")
    append_to_trace(event)
    return event
```

#### Validation
- Event chain integrity
- Timestamp ordering
- Schema conformance

### 4. State Machine Execution

#### Purpose
Execute state transitions according to formal governance rules.

#### Method
```python
def execute_state_transition(current_state, event, asm):
    allowed_transitions = asm.get_transitions(current_state)
    
    for transition in allowed_transitions:
        if transition.matches(event):
            if check_guards(transition.guards):
                new_state = transition.target
                execute_actions(transition.actions)
                record_trace_event("state_transition", {
                    "from": current_state,
                    "to": new_state,
                    "event": event
                })
                return new_state
    
    raise StateTransitionError("No valid transition found")
```

#### Validation
- Guard condition evaluation
- State invariant checking
- Transition recording

### 5. Oracle Verification

#### Purpose
Verify that trace events satisfy system invariants.

#### Method
```python
def verify_trace(trace, invariants):
    violations = []
    
    for invariant in invariants:
        if not invariant.check(trace):
            violations.append({
                "invariant": invariant.name,
                "violation_point": invariant.find_violation(trace)
            })
    
    return {
        "valid": len(violations) == 0,
        "violations": violations
    }
```

#### Validation
- Invariant coverage
- Violation detection
- Recovery recommendations

### 6. Recovery Procedures

#### Purpose
Handle misalignment detection and correction.

#### Method
```python
def initiate_recovery(violation_report):
    # Halt affected processes
    halt_affected_systems(violation_report)
    
    # Notify human operators
    notify_operators(violation_report)
    
    # Execute rollback if configured
    if has_rollback_plan(violation_report):
        execute_rollback(violation_report)
    
    # Wait for human decision
    return await_human_override()
```

## Best Practices

1. **Always validate inputs** against schemas before processing
2. **Record all state transitions** in the trace
3. **Check invariants regularly**, not just on failures
4. **Design for recovery** from the start
5. **Test edge cases** including all veto mechanisms

## See Also

- [SPECIFICATION.md](SPECIFICATION.md) - Formal specification
- [Examples](../examples/) - Working examples
