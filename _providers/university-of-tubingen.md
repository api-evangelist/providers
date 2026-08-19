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
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 3.0
  scored_at: '2026-08-19'
api_count: 2
apis:
- description: JSON REST API for the FDAT institutional research data repository, operated by the University of Tübingen Digital Humanities Center on the InvenioRDM platform. Provides programmatic access to publishe
  name: FDAT Repository REST API
  slug: fdat-rest
- description: OAI-PMH 2.0 metadata harvesting endpoint for the FDAT research data repository. Exposes dataset metadata in DataCite and Dublin Core formats for harvesting by discovery and aggregation services. Admin
  name: FDAT Repository OAI-PMH
  slug: fdat-oai
artifact_total: 7
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/university-of-tubingen-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://uni-tuebingen.de/en/
- group: build
  title: ''
  type: GitHub
  url: https://github.com/ubtue
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/university-of-tuebingen
- group: build
  title: ''
  type: SourceCode
  url: https://github.com/se-tuebingen
- group: commercial
  title: ''
  type: Plans
  url: plans/university-of-tubingen-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/university-of-tubingen-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/university-of-tubingen-finops.yml
- group: other
  title: ''
  type: Review
  url: review.yml
created: '2026-06-03'
description: 'The University of Tübingen (Eberhard Karls Universität Tübingen), founded in 1477 in Tübingen, Germany, is one of the oldest universities in the country and ranks #222 in the QS World University Rankings 2025. It is a public research university serving roughly 23,000 to 35,000 students. Its publicly documented developer/API footprint is modest and centers on its institutional research data repository, FDAT, run by the Digital Humanities Center on the InvenioRDM platform, which exposes a JSON REST API and an OAI-PMH metadata harvesting endpoint. Source code from several university units is published across multiple GitHub organizations, including the University Library.'
finops:
- name: University Of Tubingen Finops
  service_category: Education
  slug: university-of-tubingen-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/university-of-tubingen.png
jsonld:
- class_count: 20
  name: University Of Tubingen Context
  property_count: 11
  slug: university-of-tubingen-context
layout: provider
modified: '2026-06-03'
name: University of Tübingen
nav: Providers
network: true
overview: 'University of Tübingen publishes 2 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Education, Higher Education, University, Research Data, and Germany.


  The University of Tübingen catalog on APIs.io includes 1 JSON-LD context.


  University of Tübingen''s developer surface includes GitHub presence and 8 more developer resources.'
plans:
- name: University Of Tubingen Plans Pricing
  plan_count: 2
  slug: university-of-tubingen-plans-pricing
random_paper: 50
rate_limits:
- limit_count: 1
  name: University Of Tubingen Rate Limits
  slug: university-of-tubingen-rate-limits
score:
  band: emerging
  composite: 18.8
  delta: -1.7
  facets:
    access_clarity: 28.9
    commercial_clarity: 28.9
    contract_governance: 0.0
    contract_quality: 15.5
    developer_ergonomics: 0.0
    discoverability: 68.5
    governance: 0.0
    operational_transparency: 26.3
  previous_composite: 20.5
  regulatory:
    applies: true
    matched_via: tags
    regime: Education & Research
    regime_id: education
    score: 20.4
  schema_version: 0.12.0
  scored_at: '2026-08-19'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/university-of-tubingen/refs/heads/main/screenshots/university-of-tubingen-2026-06-20T200240.png
security:
- kind: domain-security
  name: University Of Tubingen Domain Security
  slug: university-of-tubingen-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: university-of-tubingen
tags:
- Education
- Higher Education
- University
- Research Data
- Germany
- Open Data
website: https://uni-tuebingen.de/en/
---
