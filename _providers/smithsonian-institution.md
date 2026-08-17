---
access_model:
  confidence: high
  label: Freemium · Self-serve signup
  onboarding: self-serve
  pricing: freemium
  public: false
  source:
  - plans
  - authentication
  trial: false
  try_now: true
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
    auth_clarity: true
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
  score: 30.6
  scored_at: '2026-08-17'
agentic_access:
- acting_count: 0
  human_in_the_loop: 0
  name: Smithsonian Institution Agentic Access
  operation_count: 5
  slug: smithsonian-institution-agentic-access
  summary_line: 5 operations
api_count: 3
apis:
- description: The Content API from Smithsonian Institution — 1 operation(s) for content.
  name: Smithsonian Institution Content API
  slug: smithsonian-institution-content-api
- description: The Metrics API from Smithsonian Institution — 1 operation(s) for metrics.
  name: Smithsonian Institution Metrics API
  slug: smithsonian-institution-metrics-api
- description: The Search API from Smithsonian Institution — 3 operation(s) for search.
  name: Smithsonian Institution Search API
  slug: smithsonian-institution-search-api
artifact_total: 20
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Smithsonian Open Access Content API
  slug: open-smithsonian-institution-content-api
- collection_type: open
  name: Smithsonian Open Access Content Metrics API
  slug: open-smithsonian-institution-metrics-api
- collection_type: open
  name: Smithsonian Open Access Content Search API
  slug: open-smithsonian-institution-search-api
- collection_type: open
  name: Smithsonian Open Access API
  slug: open-smithsonian-open-access
common:
- group: commercial
  title: ''
  type: License
  url: https://github.com/Smithsonian/smithsonian-openaccess/blob/main/LICENSE
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/smithsonian-institution-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/smithsonian-institution-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/smithsonian-institution-authentication.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/smithsonian-institution
- group: company
  title: ''
  type: Website
  url: https://www.si.edu/
- group: start
  title: ''
  type: Open Access Portal
  url: https://www.si.edu/openaccess
- group: build
  title: ''
  type: Developer Tools
  url: https://www.si.edu/openaccess/devtools
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/Smithsonian
- group: other
  title: ''
  type: Data Repository
  url: https://github.com/Smithsonian/OpenAccess
- group: auth
  title: ''
  type: API Key Registration
  url: https://api.data.gov/signup
- group: build
  title: ''
  type: Python Client
  url: https://github.com/Smithsonian/smithsonian-openaccess
- group: docs
  title: ''
  type: Metadata Documentation
  url: https://edan.si.edu/openaccess/docs/
created: '2024-12-25'
description: The Smithsonian Institution provides open access APIs to its collections of over 22 million objects, artworks, and natural history specimens from 19 museums, 21 libraries, and 9 research centers. The Open Access API enables developers to search and retrieve collection data, images, and metadata across the world's largest museum and research complex.
examples:
- key_count: 2
  name: Smithsonian Search Collections Example
  slug: smithsonian-search-collections-example
finops:
- name: Smithsonian Institution Finops
  service_category: API
  slug: smithsonian-institution-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/smithsonian-institution.png
json_schemas:
- name: Smithsonian Collection Item
  property_count: 7
  slug: smithsonian-collection-item
json_structures:
- name: Smithsonian Collection Item Structure
  property_count: 0
  slug: smithsonian-collection-item-structure
jsonld:
- class_count: 31
  name: Smithsonian Institution Context
  property_count: 0
  slug: smithsonian-institution-context
layout: provider
modified: '2026-05-19'
name: Smithsonian Institution
nav: Providers
network: true
overview: 'Smithsonian Institution publishes 3 APIs on the [APIs.io](https://apis.io/) network: Content API, Metrics API, and Search API. Tagged areas include Collections, Cultural Heritage, Museums, Open Data, and Art.


  The Smithsonian Institution catalog on APIs.io includes 1 JSON-LD context and 2 Spectral governance rulesets.


  Smithsonian Institution''s developer surface includes authentication and 12 more developer resources.'
plans:
- name: Smithsonian Institution Plans Pricing
  plan_count: 3
  slug: smithsonian-institution-plans-pricing
random_paper: 84
rate_limits:
- limit_count: 5
  name: Smithsonian Institution Rate Limits
  slug: smithsonian-institution-rate-limits
rules:
- name: Smithsonian Institution API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 3
  slug: smithsonian-institution-jsonschema-spectral-rules
- name: Smithsonian Institution API Rules
  rule_count: 8
  severity_counts:
    error: 2
    hint: 0
    info: 0
    warn: 6
  slug: smithsonian-rules
score:
  band: thin
  composite: 36.8
  delta: 0.0
  facets:
    commercial_clarity: 15.8
    contract_quality: 64.9
    developer_ergonomics: 10.9
    discoverability: 74.1
    governance: 58.3
    operational_transparency: 13.2
  previous_composite: 36.8
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 3
  regulatory:
    applies: true
    matched_via: tags
    regime: Government & Public Sector
    regime_id: government
    score: 31.5
  schema_version: 0.11.0
  scored_at: '2026-08-17'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/smithsonian-institution/refs/heads/main/screenshots/smithsonian-institution-2026-06-20T194059.png
security:
- kind: authentication
  name: Smithsonian Institution Authentication
  slug: smithsonian-institution-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Smithsonian Institution Domain Security
  slug: smithsonian-institution-domain-security
  summary_line: TLSv1.3 · DNSSEC · DMARC
slug: smithsonian-institution
tags:
- Collections
- Cultural Heritage
- Museums
- Open Data
- Art
- Natural History
- Research
website: https://www.si.edu/
---
