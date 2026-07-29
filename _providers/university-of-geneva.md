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
    agentic_access: derived
    asyncapi_events: false
    auth_clarity: false
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 21.6
  scored_at: '2026-07-28'
agentic_access:
- acting_count: 148
  human_in_the_loop: 0
  name: University Of Geneva Agentic Access
  operation_count: 337
  slug: university-of-geneva-agentic-access
  summary_line: 337 operations · 148 acting
api_count: 5
apis:
- description: OAI-PMH 2.0 metadata-harvesting interface for the Archive ouverte UNIGE institutional repository, exposing the University's scientific publications and records in multiple metadata formats (Dublin Cor
  name: Archive ouverte UNIGE OAI-PMH
  slug: archive-ouverte-oai
- description: Terminus is a UNIGE-developed prediction service for protein N-terminal modifications (initial methionine cleavage and N-terminal acetylation) across taxonomic groups. It accepts protein sequences via
  name: Terminus Protein Prediction API
  slug: terminus
- description: Discover, order and download archives (AIP/DIP).
  name: University of Geneva Access API
  slug: university-of-geneva-access-api
- description: Deposit, validate and submit research data.
  name: University of Geneva Ingest API
  slug: university-of-geneva-ingest-api
- description: OAI-PMH provider information and metadata formats.
  name: University of Geneva OAI-PMH API
  slug: university-of-geneva-oai-pmh-api
artifact_total: 24
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/university-of-geneva-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/university-of-geneva-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.unige.ch/
- group: build
  title: ''
  type: GitHub
  url: https://github.com/dis-unige
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/school/university-of-geneva/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://www.unige.ch/eresearch/en/
- group: commercial
  title: ''
  type: Plans
  url: plans/university-of-geneva-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/university-of-geneva-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/university-of-geneva-finops.yml
- group: other
  title: ''
  type: Review
  url: review.yml
- group: company
  title: ''
  type: Blog
  url: https://www.unige.ch/feed/rss
created: '2026-06-03'
description: 'The University of Geneva (Université de Genève, UNIGE) is a public research university in Geneva, Switzerland, founded in 1559, and ranked #93 in the QS World University Rankings 2025. Its public developer and API footprint is centered on open science and research infrastructure operated by the Division of Scientific Information (DIS) and the e-Research services: the Archive ouverte UNIGE institutional repository exposes metadata via a live OAI-PMH endpoint, the Yareta research-data-management platform (built on the DLCM stack) offers a REST API for preservation and access, and domain research groups publish specialized services such as the Terminus protein-prediction API. UNIGE maintains a public GitHub organization (dis-unige) for library and data tooling. There is no single unified public developer portal; most APIs are research- or service-specific.'
examples:
- key_count: 7
  name: University Of Geneva Aip Response Example
  slug: university-of-geneva-aip-response-example
- key_count: 5
  name: University Of Geneva Order Create Request Example
  slug: university-of-geneva-order-create-request-example
- key_count: 8
  name: University Of Geneva Order Response Example
  slug: university-of-geneva-order-response-example
- key_count: 5
  name: University Of Geneva Orgunit Response Example
  slug: university-of-geneva-orgunit-response-example
finops:
- name: University Of Geneva Finops
  service_category: Education
  slug: university-of-geneva-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/university-of-geneva.png
json_schemas:
- name: Yareta Archival Information Package (AIP)
  property_count: 33
  slug: university-of-geneva-aip
- name: Yareta Dissemination Information Package (DIP)
  property_count: 8
  slug: university-of-geneva-dip
- name: Yareta Order
  property_count: 19
  slug: university-of-geneva-order
- name: Yareta Organizational Unit
  property_count: 10
  slug: university-of-geneva-orgunit
json_structures:
- name: University Of Geneva Aip Structure
  property_count: 33
  slug: university-of-geneva-aip-structure
- name: University Of Geneva Order Structure
  property_count: 19
  slug: university-of-geneva-order-structure
- name: University Of Geneva Orgunit Structure
  property_count: 10
  slug: university-of-geneva-orgunit-structure
jsonld:
- class_count: 30
  name: University Of Geneva Context
  property_count: 5
  slug: university-of-geneva-context
layout: provider
modified: '2026-06-03'
name: University of Geneva
nav: Providers
network: true
overview: 'University of Geneva publishes 3 APIs on the [APIs.io](https://apis.io/) network: Access API, Ingest API, and OAI-PMH API. Tagged areas include Education, Higher Education, University, Open Science, and Research Data.


  The University of Geneva catalog on APIs.io includes 1 JSON-LD context and 2 Spectral governance rulesets.


  University of Geneva''s developer surface includes GitHub presence, engineering blog, and 9 more developer resources.'
plans:
- name: University Of Geneva Plans Pricing
  plan_count: 2
  slug: university-of-geneva-plans-pricing
random_paper: 55
rate_limits:
- limit_count: 1
  name: University Of Geneva Rate Limits
  slug: university-of-geneva-rate-limits
rules:
- name: University of Geneva API Rules
  rule_count: 6
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 4
  slug: university-of-geneva-jsonschema-spectral-rules
- name: University of Geneva API Rules
  rule_count: 7
  severity_counts:
    error: 0
    hint: 0
    info: 3
    warn: 4
  slug: university-of-geneva-rules
score:
  band: thin
  composite: 38.8
  delta: -3.6
  facets:
    commercial_clarity: 28.9
    contract_quality: 55.6
    developer_ergonomics: 10.9
    discoverability: 64.8
    governance: 58.3
    operational_transparency: 26.3
  previous_composite: 42.4
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 3
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/university-of-geneva/refs/heads/main/screenshots/university-of-geneva-2026-06-20T200151.png
security:
- kind: domain-security
  name: University Of Geneva Domain Security
  slug: university-of-geneva-domain-security
  summary_line: TLSv1.3 · DNSSEC · DMARC
slug: university-of-geneva
tags:
- Education
- Higher Education
- University
- Open Science
- Research Data
- Institutional Repository
- Switzerland
- Europe
website: https://www.unige.ch/
---
