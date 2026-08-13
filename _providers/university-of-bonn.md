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
    auth_clarity: false
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 21.6
  scored_at: '2026-08-12'
agentic_access:
- acting_count: 0
  human_in_the_loop: 0
  name: University Of Bonn Agentic Access
  operation_count: 7
  slug: university-of-bonn-agentic-access
  summary_line: 7 operations
api_count: 5
apis:
- description: OAI-PMH (Open Archives Initiative Protocol for Metadata Harvesting) endpoint for the bonndata repository, supporting metadata harvesting of published research datasets (verified live via verb=Identify
  name: bonndata OAI-PMH Metadata Endpoint
  slug: bonndata-oai-pmh
- description: Retrieve published datasets, their versions, and export metadata.
  name: University of Bonn Datasets API
  slug: university-of-bonn-datasets-api
- description: Repository version and software information.
  name: University of Bonn Info API
  slug: university-of-bonn-info-api
- description: Aggregate repository metrics.
  name: University of Bonn Metrics API
  slug: university-of-bonn-metrics-api
- description: Search the published catalog of datasets, dataverses, and files.
  name: University of Bonn Search API
  slug: university-of-bonn-search-api
artifact_total: 20
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/university-of-bonn-agentic-access.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/university-of-bonn-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/university-of-bonn-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.uni-bonn.de/en
- group: build
  title: ''
  type: GitHub
  url: https://github.com/unibonn
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/school/university-of-bonn/
- group: commercial
  title: ''
  type: Plans
  url: plans/university-of-bonn-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/university-of-bonn-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/university-of-bonn-finops.yml
- group: other
  title: ''
  type: Review
  url: review.yml
- group: company
  title: ''
  type: Blog
  url: https://www.uni-bonn.de/news/rss.xml
created: '2026-06-03'
description: 'The University of Bonn (Rheinische Friedrich-Wilhelms-Universität Bonn) is a public research university in Bonn, Germany, ranked #227 in the QS World University Rankings 2025. Its primary public, machine-readable developer footprint is bonndata, the institutional cross-disciplinary research data repository built on the open-source Dataverse platform, which exposes a public Dataverse Native REST API and an OAI-PMH metadata harvesting endpoint. The university also maintains an official GitHub organization (unibonn) with code from across the institution. Most other systems (library Alma/Primo discovery, identity/SSO, student information systems) are operated through standard vendor platforms without separately published public developer portals.'
examples:
- key_count: 2
  name: University Of Bonn Info Version Example
  slug: university-of-bonn-info-version-example
- key_count: 2
  name: University Of Bonn Metrics Datasets Example
  slug: university-of-bonn-metrics-datasets-example
- key_count: 2
  name: University Of Bonn Search Example
  slug: university-of-bonn-search-example
finops:
- name: University Of Bonn Finops
  service_category: Education
  slug: university-of-bonn-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/university-of-bonn.png
json_schemas:
- name: bonnDataSearchItem
  property_count: 24
  slug: university-of-bonn-search-item
- name: bonnDataSearchResponse
  property_count: 2
  slug: university-of-bonn-search-response
json_structures:
- name: University Of Bonn Dataset Structure
  property_count: 22
  slug: university-of-bonn-dataset-structure
jsonld:
- class_count: 14
  name: University Of Bonn Context
  property_count: 8
  slug: university-of-bonn-context
layout: provider
modified: '2026-06-03'
name: University of Bonn
nav: Providers
network: true
overview: 'University of Bonn publishes 4 APIs on the [APIs.io](https://apis.io/) network, including Datasets API, Info API, Metrics API, and 1 more. Tagged areas include Education, Higher Education, University, Research Data, and Open Data.


  The University of Bonn catalog on APIs.io includes 1 JSON-LD context and 2 Spectral governance rulesets.


  University of Bonn''s developer surface includes GitHub presence, engineering blog, and 9 more developer resources.'
plans:
- name: University Of Bonn Plans Pricing
  plan_count: 2
  slug: university-of-bonn-plans-pricing
random_paper: 54
rate_limits:
- limit_count: 1
  name: University Of Bonn Rate Limits
  slug: university-of-bonn-rate-limits
rules:
- name: University of Bonn API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 3
  slug: university-of-bonn-jsonschema-spectral-rules
- name: University of Bonn API Rules
  rule_count: 6
  severity_counts:
    error: 1
    hint: 0
    info: 1
    warn: 4
  slug: university-of-bonn-rules
score:
  band: thin
  composite: 37.7
  delta: 0.0
  facets:
    commercial_clarity: 28.9
    contract_quality: 59.0
    developer_ergonomics: 2.2
    discoverability: 74.1
    governance: 58.3
    operational_transparency: 26.3
  previous_composite: 37.7
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 4
  regulatory:
    applies: true
    matched_via: tags
    regime: Government & Public Sector
    regime_id: government
    score: 31.5
  schema_version: 0.11.0
  scored_at: '2026-08-12'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/university-of-bonn/refs/heads/main/screenshots/university-of-bonn-2026-06-20T200139.png
security:
- kind: domain-security
  name: University Of Bonn Domain Security
  slug: university-of-bonn-domain-security
  summary_line: TLSv1.3 · DNSSEC · DMARC
- kind: vulnerability-disclosure
  name: University Of Bonn Vulnerability Disclosure
  slug: university-of-bonn-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: university-of-bonn
tags:
- Education
- Higher Education
- University
- Research Data
- Open Data
- Germany
website: https://www.uni-bonn.de/en
---
