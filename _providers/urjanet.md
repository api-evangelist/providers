---
access_model:
  confidence: high
  label: Enterprise · Self-serve signup
  onboarding: self-serve
  pricing: enterprise
  public: false
  source:
  - plans
  - authentication
  trial: false
  try_now: false
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
    auth_clarity: true
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
  score: 30.6
  scored_at: '2026-08-06'
agentic_access:
- acting_count: 7
  human_in_the_loop: 0
  name: Urjanet Agentic Access
  operation_count: 12
  slug: urjanet-agentic-access
  summary_line: 12 operations · 7 acting
api_count: 6
apis:
- description: The Authentication API from Urjanet — 1 operation(s) for authentication.
  name: Urjanet Authentication API
  slug: urjanet-authentication-api
- description: The Credentials & Connections API from Urjanet — 3 operation(s) for credentials & connections.
  name: Urjanet Credentials & Connections API
  slug: urjanet-credentials-connections-api
- description: The Meters API from Urjanet — 2 operation(s) for meters.
  name: Urjanet Meters API
  slug: urjanet-meters-api
- description: The Statements & Bills API from Urjanet — 3 operation(s) for statements & bills.
  name: Urjanet Statements & Bills API
  slug: urjanet-statements-bills-api
- description: The Users API from Urjanet — 1 operation(s) for users.
  name: Urjanet Users API
  slug: urjanet-users-api
- description: The Webhooks API from Urjanet — 1 operation(s) for webhooks.
  name: Urjanet Webhooks API
  slug: urjanet-webhooks-api
artifact_total: 13
collections:
- collection_type: open
  name: Urjanet Utility Cloud API
  slug: open-urjanet
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/urjanet-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/urjanet-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/urjanet-authentication.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/urjanet
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/urjanet-inc
- group: company
  title: ''
  type: Website
  url: https://urjanet.com/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.arcadia.com/v1.0-Utility-Cloud/reference/introduction
- group: commercial
  title: ''
  type: Plans
  url: plans/urjanet-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/urjanet-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/urjanet-finops.yml
created: '2026-06-21'
description: Urjanet (now part of Arcadia) is a utility-data aggregation platform that programmatically collects utility bill, statement, meter, and interval usage data from thousands of electricity, gas, water, waste, and telecom providers worldwide. Following Arcadia's 2022 acquisition, Urjanet's data access powers the Arcadia "Arc" / Utility Cloud platform, exposed through a REST API (base URL https://api.urjanet.com) for connecting utility credentials and retrieving normalized utility data. Pricing is sales-led and not publicly published.
finops:
- name: Urjanet Finops
  service_category: Data and Analytics
  slug: urjanet-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/urjanet.png
layout: provider
name: Urjanet
nav: Providers
network: true
overview: 'Urjanet publishes 6 APIs on the [APIs.io](https://apis.io/) network, including Authentication API, Credentials & Connections API, Meters API, and 3 more. Tagged areas include Utility Data, Energy, Utility Bills, Aggregation, and Meters.


  Urjanet''s developer surface includes authentication, documentation, and 8 more developer resources.'
plans:
- name: Urjanet Plans Pricing
  plan_count: 1
  slug: urjanet-plans-pricing
random_paper: 83
rate_limits:
- limit_count: 1
  name: Urjanet Rate Limits
  slug: urjanet-rate-limits
score:
  band: thin
  composite: 32.7
  delta: 0.0
  facets:
    commercial_clarity: 28.9
    contract_quality: 60.5
    developer_ergonomics: 19.6
    discoverability: 74.1
    governance: 0.0
    operational_transparency: 26.3
  previous_composite: 32.7
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 6
  regulatory:
    applies: true
    matched_via: tags
    regime: Energy & Utilities
    regime_id: energy_utilities
    score: 16.2
  schema_version: 0.9.1
  scored_at: '2026-08-06'
  trend: flat
security:
- kind: authentication
  name: Urjanet Authentication
  slug: urjanet-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Urjanet Domain Security
  slug: urjanet-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: urjanet
tags:
- Utility Data
- Energy
- Utility Bills
- Aggregation
- Meters
- Sustainability
website: https://urjanet.com/
---
