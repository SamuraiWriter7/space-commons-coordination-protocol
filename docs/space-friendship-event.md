# docs/space-friendship-event.md

:::writing{variant="document" id="73428"}
# Space Friendship Event Layer v0.1

## Purpose

Space Friendship Event Layer defines the minimum event format for peaceful, AI-assisted space coordination.

Its purpose is to record space-related safety events in a way that prevents premature hostility, supports multi-source verification, and requires human review before escalation.

This layer is designed for events such as:

- satellite collision risk
- space debris warning
- AI false-positive review
- communication anomaly
- space weather alert
- emergency coordination

## Core Principles

### Defense without Hostility

The protocol treats safety, continuity, and shared-space preservation as the first priority.  
It does not treat uncertainty as hostility.

### Coordination before Command

The protocol is not a command system.  
It is a coordination layer for observation sharing, source verification, and human review.

### Trace before Retaliation

Every event must include trace information before attribution or escalation is considered.

### Human Review before Escalation

AI may assist with classification, anomaly detection, uncertainty estimation, and notification prioritization.  
AI must not make final hostile attribution or escalation decisions.

### Commons before Sovereignty

The protocol begins from the assumption that space is a shared operational environment.  
Protection of the shared orbital environment comes before unilateral reaction.

## Event Types

v0.1 supports the following event types:

- `collision_risk`
- `debris_warning`
- `ai_false_positive_review`
- `communication_anomaly`
- `space_weather_alert`
- `emergency_coordination`

## Minimum Event Requirements

A Space Friendship Event must include:

- event identity
- event type
- severity
- affected object references
- observation sources
- AI assistance status
- trace record
- coordination status
- human review status
- safety boundary confirmation

## AI Use Boundary

AI may be used for:

- risk classification
- trajectory uncertainty estimation
- anomaly detection
- data consistency checking
- notification priority ranking
- false-positive review

AI must not be used for:

- target selection
- automatic retaliation
- final hostile attribution
- weapon-use recommendation
- escalation without human review

## De-escalation Default

When uncertainty exists, the event should default to de-escalation review rather than hostile attribution.

The recommended sequence is:

1. Record the event
2. Attach observation sources
3. Assign trace ID
4. Compare multiple sources
5. Notify relevant parties
6. Require human review
7. Resolve or escalate only through reviewed process

## v0.1 Scope

v0.1 does not define a full governance system, defense layer, or international treaty.

It only defines the minimum shared event format required to begin peaceful coordination.

Future versions may add:

- Neutral Coordination Node
- De-escalation Workflow
- SSA Interoperability Layer
- Nakayoshi Certification
- Optional Defense Coordination Module
:::

---

# schemas/space-friendship-event.schema.json

