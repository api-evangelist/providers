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
- description: GUPEA (Gothenburg University Publications Electronic Archive) is the university's DSpace-based institutional repository. It exposes an OAI-PMH 2.0 metadata harvesting endpoint (repository name "GUPEA"
  name: GUPEA Repository OAI-PMH Interface
  slug: gupea-oai-pmh
- description: 'The Quality of Government Institute at the University of Gothenburg publishes open-access governance datasets (Standard, Basic, OECD, and original datasets) available as direct file downloads in CSV, '
  name: Quality of Government (QoG) Open Data
  slug: qog-data
artifact_total: 7
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/university-of-gothenburg-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.gu.se/en
- group: build
  title: ''
  type: GitHub
  url: https://github.com/bcfgothenburg
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/school/university-of-gothenburg/
- group: commercial
  title: ''
  type: Plans
  url: plans/university-of-gothenburg-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/university-of-gothenburg-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/university-of-gothenburg-finops.yml
- group: other
  title: ''
  type: Review
  url: review.yml
created: '2026-06-03'
description: 'The University of Gothenburg (Göteborgs universitet) is a public research university in Sweden, founded in 1891, with roughly 37,000 students and 6,000 employees, and ranked #194 in the QS World University Rankings 2025. Its public, machine-accessible footprint is research- and library-centric rather than a unified developer program: the Gothenburg University Library operates the GUPEA institutional repository (DSpace) which exposes a standards-based OAI-PMH metadata interface, and the Quality of Government (QoG) Institute publishes open-access datasets via downloads and a Data Finder tool. The university does not appear to operate a central, documented developer portal with public REST API keys; affiliated technical work is distributed across departmental GitHub organizations.'
finops:
- name: University Of Gothenburg Finops
  service_category: Education
  slug: university-of-gothenburg-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/university-of-gothenburg.png
jsonld:
- class_count: 23
  name: University Of Gothenburg Context
  property_count: 3
  slug: university-of-gothenburg-context
layout: provider
modified: '2026-06-03'
name: University of Gothenburg
nav: Providers
network: true
overview: 'University of Gothenburg publishes 2 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Education, Higher Education, University, Sweden, and Research.


  The University of Gothenburg catalog on APIs.io includes 1 JSON-LD context.


  University of Gothenburg''s developer surface includes GitHub presence and 7 more developer resources.'
plans:
- name: University Of Gothenburg Plans Pricing
  plan_count: 2
  slug: university-of-gothenburg-plans-pricing
random_paper: 66
rate_limits:
- limit_count: 1
  name: University Of Gothenburg Rate Limits
  slug: university-of-gothenburg-rate-limits
score:
  band: emerging
  composite: 18.7
  delta: 0.0
  facets:
    commercial_clarity: 28.9
    contract_quality: 12.9
    developer_ergonomics: 0.0
    discoverability: 59.3
    governance: 0.0
    operational_transparency: 26.3
  previous_composite: 18.7
  regulatory:
    applies: true
    matched_via: tags
    regime: Government & Public Sector
    regime_id: government
    score: 20.4
  schema_version: 0.11.0
  scored_at: '2026-08-11'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/university-of-gothenburg/refs/heads/main/screenshots/university-of-gothenburg-2026-06-20T200152.png
security:
- kind: domain-security
  name: University Of Gothenburg Domain Security
  slug: university-of-gothenburg-domain-security
  summary_line: TLSv1.3 · DNSSEC · DMARC
slug: university-of-gothenburg
tags:
- Education
- Higher Education
- University
- Sweden
- Research
- Open Data
- Library
- OAI-PMH
website: https://www.gu.se/en
---
