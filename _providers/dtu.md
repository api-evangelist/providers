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
    auth_clarity: true
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
  score: 30.6
  scored_at: '2026-07-28'
agentic_access:
- acting_count: 0
  human_in_the_loop: 0
  name: Dtu Agentic Access
  operation_count: 7
  slug: dtu-agentic-access
  summary_line: 7 operations
api_count: 3
apis:
- description: DTU Orbit is DTU's research information database (publications, projects, activities, researcher and department profiles), built on Elsevier Pure. The public web portal is openly browsable and searcha
  name: DTU Orbit Research Database (Pure)
  slug: orbit
- description: The articles API from Technical University of Denmark — 6 operation(s) for articles.
  name: Technical University of Denmark articles API
  slug: dtu-articles-api
- description: The institutions API from Technical University of Denmark — 1 operation(s) for institutions.
  name: Technical University of Denmark institutions API
  slug: dtu-institutions-api
artifact_total: 18
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/dtu-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/dtu-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.dtu.dk/english
- group: build
  title: ''
  type: GitHub
  url: https://github.com/dtudk
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/school/technical-university-of-denmark/
- group: auth
  title: ''
  type: Authentication
  url: https://auth.dtu.dk/
- group: commercial
  title: ''
  type: Plans
  url: plans/dtu-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/dtu-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/dtu-finops.yml
- group: other
  title: ''
  type: Review
  url: review.yml
- group: company
  title: ''
  type: Blog
  url: https://www.dtu.dk/english/news/all-news
created: '2026-06-03'
description: 'The Technical University of Denmark (DTU) is a leading engineering and science university in Kongens Lyngby, Denmark, ranked #109 in the QS World University Rankings 2025. DTU''s public developer/API footprint is research- and metadata-oriented rather than a unified developer program: its DTU Data research repository is built on the Figshare platform and exposes the open Figshare REST API (institution id 379), and the DTU Orbit research database runs on Elsevier Pure. DTU also maintains a public GitHub organization (dtudk) hosting affiliated open-source software. Identity is handled through DTU''s federated SSO (Shibboleth/OCES). There is no consolidated public developer portal documenting institution-wide APIs.'
examples:
- key_count: 3
  name: Dtu Get Article Example
  slug: dtu-get-article-example
- key_count: 3
  name: Dtu List Articles Example
  slug: dtu-list-articles-example
finops:
- name: Dtu Finops
  service_category: Education
  slug: dtu-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/dtu.png
json_schemas:
- name: DTU Data Article (Complete)
  property_count: 7
  slug: dtu-article
- name: DTU Data Author
  property_count: 7
  slug: dtu-author
- name: DTU Data Article File
  property_count: 8
  slug: dtu-file
json_structures:
- name: Dtu Article Structure
  property_count: 24
  slug: dtu-article-structure
- name: Dtu File Structure
  property_count: 8
  slug: dtu-file-structure
jsonld:
- class_count: 5
  name: Dtu Context
  property_count: 6
  slug: dtu-context
layout: provider
modified: '2026-06-03'
name: Technical University of Denmark
nav: Providers
network: true
overview: 'Technical University of Denmark publishes 2 APIs on the [APIs.io](https://apis.io/) network: articles API and institutions API. Tagged areas include Education, Higher Education, University, Research Data, and Open Data.


  The Technical University of Denmark catalog on APIs.io includes 1 JSON-LD context and 2 Spectral governance rulesets.


  Technical University of Denmark''s developer surface includes GitHub presence, authentication, engineering blog, and 8 more developer resources.'
plans:
- name: Dtu Plans Pricing
  plan_count: 2
  slug: dtu-plans-pricing
random_paper: 13
rate_limits:
- limit_count: 1
  name: Dtu Rate Limits
  slug: dtu-rate-limits
rules:
- name: Technical University of Denmark API Rules
  rule_count: 6
  severity_counts:
    error: 0
    hint: 0
    info: 1
    warn: 5
  slug: dtu-jsonschema-spectral-rules
- name: Technical University of Denmark API Rules
  rule_count: 7
  severity_counts:
    error: 1
    hint: 0
    info: 1
    warn: 5
  slug: dtu-rules
score:
  band: thin
  composite: 39.9
  delta: -4.7
  facets:
    commercial_clarity: 28.9
    contract_quality: 64.4
    developer_ergonomics: 13.0
    discoverability: 64.8
    governance: 58.3
    operational_transparency: 26.3
  previous_composite: 44.6
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 2
  regulatory:
    applies: true
    matched_via: tags
    regime: Government & Public Sector
    regime_id: government
    score: 31.5
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/dtu/refs/heads/main/screenshots/dtu-2026-06-20T180302.png
security:
- kind: domain-security
  name: Dtu Domain Security
  slug: dtu-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: dtu
tags:
- Education
- Higher Education
- University
- Research Data
- Open Data
- Denmark
- Europe
website: https://www.dtu.dk/english
---
