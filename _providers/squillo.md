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
  band: agent-ready
  dimensions:
    agent_skills: false
    agentic_access: true
    asyncapi_events: false
    auth_clarity: true
    consent_identity: false
    error_semantics: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: true
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.1
  score: 48.1
  scored_at: '2026-07-27'
agentic_access:
- acting_count: 9
  human_in_the_loop: 0
  name: Squillo Agentic Access
  operation_count: 16
  slug: squillo-agentic-access
  summary_line: 16 operations · 9 acting
api_count: 4
apis:
- description: Integration connector configuration
  name: Squillo Connectors API
  slug: squillo-connectors-api
- description: Workflow execution monitoring and management
  name: Squillo Executions API
  slug: squillo-executions-api
- description: Workflow variable and secret management
  name: Squillo Variables API
  slug: squillo-variables-api
- description: Workflow definition and management
  name: Squillo Workflows API
  slug: squillo-workflows-api
artifact_total: 18
collections:
- collection_type: open
  name: Squillo Platform API
  slug: open-squillo-platform
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/squillo-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/squillo-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/squillo-authentication.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/squillo
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/squillo
- group: company
  title: ''
  type: Website
  url: https://squillo.io/
- group: docs
  title: ''
  type: Documentation
  url: https://squillo.io/
- group: docs
  title: ''
  type: OpenAPI
  url: https://raw.githubusercontent.com/api-evangelist/squillo/refs/heads/main/openapi/squillo-platform-openapi.yml
- group: docs
  title: ''
  type: JSONSchema
  url: https://raw.githubusercontent.com/api-evangelist/squillo/refs/heads/main/json-schema/squillo-workflow-schema.json
- group: design
  title: ''
  type: JSONStructure
  url: https://raw.githubusercontent.com/api-evangelist/squillo/refs/heads/main/json-structure/squillo-workflow-structure.json
- group: design
  title: ''
  type: JSONLDContext
  url: https://raw.githubusercontent.com/api-evangelist/squillo/refs/heads/main/json-ld/squillo-context.jsonld
- group: design
  title: ''
  type: SpectralRules
  url: https://raw.githubusercontent.com/api-evangelist/squillo/refs/heads/main/rules/squillo-rules.yml
- group: design
  title: ''
  type: Vocabulary
  url: https://raw.githubusercontent.com/api-evangelist/squillo/refs/heads/main/vocabulary/squillo-vocabulary.yml
- group: company
  title: ''
  type: Blog
  url: https://squillo.io/rss
created: '2025-08-19'
description: Squillo is a Software as a Utility (SaaU) platform that enables integration and automation of entire IT systems and human processes in minutes, not months. It provides a low-code/no-code approach to connecting enterprise applications, automating workflows, and orchestrating complex IT processes without traditional development overhead.
examples:
- key_count: 4
  name: Squillo Execute Workflow Example
  slug: squillo-execute-workflow-example
- key_count: 4
  name: Squillo List Workflows Example
  slug: squillo-list-workflows-example
finops:
- name: Squillo Finops
  service_category: API
  slug: squillo-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/squillo.png
json_schemas:
- name: Squillo Workflow
  property_count: 9
  slug: squillo-workflow
json_structures:
- name: Squillo Workflow Structure
  property_count: 0
  slug: squillo-workflow-structure
jsonld:
- class_count: 17
  name: Squillo Context
  property_count: 7
  slug: squillo-context
layout: provider
modified: '2026-05-19'
name: Squillo
nav: Providers
network: true
overview: 'Squillo publishes 4 APIs on the [APIs.io](https://apis.io/) network, including Connectors API, Executions API, Variables API, and 1 more. Tagged areas include Integration Platform, Automation, Workflow, No-Code, and IT Process Automation.


  The Squillo catalog on APIs.io includes 1 JSON-LD context and 2 Spectral governance rulesets.


  Squillo''s developer surface includes authentication, documentation, engineering blog, and 11 more developer resources.'
plans:
- name: Squillo Plans Pricing
  plan_count: 3
  slug: squillo-plans-pricing
random_paper: 29
rate_limits:
- limit_count: 5
  name: Squillo Rate Limits
  slug: squillo-rate-limits
rules:
- name: Squillo API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 3
  slug: squillo-jsonschema-spectral-rules
- name: Squillo API Rules
  rule_count: 7
  severity_counts:
    error: 2
    hint: 1
    info: 0
    warn: 4
  slug: squillo-rules
score:
  band: developing
  composite: 53.4
  delta: 3.3
  facets:
    commercial_clarity: 39.5
    contract_quality: 63.7
    developer_ergonomics: 21.7
    discoverability: 100.0
    governance: 86.8
    operational_transparency: 36.8
  previous_composite: 50.1
  schema_version: 0.5
  scored_at: '2026-07-27'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/squillo/refs/heads/main/screenshots/squillo-2026-06-20T194434.png
security:
- kind: authentication
  name: Squillo Authentication
  slug: squillo-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Squillo Domain Security
  slug: squillo-domain-security
  summary_line: TLSv1.3 · HSTS
slug: squillo
tags:
- Integration Platform
- Automation
- Workflow
- No-Code
- IT Process Automation
- Software As A Utility
website: https://squillo.io/
---
