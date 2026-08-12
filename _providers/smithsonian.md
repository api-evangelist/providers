---
access_model:
  confidence: high
  label: Paid · Self-serve signup
  onboarding: self-serve
  pricing: paid
  public: false
  source:
  - plans
  - authentication
  trial: false
  try_now: false
agent_readiness:
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: verified
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: partial
    rate_limit_signal: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 41.0
  scored_at: '2026-08-11'
agentic_access:
- acting_count: 0
  human_in_the_loop: 0
  name: Smithsonian Agentic Access
  operation_count: 5
  slug: smithsonian-agentic-access
  summary_line: 5 operations
api_count: 3
apis:
- description: Retrieve individual collection objects by ID or URL
  name: Smithsonian Institution content API
  slug: smithsonian-content-api
- description: Statistics about CC0 objects and media
  name: Smithsonian Institution metrics API
  slug: smithsonian-metrics-api
- description: Search across Smithsonian collections
  name: Smithsonian Institution search API
  slug: smithsonian-search-api
artifact_total: 15
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/smithsonian-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/smithsonian-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/smithsonian-authentication.yml
- group: company
  title: ''
  type: Website
  url: https://www.si.edu
- group: docs
  title: ''
  type: Documentation
  url: https://edan.si.edu/openaccess/apidocs/
- group: build
  title: ''
  type: GitHubOrg
  url: https://github.com/Smithsonian
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/smithsonian-institution
- group: company
  title: ''
  type: Blog
  url: https://www.si.edu/openaccess
- group: commercial
  title: ''
  type: Pricing
  url: https://api.data.gov/signup/
- group: operate
  title: ''
  type: StatusPage
  url: https://api.data.gov/
- group: other
  title: ''
  type: X
  url: https://twitter.com/smithsonian
- group: commercial
  title: ''
  type: Plans
  url: plans/smithsonian-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/smithsonian-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/smithsonian-finops.yml
created: '2026-06-13'
description: Smithsonian Institution Open Access REST API providing search and retrieval of over 4.7 million digitized objects, images, 3D models, and metadata across 19 museums and research centers. All content is released under CC0 (public domain) and covers art and design, history and culture, and science and technology collections.
examples:
- key_count: 4
  name: Smithsonian Content Response Example
  slug: smithsonian-content-response-example
- key_count: 3
  name: Smithsonian Search Response Example
  slug: smithsonian-search-response-example
finops:
- name: Smithsonian Finops
  service_category: ''
  slug: smithsonian-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/smithsonian.png
json_schemas:
- name: Smithsonian Collection Object
  property_count: 12
  slug: smithsonian-collection-object
- name: Smithsonian Search Response
  property_count: 3
  slug: smithsonian-search-response
jsonld:
- class_count: 5
  name: Smithsonian Context
  property_count: 39
  slug: smithsonian-context
layout: provider
modified: '2026-06-13'
name: Smithsonian Institution
nav: Providers
network: true
overview: 'Smithsonian Institution publishes 3 APIs on the [APIs.io](https://apis.io/) network: content API, metrics API, and search API. Tagged areas include Museums, Open Access, Cultural Heritage, Collections, and Images.


  The Smithsonian Institution catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  Smithsonian Institution''s developer surface includes authentication, documentation, engineering blog, pricing, and 10 more developer resources.'
plans:
- name: Smithsonian Plans Pricing
  plan_count: 3
  slug: smithsonian-plans-pricing
random_paper: 37
rate_limits:
- limit_count: 0
  name: Smithsonian Rate Limits
  slug: smithsonian-rate-limits
rules:
- name: Smithsonian Institution API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 3
  slug: smithsonian-jsonschema-spectral-rules
score:
  band: developing
  composite: 48.5
  delta: -0.7
  facets:
    commercial_clarity: 50.0
    contract_quality: 68.2
    developer_ergonomics: 21.7
    discoverability: 74.1
    governance: 58.3
    operational_transparency: 21.1
  previous_composite: 49.2
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 3
  schema_version: 0.11.0
  scored_at: '2026-08-11'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/smithsonian/refs/heads/main/screenshots/smithsonian-2026-06-20T194054.png
security:
- kind: authentication
  name: Smithsonian Authentication
  slug: smithsonian-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Smithsonian Domain Security
  slug: smithsonian-domain-security
  summary_line: TLSv1.3 · DNSSEC · DMARC
slug: smithsonian
tags:
- Museums
- Open Access
- Cultural Heritage
- Collections
- Images
- 3D Models
- Public Domain
- CC0
website: https://www.si.edu
---
