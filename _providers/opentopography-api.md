---
access_model:
  confidence: medium
  label: Freemium
  onboarding: unknown
  pricing: freemium
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
    dry_run_mode: na
    dynamic_client_registration: false
    error_semantics: false
    event_surface_described: false
    idempotency: na
    mcp_server: false
    openapi_examples: verified
    protected_resource_metadata: false
    rate_limit_signal: derived
    reversibility_documented: na
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 21.6
  scored_at: '2026-10-17'
api_count: 1
apis:
- baseURL: /API
  baseurl_source: spec
  description: The Public API from OpenTopography API — 3 operation(s) for public.
  name: OpenTopography API Public API
  slug: opentopography-api-public-api
artifact_total: 8
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: OpenTopography Public API
  slug: open-opentopography-api-public-api
- collection_type: open
  name: OpenTopography API
  slug: open-opentopography-api
common:
- group: commercial
  href: https://raw.githubusercontent.com/api-evangelist/opentopography-api/refs/heads/main/plans/opentopography-api-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/opentopography-api-plans-pricing.yml
- group: operate
  href: https://raw.githubusercontent.com/api-evangelist/opentopography-api/refs/heads/main/rate-limits/opentopography-api-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/opentopography-api-rate-limits.yml
- group: commercial
  href: https://raw.githubusercontent.com/api-evangelist/opentopography-api/refs/heads/main/finops/opentopography-api-finops.yml
  title: ''
  type: FinOps
  url: finops/opentopography-api-finops.yml
- group: company
  title: ''
  type: Blog
  url: https://opentopography.org/news
- group: company
  title: ''
  type: BlogRSS
  url: https://opentopography.org/index.php/news/rss_2.0
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/opentopography-api/refs/heads/main/security/opentopography-api-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/opentopography-api-domain-security.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/opentopography
- group: company
  title: ''
  type: Website
  url: https://opentopography.org/
- group: start
  title: ''
  type: Portal
  url: https://portal.opentopography.org/
- group: docs
  title: ''
  type: Documentation
  url: https://portal.opentopography.org/apidocs
- group: company
  title: ''
  type: Blog
  url: https://opentopography.org/blog
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/OpenTopography
- group: operate
  title: ''
  type: Support
  url: https://opentopography.org/contact
- group: other
  title: ''
  type: Citations
  url: https://opentopography.org/citations
- group: commercial
  title: ''
  type: Privacy
  url: https://opentopography.org/privacy
- group: commercial
  title: ''
  type: TermsOfService
  url: https://opentopography.org/usageterms
created: '2024-11-14'
description: OpenTopography API is a web service that provides users with access to high-resolution topographic data and tools for analysis and visualization. The API allows users to query a vast collection of LiDAR and other topographic data from around the world, making it easier for researchers, engineers, and scientists to study the Earth's surface and its features.
finops:
- has_sources: false
  method: generated
  name: Opentopography Api Finops
  primary_unit: ''
  service_category: API
  slug: opentopography-api-finops
  template: true
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/opentopography-api.png
layout: provider
modified: '2026-10-06'
name: OpenTopography API
nav: Providers
network: true
overview: 'OpenTopography API publishes 1 API contract indexed on the [APIs.io](https://apis.io/) network: Public API. Tagged areas include DEM, Data, Elevation, Geospatial, and LiDAR.


  OpenTopography API''s developer surface includes engineering blog, developer portal, documentation, support, privacy policy, and 11 more developer resources.'
plans:
- name: Opentopography Api Plans Pricing
  plan_count: 3
  slug: opentopography-api-plans-pricing
random_paper: 2
rate_limits:
- limit_count: 5
  name: Opentopography Api Rate Limits
  slug: opentopography-api-rate-limits
score:
  band: thin
  composite: 30.7
  coverage:
    artifact_dirs: 9
    catalog_earned: 38.0
    catalog_earned_first_party: 0.0
    catalog_gap: 77.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -1.5
  facets:
    access_clarity: 42.1
    contract_governance: 0.0
    contract_quality: 39.2
    developer_ergonomics: 26.2
    discoverability: 57.1
    operational_transparency: 13.2
  previous_composite: 32.2
  provenance:
    contracts:
      callable: 0.0
      derived: 0
      marker_coverage: 0.0
      total: 1
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 13.7
  schema_version: 0.24.0
  scored_at: '2026-10-17'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: this provider''s published contracts declare no write operations, and a read-only API cannot create-or-update. Excluded from the denominator, not zeroed.'
    reason: read_only
screenshot: https://raw.githubusercontent.com/api-evangelist/opentopography-api/refs/heads/main/screenshots/opentopography-api-2026-06-20T191044.png
security:
- kind: domain-security
  name: Opentopography Api Domain Security
  slug: opentopography-api-domain-security
  summary_line: TLSv1.3 · DMARC
slug: opentopography-api
tags:
- DEM
- Data
- Elevation
- Geospatial
- LiDAR
- Topographical
- Topography
website: https://opentopography.org/
---
