## v0.3 — De-escalation Workflow

v0.3 adds the De-escalation Workflow model.

The De-escalation Workflow connects Space Friendship Events and Neutral Coordination Nodes into a step-by-step process for preventing premature escalation.

It defines:

- event recording
- observation collection
- cross-source verification
- AI false-positive checking
- neutral node review
- human review
- operator notification
- public summary review
- resolution or continued monitoring

The default posture is de-escalation.

When evidence is uncertain, disputed, or incomplete, the workflow requires additional verification and human review before escalation-sensitive interpretation.


## v0.2 — Neutral Coordination Node

## Civilizational Positioning

SCCP is positioned as a thin coordination OS for preserving outer space as a shared commons.

It is not a military command structure.  
It is a coordination, verification, traceability, and de-escalation layer for peaceful AI-assisted space safety.

See:

- `docs/civilizational-positioning.md`

v0.2 adds the Neutral Coordination Node model.

A Neutral Coordination Node is a non-command coordination structure for:

- observation aggregation
- cross-source verification
- de-escalation review
- AI false-positive checking
- operator notification
- public summary preparation

The node is designed to process v0.1 Space Friendship Events without creating military command authority.

Core boundaries:

- no command authority
- no target selection
- no automatic retaliation
- no weapon-use recommendation
- no final hostile attribution by AI
- human review required

# Space Commons Coordination Protocol

A Nakayoshi Network for peaceful, AI-assisted space coordination.

## Overview

Space Commons Coordination Protocol is a lightweight coordination protocol for preventing escalation in space operations.

It begins with the **Space Friendship Event Layer**, a minimal event format for recording:

- collision risk
- debris warning
- AI false-positive review
- multi-source verification
- human review
- de-escalation status

The purpose of this protocol is not to militarize space, but to preserve space as a shared commons through transparency, traceability, and coordination.

## v0.1 — Space Friendship Event Layer

v0.1 defines the minimum event format for peaceful AI-assisted space safety coordination.

Core principles:

- Defense without hostility
- Coordination before command
- Trace before retaliation
- Human review before escalation
- Commons before sovereignty

## Directory Structure

```text
docs/
  space-friendship-event.md

schemas/
  space-friendship-event.schema.json

examples/
  collision-risk-event.example.yaml
  debris-warning-event.example.yaml
  ai-false-positive-review.example.yaml

scripts/
  validate_examples.py
