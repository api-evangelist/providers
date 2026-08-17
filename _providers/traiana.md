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
  scored_at: '2026-08-17'
agentic_access:
- acting_count: 10
  human_in_the_loop: 0
  name: Traiana Agentic Access
  operation_count: 26
  slug: traiana-agentic-access
  summary_line: 26 operations · 10 acting
api_count: 10
apis:
- description: The Allocations API from Traiana — 1 operation(s) for allocations.
  name: Traiana Allocations API
  slug: traiana-allocations-api
- description: The Compression API from Traiana — 1 operation(s) for compression.
  name: Traiana Compression API
  slug: traiana-compression-api
- description: The Credit Limits API from Traiana — 4 operation(s) for credit limits.
  name: Traiana Credit Limits API
  slug: traiana-credit-limits-api
- description: The Designation Notices API from Traiana — 1 operation(s) for designation notices.
  name: Traiana Designation Notices API
  slug: traiana-designation-notices-api
- description: The Give-Ups API from Traiana — 1 operation(s) for give-ups.
  name: Traiana Give-Ups API
  slug: traiana-give-ups-api
- description: The Matching API from Traiana — 1 operation(s) for matching.
  name: Traiana Matching API
  slug: traiana-matching-api
- description: The Netting API from Traiana — 3 operation(s) for netting.
  name: Traiana Netting API
  slug: traiana-netting-api
- description: The Settlement API from Traiana — 2 operation(s) for settlement.
  name: Traiana Settlement API
  slug: traiana-settlement-api
- description: The Trades API from Traiana — 3 operation(s) for trades.
  name: Traiana Trades API
  slug: traiana-trades-api
- description: The Utilization API from Traiana — 1 operation(s) for utilization.
  name: Traiana Utilization API
  slug: traiana-utilization-api
artifact_total: 42
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Traiana Harmony CreditLink Allocations API
  slug: open-traiana-allocations-api
- collection_type: open
  name: Traiana Harmony CreditLink Allocations Compression API
  slug: open-traiana-compression-api
- collection_type: open
  name: Traiana Harmony CreditLink Allocations Credit Limits API
  slug: open-traiana-credit-limits-api
- collection_type: open
  name: Traiana Harmony CreditLink Allocations Designation Notices API
  slug: open-traiana-designation-notices-api
- collection_type: open
  name: Traiana Harmony CreditLink Allocations Give-Ups API
  slug: open-traiana-give-ups-api
- collection_type: open
  name: Traiana Harmony CreditLink API
  slug: open-traiana-harmony-creditlink
- collection_type: open
  name: Traiana Harmony NetLink API
  slug: open-traiana-harmony-netlink
- collection_type: open
  name: Traiana Harmony Trade Processing API
  slug: open-traiana-harmony-trade-processing
- collection_type: open
  name: Traiana Harmony CreditLink Allocations Matching API
  slug: open-traiana-matching-api
- collection_type: open
  name: Traiana Harmony CreditLink Allocations Netting API
  slug: open-traiana-netting-api
- collection_type: open
  name: Traiana Harmony CreditLink Allocations Settlement API
  slug: open-traiana-settlement-api
- collection_type: open
  name: Traiana Harmony CreditLink Allocations Trades API
  slug: open-traiana-trades-api
- collection_type: open
  name: Traiana Harmony CreditLink Allocations Utilization API
  slug: open-traiana-utilization-api
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/traiana-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/traiana-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/traiana-authentication.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/traiana
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/traiana
- group: docs
  title: ''
  type: Documentation
  url: https://www.cmegroup.com/services/traiana.html
- group: docs
  title: ''
  type: Documentation
  url: https://osttra.com/services/post-trade-processing/trade-processing/
- group: operate
  title: ''
  type: Support
  url: https://osttra.com/support/
- group: design
  title: ''
  type: Spectral
  url: rules/traiana-rules.yml
- group: design
  title: ''
  type: Vocabulary
  url: vocabulary/traiana-vocabulary.yml
created: '2025-01-01'
description: Traiana, part of CME Group and now operating under OSTTRA, is a leading market infrastructure technology provider offering pre-trade risk monitoring and automated post-trade processing for listed and OTC trading. Its Harmony network connects over 1,000 firms via a cloud-based platform supporting 15,000 cross-asset trading relationships and handling $2 trillion in daily transaction volume across FX, equities, equity derivatives, and exchange-traded derivatives.
examples:
- key_count: 10
  name: Traiana Get Credit Utilization Example
  slug: traiana-get-credit-utilization-example
- key_count: 4
  name: Traiana List Trades Example
  slug: traiana-list-trades-example
finops:
- name: Traiana Finops
  service_category: Post-Trade Network
  slug: traiana-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/traiana.png
json_schemas:
- name: Allocation
  property_count: 10
  slug: allocation
- name: Credit Limit
  property_count: 14
  slug: credit-limit
- name: Give-Up
  property_count: 12
  slug: give-up
- name: Netting Session
  property_count: 11
  slug: netting-session
- name: Settlement
  property_count: 12
  slug: settlement
- name: Trade
  property_count: 16
  slug: trade
json_structures:
- name: Traiana Trade Structure
  property_count: 0
  slug: traiana-trade-structure
jsonld:
- class_count: 22
  name: Traiana Context
  property_count: 18
  slug: traiana-context
layout: provider
modified: '2026-05-19'
name: Traiana
nav: Providers
network: true
overview: 'Traiana publishes 10 APIs on the [APIs.io](https://apis.io/) network, including Allocations API, Compression API, Credit Limits API, and 7 more. Tagged areas include Fintech, Foreign Exchange, Post-Trade Processing, and Risk Management.


  The Traiana catalog on APIs.io includes 1 JSON-LD context and 2 Spectral governance rulesets.


  Traiana''s developer surface includes authentication, documentation, support, and 7 more developer resources.'
plans:
- name: Traiana Plans Pricing
  plan_count: 1
  slug: traiana-plans-pricing
random_paper: 140
rate_limits:
- limit_count: 1
  name: Traiana Rate Limits
  slug: traiana-rate-limits
rules:
- name: Traiana API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 3
  slug: traiana-jsonschema-spectral-rules
- name: Traiana API Rules
  rule_count: 16
  severity_counts:
    error: 9
    hint: 0
    info: 0
    warn: 7
  slug: traiana-rules
score:
  band: thin
  composite: 41.5
  delta: 0.0
  facets:
    commercial_clarity: 13.2
    contract_quality: 75.7
    developer_ergonomics: 23.9
    discoverability: 55.6
    governance: 68.8
    operational_transparency: 10.5
  previous_composite: 41.5
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 10
  schema_version: 0.11.0
  scored_at: '2026-08-17'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/traiana/refs/heads/main/screenshots/traiana-2026-06-20T195541.png
security:
- kind: authentication
  name: Traiana Authentication
  slug: traiana-authentication
  summary_line: apiKey/http · 2 schemes
- kind: domain-security
  name: Traiana Domain Security
  slug: traiana-domain-security
  summary_line: TLSv1.3 · DNSSEC · DMARC
slug: traiana
tags:
- Fintech
- Foreign Exchange
- Post-Trade Processing
- Risk Management
---
