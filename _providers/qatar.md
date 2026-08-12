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
  scored_at: '2026-08-11'
api_count: 2
apis:
- description: Open Archives Initiative Protocol for Metadata Harvesting (OAI-PMH 2.0) endpoint for QSpace, the Qatar University institutional repository (DSpace 7.6). Supports the standard Identify, ListRecords, Li
  name: QSpace OAI-PMH Metadata Endpoint
  slug: qspace-oai
- description: Public DSpace 7.6 REST/HAL API backing the QSpace institutional repository. The API root reports dspaceVersion "DSpace 7.6" and exposes HAL-linked resources for communities, collections, items, bitstr
  name: QSpace DSpace REST API
  slug: qspace-rest
artifact_total: 7
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/qatar-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.qu.edu.qa/
- group: build
  title: ''
  type: GitHub
  url: https://github.com/qataruniversity
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/school/qatar-university/
- group: commercial
  title: ''
  type: Plans
  url: plans/qatar-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/qatar-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/qatar-finops.yml
- group: other
  title: ''
  type: Review
  url: review.yml
created: '2026-06-03'
description: 'Qatar University is the national public research university of the State of Qatar, located in Doha, and ranked #122 in the QS World University Rankings 2025. Its public, machine-readable developer footprint is concentrated in QSpace, the university''s institutional repository running on DSpace 7.6, which exposes a public OAI-PMH metadata-harvesting endpoint and a public DSpace REST/HAL API for scholarly output and academic records. Most other institutional systems (Self-Service Banner SIS, library discovery, SSO/MFA) are gated behind authentication and do not publish open developer documentation.'
finops:
- name: Qatar Finops
  service_category: Education
  slug: qatar-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/qatar.png
jsonld:
- class_count: 33
  name: Qatar Context
  property_count: 0
  slug: qatar-context
layout: provider
modified: '2026-06-03'
name: Qatar University
nav: Providers
network: true
overview: 'Qatar University publishes 2 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Education, Higher Education, University, Qatar, and Middle East.


  The Qatar University catalog on APIs.io includes 1 JSON-LD context.


  Qatar University''s developer surface includes GitHub presence and 7 more developer resources.'
plans:
- name: Qatar Plans Pricing
  plan_count: 2
  slug: qatar-plans-pricing
random_paper: 73
rate_limits:
- limit_count: 1
  name: Qatar Rate Limits
  slug: qatar-rate-limits
score:
  band: emerging
  composite: 19.3
  delta: 0.0
  facets:
    commercial_clarity: 28.9
    contract_quality: 12.9
    developer_ergonomics: 0.0
    discoverability: 68.5
    governance: 0.0
    operational_transparency: 26.3
  previous_composite: 19.3
  schema_version: 0.11.0
  scored_at: '2026-08-11'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/qatar/refs/heads/main/screenshots/qatar-2026-06-20T192353.png
security:
- kind: domain-security
  name: Qatar Domain Security
  slug: qatar-domain-security
  summary_line: TLSv1.2 · HSTS · DMARC
slug: qatar
tags:
- Education
- Higher Education
- University
- Qatar
- Middle East
- Research
- Open Access
- Institutional Repository
- DSpace
- OAI-PMH
website: https://www.qu.edu.qa/
---
