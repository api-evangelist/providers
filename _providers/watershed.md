---
access_model:
  confidence: low
  label: Free
  onboarding: unknown
  pricing: free
  public: false
  source:
  - plans
  - security
  trial: false
  try_now: false
agent_readiness:
  band: human-only
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    agentic_commerce: false
    auth_clarity: false
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    mcp_tool_quality: na
    openapi_examples: false
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: derived
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: '0.2'
  score: 0.6
  scored_at: '2026-11-06'
api_count: 1
apis:
- description: The Watershed Platform API enables programmatic ingestion of activity data, retrieval of computed emissions footprints, and integration with reporting and decarbonization workflows. API keys are manag
  name: Watershed Platform API
  slug: platform-api
artifact_total: 6
common:
- group: commercial
  href: https://artifacts.apis.io/watershed/plans/watershed-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/watershed-plans-pricing.yml
- group: operate
  href: https://artifacts.apis.io/watershed/rate-limits/watershed-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/watershed-rate-limits.yml
- group: commercial
  href: https://artifacts.apis.io/watershed/finops/watershed-finops.yml
  title: ''
  type: FinOps
  url: finops/watershed-finops.yml
- group: auth
  href: https://artifacts.apis.io/watershed/security/watershed-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/watershed-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/watershed/security/watershed-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/watershed-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://watershed.com/
- group: other
  title: ''
  type: Platform
  url: https://watershed.com/platform
- group: other
  title: ''
  type: Industries
  url: https://watershed.com/industry/technology
- group: other
  title: ''
  type: Customers
  url: https://watershed.com/customers
- group: other
  title: ''
  type: Marketplace
  url: https://watershed.com/marketplace
- group: company
  title: ''
  type: Blog
  url: https://watershed.com/blog
- group: company
  title: ''
  type: Careers
  url: https://watershed.com/careers
- group: other
  title: ''
  type: Dashboard
  url: https://dashboard.watershedclimate.com/
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/watershed-climate/
- group: build
  title: ''
  type: GitHub
  url: https://github.com/watershed-climate
created: '2026-05-23'
description: Watershed is an enterprise sustainability platform used by large companies to measure their carbon footprint, report against regulatory and voluntary frameworks, and act on decarbonization opportunities. The platform combines a library of 500,000+ emissions factors, pre-verified methodologies, and AI agents for data cleaning, analysis, and report drafting. Watershed exposes an API for automated data ingestion and reporting, alongside guided uploads, and publishes integrations for common enterprise data sources. API keys are provisioned to customers via the Watershed dashboard at dashboard.watershedclimate.com. Public developer documentation is limited; most API access is delivered through customer onboarding and partner enablement.
finops:
- has_sources: false
  method: generated
  name: Watershed Finops
  primary_unit: ''
  service_category: API
  slug: watershed-finops
  template: true
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/watershed.png
layout: provider
modified: '2026-05-23'
name: Watershed
nav: Providers
network: true
overview: 'Watershed is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Climate, Carbon Accounting, ESG, Sustainability, and Disclosure.


  Watershed''s developer surface includes engineering blog, GitHub presence, and 13 more developer resources.'
plans:
- name: Watershed Plans Pricing
  plan_count: 1
  slug: watershed-plans-pricing
random_paper: 7
rate_limits:
- limit_count: 2
  name: Watershed Rate Limits
  slug: watershed-rate-limits
score:
  band: minimal
  composite: 9.5
  coverage:
    artifact_dirs: 9
    catalog_earned: 36.0
    catalog_earned_first_party: 0.0
    catalog_gap: 79.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 5.3
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 2.4
    discoverability: 57.1
    operational_transparency: 21.1
  previous_composite: 9.5
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 11.8
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
screenshot: https://apis.io/screenshots/watershed/watershed-2026-10-11T194253.png
security:
- kind: domain-security
  name: Watershed Domain Security
  slug: watershed-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Watershed Vulnerability Disclosure
  slug: watershed-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: watershed
tags:
- Climate
- Carbon Accounting
- ESG
- Sustainability
- Disclosure
- CSRD
- SBTi
- Decarbonization
- Scope 3
- Enterprise
- Reporting
website: https://watershed.com/
---
