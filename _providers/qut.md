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
  scored_at: '2026-08-12'
api_count: 0
artifact_total: 5
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/qut-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.qut.edu.au/
- group: build
  title: ''
  type: GitHub
  url: https://github.com/eresearchqut
- group: company
  title: ''
  type: LinkedIn
  url: https://au.linkedin.com/school/queensland-university-of-technology/
- group: commercial
  title: ''
  type: Plans
  url: plans/qut-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/qut-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/qut-finops.yml
- group: other
  title: ''
  type: Review
  url: review.yml
- group: company
  title: ''
  type: About
  url: https://www.library.qut.edu.au/about/collections/qut-eprints/
created: '2026-06-03'
description: 'Queensland University of Technology (QUT) is a public research university based in Brisbane, Australia, ranked #213 in the QS World University Rankings 2025. QUT serves around 50,000 students with an applied emphasis in teaching and research. Its public, machine-accessible developer footprint is modest and centered on open research infrastructure: the QUT ePrints institutional repository exposes a live OAI-PMH metadata harvesting interface, and QUT maintains several active research-group GitHub organizations (eResearch, Centre for Robotics, Aerospace Systems, Digital Observatory). Most other institutional systems (Library Search built on Ex Libris Primo VE / Alma, the Timetable Planner, the QUT mobile app backend, and the SSO identity layer) are internal or gated and do not publish open developer documentation.'
finops:
- name: Qut Finops
  service_category: Education
  slug: qut-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/qut.png
jsonld:
- class_count: 19
  name: Qut Context
  property_count: 1
  slug: qut-context
layout: provider
modified: '2026-07-25'
name: Queensland University of Technology
nav: Providers
network: true
overview: 'Queensland University of Technology is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Education, Higher Education, University, Research, and Open Data.


  The Queensland University of Technology catalog on APIs.io includes 1 JSON-LD context.


  Queensland University of Technology''s developer surface includes GitHub presence and 8 more developer resources.'
plans:
- name: Qut Plans Pricing
  plan_count: 2
  slug: qut-plans-pricing
random_paper: 106
rate_limits:
- limit_count: 1
  name: Qut Rate Limits
  slug: qut-rate-limits
score:
  band: emerging
  composite: 17.9
  delta: 0.0
  facets:
    commercial_clarity: 28.9
    contract_quality: 12.9
    developer_ergonomics: 0.0
    discoverability: 50.0
    governance: 0.0
    operational_transparency: 26.3
  previous_composite: 17.9
  regulatory:
    applies: true
    matched_via: tags
    regime: Government & Public Sector
    regime_id: government
    score: 20.4
  schema_version: 0.11.0
  scored_at: '2026-08-12'
  trend: flat
security:
- kind: domain-security
  name: Qut Domain Security
  slug: qut-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: qut
tags:
- Education
- Higher Education
- University
- Research
- Open Data
- Australia
- OAI-PMH
website: https://www.qut.edu.au/
---
