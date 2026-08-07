---
access_model:
  confidence: high
  label: Enterprise · Self-serve signup
  onboarding: self-serve
  pricing: enterprise
  public: false
  source:
  - plans
  - authentication
  trial: false
  try_now: false
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
  scored_at: '2026-08-06'
agentic_access:
- acting_count: 4
  human_in_the_loop: 0
  name: Salesforce Flow Agentic Access
  operation_count: 10
  slug: salesforce-flow-agentic-access
  summary_line: 10 operations · 4 acting
api_count: 5
apis:
- description: Tooling API endpoints for managing Flow definitions and metadata. Supports deployment, retrieval, and management of Flow versions.
  name: Salesforce Tooling API (Flow)
  slug: salesforce-tooling-api-flow
- description: API for executing and managing Flow interviews (instances). Provides endpoints to start, resume, pause, and monitor flow execution state.
  name: Salesforce Flow Interviews API
  slug: salesforce-flow-interviews-api
- description: Operations for managing Flow metadata and definitions
  name: Salesforce Flow Flow Definitions API
  slug: salesforce-flow-flow-definitions-api
- description: Operations for executing and managing Flow interviews
  name: Salesforce Flow Flow Interviews API
  slug: salesforce-flow-flow-interviews-api
- description: Operations for triggering invocable flows as actions
  name: Salesforce Flow Invocable Actions API
  slug: salesforce-flow-invocable-actions-api
artifact_total: 24
collections:
- collection_type: postman
  name: Salesforce Flow REST Flow Definitions API
  slug: postman-salesforce-flow-flow-definitions-api
- collection_type: postman
  name: Salesforce Flow REST Flow Definitions Flow Interviews API
  slug: postman-salesforce-flow-flow-interviews-api
- collection_type: postman
  name: Salesforce Flow REST Flow Definitions Invocable Actions API
  slug: postman-salesforce-flow-invocable-actions-api
- collection_type: open
  name: Salesforce Flow REST API
  slug: open-salesforce-flow-rest-api
common:
- group: build
  title: ''
  type: PostmanWorkspace
  url: https://www.postman.com/kinlaneapi/salesforce-flow/overview
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/salesforce-flow-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/salesforce-flow-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/salesforce-flow-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/salesforce-flow-scopes.yml
- group: start
  title: ''
  type: Portal
  url: https://developer.salesforce.com/
- group: start
  title: ''
  type: GettingStarted
  url: https://trailhead.salesforce.com/content/learn/modules/flow-builder
- group: auth
  title: ''
  type: Authentication
  url: https://developer.salesforce.com/docs/atlas.en-us.api_rest.meta/api_rest/intro_oauth_and_connected_apps.htm
- group: operate
  title: ''
  type: RateLimits
  url: https://developer.salesforce.com/docs/atlas.en-us.salesforce_app_limits_cheatsheet.meta/salesforce_app_limits_cheatsheet/salesforce_app_limits_platform_api.htm
- group: operate
  title: ''
  type: StatusPage
  url: https://status.salesforce.com/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.salesforce.com/company/legal/agreements/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.salesforce.com/company/privacy/
- group: docs
  title: ''
  type: Documentation
  url: https://developer.salesforce.com/docs/atlas.en-us.flow.meta/flow/
- group: learn
  title: ''
  type: Trailhead Learning
  url: https://trailhead.salesforce.com/content/learn/modules/flow-builder
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/salesforce
- group: design
  title: ''
  type: SpectralRules
  url: rules/salesforce-flow-rules.yml
- group: other
  title: ''
  type: Capabilities
  url: capabilities/flow-automation.yaml
- group: docs
  title: Flow Definition Schema
  type: JSONSchema
  url: json-schema/salesforce-flow-flow-definition-schema.json
- group: docs
  title: Flow Interview Schema
  type: JSONSchema
  url: json-schema/salesforce-flow-flow-interview-schema.json
