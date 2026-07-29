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
- acting_count: 0
  human_in_the_loop: 0
  name: Neighbor Agentic Access
  operation_count: 2
  slug: neighbor-agentic-access
  summary_line: 2 operations
api_count: 1
apis:
- description: The Public API from Neighbor — 2 operation(s) for public.
  name: Neighbor Public API
  slug: neighbor-public-api
artifact_total: 8
collections:
- collection_type: open
  name: Neighbor API
  slug: open-neighbor
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/neighbor-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/neighbor-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/neighbor-authentication.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/neiybor
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/neighbor
created: '2025-02-09'
description: The Neighbor API allows trusted hosts to retrieve reports related to their account, including active reservations and payout transfers.
finops:
- name: Neighbor Finops
  service_category: API
  slug: neighbor-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/neighbor.png
layout: provider
modified: '2026-05-19'
name: Neighbor
nav: Providers
network: true
overview: 'Neighbor publishes 1 API on the [APIs.io](https://apis.io/) network: Public API. Tagged areas include Storage, Marketplace, and Reporting.


  Neighbor''s developer surface includes authentication and 4 more developer resources.'
plans:
- name: Neighbor Plans Pricing
  plan_count: 3
  slug: neighbor-plans-pricing
random_paper: 76
rate_limits:
- limit_count: 5
  name: Neighbor Rate Limits
  slug: neighbor-rate-limits
score:
  band: thin
  composite: 34.9
  delta: -1.3
  facets:
    commercial_clarity: 39.5
    contract_quality: 60.2
    developer_ergonomics: 10.9
    discoverability: 50.0
    governance: 0.0
    operational_transparency: 36.8
  previous_composite: 36.2
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 1
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/neighbor/refs/heads/main/screenshots/neighbor-2026-06-20T190130.png
security:
- kind: authentication
  name: Neighbor Authentication
  slug: neighbor-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Neighbor Domain Security
  slug: neighbor-domain-security
  summary_line: TLSv1.2 · DNSSEC · DMARC
slug: neighbor
tags:
- Storage
- Marketplace
- Reporting
---
