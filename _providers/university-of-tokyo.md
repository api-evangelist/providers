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
api_count: 2
apis:
- description: The University of Tokyo Academic Assets Archives shared server publishes digitized collections via the International Image Interoperability Framework (IIIF). IIIF Image and Presentation APIs (manifest
  name: UTokyo Digital Archive Portal (IIIF)
  slug: digital-archive-iiif
- description: The UTokyo Repository is the University of Tokyo's institutional repository (running the WEKO platform) for storing and disseminating digital research outputs including journal articles, theses, repor
  name: UTokyo Repository OAI-PMH
  slug: repository-oai-pmh
artifact_total: 7
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/university-of-tokyo-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.u-tokyo.ac.jp/en/
- group: build
  title: ''
  type: GitHub
  url: https://github.com/utda
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/school/university-of-tokyo/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://da.dl.itc.u-tokyo.ac.jp/portal/en/help/api
- group: build
  title: ''
  type: SourceCode
  url: https://github.com/utda/dataset
- group: commercial
  title: ''
  type: Plans
  url: plans/university-of-tokyo-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/university-of-tokyo-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/university-of-tokyo-finops.yml
- group: other
  title: ''
  type: Review
  url: review.yml
created: '2026-06-03'
description: 'The University of Tokyo (UTokyo) is Japan''s leading national research university, founded in 1877 and ranked #29 in the QS World University Rankings 2025. Its public, machine-readable developer footprint is centered on its library and digital humanities infrastructure rather than a unified developer portal. Confirmed public APIs include the UTokyo Academic Assets Archives (utda) Digital Archive Portal, which exposes IIIF-compliant image and presentation APIs plus downloadable IIIF Collections and JSON-LD/RDF metadata datasets, and the UTokyo Repository (WEKO) institutional repository, which offers an OAI-PMH 2.0 metadata harvesting endpoint. No general-purpose, authenticated REST developer program (course/SIS/timetable APIs) was found publicly documented.'
finops:
- name: University Of Tokyo Finops
  service_category: Education
  slug: university-of-tokyo-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/university-of-tokyo.png
jsonld:
- class_count: 22
  name: University Of Tokyo Context
  property_count: 1
  slug: university-of-tokyo-context
layout: provider
modified: '2026-06-03'
name: University of Tokyo
nav: Providers
network: true
overview: 'University of Tokyo publishes 2 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Education, Higher Education, University, Japan, and Research.


  The University of Tokyo catalog on APIs.io includes 1 JSON-LD context.


  University of Tokyo''s developer surface includes GitHub presence and 9 more developer resources.'
plans:
- name: University Of Tokyo Plans Pricing
  plan_count: 2
  slug: university-of-tokyo-plans-pricing
random_paper: 16
rate_limits:
- limit_count: 1
  name: University Of Tokyo Rate Limits
  slug: university-of-tokyo-rate-limits
score:
  band: emerging
  composite: 20.1
  delta: -2.8
  facets:
    commercial_clarity: 28.9
    contract_quality: 12.9
    developer_ergonomics: 8.7
    discoverability: 59.3
    governance: 0.0
    operational_transparency: 26.3
  previous_composite: 22.9
  regulatory:
    applies: true
    matched_via: tags
    regime: Government & Public Sector
    regime_id: government
    score: 20.4
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/university-of-tokyo/refs/heads/main/screenshots/university-of-tokyo-2026-06-20T200308.png
security:
- kind: domain-security
  name: University Of Tokyo Domain Security
  slug: university-of-tokyo-domain-security
  summary_line: TLSv1.2 · HSTS · DMARC
slug: university-of-tokyo
tags:
- Education
- Higher Education
- University
- Japan
- Research
- Library
- Digital Archives
- IIIF
- Open Data
- OAI-PMH
website: https://www.u-tokyo.ac.jp/en/
---
