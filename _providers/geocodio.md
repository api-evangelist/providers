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
- acting_count: 4
  human_in_the_loop: 0
  name: Geocodio Agentic Access
  operation_count: 9
  slug: geocodio-agentic-access
  summary_line: 9 operations · 4 acting
api_count: 4
apis:
- description: Geocode or reverse geocode up to 10,000 records per request.
  name: Geocodio Batch API
  slug: geocodio-batch-api
- description: Convert addresses into coordinates.
  name: Geocodio Forward Geocoding API
  slug: geocodio-forward-geocoding-api
- description: Asynchronous spreadsheet geocoding jobs.
  name: Geocodio Lists API
  slug: geocodio-lists-api
- description: Convert coordinates into addresses.
  name: Geocodio Reverse Geocoding API
  slug: geocodio-reverse-geocoding-api
artifact_total: 13
collections:
- collection_type: open
  name: Geocodio API
  slug: open-geocodio
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/geocodio-agentic-access.yml
- group: auth
  title: ''
  type: TrustCenter
  url: security/geocodio-trust-center.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/geocodio-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/geocodio-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/geocodio-authentication.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/Geocodio
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/geocodio
- group: company
  title: ''
  type: Website
  url: https://www.geocod.io
- group: docs
  title: ''
  type: Documentation
  url: https://www.geocod.io/docs/
- group: commercial
  title: ''
  type: Plans
  url: plans/geocodio-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/geocodio-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/geocodio-finops.yml
- group: company
  title: ''
  type: Blog
  url: https://www.geocod.io/updates/rss.xml
created: '2026-06-21'
description: Geocodio is a US and Canada geocoding API that converts addresses to coordinates (forward), coordinates to addresses (reverse), processes batches and spreadsheet lists, and enriches results with appended data such as congressional and state legislative districts, census geographies, ACS demographics, school districts, and timezones. Authentication is via an api_key query parameter and the first 2,500 lookups per day are free.
finops:
- name: Geocodio Finops
  service_category: Maps and Geospatial
  slug: geocodio-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/geocodio.png
layout: provider
modified: '2026-06-21'
name: Geocodio
nav: Providers
network: true
overview: 'Geocodio publishes 4 APIs on the [APIs.io](https://apis.io/) network, including Batch API, Forward Geocoding API, Lists API, and 1 more. Tagged areas include Geocoding, Reverse Geocoding, Addresses, Data Append, and Census.


  Geocodio''s developer surface includes authentication, documentation, engineering blog, and 10 more developer resources.'
plans:
- name: Geocodio Plans Pricing
  plan_count: 3
  slug: geocodio-plans-pricing
random_paper: 21
rate_limits:
- limit_count: 4
  name: Geocodio Rate Limits
  slug: geocodio-rate-limits
score:
  band: thin
  composite: 40.6
  delta: -3.1
  facets:
    commercial_clarity: 47.4
    contract_quality: 58.5
    developer_ergonomics: 21.7
    discoverability: 74.1
    governance: 0.0
    operational_transparency: 36.8
  previous_composite: 43.7
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 4
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/geocodio/refs/heads/main/screenshots/geocodio-2026-07-25T215651.png
security:
- kind: authentication
  name: Geocodio Authentication
  slug: geocodio-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Geocodio Domain Security
  slug: geocodio-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Geocodio Vulnerability Disclosure
  slug: geocodio-vulnerability-disclosure
  summary_line: security.txt · contact published
- kind: trust-center
  name: Geocodio Trust Center
  slug: geocodio-trust-center
  summary_line: SOC 2, HIPAA, GDPR
slug: geocodio
tags:
- Geocoding
- Reverse Geocoding
- Addresses
- Data Append
- Census
website: https://www.geocod.io
---