- group: design
  title: ''
  type: JSONLDContext
  url: json-ld/salesforce-flow-context.jsonld
- group: design
  title: ''
  type: Vocabulary
  url: vocabulary/salesforce-flow-vocabulary.yml
- group: company
  title: ''
  type: Blog
  url: https://developer.salesforce.com/blogs/feed
created: 2024-01-15 00:00:00+00:00
description: The Salesforce Flow API enables developers to interact with and manage Salesforce Flow automation processes programmatically. This includes creating, updating, querying, and executing flows within Salesforce using the REST API, Tooling API, and Invocable Actions framework.
examples:
- key_count: 7
  name: Salesforce Flow Invoke Flow Example
  slug: salesforce-flow-invoke-flow-example
- key_count: 7
  name: Salesforce Flow List Flows Example
  slug: salesforce-flow-list-flows-example
finops:
- name: Salesforce Flow Finops
  service_category: Workflow Automation
  slug: salesforce-flow-finops
image: https://www.salesforce.com/content/dam/web/en_us/www/images/nav/logo-salesforce.svg
json_schemas:
- name: Salesforce Flow Definition
  property_count: 12
  slug: salesforce-flow-flow-definition
- name: Salesforce Flow Interview
  property_count: 11
  slug: salesforce-flow-flow-interview
json_structures:
- name: Salesforce Flow Flow Definition Structure
  property_count: 0
  slug: salesforce-flow-flow-definition-structure
jsonld:
- class_count: 0
  name: Salesforce Flow Context
  property_count: 23
  slug: salesforce-flow-context
layout: provider
modified: '2026-05-19'
name: Salesforce Flow
nav: Providers
network: true
overview: 'Salesforce Flow publishes 3 APIs on the [APIs.io](https://apis.io/) network: Flow Definitions API, Flow Interviews API, and Invocable Actions API. Tagged areas include Automation, Business Process, CRM, Flow, and Process Builder.


  The Salesforce Flow catalog on APIs.io includes 1 JSON-LD context and 2 Spectral governance rulesets.


  Salesforce Flow''s developer surface includes authentication, developer portal, getting-started guide, documentation, engineering blog, and 17 more developer resources.'
plans:
- name: Salesforce Flow Plans Pricing
  plan_count: 1
  slug: salesforce-flow-plans-pricing
random_paper: 79
rate_limits:
- limit_count: 1
  name: Salesforce Flow Rate Limits
  slug: salesforce-flow-rate-limits
rules:
- name: Salesforce Flow API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 3
  slug: salesforce-flow-jsonschema-spectral-rules
- name: Salesforce Flow API Rules
  rule_count: 10
  severity_counts:
    error: 5
    hint: 0
    info: 1
    warn: 4
  slug: salesforce-flow-rules
scopes:
- name: Salesforce Flow Scopes
  scope_count: 2
  slug: salesforce-flow-scopes
  summary_line: 2 scopes · authorizationCode
score:
  band: strong
  composite: 58.6
  delta: 0.0
  facets:
    commercial_clarity: 50.0
    contract_quality: 70.3
    developer_ergonomics: 45.7
    discoverability: 81.5
    governance: 68.8
    operational_transparency: 42.1
  previous_composite: 58.6
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 3
  schema_version: 0.9.1
  scored_at: '2026-08-06'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/salesforce-flow/refs/heads/main/screenshots/salesforce-flow-2026-06-20T193348.png
security:
- kind: authentication
  name: Salesforce Flow Authentication
  slug: salesforce-flow-authentication
  summary_line: http/oauth2 · 2 schemes
- kind: domain-security
  name: Salesforce Flow Domain Security
  slug: salesforce-flow-domain-security
  summary_line: TLSv1.3 · DNSSEC · DMARC
slug: salesforce-flow
tags:
- Automation
- Business Process
- CRM
- Flow
- Process Builder
- Salesforce
- Workflow
website: https://developer.salesforce.com/
---
