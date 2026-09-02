---
access_model:
  confidence: medium
  label: Freemium
  onboarding: unknown
  pricing: freemium
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
    agentic_commerce: false
    auth_clarity: false
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: verified
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: verified
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 28.1
  scored_at: '2026-09-01'
agentic_access:
- acting_count: 10
  human_in_the_loop: 0
  name: Factory I O Agentic Access
  operation_count: 15
  slug: factory-i-o-agentic-access
  summary_line: 15 operations · 10 acting
api_count: 1
apis:
- description: 'The web server in Factory I/O exposes a REST API for reading and writing simulation values from external clients. The web server uses conventional HTTP response codes to indicate success or failure: 2'
  name: FACTORY I/O Web API
  slug: factory-i-o
- description: Operations for reading and writing tag values by ID
  name: FACTORY I/O Tag Values API
  slug: factory-i-o-tag-values-api
- description: Operations for reading and writing tag values by name
  name: FACTORY I/O Tag Values by Name API
  slug: factory-i-o-tag-values-by-name-api
- description: Operations for listing and querying scene tags
  name: FACTORY I/O Tags API
  slug: factory-i-o-tags-api
artifact_total: 23
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: FACTORY I/O Web Tag Values API
  slug: open-factory-i-o-tag-values-api
- collection_type: open
  name: FACTORY I/O Web Tag Values Tag Values by Name API
  slug: open-factory-i-o-tag-values-by-name-api
- collection_type: open
  name: FACTORY I/O Web Tag Values Tags API
  slug: open-factory-i-o-tags-api
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/factory-i-o-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/factory-i-o-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://factoryio.com
- group: docs
  title: ''
  type: Documentation
  url: https://docs.factoryio.com/
- group: company
  title: ''
  type: Blog
  url: https://factoryio.com/blog
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/RealGames
created: '2025-03-01'
description: FACTORY I/O is a software simulation tool that allows users to create and simulate industrial automation systems in a virtual environment. It provides a realistic and interactive platform for training, testing, and troubleshooting automation processes without the need for physical equipment. Users can design their own control systems, program PLCs, and observe the behavior of machines and processes in real-time.
examples:
- key_count: 2
  name: Factory I O Get Tag Values Example
  slug: factory-i-o-get-tag-values-example
- key_count: 2
  name: Factory I O List Tags Example
  slug: factory-i-o-list-tags-example
- key_count: 2
  name: Factory I O Set Tag Values Example
  slug: factory-i-o-set-tag-values-example
finops:
- name: Factory I O Finops
  service_category: API
  slug: factory-i-o-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/factory-i-o.png
json_schemas:
- name: Tag
  property_count: 10
  slug: factory-i-o-tag
- name: TagValueResult
  property_count: 5
  slug: factory-i-o-tag-value
json_structures:
- name: Factory I O Tag Structure
  property_count: 0
  slug: factory-i-o-tag-structure
- name: Factory I O Tag Value Structure
  property_count: 0
  slug: factory-i-o-tag-value-structure
jsonld:
- class_count: 6
  name: Factory I O Context
  property_count: 11
  slug: factory-i-o-context
layout: provider
modified: '2026-04-28'
name: FACTORY I/O
nav: Providers
network: true
overview: 'FACTORY I/O publishes 3 APIs on the [APIs.io](https://apis.io/) network: Tag Values API, Tag Values by Name API, and Tags API. Tagged areas include Industrial Automation, Simulations, and Software Simulation.


  The FACTORY I/O catalog on APIs.io includes 1 JSON-LD context and 2 Spectral governance rulesets.


  FACTORY I/O''s developer surface includes documentation, engineering blog, and 4 more developer resources.'
plans:
- name: Factory I O Plans Pricing
  plan_count: 3
  slug: factory-i-o-plans-pricing
random_paper: 16
rate_limits:
- limit_count: 5
  name: Factory I O Rate Limits
  slug: factory-i-o-rate-limits
rules:
- effective_rule_count: 5
  extends: []
  name: FACTORY I/O API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 3
  slug: factory-i-o-jsonschema-spectral-rules
- effective_rule_count: 6
  extends: []
  name: FACTORY I/O API Rules
  rule_count: 6
  severity_counts:
    error: 1
    hint: 1
    info: 0
    warn: 4
  slug: factory-i-o-rules
score:
  band: thin
  composite: 26.3
  coverage:
    artifact_dirs: 15
    catalog_gap: 64.8
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 15.8
    commercial_clarity: 15.8
    contract_governance: 9.8
    contract_quality: 54.9
    developer_ergonomics: 9.5
    discoverability: 50.0
    governance: 9.8
    operational_transparency: 10.5
  previous_composite: 26.3
  provenance:
    agentic_access: derived
    contracts:
      callable: 0.0
      derived: 0
      marker_coverage: 0.0
      total: 3
  schema_version: 0.18.0
  scored_at: '2026-09-01'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/factory-i-o/refs/heads/main/screenshots/factory-i-o-2026-06-20T181011.png
security:
- kind: domain-security
  name: Factory I O Domain Security
  slug: factory-i-o-domain-security
  summary_line: TLSv1.3 · HSTS
slug: factory-i-o
tags:
- Industrial Automation
- Simulations
- Software Simulation
website: https://factoryio.com
---
