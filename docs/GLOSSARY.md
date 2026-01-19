# Glossary

## Terms and Definitions

### Eligibility Capsule
A cryptographically sealed data structure containing authorization context, constraints, and metadata that determines whether an action can be performed.

### Authorization Token
A credential that represents granted permission for a specific action or set of actions within a defined scope and time period.

### Trace Event
An immutable, timestamped record of a decision-making event, including inputs, outputs, and contextual information for auditing and recovery.

### ASM (Alignment State Machine)
A formal state machine that defines allowed transitions and governance rules for human-AI coordination.

### WET-1 (Wisdom Execution Trace - Level 1)
The first level of execution tracing that captures basic decision flow and authorization checks.

### Heart Block
A safety mechanism that prevents an AI action when human values or emotional considerations override logical authorization.

### Gut Veto
An intuitive override mechanism allowing humans to reject AI decisions based on instinct or tacit knowledge.

### Gate Deny
A formal denial of access or action at a defined control gate in the governance architecture.

### Golden Path
The ideal execution flow through the governance architecture where all checks pass and alignment is maintained.

### Oracle
A verification system that checks invariants and validates trace events against expected governance rules.

### Invariant
A condition that must always hold true throughout the execution of the governance system.

## Acronyms

- **ASM**: Alignment State Machine
- **WET**: Wisdom Execution Trace
- **AI**: Artificial Intelligence

## Related Documents

- [SPECIFICATION.md](SPECIFICATION.md) - Technical specification
- [PHILOSOPHY.md](PHILOSOPHY.md) - Design philosophy
