---
access_model:
  confidence: medium
  label: Freemium · Self-serve signup
  onboarding: self-serve
  pricing: freemium
  public: false
  source:
  - plans
  - authentication
  - security
  trial: false
  try_now: true
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
    error_semantics: verified
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: verified
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 30.6
  scored_at: '2026-09-05'
agentic_access:
- acting_count: 1
  human_in_the_loop: 0
  name: Entso E Agentic Access
  operation_count: 2
  slug: entso-e-agentic-access
  summary_line: 2 operations · 1 acting
api_count: 1
apis:
- baseURL: https://web-api.tp.entsoe.eu/api
  baseurl_source: declared
  description: Single query endpoint for every Transparency Platform data item. The documentType, processType, and domain parameters select the dataset.
  name: ENTSO-E Market Data Query API
  slug: entso-e-market-data-query-api
artifact_total: 13
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: ENTSO-E Transparency Platform RESTful Market Data Query API
  slug: open-entso-e-market-data-query-api
- collection_type: open
  name: ENTSO-E Transparency Platform RESTful API
  slug: open-entso-e
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/entso-e-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/entso-e-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/entso-e-authentication.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/entso-e
- group: company
  title: ''
  type: Website
  url: https://www.entsoe.eu/
- group: start
  title: ''
  type: Portal
  url: https://transparency.entsoe.eu/
- group: docs
  title: ''
  type: Documentation
  url: https://transparencyplatform.zendesk.com/hc/en-us
- group: commercial
  title: ''
  type: Plans
  url: plans/entso-e-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/entso-e-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/entso-e-finops.yml
- group: company
  title: ''
  type: Blog
  url: https://www.entsoe.eu/news/
- group: other
  title: ''
  type: TransparencyPlatform
  url: https://transparency.entsoe.eu/
- group: other
  title: ''
  type: KnowledgeBase
  url: https://transparencyplatform.zendesk.com/hc/en-us
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/EnergieID/entsoe-py
- group: docs
  title: ''
  type: PostmanDocumentation
  url: https://documenter.getpostman.com/view/7009892/2s93JtP3F6
- group: other
  title: ''
  type: Registration
  url: https://transparency.entsoe.eu/usrm/user/createPublicUser
- group: operate
  title: ''
  type: Contact
  url: https://www.entsoe.eu/contact/
- group: company
  title: ''
  type: About
  url: https://www.entsoe.eu/about/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://transparency.entsoe.eu/content/static_content/Static%20content/web%20api/Guide.html
- group: other
  title: ''
  type: Email
  url: mailto:transparency@entsoe.eu
created: '2026-07-11'
description: ENTSO-E, the European Network of Transmission System Operators for Electricity, operates the Transparency Platform - the central publication point for pan-European electricity market data under EU Regulation 543/2013. Its free RESTful API returns day-ahead prices, system load, generation, balancing, and cross-border transmission data for every European bidding zone and control area as IEC 62325 XML market documents, selected by coded documentType and processType parameters against a single endpoint.
finops:
- name: Entso E Finops
  service_category: Analytics and Data
  slug: entso-e-finops
- name: Finops
  service_category: ''
  slug: finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/entso-e.png
layout: provider
modified: '2026-08-08'
name: ENTSO-E
nav: Providers
network: true
overview: 'ENTSO-E publishes 1 API on the [APIs.io](https://apis.io/) network: Market Data Query API. Tagged areas include Electricity, Energy, Energy Markets, Day-Ahead Prices, and Balancing.


  ENTSO-E''s developer surface includes authentication, developer portal, documentation, engineering blog, and 16 more developer resources.'
plans:
- name: Entso E Plans Pricing
  plan_count: 1
  slug: entso-e-plans-pricing
- name: Plans
  plan_count: 1
  slug: plans
random_paper: 6
rate_limits:
- limit_count: 5
  name: Entso E Rate Limits
  slug: entso-e-rate-limits
- limit_count: 1
  name: Rate Limits
  slug: rate-limits
score:
  band: developing
  composite: 42.8
  coverage:
    artifact_dirs: 11
    catalog_earned: 60.0
    catalog_earned_first_party: 0.0
    catalog_gap: 55.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 47.4
    commercial_clarity: 47.4
    contract_governance: 0.0
    contract_quality: 55.1
    developer_ergonomics: 41.7
    discoverability: 68.5
    governance: 0.0
    operational_transparency: 34.2
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
    regions:
    - europe
  previous_composite: 42.8
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 1
  regulatory:
    applies: true
    matched_via: tags
    regime: Energy & Utilities
    regime_id: energy_utilities
    score: 18.9
  schema_version: 0.18.3
  scored_at: '2026-09-05'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/entso-e/refs/heads/main/screenshots/entso-e-2026-07-25T213441.png
security:
- kind: authentication
  name: Entso E Authentication
  slug: entso-e-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Entso E Domain Security
  slug: entso-e-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
slug: entso-e
tags:
- Electricity
- Energy
- Energy Markets
- Day-Ahead Prices
- Balancing
- Transmission
- Grid Data
- Europe
website: https://www.entsoe.eu/
---
