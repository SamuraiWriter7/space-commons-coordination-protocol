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
