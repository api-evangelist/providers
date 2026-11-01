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
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: documented
    openapi_examples: verified
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: verified
    rate_limit_signal: derived
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 30.0
  scored_at: '2026-10-31'
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
  href: https://artifacts.apis.io/serif-health/capabilities/serif-health-capability-edges.yml
  title: ''
  type: CapabilityMap
  url: capabilities/serif-health-capability-edges.yml
- group: agent
  href: https://artifacts.apis.io/serif-health/agentic-access/serif-health-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/serif-health-agentic-access.yml
- group: auth
  href: https://artifacts.apis.io/serif-health/security/serif-health-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/serif-health-domain-security.yml
- group: auth
  href: https://artifacts.apis.io/serif-health/authentication/serif-health-authentication.yml
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
  href: https://artifacts.apis.io/serif-health/plans/serif-health-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/serif-health-plans-pricing.yml
- group: operate
  href: https://artifacts.apis.io/serif-health/rate-limits/serif-health-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/serif-health-rate-limits.yml
- group: commercial
  href: https://artifacts.apis.io/serif-health/finops/serif-health-finops.yml
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
- has_sources: true
  method: generated
  name: Serif Health Finops
  primary_unit: ''
  service_category: Healthcare Data and Analytics
  slug: serif-health-finops
  template: false
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/serif-health.png
layout: provider
mcp_servers:
- description: Remote MCP server at mcp.serifhealth.com over HTTP.
  name: Serif Health MCP Server
  slug: serif-health
modified: '2026-06-21'
name: Serif Health
nav: Providers
network: true
overview: 'Serif Health publishes 4 API contracts indexed on the [APIs.io](https://apis.io/) network, including Distributions API, Rates API, and 2 more. Tagged areas include Healthcare, Price Transparency, Negotiated Rates, Payers, and Data.


  Serif Health''s developer surface includes authentication, documentation, engineering blog, and 9 more developer resources.'
plans:
- name: Serif Health Plans Pricing
  plan_count: 4
  slug: serif-health-plans-pricing
random_paper: 12
rate_limits:
- limit_count: 2
  name: Serif Health Rate Limits
  slug: serif-health-rate-limits
score:
  band: thin
  composite: 27.1
  coverage:
    artifact_dirs: 13
    catalog_earned: 37.0
    catalog_earned_first_party: 0.0
    catalog_gap: 78.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 7.9
    contract_governance: 0.0
    contract_quality: 49.6
    developer_ergonomics: 32.1
    discoverability: 57.1
    operational_transparency: 10.5
  previous_composite: 27.1
  provenance:
    agentic_access: derived
    contracts:
      callable: 0.0
      derived: 0
      marker_coverage: 0.0
      total: 2
    mcp: first-party
  regulatory:
    applies: true
    matched_via: tags
    regime: Health
    regime_id: health
    score: 9.4
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
screenshot: https://apis.io/screenshots/serif-health/serif-health-2026-09-02T155111.png
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
- Payers
- Data
website: https://www.serifhealth.com
---
