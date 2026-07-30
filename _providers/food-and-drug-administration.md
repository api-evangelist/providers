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
  name: Food And Drug Administration Agentic Access
  operation_count: 22
  slug: food-and-drug-administration-agentic-access
  summary_line: 22 operations
api_count: 6
apis:
- description: Adverse events involving animal and veterinary products.
  name: Food and Drug Administration Animal & Veterinary API
  slug: food-and-drug-administration-animal-veterinary-api
- description: Device-related endpoints (adverse events, classifications, recalls, 510(k), PMA, UDI).
  name: Food and Drug Administration Device API
  slug: food-and-drug-administration-device-api
- description: Drug-related endpoints (adverse events, labeling, recalls, NDC).
  name: Food and Drug Administration Drug API
  slug: food-and-drug-administration-drug-api
- description: Food-related endpoints (enforcement reports, adverse events).
  name: Food and Drug Administration Food API
  slug: food-and-drug-administration-food-api
- description: Cross-cutting datasets (NSDE, substance, harmonized).
  name: Food and Drug Administration Other API
  slug: food-and-drug-administration-other-api
- description: Tobacco product problem reports.
  name: Food and Drug Administration Tobacco API
  slug: food-and-drug-administration-tobacco-api
artifact_total: 14
collections:
- collection_type: open
  name: openFDA API
  slug: open-openfda
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/food-and-drug-administration-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/food-and-drug-administration-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/food-and-drug-administration-authentication.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/fda
- group: company
  title: ''
  type: Website
  url: https://www.fda.gov/
- group: docs
  title: ''
  type: Documentation
  url: https://open.fda.gov/apis
- group: auth
  title: ''
  type: Authentication
  url: https://open.fda.gov/apis/authentication/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://open.fda.gov/terms/
- group: build
  title: ''
  type: GitHub
  url: https://github.com/FDA/openfda
created: '2024-12-03'
description: openFDA is an Elasticsearch-based public API that serves FDA data on drugs, devices, foods, animal/veterinary products, and tobacco. Each noun exposes one or more datasets including adverse events, recall enforcement reports, product labeling, classifications, registrations, and approvals.
finops:
- name: Food And Drug Administration Finops
  service_category: API
  slug: food-and-drug-administration-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/food-and-drug-administration.png
layout: provider
modified: '2026-05-19'
name: Food and Drug Administration
nav: Providers
network: true
overview: 'Food and Drug Administration publishes 6 APIs on the [APIs.io](https://apis.io/) network, including Animal & Veterinary API, Device API, Drug API, and 3 more. Tagged areas include Drugs, Devices, Federal Government, Food Safety, and Public Data.


  The Food and Drug Administration catalog on APIs.io includes 1 Spectral governance ruleset.


  Food and Drug Administration''s developer surface includes authentication, documentation, GitHub presence, and 6 more developer resources.'
plans:
- name: Food And Drug Administration Plans Pricing
  plan_count: 3
  slug: food-and-drug-administration-plans-pricing
random_paper: 22
rate_limits:
- limit_count: 5
  name: Food And Drug Administration Rate Limits
  slug: food-and-drug-administration-rate-limits
rules:
- name: Food and Drug Administration API Rules
  rule_count: 0
  severity_counts:
    error: 0
    hint: 0
    info: 0
    warn: 0
  slug: openfda-rules
score:
  band: thin
  composite: 39.2
  delta: -3.6
  facets:
    commercial_clarity: 50.0
    contract_quality: 54.2
    developer_ergonomics: 19.6
    discoverability: 74.1
    governance: 10.4
    operational_transparency: 36.8
  previous_composite: 42.8
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
    regime: Government & Public Sector
    regime_id: government
    score: 29.6
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/food-and-drug-administration/refs/heads/main/screenshots/food-and-drug-administration-2026-06-20T181356.png
security:
- kind: authentication
  name: Food And Drug Administration Authentication
  slug: food-and-drug-administration-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Food And Drug Administration Domain Security
  slug: food-and-drug-administration-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
slug: food-and-drug-administration
tags:
- Drugs
- Devices
- Federal Government
- Food Safety
- Public Data
- Recalls
- Adverse Events
website: https://www.fda.gov/
---
