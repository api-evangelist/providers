---
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    auth_clarity: false
    consent_identity: false
    dry_run_mode: false
    error_semantics: verified
    event_surface_described: false
    idempotency: verified
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 31.5
  scored_at: '2026-08-17'
api_count: 3
apis:
- description: For creditors. Uploading B2B and B2C invoices to collection, then tracking cases, contracts, payments and tasks through recovery. 53 operations across 44 paths, OpenAPI 3.0.4 with 81 component schemas
  name: Debitura Customer API
  slug: debitura-customer-api
- description: For platforms embedding collection as a referral. Setting up clients, previewing cases, tracking revenue share, and minting bearer tokens through OAuth operations. 22 operations across 17 paths, OpenA
  name: Debitura Referral Partner API
  slug: debitura-referral-partner-api
- description: For collection agencies operating cases on the platform. Managed cases, bulk ingestion jobs, and the user and webhook surface behind them. 48 operations across 38 paths, OpenAPI 3.0.4 with 68 componen
  name: Debitura Collection Partner API
  slug: debitura-collection-partner-api
artifact_total: 6
collections:
- collection_type: open
  name: Debitura Collection Partner API
  slug: open-debitura-collection-partner-api
- collection_type: open
  name: Debitura Customer API
  slug: open-debitura-customer-api
- collection_type: open
  name: Debitura Referral Partner API
  slug: open-debitura-referral-partner-api
created: '2026-08-01'
description: 'Debitura is an API-first international debt collection platform covering cross-border B2B and B2C receivables. It publishes three separate public REST APIs, one per role in the network rather than one API with role-gated endpoints: the Customer API for creditors uploading invoices to collection and tracking cases, the Referral Partner API for platforms embedding collection as a referral and tracking revenue share, and the Collection Partner API for collection agencies operating cases on the platform. All three are OpenAPI 3.0.4, each on its own host, and each authenticates with an API key in the XApiKey header; the Customer API additionally accepts a bearer token, and the Referral Partner API exposes OAuth operations for minting them. Webhooks appear in all three, each with a paired test surface for exercising events before going live. Debitura publishes its own APIs.json at docs.debitura.com, which is how this profile was built.'
layout: provider
modified: '2026-08-01'
name: Debitura
nav: Providers
network: true
overview: 'Debitura publishes 3 APIs on the [APIs.io](https://apis.io/) network: Customer API, Referral Partner API, and Collection Partner API. Tagged areas include Debt Collection, Accounts Receivable, Debt Recovery, FinTech, and Payments.'
random_paper: 103
score:
  band: emerging
  composite: 18.4
  delta: 0.0
  facets:
    commercial_clarity: 0.0
    contract_quality: 58.2
    developer_ergonomics: 0.0
    discoverability: 70.4
    governance: 0.0
    operational_transparency: 0.0
  previous_composite: 18.4
  provenance:
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 3
  regulatory:
    applies: true
    matched_via: tags
    regime: Payments
    regime_id: payments
    score: 0.0
  schema_version: 0.11.0
  scored_at: '2026-08-17'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/debitura/refs/heads/main/screenshots/debitura-2026-08-07T164217.png
slug: debitura
tags:
- Debt Collection
- Accounts Receivable
- Debt Recovery
- FinTech
- Payments
- Invoicing
- Webhooks
---
