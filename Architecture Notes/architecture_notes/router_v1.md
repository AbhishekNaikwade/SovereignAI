# Decision Router System — v1

## System Flow

input
→ validation
→ guardrail check
→ classification
→ routing
→ handler
→ structured logging

## Components

get_user_input — collects input
validate_input — length & empty checks
guardrail_check — abuse & pattern defense
classify_input — intent classification
route — handler dispatch
handlers — response generators
log_result — structured metrics log

## Redesign v2
Changed classifier priority:
- command detection before question rule
- question requires alphabetic characters
Reason:
Fix misclassification of command-with-question-mark and symbol-only inputs

## Logging Upgrade v3
Added structured logging with:
- validation status
- category
- input length
Purpose:
Enable evaluation and behavior tracking

## Redesign History

v1 — base router
v2 — classifier priority fix
v3 — structured logging added
v4 — guardrail layer added
v4.1 — guardrail loop bug fixed

## Key Design Decisions

- command detection before question rule
- strip() normalization
- guardrail before classification
- structured logs for observability

## Known Limits

- rule-based classification only
- no semantic NLP
- simple pattern guardrails
