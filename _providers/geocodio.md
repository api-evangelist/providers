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
  band: agent-aware
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
    mcp_server: false
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 21.5
  scored_at: '2026-09-04'
agentic_access:
- acting_count: 4
  human_in_the_loop: 0
  name: Geocodio Agentic Access
  operation_count: 9
  slug: geocodio-agentic-access
  summary_line: 9 operations · 4 acting
api_count: 1
apis:
- baseURL: https://api.geocod.io/v1.7
  baseurl_source: declared
  description: Geocode or reverse geocode up to 10,000 records per request.
  name: Geocodio Batch API
  slug: geocodio-batch-api
- baseURL: https://api.geocod.io/v1.7
  baseurl_source: declared
  description: Convert addresses into coordinates.
  name: Geocodio Forward Geocoding API
  slug: geocodio-forward-geocoding-api
- baseURL: https://api.geocod.io/v1.7
  baseurl_source: declared
  description: Asynchronous spreadsheet geocoding jobs.
  name: Geocodio Lists API
  slug: geocodio-lists-api
- baseURL: https://api.geocod.io/v1.7
  baseurl_source: declared
  description: Convert coordinates into addresses.
  name: Geocodio Reverse Geocoding API
  slug: geocodio-reverse-geocoding-api
artifact_total: 18
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Geocodio Batch API
  slug: open-geocodio-batch-api
- collection_type: open
  name: Geocodio Batch Forward Geocoding API
  slug: open-geocodio-forward-geocoding-api
- collection_type: open
  name: Geocodio Batch Lists API
  slug: open-geocodio-lists-api
- collection_type: open
  name: Geocodio Batch Reverse Geocoding API
  slug: open-geocodio-reverse-geocoding-api
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
random_paper: 1
rate_limits:
- limit_count: 4
  name: Geocodio Rate Limits
  slug: geocodio-rate-limits
score:
  band: developing
  composite: 40.6
  coverage:
    artifact_dirs: 10
    catalog_earned: 64.0
    catalog_earned_first_party: 0.0
    catalog_gap: 51.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 47.4
    commercial_clarity: 47.4
    contract_governance: 0.0
    contract_quality: 54.4
    developer_ergonomics: 31.0
    discoverability: 68.5
    governance: 0.0
    operational_transparency: 34.2
  previous_composite: 40.6
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 4
  schema_version: 0.18.3
  scored_at: '2026-09-04'
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
