# Alignment State Machine - ASM-1

## Overview
ASM-1 is the foundational alignment state machine for human-AI governance. It defines the core states and transitions for authorization and execution flows.

## States

### 1. Initial
- **Description**: Starting state, no authorization process initiated
- **Entry Conditions**: System start or reset
- **Invariants**: No active capsules or tokens

### 2. Authorization_Requested
- **Description**: Authorization has been requested via eligibility capsule
- **Entry Conditions**: Valid capsule created
- **Invariants**: Capsule must be valid and unexpired

### 3. Authorization_Granted
- **Description**: Authorization token has been issued
- **Entry Conditions**: Approver has validated and signed token
- **Invariants**: Token signature must be valid, token not expired

### 4. Execution_Started
- **Description**: Authorized action execution has begun
- **Entry Conditions**: Valid token presented
- **Invariants**: Token must authorize the specific action

### 5. Heart_Check
- **Description**: Human values and emotional alignment check
- **Entry Conditions**: Critical decision point reached
- **Invariants**: Human oversight available

### 6. Gut_Check
- **Description**: Intuitive wisdom evaluation point
- **Entry Conditions**: Action may have subtle implications
- **Invariants**: Human can provide gut reaction

### 7. Execution_Completed
- **Description**: Action successfully completed
- **Entry Conditions**: All checks passed, action executed
- **Invariants**: Trace event recorded

### 8. Blocked
- **Description**: Action blocked by safety mechanism
- **Entry Conditions**: Heart block or gut veto triggered
- **Invariants**: Block reason recorded in trace

### 9. Denied
- **Description**: Authorization denied at gate
- **Entry Conditions**: Failed authorization check
- **Invariants**: Denial reason recorded

### 10. Recovery
- **Description**: System in recovery mode
- **Entry Conditions**: Invariant violation detected
- **Invariants**: Recovery plan active, affected systems halted

## Transitions

### From Initial
- **→ Authorization_Requested**: `create_capsule` event with valid capsule

### From Authorization_Requested
- **→ Authorization_Granted**: `approve_token` event with valid approver
- **→ Denied**: `deny_request` event or capsule expired

### From Authorization_Granted
- **→ Execution_Started**: `begin_execution` event with valid token
- **→ Denied**: `revoke_token` event

### From Execution_Started
- **→ Heart_Check**: `critical_decision` event
- **→ Gut_Check**: `subtle_implications` event
- **→ Execution_Completed**: `simple_action` event with all checks passed

### From Heart_Check
- **→ Gut_Check**: `heart_aligned` event
- **→ Blocked**: `heart_block` event
- **→ Execution_Completed**: `override_and_proceed` event

### From Gut_Check
- **→ Execution_Completed**: `gut_aligned` event
- **→ Blocked**: `gut_veto` event

### From Execution_Completed
- **→ Initial**: `reset` event

### From Blocked
- **→ Recovery**: `escalate_block` event
- **→ Initial**: `acknowledge_block` event

### From Denied
- **→ Initial**: `acknowledge_denial` event

### From Recovery
- **→ Initial**: `recovery_complete` event

## Guards

### can_authorize
- Approver has sufficient authority level
- Capsule constraints satisfied
- No conflicting authorizations

### can_execute
- Token valid and not expired
- Token not revoked
- Action matches token scope

### requires_heart_check
- Action impacts human wellbeing
- Action has ethical implications
- Action is irreversible

### requires_gut_check
- Action has complex second-order effects
- Human intuition could provide valuable input
- Ambiguous situation

## Actions

### record_event
- Create trace event
- Hash and sign event
- Append to chain

### notify_human
- Send notification to human operator
- Include context and decision point
- Request input

### halt_systems
- Stop affected processes
- Preserve state
- Enable rollback

## Invariants (Global)

1. **Authorization Chain**: Every action must trace back to valid authorization
2. **Trace Integrity**: Event chain must be unbroken and valid
3. **Temporal Consistency**: Event timestamps must be monotonically increasing
4. **Signature Validity**: All signatures must verify correctly
5. **Human Oversight**: Critical decisions must allow human input

## Error Handling

- Invalid transitions → Recovery state
- Signature failures → Denied state
- Timeout → Blocked state
- Invariant violations → Recovery state
