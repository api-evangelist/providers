---
access_model:
  confidence: high
  label: Self-serve signup
  onboarding: self-serve
  pricing: unknown
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
- acting_count: 4
  human_in_the_loop: 0
  name: Nirvana Agentic Access
  operation_count: 4
  slug: nirvana-agentic-access
  summary_line: 4 operations · 4 acting
api_count: 4
apis:
- description: Real-time per-session patient cost estimates.
  name: Nirvana Health Cost Estimation API
  slug: nirvana-cost-estimation-api
- description: Multi-payer coverage discovery.
  name: Nirvana Health Coverage Scan API
  slug: nirvana-coverage-scan-api
- description: Active-coverage discovery and eligibility verification.
  name: Nirvana Health Eligibility API
  slug: nirvana-eligibility-api
- description: Medicaid coverage and eligibility.
  name: Nirvana Health Medicaid API
  slug: nirvana-medicaid-api
artifact_total: 11
collections:
- collection_type: open
  name: Nirvana Coverage API
  slug: open-nirvana
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/nirvana-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/nirvana-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/nirvana-authentication.yml
- group: company
  title: ''
  type: Blog
  url: https://www.meetnirvana.com/blog
created: '2026-06-21'
description: Nirvana is a real-time insurance eligibility, benefits, and patient cost-estimation platform purpose-built for behavioral and mental health. Its Coverage API normalizes complex payer data into structured JSON, returning eligibility, plan-level benefits, patient cost-share, session limits, and prior authorization details, and can recover active coverage from only basic patient demographics.
finops:
- name: Nirvana Finops
  service_category: Healthcare and Insurance
  slug: nirvana-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/nirvana.png
layout: provider
modified: '2026-06-21'
name: Nirvana Health
nav: Providers
network: true
overview: 'Nirvana Health publishes 4 APIs on the [APIs.io](https://apis.io/) network, including Cost Estimation API, Coverage Scan API, Eligibility API, and 1 more. Tagged areas include Healthcare, Insurance, Eligibility, Benefits, and Cost Estimation.


  Nirvana Health''s developer surface includes authentication, engineering blog, and 2 more developer resources.'
plans:
- name: Nirvana Plans Pricing
  plan_count: 1
  slug: nirvana-plans-pricing
random_paper: 73
rate_limits:
- limit_count: 1
  name: Nirvana Rate Limits
  slug: nirvana-rate-limits
score:
  band: thin
  composite: 32.0
  delta: 0.0
  facets:
    commercial_clarity: 28.9
    contract_quality: 63.6
    developer_ergonomics: 13.0
    discoverability: 74.1
    governance: 0.0
    operational_transparency: 21.1
  previous_composite: 32.0
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
    regime: Insurance
    regime_id: insurance
    score: 18.2
  schema_version: 0.9.1
  scored_at: '2026-08-06'
  trend: flat
security:
- kind: authentication
  name: Nirvana Authentication
  slug: nirvana-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Nirvana Domain Security
  slug: nirvana-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: nirvana
tags:
- Healthcare
- Insurance
- Eligibility
- Benefits
- Cost Estimation
- Behavioral Health
---
