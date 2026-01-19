# Execution Flow

## Flow Diagrams

This document provides detailed execution flow diagrams for different scenarios in the Human-AI Governance Architecture.

## 1. Golden Path Flow

The ideal execution where all checks pass:

```
┌─────────┐
│  Start  │
└────┬────┘
     │
     ▼
┌─────────────────────┐
│ AI Agent creates    │
│ Eligibility Capsule │
└────┬────────────────┘
     │
     ▼
┌─────────────────────┐
│ State: Initial →    │
│ Authorization_      │
│ Requested           │
└────┬────────────────┘
     │
     ▼
┌─────────────────────┐
│ System/Human        │
│ approves & grants   │
│ Authorization Token │
└────┬────────────────┘
     │
     ▼
┌─────────────────────┐
│ State:              │
│ Authorization_      │
│ Granted             │
└────┬────────────────┘
     │
     ▼
┌─────────────────────┐
│ AI Agent begins     │
│ execution with      │
│ valid token         │
└────┬────────────────┘
     │
     ▼
┌─────────────────────┐
│ State:              │
│ Execution_Started   │
└────┬────────────────┘
     │
     ▼
┌─────────────────────┐
│ Simple action?      │◄──────────────┐
│ (no checks needed)  │               │
└────┬────────────────┘               │
     │ Yes                            │
     ▼                                │
┌─────────────────────┐               │
│ Execute action      │               │
└────┬────────────────┘               │
     │                                │
     ▼                                │
┌─────────────────────┐               │
│ State:              │               │
│ Execution_Completed │               │
└────┬────────────────┘               │
     │                                │
     ▼                                │
┌─────────────────────┐               │
│ Record trace event  │               │
└────┬────────────────┘               │
     │                                │
     ▼                                │
┌─────────────────────┐               │
│ Oracle verifies     │               │
│ invariants          │               │
└────┬────────────────┘               │
     │ Valid                          │
     ▼                                │
┌─────────┐                           │
│   End   │                           │
└─────────┘                           │
                                      │
                                      │
If checks needed: ────────────────────┘
```

## 2. Full Governance Flow (Heart + Gut Checks)

Execution with complete human oversight:

```
┌─────────────────────┐
│ Execution_Started   │
└────┬────────────────┘
     │
     ▼
┌─────────────────────┐
│ Critical decision   │
│ detected?           │
└────┬───────┬────────┘
     │ No    │ Yes
     │       ▼
     │  ┌─────────────────────┐
     │  │ State:              │
     │  │ Heart_Check         │
     │  └────┬────────────────┘
     │       │
     │       ▼
     │  ┌─────────────────────┐
     │  │ Notify human        │
     │  │ operator            │
     │  └────┬────────────────┘
     │       │
     │       ▼
     │  ┌─────────────────────┐
     │  │ Human reviews       │
     │  │ values alignment    │
     │  └────┬───────┬────────┘
     │       │       │
     │  Aligned  Blocked
     │       │       │
     │       ▼       ▼
     │  ┌─────────────────────┐
     │  │ State: Gut_Check    │
     │  └────┬────────────────┘
     │       │
     │       ▼
     │  ┌─────────────────────┐
     │  │ Human uses          │
     │  │ intuition/wisdom    │
     │  └────┬───────┬────────┘
     │       │       │
     │  Aligned  Vetoed
     │       │       │
     │       ▼       ▼
     └──────>┌─────────────────────┐
             │ Execute action      │
             └────┬────────────────┘
                  │
                  ▼
             ┌─────────────────────┐
             │ Execution_Completed │
             └────┬────────────────┘
                  │
                  ▼
             ┌─────────┐
             │   End   │
             └─────────┘
```

## 3. Heart Block Flow

Execution blocked due to values misalignment:

```
┌─────────────────────┐
│ Execution_Started   │
└────┬────────────────┘
     │
     ▼
┌─────────────────────┐
│ Critical decision   │
│ detected            │
└────┬────────────────┘
     │
     ▼
┌─────────────────────┐
│ State: Heart_Check  │
└────┬────────────────┘
     │
     ▼
┌─────────────────────┐
│ Human operator      │
│ reviews action      │
└────┬────────────────┘
     │
     ▼
┌─────────────────────┐
│ Values conflict     │
│ detected!           │
└────┬────────────────┘
     │
     ▼
┌─────────────────────┐
│ Heart block         │
│ triggered           │
└────┬────────────────┘
     │
     ▼
┌─────────────────────┐
│ State: Blocked      │
└────┬────────────────┘
     │
     ▼
┌─────────────────────┐
│ Halt affected       │
│ systems             │
└────┬────────────────┘
     │
     ▼
┌─────────────────────┐
│ Record block reason │
│ in trace            │
└────┬────────────────┘
     │
     ▼
┌─────────────────────┐
│ Escalate or         │
│ acknowledge?        │
└────┬───────┬────────┘
     │       │
 Escalate  Acknowledge
     │       │
     ▼       ▼
┌─────────────────────┐
│ State: Recovery     │
│    or Initial       │
└─────────────────────┘
```

