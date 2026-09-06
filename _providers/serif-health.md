---
access_model:
  confidence: medium
  label: Paid
  onboarding: unknown
  pricing: paid
  public: false
  source:
  - plans
  - authentication
  - security
  trial: false
  try_now: false
agent_readiness:
  band: agent-ready
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
    openapi_examples: verified
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: na
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 28.7
  scored_at: '2026-09-05'
agentic_access:
- acting_count: 0
  human_in_the_loop: 0
  name: Serif Health Agentic Access
  operation_count: 2
  slug: serif-health-agentic-access
  summary_line: 2 operations
api_count: 1
apis:
- description: Custom data pulls and extracts for specific EINs, NPIs, or taxonomy codes, delivered in common formats and optionally indexed back into the API by request.
  name: Serif Health Datasets & Extracts
  slug: datasets-extracts-api
- description: Live public inventory of 200+ payers with network-quality scoring, updated monthly, exposing data coverage and freshness across payer machine-readable files.
  name: Serif Health Payer Inventory
  slug: payer-inventory-api
- baseURL: https://pricing-api.serifhealth.com
  baseurl_source: declared
  description: The Distributions API from Serif Health — 1 operation(s) for distributions.
  name: Serif Health Distributions API
  slug: serif-health-distributions-api
- baseURL: https://pricing-api.serifhealth.com
  baseurl_source: declared
  description: The Rates API from Serif Health — 1 operation(s) for rates.
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
- group: other
  title: ''
  type: CapabilityMap
  url: capabilities/serif-health-capability-edges.yml
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


  Serif Health''s developer surface includes authentication, documentation, engineering blog, and 9 more developer resources.'
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
  composite: 35.6
  coverage:
    artifact_dirs: 11
    catalog_earned: 60.0
    catalog_earned_first_party: 0.0
    catalog_gap: 55.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 39.5
    commercial_clarity: 39.5
    contract_governance: 0.0
    contract_quality: 55.1
    developer_ergonomics: 22.6
    discoverability: 68.5
    governance: 0.0
    operational_transparency: 23.7
  previous_composite: 35.6
  provenance:
    agentic_access: derived
    contracts:
      callable: 0.0
      derived: 0
      marker_coverage: 0.0
      total: 2
  regulatory:
    applies: true
    matched_via: tags
    regime: Health
    regime_id: health
    score: 15.0
  schema_version: 0.18.3
  scored_at: '2026-09-05'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/serif-health/refs/heads/main/screenshots/serif-health-2026-09-02T155111.png
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
