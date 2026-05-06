---
aid: modern-treasury
name: Modern Treasury
description: Modern Treasury transforms how teams move and track money to support impactful businesses rooted in trust and transparency.
type: Index
position: Consumer
access: 3rd-Party
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
url: https://raw.githubusercontent.com/api-evangelist/modern-treasury/refs/heads/main/apis.yml
tags:
  - Financial
  - Money
  - Payments
  - Treasury
created: '2024-11-07'
modified: '2026-05-04'
specificationVersion: '0.19'
apis:
  - aid: modern-treasury:modern-treasury
    name: Modern Treasury
    description: Modern Treasury transforms how teams move and track money to support impactful businesses rooted in trust and transparency.
    humanURL: https://www.moderntreasury.com/
    baseURL: https://app.moderntreasury.com/api
    tags:
      - Financial
      - Money
      - Payments
    properties:
      - type: Documentation
        url: https://docs.moderntreasury.com/
      - type: API Reference
        url: https://docs.moderntreasury.com/platform/reference
      - type: Sign Up
        url: https://app.moderntreasury.com/register
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
common:
  - type: Features
    data:
      - Custom usage-based pricing across all payment rails
      - Volume tiers reduce per-unit cost
      - ACH, wires, RTP, FedNow, push-to-card, stablecoins
      - Direct bank integrations (no PSPs in middle)
      - REST API at app.moderntreasury.com/api/
      - 'REST API: 600 req/min/organization'
      - OAuth + API tokens
      - Webhooks for payment, transaction, ledger events
      - Internal accounts (sub-ledgers) for embedded finance
      - Counterparties for payee management
      - Returns and reconciliation engine
      - Idempotency keys for safe retries
      - Compliance and Bank Operations products
      - Ledgers product for double-entry accounting
      - Bank Notes (UI for human approval workflows)
      - SOC 1/2 Type 2
    sources:
      - https://www.moderntreasury.com/pricing
    updated: '2026-05-04'
---
