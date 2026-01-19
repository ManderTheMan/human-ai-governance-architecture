# Human-AI Execution & Governance Architecture

A formal framework for coordinating human and AI systems with explicit mechanisms for authorization, recovery, and alignment.

## The Problem

How do we build AI systems (and human-AI workflows) that can be:
- **Powerful** without being coercive
- **Precise** without being fragile
- **Interruptible** without collapsing

## The Approach

This architecture treats authorization, recovery, and alignment as first-class concerns—not afterthoughts.

### Key Principles

| Principle | Description |
|-----------|-------------|
| **Layered Veto** | Multiple components can stop execution. None can force it. |
| **Two-Key Authorization** | Execution requires both eligibility AND runtime permission. |
| **Recovery as Structure** | Not optional—a required phase after any terminal condition. |
| **Anti-Coercion** | Systems should constrain, not compel. Stillness is valid. |

## Architecture Overview

┌─────────────────────────────────────────────────────────────┐
│ LAYERS │
├──────────┬──────────┬──────────┬──────────┬─────────────────┤
│   Fascia│ Brain  │ Heart │ Gut │ Organs │
│ (persist)│ (reason) │ (values) │(readiness)│ (execute) │
└────┬─────┴────┬─────┴────┬─────┴────┬─────┴────────┬────────┘
│ │ │ │ │
└──────────┴──────────┴──────────┴──────────────┘
│
┌──────┴──────┐
│ GATE │ ← Only component that authorizes
│ (authorize) │
└──────┬──────┘
│
┌──────┴──────┐
│ RECOVERY │ ← Mandatory after any terminal
│ (stabilize) │
└─────────────┘


## Components

| Component | Description | Status |
|-----------|-------------|--------|
| **Layered Architecture** | Seven functional layers with explicit authority boundaries | ✅ Specified |
| **State Machine (ASM-1)** | 17 states, 12 events, 7 invariants | ✅ Specified |
| **Two-Key Model** | Crucible (eligibility) + Gate (runtime auth) | ✅ Specified |
| **Eligibility Capsule (EC-1)** | JSON schema for execution eligibility | ✅ Schema complete |
| **Validation Oracle** | Python invariant checking | ✅ Implemented |
| **Recovery Protocol (RP-1)** | Six-phase mandatory stabilization | ✅ Specified |
| **Worked Example (WET-1)** | Complete trace from proposal to recovery | ✅ Documented |

## Repository Structure

├── README.md # This file
├── CHANGELOG.md # Version history & learning record
├── docs/
│ ├── SPECIFICATION.md # Full system specification
│ └── GLOSSARY.md # Term definitions
├── schemas/
│ └── eligibility-capsule.schema.json
├── examples/
│ └── wet-1-trace.json
└── oracle/
└── invariants.py


## Key Concepts

### Layered Veto Architecture

The system has multiple components that can **stop** execution:
- **Heart** blocks on value violations
- **Gut** vetoes on readiness/safety
- **Gate** denies on missing prerequisites

No component can **force** execution. This prevents capability from becoming uncontrolled action.

### Two-Key Authorization

Execution requires two separate approvals:
1. **Eligibility** (Crucible seal) — "This is allowed to be executed in principle"
2. **Authorization** (Gate token) — "This specific run is permitted now"

Neither is sufficient alone. This prevents premature commitment and specification gaming.

### Recovery as Structure

Recovery isn't "take a break." It's a mandatory system phase with explicit steps:
1. Revoke all authority
2. Preserve context
3. Update load signals
4. Return to safe state

This enables sustainable long-horizon operation.

## Status

This is active research. The framework is being developed and refined.

See [CHANGELOG.md](CHANGELOG.md) for version history and evolution of thinking.

## Author

**Alexander Campbell**
- 📧 Mandertheman@gmail.com
- 💼 [LinkedIn](https://www.linkedin.com/in/alexander-campbell-682489363/)

Building toward augmented intelligence through human-AI collaboration.
