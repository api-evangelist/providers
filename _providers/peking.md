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
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    auth_clarity: true
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
  score: 11.5
  scored_at: '2026-08-19'
api_count: 2
apis:
- description: 'The Peking University Open Research Data Platform is built on Dataverse and exposes the standard Dataverse native REST API for searching, retrieving, and managing dataverses, datasets, and files. The '
  name: PKU Open Research Data Platform (Dataverse REST API)
  slug: opendata-rest
- description: Live OAI-PMH 2.0 metadata-harvesting endpoint for the Peking University Open Research Data Platform Dataverse archive. Verified to respond to the Identify verb, supporting metadata standards including
  name: PKU Open Research Data Platform (OAI-PMH)
  slug: opendata-oaipmh
artifact_total: 7
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/peking-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://english.pku.edu.cn/
- group: build
  title: ''
  type: GitHub
  url: https://github.com/PKUHPC
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/school/peking-university/
- group: auth
  title: ''
  type: Authentication
  url: https://iaaa.pku.edu.cn/
- group: build
  title: ''
  type: SourceCode
  url: https://github.com/pengchengluo/Peking-University-Open-Research-Data-Platform
- group: commercial
  title: ''
  type: Plans
  url: plans/peking-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/peking-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/peking-finops.yml
- group: other
  title: ''
  type: Review
  url: review.yml
created: '2026-06-03'
description: 'Peking University (PKU) is a major public research university in Beijing, China, ranked #25 in the QS World University Rankings 2025. Its most clearly documented public, machine-readable API footprint is the Peking University Open Research Data Platform, a Dataverse-based research data repository operated by the PKU Library that exposes both the native Dataverse REST API and a live OAI-PMH 2.0 metadata-harvesting endpoint. Campus identity is handled by the PKU IAAA unified authentication system (a CAS/SSO service), which is gated and not a public developer API. No general-purpose institutional developer portal was found at the time of review.'
finops:
- name: Peking Finops
  service_category: Education
  slug: peking-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/peking.png
jsonld:
- class_count: 17
  name: Peking Context
  property_count: 4
  slug: peking-context
layout: provider
modified: '2026-06-03'
name: Peking University
nav: Providers
network: true
overview: 'Peking University publishes 2 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Education, Higher Education, University, Research Data, and Open Data.


  The Peking University catalog on APIs.io includes 1 JSON-LD context.


  Peking University''s developer surface includes GitHub presence, authentication, and 8 more developer resources.'
plans:
- name: Peking Plans Pricing
  plan_count: 2
  slug: peking-plans-pricing
random_paper: 42
rate_limits:
- limit_count: 1
  name: Peking Rate Limits
  slug: peking-rate-limits
score:
  band: emerging
  composite: 20.7
  delta: -2.3
  facets:
    access_clarity: 28.9
    commercial_clarity: 28.9
    contract_governance: 0.0
    contract_quality: 11.3
    developer_ergonomics: 6.0
    discoverability: 68.5
    governance: 0.0
    operational_transparency: 26.3
  previous_composite: 23.0
  regulatory:
    applies: true
    matched_via: tags
    regime: Education & Research
    regime_id: education
    score: 31.5
  schema_version: 0.12.0
  scored_at: '2026-08-19'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/peking/refs/heads/main/screenshots/peking-2026-06-20T191532.png
security:
- kind: domain-security
  name: Peking Domain Security
  slug: peking-domain-security
  summary_line: TLSv1.2 · HSTS · DMARC
slug: peking
tags:
- Education
- Higher Education
- University
- Research Data
- Open Data
- China
website: https://english.pku.edu.cn/
---
