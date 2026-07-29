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
    openapi_examples: verified
    rate_limit_signal: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 27.9
  scored_at: '2026-07-28'
agentic_access:
- acting_count: 0
  human_in_the_loop: 0
  name: Ntu Agentic Access
  operation_count: 6
  slug: ntu-agentic-access
  summary_line: 6 operations
api_count: 6
apis:
- description: The Discover API from Nanyang Technological University — 1 operation(s) for discover.
  name: Nanyang Technological University Discover API
  slug: ntu-discover-api
- description: The Info API from Nanyang Technological University — 1 operation(s) for info.
  name: Nanyang Technological University Info API
  slug: ntu-info-api
- description: The Items API from Nanyang Technological University — 1 operation(s) for items.
  name: Nanyang Technological University Items API
  slug: ntu-items-api
- description: The OAI-PMH API from Nanyang Technological University — 1 operation(s) for oai-pmh.
  name: Nanyang Technological University OAI-PMH API
  slug: ntu-oai-pmh-api
- description: The Root API from Nanyang Technological University — 1 operation(s) for root.
  name: Nanyang Technological University Root API
  slug: ntu-root-api
- description: The Search API from Nanyang Technological University — 1 operation(s) for search.
  name: Nanyang Technological University Search API
  slug: ntu-search-api
artifact_total: 20
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/ntu-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/ntu-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.ntu.edu.sg/
- group: build
  title: ''
  type: GitHub
  url: https://github.com/NTUsg
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/school/nanyang-technological-university/
- group: commercial
  title: ''
  type: Plans
  url: plans/ntu-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/ntu-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/ntu-finops.yml
- group: other
  title: ''
  type: Review
  url: review.yml
- group: design
  title: ''
  type: x-vocabulary
  url: vocabulary/ntu-vocabulary.yml
- group: design
  title: ''
  type: x-spectral-rules
  url: rules/ntu-rules.yml
- group: design
  title: ''
  type: x-json-ld-context
  url: json-ld/ntu-context.jsonld
created: '2026-06-03'
description: 'Nanyang Technological University (NTU Singapore) is a public research university in Singapore and is ranked #15 in the QS World University Rankings 2025. NTU''s public, machine-readable footprint is concentrated in its library and research infrastructure: DR-NTU (Data), a Dataverse-based open research data repository, exposes a documented HTTP API, and DR-NTU (Digital Repository of NTU), a DSpace 7 / DSpace-CRIS institutional repository, exposes a REST API and an OAI-PMH endpoint. Other institutional systems (student information, timetabling, mobile app backends, SSO) are present but not publicly documented as open APIs.'
examples:
- key_count: 2
  name: Ntu Discover Example
  slug: ntu-discover-example
- key_count: 2
  name: Ntu Search Example
  slug: ntu-search-example
finops:
- name: Ntu Finops
  service_category: Education
  slug: ntu-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/ntu.png
json_schemas:
- name: DR-NTU (Data) Dataset Search Item
  property_count: 23
  slug: ntu-dataset
- name: DR-NTU (Digital Repository) Item
  property_count: 9
  slug: ntu-item
json_structures:
- name: Ntu Dataset Structure
  property_count: 21
  slug: ntu-dataset-structure
- name: Ntu Item Structure
  property_count: 9
  slug: ntu-item-structure
jsonld:
- class_count: 16
  name: Ntu Context
  property_count: 12
  slug: ntu-context
layout: provider
modified: '2026-06-03'
name: Nanyang Technological University
nav: Providers
network: true
overview: 'Nanyang Technological University publishes 6 APIs on the [APIs.io](https://apis.io/) network, including Discover API, Info API, Items API, and 3 more. Tagged areas include Education, Higher Education, University, Singapore, and Research Data.


  The Nanyang Technological University catalog on APIs.io includes 1 JSON-LD context and 2 Spectral governance rulesets.


  Nanyang Technological University''s developer surface includes GitHub presence and 11 more developer resources.'
plans:
- name: Ntu Plans Pricing
  plan_count: 2
  slug: ntu-plans-pricing
random_paper: 19
rate_limits:
- limit_count: 1
  name: Ntu Rate Limits
  slug: ntu-rate-limits
rules:
- name: Nanyang Technological University API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 3
  slug: ntu-jsonschema-spectral-rules
- name: Nanyang Technological University API Rules
  rule_count: 7
  severity_counts:
    error: 2
    hint: 0
    info: 0
    warn: 5
  slug: ntu-rules
score:
  band: thin
  composite: 36.4
  delta: -4.2
  facets:
    commercial_clarity: 28.9
    contract_quality: 62.4
    developer_ergonomics: 0.0
    discoverability: 74.1
    governance: 58.3
    operational_transparency: 26.3
  previous_composite: 40.6
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 6
  regulatory:
    applies: true
    matched_via: tags
    regime: Government & Public Sector
    regime_id: government
    score: 20.4
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/ntu/refs/heads/main/screenshots/ntu-2026-06-20T190501.png
security:
- kind: domain-security
  name: Ntu Domain Security
  slug: ntu-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: ntu
tags:
- Education
- Higher Education
- University
- Singapore
- Research Data
- Open Data
- Repository
- Library
website: https://www.ntu.edu.sg/
---
