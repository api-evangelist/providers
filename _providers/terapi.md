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
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 19.8
  scored_at: '2026-08-30'
agentic_access:
- acting_count: 6
  human_in_the_loop: 0
  name: Terapi Agentic Access
  operation_count: 12
  slug: terapi-agentic-access
  summary_line: 12 operations · 6 acting
api_count: 1
apis:
- description: Trigger actions on connected third-party services
  name: Terapi Actions API
  slug: terapi-actions-api
- description: Manage authentication and token refresh for integrations
  name: Terapi Authentication API
  slug: terapi-authentication-api
- description: Manage end-user connections to third-party integrations
  name: Terapi Connections API
  slug: terapi-connections-api
- description: Manage available integration configurations
  name: Terapi Integrations API
  slug: terapi-integrations-api
- description: Trigger and manage data synchronization between services
  name: Terapi Sync API
  slug: terapi-sync-api
artifact_total: 25
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Terapi Actions API
  slug: open-terapi-actions-api
- collection_type: open
  name: Terapi Actions Authentication API
  slug: open-terapi-authentication-api
- collection_type: open
  name: Terapi Actions Connections API
  slug: open-terapi-connections-api
- collection_type: open
  name: Terapi Actions Integrations API
  slug: open-terapi-integrations-api
- collection_type: open
  name: Terapi Actions Sync API
  slug: open-terapi-sync-api
- collection_type: open
  name: Terapi API
  slug: open-terapi
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/terapi-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/terapi-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/terapi-authentication.yml
- group: company
  title: ''
  type: Website
  url: https://terapi.dev
- group: docs
  title: ''
  type: Documentation
  url: https://docs.terapi.dev
- group: build
  title: ''
  type: GitHub
  url: https://github.com/terapi-dev
- group: docs
  title: ''
  type: OpenAPI
  url: https://raw.githubusercontent.com/api-evangelist/terapi/refs/heads/main/openapi/terapi-openapi.yml
- group: design
  title: ''
  type: Vocabulary
  url: https://raw.githubusercontent.com/api-evangelist/terapi/refs/heads/main/vocabulary/terapi-vocabulary.yml
created: '2026-03-27'
description: Terapi is an open-source embedded integration platform for building native product integrations. It provides a self-hosted iPaaS with pre-built connectors, authentication management, unified APIs, and workflow automation for SaaS products needing to offer native third-party integrations to their customers.
examples:
- key_count: 4
  name: Terapi List Connections Example
  slug: terapi-list-connections-example
- key_count: 4
  name: Terapi Trigger Action Example
  slug: terapi-trigger-action-example
finops:
- name: Terapi Finops
  service_category: API
  slug: terapi-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/terapi.png
json_schemas:
- name: Terapi Integration Connection
  property_count: 7
  slug: terapi-connection
json_structures:
- name: Terapi Connection Structure
  property_count: 0
  slug: terapi-connection-structure
jsonld:
- class_count: 5
  name: Terapi Context
  property_count: 21
  slug: terapi-context
layout: provider
modified: '2026-05-19'
name: Terapi
nav: Providers
network: true
overview: 'Terapi publishes 5 APIs on the [APIs.io](https://apis.io/) network, including Actions API, Authentication API, Connections API, and 2 more. Tagged areas include Authentication, Connectors, Embedded iPaaS, Integration, and Native Integrations.


  The Terapi catalog on APIs.io includes 1 JSON-LD context and 2 Spectral governance rulesets.


  Terapi''s developer surface includes authentication, documentation, GitHub presence, and 5 more developer resources.'
plans:
- name: Terapi Plans Pricing
  plan_count: 3
  slug: terapi-plans-pricing
random_paper: 15
rate_limits:
- limit_count: 5
  name: Terapi Rate Limits
  slug: terapi-rate-limits
rules:
- effective_rule_count: 5
  extends: []
  name: Terapi API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 1
    warn: 4
  slug: terapi-jsonschema-spectral-rules
- effective_rule_count: 61
  extends:
  - spectral:oas
  name: Terapi API Rules
  rule_count: 20
  severity_counts:
    error: 8
    hint: 0
    info: 0
    warn: 12
  slug: terapi-rules
score:
  band: thin
  composite: 34.1
  coverage:
    artifact_dirs: 15
    catalog_gap: 53.5
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: -0.5
  facets:
    access_clarity: 15.8
    commercial_clarity: 15.8
    contract_governance: 28.8
    contract_quality: 61.2
    developer_ergonomics: 22.6
    discoverability: 59.3
    governance: 28.8
    operational_transparency: 13.2
  previous_composite: 34.6
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 5
  schema_version: 0.17.2
  scored_at: '2026-08-30'
  trend: flat
security:
- kind: authentication
  name: Terapi Authentication
  slug: terapi-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Terapi Domain Security
  slug: terapi-domain-security
  summary_line: DMARC
slug: terapi
tags:
- Authentication
- Connectors
- Embedded iPaaS
- Integration
- Native Integrations
- Open-Source
- Workflow-Automation
website: https://terapi.dev
---
