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
- acting_count: 0
  human_in_the_loop: 0
  name: Federal Communications Commission Agentic Access
  operation_count: 4
  slug: federal-communications-commission-agentic-access
  summary_line: 4 operations
api_count: 4
apis:
- description: Dataset catalog and resources
  name: Federal Communications Commission Datasets API
  slug: federal-communications-commission-datasets-api
- description: The Filings API from Federal Communications Commission — 1 operation(s) for filings.
  name: Federal Communications Commission Filings API
  slug: federal-communications-commission-filings-api
- description: Pirate Radio Broadcasting Database
  name: Federal Communications Commission Pirate Radio API
  slug: federal-communications-commission-pirate-radio-api
- description: The Proceedings API from Federal Communications Commission — 1 operation(s) for proceedings.
  name: Federal Communications Commission Proceedings API
  slug: federal-communications-commission-proceedings-api
artifact_total: 14
collections:
- collection_type: open
  name: FCC ECFS API
  slug: open-ecfs
- collection_type: open
  name: FCC Open Data API
  slug: open-opendata
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/federal-communications-commission-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/federal-communications-commission-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/federal-communications-commission-authentication.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/fcc
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/federal-communications-commission
- group: company
  title: ''
  type: Website
  url: https://www.fcc.gov/
- group: docs
  title: ''
  type: Documentation
  url: https://www.fcc.gov/reports-research/developers
created: '2024-12-03'
description: The Federal Communications Commission (FCC) regulates interstate and international communications by radio, television, wire, satellite, and cable in the United States. The FCC exposes public APIs including the Electronic Comment Filing System (ECFS) and the FCC Open Data portal.
finops:
- name: Federal Communications Commission Finops
  service_category: API
  slug: federal-communications-commission-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/federal-communications-commission.png
layout: provider
modified: '2026-05-19'
name: Federal Communications Commission
nav: Providers
network: true
overview: 'Federal Communications Commission publishes 4 APIs on the [APIs.io](https://apis.io/) network, including Datasets API, Filings API, Pirate Radio API, and 1 more. Tagged areas include Communications, Federal Government, and Open Data.


  The Federal Communications Commission catalog on APIs.io includes 2 Spectral governance rulesets.


  Federal Communications Commission''s developer surface includes authentication, documentation, and 5 more developer resources.'
plans:
- name: Federal Communications Commission Plans Pricing
  plan_count: 3
  slug: federal-communications-commission-plans-pricing
random_paper: 25
rate_limits:
- limit_count: 5
  name: Federal Communications Commission Rate Limits
  slug: federal-communications-commission-rate-limits
rules:
- name: Federal Communications Commission API Rules
  rule_count: 0
  severity_counts:
    error: 0
    hint: 0
    info: 0
    warn: 0
  slug: ecfs-rules
- name: Federal Communications Commission API Rules
  rule_count: 0
  severity_counts:
    error: 0
    hint: 0
    info: 0
    warn: 0
  slug: opendata-rules
score:
  band: thin
  composite: 36.4
  delta: 0.0
  facets:
    commercial_clarity: 39.5
    contract_quality: 58.1
    developer_ergonomics: 19.6
    discoverability: 64.8
    governance: 10.4
    operational_transparency: 36.8
  previous_composite: 36.4
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 4
  regulatory:
    applies: true
    matched_via: tags
    regime: Government & Public Sector
    regime_id: government
    score: 22.2
  schema_version: 0.9.1
  scored_at: '2026-08-06'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/federal-communications-commission/refs/heads/main/screenshots/federal-communications-commission-2026-06-20T181114.png
security:
- kind: authentication
  name: Federal Communications Commission Authentication
  slug: federal-communications-commission-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Federal Communications Commission Domain Security
  slug: federal-communications-commission-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
slug: federal-communications-commission
tags:
- Communications
- Federal Government
- Open Data
website: https://www.fcc.gov/
---
