# Changelog

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
