## 0. Scope of This Glossary

- Applies to **all artifacts** (Paper, Spec, Diagrams)
- Words here are **technical terms**, not metaphors
- If a word appears here, it must be used **consistently**
- If a concept is not here, it is **not yet formal**

---

## 1. Core Structural Terms

### **Cognitive Prosthetic**

A system designed to augment human cognition while preserving agency, dignity, and safety by explicitly separating reasoning, readiness, authorization, execution, and recovery.

> Not an agent. Not an assistant. Not a decision-maker.
> 

### **Artifact**

Any persistent object that carries meaning or authority within the system.

Examples:

- specifications
- schemas
- plans
- sealed versions
- eligibility capsules

Artifacts are **inert unless promoted**.

### **Layer**

A subsystem with a specific role and **bounded authority**.

Layers may communicate but may not assume each other’s responsibilities.

### **Meta System**

A system that governs **how other systems are allowed to operate**, without acting on content or execution.

Meta systems:

- do not decide
- do not execute
- do not reason about content

They define *context, jurisdiction, and transformation rules*.

---

## 2. Domains & Dimensions

### **Domain**

A jurisdictional context that defines **where** an artifact or action is allowed to matter.

Domains are mutually exclusive at any moment.

Canonical domains:

- **Lab** — exploration, hypothesis, ambiguity allowed
- **Workshop** — integration, testing, preparation
- **Execution** — real-world irreversible action
- **Archive** — preserved, inert artifacts
- **Crucible** — transformation boundary (special domain)

### **Dimension**

A resolution level describing **how tightly cognition and action are bound**.

Dimensions are orthogonal to domains.

Canonical dimensions:

- **D0 — Stillness**: sensing, no obligation
- **D1 — Orientation**: mapping, naming
- **D2 — Framing**: structuring, reversible synthesis
- **D3 — Design**: detailed construction
- **D4 — Execution**: irreversible, precise action
- **D5 — Integration**: synthesis after action

### **Domain × Dimension Interaction**

The rule set defining which dimensions are permitted in which domains.

Violations indicate architectural errors, not user failure.

---

## 3. Governance & Authority

### **Authority**

The right to cause irreversible effect.

Authority is:

- explicit
- scoped
- revocable
- never implicit

### **Negative Authority**

The ability to block or defer without approving.

Used by:

- **Heart**
- **Gut**

### **Promotion**

A change in an artifact’s **ontological status** (e.g., from draft to execution-eligible).

Promotion always **constrains**.

### **Demotion**

Removal of authority or eligibility without information loss.

Demotion is:

- lossless
- reversible
- non-punitive

---

## 4. Core Governance Components

### **Crucible**

A formal protocolized boundary that governs **promotion and demotion** of artifacts across domains.

The Crucible:

- never executes
- never authorizes runtime action
- always records rationale and constraints

### **Crucible Protocol (CP-1)**

The explicit, multi-phase procedure by which promotions and demotions occur.

CP-1 defines:

- required inputs
- constraint imposition
- sealing
- recovery guarantees

### **Eligibility Capsule (EC-1)**

A sealed, Crucible-issued artifact that declares an artifact **eligible for execution in principle**.

It does not authorize execution.

### **Execution Gate**

The sole runtime authority that can authorize **a specific execution instance**.

The Gate:

- issues time-bound tokens
- enforces eligibility capsules
- revokes authority on halt or completion

### **Two-Key Rule**

Execution requires:

1. Eligibility (Crucible)
2. Authorization (Gate)

Neither is sufficient alone.

---

## 5. Functional Layers

### **Fascia**

The persistent connective layer that preserves context, partial state, and provenance across transitions.

Fascia prevents collapse during pauses, failures, and domain changes.

### **Brain**

The reasoning and synthesis layer.

The Brain:

- plans
- analyzes
- proposes actions
- cannot execute

### **Heart**

The normative constraint layer.

The Heart:

- encodes values and principles
- blocks violations
- never approves action

### **Gut**

The readiness and safety assessment layer.

The Gut:

- evaluates timing and capacity
- can veto execution
- never approves execution

### **Organs**

Bounded execution units that perform concrete operations.

Organs:

- require Gate authorization
- operate under strict scope
- report outcomes and checkpoints

### **Recovery**

The mandatory post-terminal phase that stabilizes the system after execution, denial, halt, or failure.

Recovery ensures:

- authority revocation
- context preservation
- load normalization

---

## 6. Infrastructure Systems

### **Nervous System**

The coordination and signaling layer.

Responsible for:

- routing signals
- sequencing events
- emitting traces
- handling interrupts

No authority.

### **Endocrine System**

The slow, global modulation layer.

Tracks:

- load
- fatigue
- recovery debt

Advisory only.

### **Immune System**

The anomaly and drift detection layer.

Detects:

- boundary violations
- authority creep
- invariant breaches

Escalates to review; never self-corrects.

---

## 7. Validation & Traces

### **State Machine**

A formal model describing allowed system states and transitions.

Used for validation, not control.

### **Trace**

A chronological record of system events and state transitions.

Traces are the **ground truth** for validation.

### **Oracle**

A validator that checks traces against invariants.

The Oracle:

- does not run the system
- does not influence outcomes
- only reports violations

### **Invariant**

A property that must hold across all valid traces.

Violations indicate structural failure.

---

## 8. Explicit Non-Terms (Locked Out)

The following terms are **not used** in canonical artifacts unless explicitly reintroduced later:

- agent
- autonomy (unqualified)
- intelligence (unqualified)
- productivity
- motivation
- alignment (without scope)

These terms introduce ambiguity without adding structure.

---

## 9. Change Control Rule

Any modification to this glossary requires:

- explicit version bump
- rationale
- list of affected sections

Until then, this glossary is **binding**.
