---
access_model:
  confidence: medium
  label: Freemium
  onboarding: unknown
  pricing: freemium
  public: false
  source:
  - plans
  trial: false
  try_now: false
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
    auth_clarity: false
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 21.6
  scored_at: '2026-08-10'
agentic_access:
- acting_count: 33
  human_in_the_loop: 3
  name: Lightning Labs Agentic Access
  operation_count: 71
  slug: lightning-labs-agentic-access
  summary_line: 71 operations · 33 acting · 3 human-in-the-loop
api_count: 1
apis:
- description: The Lightning API from Lightning Labs — 64 operation(s) for lightning.
  name: Lightning Labs Lightning API
  slug: lightning-labs-lightning-api
artifact_total: 7
collections:
- collection_type: open
  name: Lightning Labs LND API
  slug: open-lightning-labs
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/lightning-labs-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/lightning-labs-domain-security.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/lightning-labs-inc
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/lightningnetwork
- group: company
  title: ''
  type: Blog
  url: https://lightning.engineering/blog/
created: '2024-11-08'
description: At Lightning Labs, we develop software that powers the Lightning Network. Our open source, secure, and scalable Lightning systems enable users to send and receive money more efficiently than ever before. We also offer a series of verifiable, non-custodial Lightning-based financial services. We bridge the world of open source software and the next-generation of bitcoin financial software.
finops:
- name: Lightning Labs Finops
  service_category: API
  slug: lightning-labs-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/lightning-labs.png
layout: provider
modified: '2026-05-19'
name: Lightning Labs
nav: Providers
network: true
overview: 'Lightning Labs publishes 1 API on the [APIs.io](https://apis.io/) network: Lightning API. Tagged areas include Bitcoin, Crypto, Lightning Network, and Payments.


  Lightning Labs'' developer surface includes engineering blog and 4 more developer resources.'
plans:
- name: Lightning Labs Plans Pricing
  plan_count: 3
  slug: lightning-labs-plans-pricing
random_paper: 35
rate_limits:
- limit_count: 5
  name: Lightning Labs Rate Limits
  slug: lightning-labs-rate-limits
score:
  band: emerging
  composite: 25.1
  delta: 0.0
  facets:
    commercial_clarity: 39.5
    contract_quality: 38.8
    developer_ergonomics: 2.2
    discoverability: 50.0
    governance: 0.0
    operational_transparency: 36.8
  previous_composite: 25.1
  provenance:
    agentic_access: derived
    contracts:
      callable: 0.0
      derived: 0
      marker_coverage: 0.0
      total: 1
  regulatory:
    applies: true
    matched_via: tags
    regime: Payments
    regime_id: payments
    score: 9.4
  schema_version: 0.9.1
  scored_at: '2026-08-10'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/lightning-labs/refs/heads/main/screenshots/lightning-labs-2026-06-20T184519.png
security:
- kind: domain-security
  name: Lightning Labs Domain Security
  slug: lightning-labs-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: lightning-labs
tags:
- Bitcoin
- Crypto
- Lightning Network
- Payments
---
