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
  scored_at: '2026-08-11'
agentic_access:
- acting_count: 6
  human_in_the_loop: 0
  name: Terapi Agentic Access
  operation_count: 12
  slug: terapi-agentic-access
  summary_line: 12 operations · 6 acting
api_count: 5
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
artifact_total: 19
collections:
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
random_paper: 65
rate_limits:
- limit_count: 5
  name: Terapi Rate Limits
  slug: terapi-rate-limits
rules:
- name: Terapi API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 1
    warn: 4
  slug: terapi-jsonschema-spectral-rules
- name: Terapi API Rules
  rule_count: 20
  severity_counts:
    error: 8
    hint: 0
    info: 0
    warn: 12
  slug: terapi-rules
score:
  band: thin
  composite: 40.3
  delta: -8.5
  facets:
    commercial_clarity: 15.8
    contract_quality: 67.2
    developer_ergonomics: 19.6
    discoverability: 64.8
    governance: 68.8
    operational_transparency: 13.2
  previous_composite: 48.8
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 5
  schema_version: 0.11.0
  scored_at: '2026-08-11'
  trend: falling
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
- Open Source
- Workflow Automation
website: https://terapi.dev
---