```json
{
  "$schema": "https://json-schema.org/draft/2020-12/schema",
  "$id": "https://example.org/schemas/space-friendship-event.schema.json",
  "title": "Space Friendship Event",
  "type": "object",
  "required": ["space_friendship_event"],
  "additionalProperties": false,
  "properties": {
    "space_friendship_event": {
      "type": "object",
      "required": [
        "event_id",
        "protocol_version",
        "event_type",
        "severity",
        "status",
        "object_refs",
        "observation_sources",
        "ai_assistance",
        "trace",
        "coordination",
        "human_review",
        "safety_boundary"
      ],
      "additionalProperties": false,
      "properties": {
        "event_id": {
          "type": "string",
          "pattern": "^sfn-event-[a-zA-Z0-9._-]+$"
        },
        "protocol_version": {
          "type": "string",
          "const": "v0.1"
        },
        "event_type": {
          "type": "string",
          "enum": [
            "collision_risk",
            "debris_warning",
            "ai_false_positive_review",
            "communication_anomaly",
            "space_weather_alert",
            "emergency_coordination"
          ]
        },
        "severity": {
          "type": "string",
          "enum": ["info", "low", "medium", "high", "critical"]
        },
        "status": {
          "type": "string",
          "enum": [
            "observed",
            "under_review",
            "confirmed",
            "resolved",
            "withdrawn"
          ]
        },
        "summary": {
          "type": "string",
          "minLength": 1
        },
        "object_refs": {
          "type": "array",
          "minItems": 1,
          "items": {
            "type": "object",
            "required": ["object_id", "object_type"],
            "additionalProperties": false,
            "properties": {
              "object_id": {
                "type": "string",
                "minLength": 1
              },
              "object_type": {
                "type": "string",
                "enum": [
                  "satellite",
                  "debris",
                  "launch_vehicle",
                  "spacecraft",
                  "station",
                  "ground_system",
                  "unknown"
                ]
              },
              "operator": {
                "type": "string"
              }
            }
          }
        },
        "observation_sources": {
          "type": "array",
          "minItems": 1,
          "items": {
            "type": "object",
            "required": [
              "source_id",
              "source_type",
              "confidence",
              "observed_at"
            ],
            "additionalProperties": false,
            "properties": {
              "source_id": {
                "type": "string",
                "minLength": 1
              },
              "source_type": {
                "type": "string",
                "enum": [
                  "space_agency",
                  "commercial_ssa_provider",
                  "academic_observatory",
                  "satellite_operator",
                  "public_dataset",
                  "neutral_coordination_node",
                  "other"
                ]
              },
              "confidence": {
                "type": "number",
                "minimum": 0,
                "maximum": 1
              },
              "observed_at": {
                "type": "string",
                "format": "date-time"
              },
              "evidence_refs": {
                "type": "array",
                "items": {
                  "type": "string"
                }
              }
            }
          }
        },
        "ai_assistance": {
          "type": "object",
          "required": [
            "used",
            "role",
            "autonomy_level",
            "human_review_required"
          ],
          "additionalProperties": false,
          "properties": {
            "used": {
              "type": "boolean"
            },
            "role": {
              "type": "string",
              "enum": [
                "none",
                "risk_classification",
                "trajectory_uncertainty_estimation",
                "anomaly_detection",
                "data_consistency_check",
                "notification_priority_ranking",
                "false_positive_review"
              ]
            },
            "autonomy_level": {
              "type": "string",
              "enum": [
                "advisory_only",
                "human_supervised"
              ]
            },
            "human_review_required": {
              "type": "boolean",
              "const": true
            }
          }
        },
        "trace": {
          "type": "object",
          "required": [
            "trace_id",
            "evidence_status",
            "attribution_status"
          ],
          "additionalProperties": false,
          "properties": {
            "trace_id": {
              "type": "string",
              "pattern": "^trace-sfn-[a-zA-Z0-9._-]+$"
            },
            "evidence_status": {
              "type": "string",
              "enum": [
                "single_source",
                "multi_source_unconfirmed",
                "multi_source_confirmed",
                "disputed",
                "insufficient"
              ]
            },
            "attribution_status": {
              "type": "string",
              "enum": [
                "not_applicable",
                "unresolved",
                "suspected",
                "disputed",
                "confirmed_by_human_review"
              ]
            },
            "rationale": {
              "type": "string"
            }
          }
        },
        "coordination": {
          "type": "object",
          "required": [
            "notified_parties",
            "deescalation_required",
            "recommended_actions"
          ],
          "additionalProperties": false,
          "properties": {
            "notified_parties": {
              "type": "array",
              "items": {
                "type": "string"
              }
            },
            "deescalation_required": {
              "type": "boolean"
            },
            "recommended_actions": {
              "type": "array",
              "items": {
                "type": "string",
                "enum": [
                  "continue_monitoring",
                  "request_additional_sources",
                  "notify_operator",
                  "perform_human_review",
                  "issue_collision_warning",
                  "issue_debris_warning",
                  "withdraw_false_positive",
                  "publish_non_sensitive_summary"
                ]
              }
            }
          }
        },
        "human_review": {
          "type": "object",
          "required": ["required", "status"],
          "additionalProperties": false,
          "properties": {
            "required": {
              "type": "boolean",
              "const": true
            },
            "status": {
              "type": "string",
              "enum": [
                "pending",
                "in_progress",
                "approved",
                "rejected",
                "resolved"
              ]
            },
            "reviewer_role": {
              "type": "string"
            },
            "review_notes": {
              "type": "string"
            }
          }
        },
        "safety_boundary": {
          "type": "object",
          "required": [
            "no_target_selection",
            "no_automatic_retaliation",
            "no_weapon_use_recommendation",
            "no_final_hostile_attribution_by_ai"
          ],
          "additionalProperties": false,
          "properties": {
            "no_target_selection": {
              "type": "boolean",
              "const": true
            },
            "no_automatic_retaliation": {
              "type": "boolean",
              "const": true
            },
            "no_weapon_use_recommendation": {
              "type": "boolean",
              "const": true
            },
            "no_final_hostile_attribution_by_ai": {
              "type": "boolean",
              "const": true
            }
          }
        }
      }
    }
  }
}
