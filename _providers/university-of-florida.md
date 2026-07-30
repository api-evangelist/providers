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
  band: human-only
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    asyncapi_events: false
    auth_clarity: false
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: documented
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 3.2
  scored_at: '2026-07-28'
api_count: 3
apis:
- description: Public JSON endpoint serving the University of Florida Schedule of Courses. Accepts query parameters such as term, category, course-code, credits, instructor and day filters, and returns course listin
  name: UF Schedule of Courses (SOC) API
  slug: soc-schedule
- description: Public JSON datasets backing the UF interactive campus map, including building footprints, bus stops, dining locations, parking lots and housing with coordinates and metadata. Community documented; ho
  name: UF Campus Map JSON Data
  slug: campus-map
- description: The University of Florida Digital Collections host over 18 million files of books, archival documents, newspapers, photographs, audio, video and datasets. UFDC metadata is available as OAI-PMH and RSS
  name: UF Digital Collections (UFDC) Metadata Feeds
  slug: ufdc
artifact_total: 8
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/university-of-florida-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.ufl.edu/
- group: build
  title: ''
  type: GitHub
  url: https://github.com/UniversityofFlorida
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/school/university-of-florida/
- group: commercial
  title: ''
  type: Plans
  url: plans/university-of-florida-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/university-of-florida-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/university-of-florida-finops.yml
- group: other
  title: ''
  type: Review
  url: review.yml
created: '2026-06-03'
description: 'The University of Florida (UF) is a public land-grant research university in Gainesville, Florida, United States, and ranks #215 in the QS World University Rankings 2025. UF does not operate a single centralized public developer portal, but several public and community-documented HTTP/JSON data endpoints exist across its web properties: a Schedule of Courses (SOC) API served from one.ufl.edu, campus map JSON datasets, and the UF Digital Collections (UFDC) which exposes metadata via OAI-PMH and RSS. Most institutional APIs (identity, SIS, enterprise integrations) are gated behind UFIT authentication and are not publicly documented.'
finops:
- name: University Of Florida Finops
  service_category: Education
  slug: university-of-florida-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/university-of-florida.png
jsonld:
- class_count: 24
  name: University Of Florida Context
  property_count: 0
  slug: university-of-florida-context
layout: provider
modified: '2026-06-03'
name: University of Florida
nav: Providers
network: true
overview: 'University of Florida publishes 3 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Education, Higher Education, University, Courses, and Digital Collections.


  The University of Florida catalog on APIs.io includes 1 JSON-LD context.


  University of Florida''s developer surface includes GitHub presence and 7 more developer resources.'
plans:
- name: University Of Florida Plans Pricing
  plan_count: 2
  slug: university-of-florida-plans-pricing
random_paper: 30
rate_limits:
- limit_count: 1
  name: University Of Florida Rate Limits
  slug: university-of-florida-rate-limits
score:
  band: emerging
  composite: 19.1
  delta: -3.0
  facets:
    commercial_clarity: 28.9
    contract_quality: 12.9
    developer_ergonomics: 0.0
    discoverability: 64.8
    governance: 0.0
    operational_transparency: 26.3
  previous_composite: 22.1
  regulatory:
    applies: true
    matched_via: tags
    regime: Government & Public Sector
    regime_id: government
    score: 20.4
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/university-of-florida/refs/heads/main/screenshots/university-of-florida-2026-06-20T200148.png
security:
- kind: domain-security
  name: University Of Florida Domain Security
  slug: university-of-florida-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: university-of-florida
tags:
- Education
- Higher Education
- University
- Courses
- Digital Collections
- Open Data
- United States
website: https://www.ufl.edu/
---
