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
  scored_at: '2026-08-17'
api_count: 2
apis:
- description: OAI-PMH 2.0 metadata harvesting endpoint for "repository civitas UGM", the institutional repository running on EPrints 3. Returns Dublin Core metadata for scholarly works. Verified live via an Identif
  name: UGM Repository OAI-PMH
  slug: repository-oai-pmh
- description: Central Authentication Service (CAS) single sign-on used across UGM systems for students, staff, and lecturers. The CAS login endpoint is publicly reachable; it is an authentication service rather tha
  name: UGM Single Sign-On (CAS)
  slug: sso-cas
artifact_total: 7
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/gadjah-mada-university-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://ugm.ac.id/en/
- group: build
  title: ''
  type: GitHub
  url: https://github.com/ugm-ac-id
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/school/universitas-gadjah-mada/
- group: commercial
  title: ''
  type: Plans
  url: plans/gadjah-mada-university-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/gadjah-mada-university-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/gadjah-mada-university-finops.yml
- group: other
  title: ''
  type: Review
  url: review.yml
- group: design
  title: ''
  type: x-json-ld
  url: json-ld/gadjah-mada-university-context.jsonld
- group: company
  title: ''
  type: x-blogs
  url: blogs/blogs.json
created: '2026-06-03'
description: 'Gadjah Mada University (Universitas Gadjah Mada, UGM) is a public research university in Yogyakarta, Indonesia, and is ranked #239 in the QS World University Rankings 2025. Its public, machine-consumable developer footprint is limited: the institutional repository (EPrints "repository civitas UGM") exposes a working OAI-PMH 2.0 metadata endpoint for harvesting scholarly output, and the university operates a centralized CAS single sign-on service. Most academic and administrative systems (SIMASTER, admissions) sit behind authentication, and there is no public, documented developer portal.'
finops:
- name: Gadjah Mada University Finops
  service_category: Education
  slug: gadjah-mada-university-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/gadjah-mada-university.png
jsonld:
- class_count: 18
  name: Gadjah Mada University Context
  property_count: 4
  slug: gadjah-mada-university-context
layout: provider
modified: '2026-06-03'
name: Gadjah Mada University
nav: Providers
network: true
overview: 'Gadjah Mada University publishes 2 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Education, Higher Education, University, Indonesia, and Research.


  The Gadjah Mada University catalog on APIs.io includes 1 JSON-LD context.


  Gadjah Mada University''s developer surface includes GitHub presence and 9 more developer resources.'
plans:
- name: Gadjah Mada University Plans Pricing
  plan_count: 2
  slug: gadjah-mada-university-plans-pricing
random_paper: 136
rate_limits:
- limit_count: 1
  name: Gadjah Mada University Rate Limits
  slug: gadjah-mada-university-rate-limits
score:
  band: emerging
  composite: 19.4
  delta: 0.0
  facets:
    commercial_clarity: 28.9
    contract_quality: 12.9
    developer_ergonomics: 0.0
    discoverability: 68.5
    governance: 0.0
    operational_transparency: 26.3
  previous_composite: 19.4
  regulatory:
    applies: true
    matched_via: tags
    regime: Government & Public Sector
    regime_id: government
    score: 20.4
  schema_version: 0.11.0
  scored_at: '2026-08-17'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/gadjah-mada-university/refs/heads/main/screenshots/gadjah-mada-university-2026-06-20T181636.png
security:
- kind: domain-security
  name: Gadjah Mada University Domain Security
  slug: gadjah-mada-university-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: gadjah-mada-university
tags:
- Education
- Higher Education
- University
- Indonesia
- Research
- Open Data
- Library
- Repository
website: https://ugm.ac.id/en/
---
