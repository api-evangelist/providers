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
    auth_clarity: false
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: documented
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 3.2
  scored_at: '2026-08-03'
api_count: 3
apis:
- description: OAI-PMH 2.0 metadata harvesting endpoint for TSpace, the University of Toronto Libraries institutional research repository, now hosted on the Scholaris DSpace platform. Supports standard OAI verbs suc
  name: TSpace Institutional Repository (OAI-PMH)
  slug: tspace-oai-pmh
- description: DSpace REST API surface exposed by the Scholaris platform that hosts the University of Toronto TSpace institutional repository. Provides programmatic access to repository communities, collections, and
  name: TSpace DSpace REST API
  slug: tspace-dspace-rest
- description: Cobalt was a student-driven open-data project providing REST APIs for University of Toronto public information including courses, buildings, textbooks, food, athletics, exams, parking, and shuttles. T
  name: Cobalt Open Data API (deprecated)
  slug: cobalt
artifact_total: 8
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/university-of-toronto-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.utoronto.ca/
- group: build
  title: ''
  type: GitHub
  url: https://github.com/utoronto
- group: build
  title: ''
  type: SourceCode
  url: https://github.com/utlib
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/school/university-of-toronto/
- group: commercial
  title: ''
  type: Plans
  url: plans/university-of-toronto-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/university-of-toronto-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/university-of-toronto-finops.yml
- group: other
  title: ''
  type: Review
  url: review.yml
created: '2026-06-03'
description: 'The University of Toronto is Canada''s leading public research university, ranked #26 in the QS World University Rankings 2025. Its public developer and API footprint is modest and decentralized: the University of Toronto Libraries operate the TSpace institutional repository (now hosted on the Scholaris DSpace platform), which exposes a standards-based OAI-PMH 2.0 metadata endpoint and a DSpace REST API. Student-facing course and timetable data is served through the EASI Timetable Builder, but that interface is not publicly documented as a developer API. Historically, the student-driven Cobalt project published open-data APIs for UofT courses, buildings, and campus services, but it has been deprecated/archived since 2020.'
finops:
- name: University Of Toronto Finops
  service_category: Education
  slug: university-of-toronto-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/university-of-toronto.png
jsonld:
- class_count: 10
  name: University Of Toronto Context
  property_count: 4
  slug: university-of-toronto-context
layout: provider
modified: '2026-06-03'
name: University of Toronto
nav: Providers
network: true
overview: 'University of Toronto publishes 3 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Education, Higher Education, University, Research, and Open Data.


  The University of Toronto catalog on APIs.io includes 1 JSON-LD context.


  University of Toronto''s developer surface includes GitHub presence and 8 more developer resources.'
plans:
- name: University Of Toronto Plans Pricing
  plan_count: 2
  slug: university-of-toronto-plans-pricing
random_paper: 29
rate_limits:
- limit_count: 1
  name: University Of Toronto Rate Limits
  slug: university-of-toronto-rate-limits
score:
  band: emerging
  composite: 19.1
  delta: 0.0
  facets:
    commercial_clarity: 28.9
    contract_quality: 12.9
    developer_ergonomics: 0.0
    discoverability: 64.8
    governance: 0.0
    operational_transparency: 26.3
  previous_composite: 19.1
  regulatory:
    applies: true
    matched_via: tags
    regime: Government & Public Sector
    regime_id: government
    score: 20.4
  schema_version: 0.9
  scored_at: '2026-08-03'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/university-of-toronto/refs/heads/main/screenshots/university-of-toronto-2026-06-20T200245.png
security:
- kind: domain-security
  name: University Of Toronto Domain Security
  slug: university-of-toronto-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: university-of-toronto
tags:
- Education
- Higher Education
- University
- Research
- Open Data
- Canada
- Library
- Institutional Repository
website: https://www.utoronto.ca/
---
