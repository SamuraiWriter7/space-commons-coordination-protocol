# Neutral Coordination Node v0.2

## Purpose

Neutral Coordination Node defines the minimum structure for a non-command coordination node within the Space Commons Coordination Protocol.

Its purpose is to receive Space Friendship Events, aggregate observations, verify multiple sources, prevent AI false positives, support de-escalation review, notify relevant parties, and preserve audit logs.

A Neutral Coordination Node is not a military command system.
It does not select targets, authorize retaliation, recommend weapon use, or finalize hostile attribution by AI.

Its role is coordination, verification, and de-escalation.

## Design Principle

### Coordination, not command

The node may coordinate observations and reviews.
It must not issue command authority over space assets.

### Verification before escalation

The node must require multi-source verification before high-severity alerts or escalation-sensitive interpretation.

### Human review before hostile attribution

AI may assist with risk classification, anomaly detection, uncertainty estimation, and false-positive review.
AI must not finalize hostile attribution.

### Transparency with tiered disclosure

The node should preserve auditability while allowing sensitive operational data to remain protected.

### Multi-stakeholder trust

A Neutral Coordination Node should be able to include space agencies, commercial SSA providers, university research labs, satellite operators, insurance or risk bodies, international organizations, and civil society observers.

## Core Responsibilities

A Neutral Coordination Node may perform the following roles:

* observation aggregation
* cross-source verification
* de-escalation review
* AI false-positive checking
* operator notification
* public summary preparation

## Governance Boundary

The node must define:

* operator type
* participating entities
* decision authority
* conflict-of-interest policy

The recommended default is:

```yaml
decision_authority: "advisory_only"
```

This means the node may recommend, warn, request verification, and route events for human review.
It does not command operational maneuvers or military responses.

## AI Policy

AI may be used for:

* risk classification
* trajectory uncertainty estimation
* anomaly detection
* data consistency checking
* notification priority ranking
* false-positive review
* public summary drafting

AI must not be used for:

* target selection
* automatic retaliation
* weapon-use recommendation
* final hostile attribution by AI
* escalation without human review

## Verification Policy

Each node must define:

* minimum sources required
* confidence threshold for alert
* disputed evidence handling
* attribution policy

The recommended default is:

```yaml
minimum_sources_required: 2
confidence_threshold_for_alert: 0.75
disputed_evidence_handling: "hold_for_human_review"
attribution_policy: "multi_party_review_required"
```

## Trust Model

A Neutral Coordination Node must preserve audit logs for:

* decision trace
* AI assistance
* human review

The node should also define:

* public disclosure policy
* data access policy
* minimum retention period

## v0.2 Scope

v0.2 does not create a defense layer, command layer, or enforcement mechanism.

It defines the minimum structure for a neutral coordination node that can process v0.1 Space Friendship Events safely and transparently.

Future versions may add:

* De-escalation Workflow
* Nakayoshi Certification
* SSA Interoperability Layer
* Optional Defense Coordination Module
