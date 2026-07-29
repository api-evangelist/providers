---
access_model:
  confidence: high
  label: Freemium · Self-serve signup
  onboarding: self-serve
  pricing: freemium
  public: false
  source:
  - plans
  - authentication
  trial: false
  try_now: true
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
    asyncapi_events: false
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 30.6
  scored_at: '2026-07-28'
agentic_access:
- acting_count: 1
  human_in_the_loop: 0
  name: Handwrite Io Agentic Access
  operation_count: 4
  slug: handwrite-io-agentic-access
  summary_line: 4 operations · 1 acting
api_count: 4
apis:
- description: Available handwriting styles
  name: Handwrite IO Handwriting API
  slug: handwrite-io-handwriting-api
- description: Order tracking and status
  name: Handwrite IO Orders API
  slug: handwrite-io-orders-api
- description: Send handwritten notes
  name: Handwrite IO Send API
  slug: handwrite-io-send-api
- description: Available stationery and cards
  name: Handwrite IO Stationery API
  slug: handwrite-io-stationery-api
artifact_total: 12
collections:
- collection_type: open
  name: Handwrite IO API
  slug: open-handwrite-io
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/handwrite-io-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/handwrite-io-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/handwrite-io-authentication.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/handwrite
- group: company
  title: ''
  type: Website
  url: https://handwrite.io/
- group: docs
  title: ''
  type: Documentation
  url: https://documentation.handwrite.io/
created: '2024-11-14'
description: Handwrite IO provides a REST API that lets you send handwritten notes in an automated manner. Using the API, businesses can send personalized handwritten cards and notes at scale through REST endpoints.
finops:
- name: Handwrite Io Finops
  service_category: API
  slug: handwrite-io-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/handwrite-io.png
layout: provider
modified: '2026-05-19'
name: Handwrite IO
nav: Providers
network: true
overview: 'Handwrite IO publishes 4 APIs on the [APIs.io](https://apis.io/) network, including Handwriting API, Orders API, Send API, and 1 more. Tagged areas include Direct Mail, Handwritten, Marketing, and Notes.


  The Handwrite IO catalog on APIs.io includes 1 Spectral governance ruleset.


  Handwrite IO''s developer surface includes authentication, documentation, and 4 more developer resources.'
plans:
- name: Handwrite Io Plans Pricing
  plan_count: 3
  slug: handwrite-io-plans-pricing
random_paper: 12
rate_limits:
- limit_count: 5
  name: Handwrite Io Rate Limits
  slug: handwrite-io-rate-limits
rules:
- name: Handwrite IO API Rules
  rule_count: 0
  severity_counts:
    error: 0
    hint: 0
    info: 0
    warn: 0
  slug: handwrite-io-rules
score:
  band: thin
  composite: 38.7
  delta: -2.2
  facets:
    commercial_clarity: 39.5
    contract_quality: 60.2
    developer_ergonomics: 19.6
    discoverability: 64.8
    governance: 10.4
    operational_transparency: 31.6
  previous_composite: 40.9
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 4
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/handwrite-io/refs/heads/main/screenshots/handwrite-io-2026-06-20T182501.png
security:
- kind: authentication
  name: Handwrite Io Authentication
  slug: handwrite-io-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Handwrite Io Domain Security
  slug: handwrite-io-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: handwrite-io
tags:
- Direct Mail
- Handwritten
- Marketing
- Notes
website: https://handwrite.io/
---