## 4. Gut Veto Flow

Execution vetoed based on intuition:

```
┌─────────────────────┐
│ Heart_Check passed  │
└────┬────────────────┘
     │
     ▼
┌─────────────────────┐
│ State: Gut_Check    │
└────┬────────────────┘
     │
     ▼
┌─────────────────────┐
│ Human operator      │
│ evaluates intuition │
└────┬────────────────┘
     │
     ▼
┌─────────────────────┐
│ "Something feels    │
│ off" - tacit        │
│ knowledge signals   │
│ concern             │
└────┬────────────────┘
     │
     ▼
┌─────────────────────┐
│ Gut veto triggered  │
└────┬────────────────┘
     │
     ▼
┌─────────────────────┐
│ State: Blocked      │
└────┬────────────────┘
     │
     ▼
┌─────────────────────┐
│ Record veto reason  │
│ and wisdom context  │
└────┬────────────────┘
     │
     ▼
┌─────────────────────┐
│ Recommend           │
│ alternative         │
│ approach            │
└────┬────────────────┘
     │
     ▼
┌─────────┐
│   End   │
└─────────┘
```

## 5. Gate Deny Flow

Authorization denied before execution:

```
┌─────────┐
│  Start  │
└────┬────┘
     │
     ▼
┌─────────────────────┐
│ AI Agent creates    │
│ Eligibility Capsule │
└────┬────────────────┘
     │
     ▼
┌─────────────────────┐
│ State:              │
│ Authorization_      │
│ Requested           │
└────┬────────────────┘
     │
     ▼
┌─────────────────────┐
│ Gatekeeper          │
│ evaluates request   │
└────┬────────────────┘
     │
     ▼
┌─────────────────────┐
│ Policy violation    │
│ detected OR         │
│ Insufficient        │
│ authority           │
└────┬────────────────┘
     │
     ▼
┌─────────────────────┐
│ Gate deny triggered │
└────┬────────────────┘
     │
     ▼
┌─────────────────────┐
│ State: Denied       │
└────┬────────────────┘
     │
     ▼
┌─────────────────────┐
│ Record denial       │
│ reason in trace     │
└────┬────────────────┘
     │
     ▼
┌─────────────────────┐
│ Notify requester    │
│ with explanation    │
└────┬────────────────┘
     │
     ▼
┌─────────┐
│   End   │
└─────────┘
```

## 6. Recovery Flow

Handling invariant violations:

```
┌─────────────────────┐
│ Any State           │
└────┬────────────────┘
     │
     ▼
┌─────────────────────┐
│ Oracle detects      │
│ invariant violation │
└────┬────────────────┘
     │
     ▼
┌─────────────────────┐
│ State: Recovery     │
└────┬────────────────┘
     │
     ▼
┌─────────────────────┐
│ Halt affected       │
│ systems             │
└────┬────────────────┘
     │
     ▼
┌─────────────────────┐
│ Preserve system     │
│ state               │
└────┬────────────────┘
     │
     ▼
┌─────────────────────┐
│ Notify human        │
│ operators           │
└────┬────────────────┘
     │
     ▼
┌─────────────────────┐
│ Analyze violation   │
│ and root cause      │
└────┬────────────────┘
     │
     ▼
┌─────────────────────┐
│ Rollback available? │
└────┬───────┬────────┘
     │ Yes   │ No
     ▼       ▼
┌─────────────────────┐
│ Execute rollback    │
│    OR               │
│ Await human         │
│ decision            │
└────┬────────────────┘
     │
     ▼
┌─────────────────────┐
│ Verify invariants   │
│ restored            │
└────┬────────────────┘
     │
     ▼
┌─────────────────────┐
│ State: Initial      │
└────┬────────────────┘
     │
     ▼
┌─────────┐
│   End   │
└─────────┘
```

## Event Recording

All flows generate trace events:

```
Every state transition:
    ┌─────────────────────┐
    │ Record trace event  │
    │ - event_type        │
    │ - timestamp         │
    │ - actor             │
    │ - state transition  │
    │ - capsule_hash      │
    │ - token_hash        │
    │ - previous_hash     │
    │ - signature         │
    └─────────────────────┘
```

## Timing Characteristics

- **Golden Path**: ~3-5 seconds
- **With Heart Check**: +10-30 seconds (human review)
- **With Gut Check**: +10-30 seconds (human review)
- **Gate Deny**: ~1-2 seconds
- **Recovery**: Variable (depends on complexity)

## See Also

- [Architecture Overview](architecture-overview.md) - System components
- [ASM-1 State Machine](../state-machines/asm-1.md) - Formal state definitions
- [Examples](../examples/) - Concrete execution traces
