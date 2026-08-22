---
access_model:
  confidence: high
  label: Paid · Self-serve signup
  onboarding: self-serve
  pricing: paid
  public: false
  source:
  - plans
  - authentication
  trial: false
  try_now: false
agent_readiness:
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
    auth_clarity: true
    consent_identity: false
    dry_run_mode: na
    error_semantics: false
    event_surface_described: false
    idempotency: na
    mcp_server: false
    openapi_examples: verified
    rate_limit_signal: documented
    reversibility_documented: na
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 41.8
  scored_at: '2026-08-19'
agentic_access:
- acting_count: 0
  human_in_the_loop: 0
  name: Serif Health Agentic Access
  operation_count: 2
  slug: serif-health-agentic-access
  summary_line: 2 operations
api_count: 4
apis:
- description: Custom data pulls and extracts for specific EINs, NPIs, or taxonomy codes, delivered in common formats and optionally indexed back into the API by request.
  name: Serif Health Datasets & Extracts
  slug: datasets-extracts-api
- description: Live public inventory of 200+ payers with network-quality scoring, updated monthly, exposing data coverage and freshness across payer machine-readable files.
  name: Serif Health Payer Inventory
  slug: payer-inventory-api
- description: The Distributions API from Serif Health — 1 operation(s) for distributions.
  name: Serif Health Distributions API
  slug: serif-health-distributions-api
- description: The Rates API from Serif Health — 1 operation(s) for rates.
  name: Serif Health Rates API
  slug: serif-health-rates-api
artifact_total: 14
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Serif Health Pricing Distributions API
  slug: open-serif-health-distributions-api
- collection_type: open
  name: Serif Health Pricing Distributions Rates API
  slug: open-serif-health-rates-api
- collection_type: open
  name: Serif Health Pricing API
  slug: open-serif-health
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/serif-health-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/serif-health-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/serif-health-authentication.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/serif-health
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/serif-health
- group: company
  title: ''
  type: Website
  url: https://www.serifhealth.com
- group: docs
  title: ''
  type: Documentation
  url: https://docs.serifhealth.com
- group: commercial
  title: ''
  type: Plans
  url: plans/serif-health-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/serif-health-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/serif-health-finops.yml
- group: company
  title: ''
  type: Blog
  url: https://www.serifhealth.com/blog
created: '2026-06-21'
description: Serif Health turns federal hospital and payer price-transparency disclosures (machine-readable files) into normalized, decision-ready negotiated-rate data. Its REST APIs let teams query negotiated reimbursement rates and rate distributions by CPT/DRG code, payer, provider, and geography, search for in-network providers, and pull custom datasets and extracts.
finops:
- name: Serif Health Finops
  service_category: Healthcare Data and Analytics
  slug: serif-health-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/serif-health.png
layout: provider
modified: '2026-06-21'
name: Serif Health
nav: Providers
network: true
overview: 'Serif Health publishes 2 APIs on the [APIs.io](https://apis.io/) network: Distributions API and Rates API. Tagged areas include Healthcare, Price Transparency, Negotiated Rates, Payer, and Data.


  Serif Health''s developer surface includes authentication, documentation, engineering blog, and 8 more developer resources.'
plans:
- name: Serif Health Plans Pricing
  plan_count: 4
  slug: serif-health-plans-pricing
random_paper: 15
rate_limits:
- limit_count: 2
  name: Serif Health Rate Limits
  slug: serif-health-rate-limits
score:
  band: thin
  composite: 35.7
  delta: 0.2
  facets:
    access_clarity: 39.5
    commercial_clarity: 39.5
    contract_governance: 0.0
    contract_quality: 60.1
    developer_ergonomics: 14.3
    discoverability: 74.1
    governance: 0.0
    operational_transparency: 23.7
  previous_composite: 35.5
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
    regime: Health
    regime_id: health
    score: 15.0
  schema_version: 0.12.0
  scored_at: '2026-08-19'
  trend: flat
security:
- kind: authentication
  name: Serif Health Authentication
  slug: serif-health-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Serif Health Domain Security
  slug: serif-health-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: serif-health
tags:
- Healthcare
- Price Transparency
- Negotiated Rates
- Payer
- Data
website: https://www.serifhealth.com
---
