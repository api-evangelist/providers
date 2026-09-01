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
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: na
    dynamic_client_registration: false
    error_semantics: false
    event_surface_described: false
    idempotency: na
    mcp_server: false
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: na
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 22.9
  scored_at: '2026-09-01'
agentic_access:
- acting_count: 0
  human_in_the_loop: 0
  name: Food And Drug Administration Agentic Access
  operation_count: 22
  slug: food-and-drug-administration-agentic-access
  summary_line: 22 operations
api_count: 1
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
artifact_total: 21
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: openFDA Animal & Veterinary API
  slug: open-food-and-drug-administration-animal-veterinary-api
- collection_type: open
  name: openFDA Animal & Veterinary Device API
  slug: open-food-and-drug-administration-device-api
- collection_type: open
  name: openFDA Animal & Veterinary Drug API
  slug: open-food-and-drug-administration-drug-api
- collection_type: open
  name: openFDA Animal & Veterinary Food API
  slug: open-food-and-drug-administration-food-api
- collection_type: open
  name: openFDA Animal & Veterinary Other API
  slug: open-food-and-drug-administration-other-api
- collection_type: open
  name: openFDA Animal & Veterinary Tobacco API
  slug: open-food-and-drug-administration-tobacco-api
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
overview: 'Food and Drug Administration publishes 6 APIs on the [APIs.io](https://apis.io/) network, including Animal & Veterinary API, Device API, Drug API, and 3 more. Tagged areas include Drugs, Devices, Federal-Government, Food Safety, and Public Data.


  The Food and Drug Administration catalog on APIs.io includes 1 Spectral governance ruleset.


  Food and Drug Administration''s developer surface includes authentication, documentation, GitHub presence, and 6 more developer resources.'
plans:
- name: Food And Drug Administration Plans Pricing
  plan_count: 3
  slug: food-and-drug-administration-plans-pricing
random_paper: 17
rate_limits:
- limit_count: 5
  name: Food And Drug Administration Rate Limits
  slug: food-and-drug-administration-rate-limits
rules:
- effective_rule_count: 0
  extends: []
  name: Food and Drug Administration API Rules
  rule_count: 0
  severity_counts:
    error: 0
    hint: 0
    info: 0
    warn: 0
  slug: openfda-rules
score:
  band: thin
  composite: 33.6
  coverage:
    artifact_dirs: 10
    catalog_gap: 69.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 26.3
    commercial_clarity: 26.3
    contract_governance: 0.0
    contract_quality: 49.0
    developer_ergonomics: 21.4
    discoverability: 68.5
    governance: 0.0
    operational_transparency: 28.9
  previous_composite: 33.6
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
  schema_version: 0.17.2
  scored_at: '2026-09-01'
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
- Federal-Government
- Food Safety
- Public Data
- Recalls
- Adverse Events
website: https://www.fda.gov/
---
