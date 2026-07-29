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
    asyncapi_events: false
    auth_clarity: false
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
  score: 21.6
  scored_at: '2026-07-28'
agentic_access:
- acting_count: 0
  human_in_the_loop: 0
  name: Httpstat Agentic Access
  operation_count: 2
  slug: httpstat-agentic-access
  summary_line: 2 operations
api_count: 2
apis:
- description: The Httpstat API from Httpstat.us — 1 operation(s) for httpstat.
  name: Httpstat.us Httpstat API
  slug: httpstat-httpstat-api
- description: The Random API from Httpstat.us — 1 operation(s) for random.
  name: Httpstat.us Random API
  slug: httpstat-random-api
artifact_total: 9
collections:
- collection_type: open
  name: httpstat
  slug: open-httpstat
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/httpstat-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/httpstat-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://httpstat.us/
- group: other
  title: ''
  type: Repository
  url: https://github.com/Readify/httpstatus
created: '2024-11-15'
description: httpstat.us is a super simple service for generating different HTTP status codes. It is useful for testing how your own scripts and applications deal with varying HTTP responses, allowing developers to simulate different server response scenarios.
finops:
- name: Httpstat Finops
  service_category: API
  slug: httpstat-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/httpstat.png
layout: provider
modified: '2026-05-19'
name: Httpstat.us
nav: Providers
network: true
overview: 'Httpstat.us publishes 2 APIs on the [APIs.io](https://apis.io/) network: Httpstat API and Random API. Tagged areas include HTTP, Status Codes, Testing, and Utilities.


  The Httpstat.us catalog on APIs.io includes 1 Spectral governance ruleset.'
plans:
- name: Httpstat Plans Pricing
  plan_count: 3
  slug: httpstat-plans-pricing
random_paper: 12
rate_limits:
- limit_count: 5
  name: Httpstat Rate Limits
  slug: httpstat-rate-limits
rules:
- name: Httpstat.us API Rules
  rule_count: 0
  severity_counts:
    error: 0
    hint: 0
    info: 0
    warn: 0
  slug: httpstat-rules
score:
  band: emerging
  composite: 27.6
  delta: -5.3
  facets:
    commercial_clarity: 39.5
    contract_quality: 47.5
    developer_ergonomics: 0.0
    discoverability: 59.3
    governance: 10.4
    operational_transparency: 31.6
  previous_composite: 32.9
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 2
  regulatory:
    applies: true
    matched_via: tags
    regime: Energy & Utilities
    regime_id: energy_utilities
    score: 8.1
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: falling
security:
- kind: domain-security
  name: Httpstat Domain Security
  slug: httpstat-domain-security
  summary_line: TLSv1.2
slug: httpstat
tags:
- HTTP
- Status Codes
- Testing
- Utilities
website: https://httpstat.us/
---
