---
access_model:
  confidence: medium
  label: Free
  onboarding: unknown
  pricing: free
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
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 15.5
  scored_at: '2026-09-01'
api_count: 1
apis:
- description: The Watershed Platform API enables programmatic ingestion of activity data, retrieval of computed emissions footprints, and integration with reporting and decarbonization workflows. API keys are manag
  name: Watershed Platform API
  slug: platform-api
artifact_total: 7
common:
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/watershed-vulnerability-disclosure.yml
- group: auth
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
- name: Watershed Finops
  service_category: API
  slug: watershed-finops
graphqls:
- description: Watershed is an enterprise climate platform for measuring, reducing, and reporting carbon emissions. The API covers footprint data ingestion, emission factor lookups, Scope 1/2/3 calculations, supplie
  name: Watershed GraphQL API
  slug: watershed-graphql
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/watershed.png
layout: provider
modified: '2026-05-23'
name: Watershed
nav: Providers
network: true
overview: 'Watershed publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Climate, Carbon Accounting, ESG, Sustainability, and Disclosure.


  Watershed''s developer surface includes engineering blog, GitHub presence, and 10 more developer resources.'
plans:
- name: Watershed Plans Pricing
  plan_count: 1
  slug: watershed-plans-pricing
random_paper: 1
rate_limits:
- limit_count: 2
  name: Watershed Rate Limits
  slug: watershed-rate-limits
score:
  band: emerging
  composite: 24.9
  coverage:
    artifact_dirs: 7
    catalog_gap: 64.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 28.9
    commercial_clarity: 28.9
    contract_governance: 0.0
    contract_quality: 37.2
    developer_ergonomics: 2.4
    discoverability: 59.3
    governance: 0.0
    operational_transparency: 26.3
  previous_composite: 24.9
  schema_version: 0.18.0
  scored_at: '2026-09-01'
  trend: flat
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
