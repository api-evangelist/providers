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
    dry_run_mode: na
    dynamic_client_registration: false
    error_semantics: false
    event_surface_described: false
    idempotency: na
    mcp_server: false
    openapi_examples: partial
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: na
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 22.9
  scored_at: '2026-09-01'
agentic_access:
- acting_count: 0
  human_in_the_loop: 0
  name: Rapidoc Agentic Access
  operation_count: 3
  slug: rapidoc-agentic-access
  summary_line: 3 operations
api_count: 1
apis:
- description: RapiDoc web component configuration attributes for general settings, colors and fonts, navigation bar, layout, sections, schema, and API server options.
  name: RapiDoc Configuration API
  slug: rapidoc-configuration-api
artifact_total: 21
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: RapiDoc Configuration API
  slug: open-rapidoc-configuration-api
- collection_type: open
  name: RapiDoc API
  slug: open-rapidoc-rapidoc
common:
- group: operate
  title: ''
  type: IssueTracker
  url: https://github.com/rapi-doc/RapiDoc/issues
- group: operate
  title: ''
  type: Releases
  url: https://github.com/rapi-doc/RapiDoc/releases
- group: docs
  title: ''
  type: ContributionGuide
  url: https://github.com/rapi-doc/RapiDoc/blob/master/CONTRIBUTING.md
- group: commercial
  title: ''
  type: License
  url: https://github.com/rapi-doc/RapiDoc/blob/master/LICENSE
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/rapidoc-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/rapidoc-domain-security.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/rapidoc-app
- group: docs
  title: ''
  type: Documentation
  url: https://rapidocweb.com/api.html
- group: build
  title: ''
  type: Examples
  url: https://rapidocweb.com/examples.html
- group: start
  title: ''
  type: GettingStarted
  url: https://rapidocweb.com/quickstart.html
- group: build
  title: ''
  type: GitHubRepository
  url: https://github.com/rapi-doc/RapiDoc
- group: build
  title: ''
  type: NPM
  url: https://www.npmjs.com/package/rapidoc
- group: design
  title: ''
  type: Vocabulary
  url: vocabulary/rapidoc-vocabulary.yml
created: '2025-01-08'
description: RapiDoc is a web component that allows developers to easily integrate interactive documentation for their APIs. It provides a user-friendly interface for exploring and testing API endpoints, displaying detailed information about request and response parameters, and offering code examples in multiple programming languages. RapiDoc also supports authentication methods, response validation, and custom theming options to tailor the documentation to a specific brand or project.
examples:
- key_count: 3
  name: Rapidoc Basic Embed Example
  slug: rapidoc-basic-embed-example
- key_count: 3
  name: Rapidoc Branded Embed Example
  slug: rapidoc-branded-embed-example
- key_count: 3
  name: Rapidoc Javascript Api Example
  slug: rapidoc-javascript-api-example
finops:
- name: Rapidoc Finops
  service_category: API
  slug: rapidoc-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/rapidoc.png
json_schemas:
- name: RapiDoc Web Component Configuration
  property_count: 55
  slug: rapidoc-configuration
- name: RapiDoc Events
  property_count: 5
  slug: rapidoc-events
- name: RapiDoc Slots
  property_count: 9
  slug: rapidoc-slots
json_structures:
- name: Rapidoc Configuration Structure
  property_count: 0
  slug: rapidoc-configuration-structure
- name: Rapidoc Events Structure
  property_count: 0
  slug: rapidoc-events-structure
- name: Rapidoc Slots Structure
  property_count: 0
  slug: rapidoc-slots-structure
jsonld:
- class_count: 0
  name: Rapidoc Context
  property_count: 6
  slug: rapidoc-context
layout: provider
modified: '2026-05-19'
name: RapiDoc
nav: Providers
network: true
overview: 'RapiDoc publishes 1 API on the [APIs.io](https://apis.io/) network: Configuration API. Tagged areas include Documentation, Platform, Web Components, and OpenAPI.


  The RapiDoc catalog on APIs.io includes 1 JSON-LD context and 2 Spectral governance rulesets.


  RapiDoc''s developer surface includes documentation, code examples, getting-started guide, and 10 more developer resources.'
plans:
- name: Rapidoc Plans Pricing
  plan_count: 3
  slug: rapidoc-plans-pricing
random_paper: 3
rate_limits:
- limit_count: 5
  name: Rapidoc Rate Limits
  slug: rapidoc-rate-limits
rules:
- effective_rule_count: 5
  extends: []
  name: RapiDoc API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 3
  slug: rapidoc-jsonschema-spectral-rules
- effective_rule_count: 46
  extends:
  - spectral:oas
  name: RapiDoc API Rules
  rule_count: 5
  severity_counts:
    error: 1
    hint: 1
    info: 0
    warn: 3
  slug: rapidoc-rules
score:
  band: thin
  composite: 34.1
  coverage:
    artifact_dirs: 14
    catalog_gap: 45.5
    catalog_max: 100.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 0.0
    commercial_clarity: 0.0
    contract_governance: 28.8
    contract_quality: 63.5
    developer_ergonomics: 21.4
    discoverability: 50.0
    governance: 28.8
    operational_transparency: 28.9
  open_source:
    applies: true
    score: 50.0
  previous_composite: 34.1
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 1
  schema_version: 0.18.0
  scored_at: '2026-09-01'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/rapidoc/refs/heads/main/screenshots/rapidoc-2026-06-20T192601.png
security:
- kind: domain-security
  name: Rapidoc Domain Security
  slug: rapidoc-domain-security
  summary_line: TLSv1.3 · HSTS
slug: rapidoc
tags:
- Documentation
- Platform
- Web Components
- OpenAPI
---
