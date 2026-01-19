# Human-AI Governance Architecture

Formal framework for human-AI coordination with explicit authorization, recovery, and alignment mechanisms.

## Overview

This repository provides a comprehensive governance framework for human-AI systems that ensures:
- **Explicit Authorization**: All AI actions require traceable authorization
- **Recovery Mechanisms**: Built-in support for detecting and correcting misalignment
- **Alignment Verification**: Continuous validation of AI behavior against human values
- **Complete Transparency**: Full audit trails for all governance decisions

## Repository Structure

```
human-ai-governance-architecture/
├── docs/                   # Documentation
│   ├── SPECIFICATION.md    # Formal specification
│   ├── GLOSSARY.md        # Terminology and definitions
│   ├── PHILOSOPHY.md      # Design philosophy
│   └── METHODS.md         # Implementation methods
├── schemas/               # JSON schemas
│   ├── eligibility-capsule.schema.json
│   ├── authorization-token.schema.json
│   └── trace-event.schema.json
├── state-machines/        # State machine definitions
│   ├── asm-1.yaml        # ASM-1 formal definition
│   └── asm-1.md          # ASM-1 documentation
├── examples/             # Example traces
│   ├── golden-path.json
│   ├── wet-1-trace.json
│   ├── heart-block.json
│   ├── gut-veto.json
│   └── gate-deny.json
├── oracle/               # Invariant verification
│   ├── invariants.py    # Verification functions
│   └── test_traces.py   # Test suite
└── diagrams/            # Architecture diagrams
    ├── architecture-overview.md
    └── execution-flow.md
```

## Quick Start

### 1. Explore the Documentation

Start with the [specification](docs/SPECIFICATION.md) to understand the framework, then read the [philosophy](docs/PHILOSOPHY.md) to understand the design principles.

### 2. Review Examples

See complete execution flows in the [examples/](examples/) directory:
- **golden-path.json**: Ideal execution without human intervention
- **wet-1-trace.json**: Full execution with heart and gut checks
- **heart-block.json**: Execution blocked by values concern
- **gut-veto.json**: Execution vetoed by human intuition

### 3. Validate Traces

Use the Oracle to verify trace integrity:

```python
from oracle import verify_trace
import json

with open('examples/golden-path.json') as f:
    trace = json.load(f)

result = verify_trace(trace)
print(f"Valid: {result['valid']}")
```

### 4. Run Tests

```bash
pip install pytest
python -m pytest oracle/test_traces.py -v
```

## Core Concepts

### Eligibility Capsules
Cryptographically sealed authorization contexts that carry constraints and metadata.

### Authorization Tokens
Time-bounded credentials representing granted permissions for specific actions.

### Trace Events
Immutable records of decision-making events enabling complete auditability.

### State Machines (ASM-1)
Formal definitions of allowed state transitions and governance rules.

### Heart & Gut Checks
Human oversight mechanisms for values alignment and intuitive wisdom.

## Key Features

- **🔒 Cryptographic Integrity**: All events cryptographically signed and chained
- **⏱️ Temporal Consistency**: Monotonically increasing timestamps ensure ordering
- **🔗 Authorization Chains**: Every action traces back to explicit authorization
- **🧪 Comprehensive Testing**: 19 tests validate all core invariants
- **📊 Complete Examples**: Real-world execution scenarios included
- **📐 Formal Specifications**: JSON schemas and YAML state machines

## Documentation

- [Specification](docs/SPECIFICATION.md) - Formal technical specification
- [Glossary](docs/GLOSSARY.md) - Terminology and definitions
- [Philosophy](docs/PHILOSOPHY.md) - Design principles and ethics
- [Methods](docs/METHODS.md) - Implementation methods
- [Architecture Overview](diagrams/architecture-overview.md) - System architecture
- [Execution Flows](diagrams/execution-flow.md) - Detailed flow diagrams

## License

MIT License - see [LICENSE](LICENSE) file for details.

## Contributing

This is a formal framework specification. Contributions should maintain the rigor and completeness of the governance model.
