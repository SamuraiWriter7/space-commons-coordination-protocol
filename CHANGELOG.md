# Changelog

## v0.3.0-candidate — De-escalation Workflow

### Added

- Added `De-escalation Workflow` model.
- Added schema for workflow steps, evidence handling, AI boundary, notification policy, human review, and outcome.
- Added example workflow for communication anomaly de-escalation.
- Updated validation script to include De-escalation Workflow validation.

### Design Intent

v0.3 connects Space Friendship Events and Neutral Coordination Nodes into an executable de-escalation process.

The workflow prevents uncertainty from becoming hostility by requiring observation collection, cross-source verification, AI false-positive review, human review, and non-escalation defaults.

## v0.2.0-candidate — Neutral Coordination Node

### Added

- Added `Neutral Coordination Node` model.
- Added schema for neutral coordination node governance, AI policy, verification policy, interoperability, trust model, audit logging, and safety boundary.
- Added example neutral coordination node.
- Updated validation script to use explicit schema-example mappings.
- Added safety boundary:
  - no command authority
  - no target selection
  - no automatic retaliation
  - no weapon-use recommendation
  - no final hostile attribution by AI

### Design Intent

v0.2 defines the first operational coordination structure for the Space Commons Coordination Protocol.

The Neutral Coordination Node is not a command node.  
It aggregates observations, verifies multiple sources, prevents false positives, supports de-escalation, and routes sensitive cases to human review.

## v0.1.0-candidate — Space Friendship Event Layer

### Added

- Added `Space Friendship Event` minimum event model.
- Added schema for collision risk, debris warning, AI false-positive review, communication anomaly, space weather alert, and emergency coordination.
- Added AI use boundary:
  - no target selection
  - no automatic retaliation
  - no weapon-use recommendation
  - no final hostile attribution by AI
- Added trace layer for evidence status and attribution status.
- Added human review requirement before escalation.
- Added example events:
  - collision risk event
  - debris warning event
  - AI false-positive review event
- Added validation script for YAML examples against JSON Schema.

### Design Intent

v0.1 establishes the minimum coordination layer for peaceful AI-assisted space safety.

The protocol does not define a military command structure.  
It defines a traceable, reviewable, de-escalation-first event format for preserving space as a shared commons.
