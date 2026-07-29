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
- acting_count: 4
  human_in_the_loop: 0
  name: Stepzen Agentic Access
  operation_count: 8
  slug: stepzen-agentic-access
  summary_line: 8 operations · 4 acting
api_count: 5
apis:
- description: 'GraphQL API platform for connecting to REST, databases, and other backends, automatically generating a GraphQL schema and resolvers from your data sources. Supports authentication via API key, OAuth, '
  name: StepZen GraphQL API
  slug: stepzen-api
- description: REST API for managing StepZen accounts, deployed GraphQL endpoints, API keys, and usage metrics programmatically.
  name: StepZen Admin API
  slug: stepzen-admin-api
- description: Account information and settings
  name: StepZen Account API
  slug: stepzen-account-api
- description: Manage API keys for endpoint access
  name: StepZen API Keys API
  slug: stepzen-api-keys-api
- description: Manage deployed GraphQL API endpoints
  name: StepZen Endpoints API
  slug: stepzen-endpoints-api
artifact_total: 19
collections:
- collection_type: open
  name: StepZen Admin API
  slug: open-stepzen-admin
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/stepzen-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/stepzen-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/stepzen-authentication.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/stepzen
- group: start
  title: ''
  type: Portal
  url: https://stepzen.com/
- group: docs
  title: ''
  type: Documentation
  url: https://stepzen.com/docs
- group: company
  title: ''
  type: Website
  url: https://stepzen.com/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/stepzen-dev
- group: other
  title: ''
  type: Dashboard
  url: https://dashboard.ibm.stepzen.com/
- group: other
  title: ''
  type: IBM Product Page
  url: https://www.ibm.com/products/api-connect
created: '2026-03-16'
description: StepZen (now IBM API Connect Essentials) is a GraphQL-as-a-Service platform that enables developers to build, deploy, and manage GraphQL APIs by connecting to multiple backends including REST APIs, SQL databases, NoSQL databases, GraphQL endpoints, and SOAP services. APIs are defined declaratively using GraphQL SDL with custom directives like @rest and @dbquery. StepZen runs a high-performance in-memory Golang GraphQL engine deployed on Kubernetes, optimizing queries at runtime for low latency and high throughput.
examples:
- key_count: 4
  name: Stepzen List Endpoints Example
  slug: stepzen-list-endpoints-example
finops:
- name: Stepzen Finops
  service_category: API
  slug: stepzen-finops
graphqls:
- description: 'GraphQL API platform for connecting to REST, databases, and other backends, automatically generating a GraphQL schema and resolvers from your data sources. Supports authentication via API key, OAuth, '
  name: StepZen GraphQL API
  slug: stepzen-graphql
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/stepzen.png
json_schemas:
- name: StepZen Endpoint
  property_count: 7
  slug: stepzen-endpoint
json_structures:
- name: Stepzen Endpoint Structure
  property_count: 0
  slug: stepzen-endpoint-structure
jsonld:
- class_count: 14
  name: Stepzen Context
  property_count: 3
  slug: stepzen-context
layout: provider
modified: '2026-05-19'
name: StepZen
nav: Providers
network: true
overview: 'StepZen publishes 3 APIs on the [APIs.io](https://apis.io/) network: Account API, API Keys API, and Endpoints API. Tagged areas include Backend Integration, GraphQL, API Gateway, REST to GraphQL, and IBM.


  The StepZen catalog on APIs.io includes 1 JSON-LD context and 2 Spectral governance rulesets.


  StepZen''s developer surface includes authentication, developer portal, documentation, and 7 more developer resources.'
plans:
- name: Stepzen Plans Pricing
  plan_count: 3
  slug: stepzen-plans-pricing
random_paper: 7
rate_limits:
- limit_count: 5
  name: Stepzen Rate Limits
  slug: stepzen-rate-limits
rules:
- name: StepZen API Rules
  rule_count: 4
  severity_counts:
    error: 0
    hint: 0
    info: 1
    warn: 3
  slug: stepzen-jsonschema-spectral-rules
- name: StepZen API Rules
  rule_count: 8
  severity_counts:
    error: 4
    hint: 0
    info: 0
    warn: 4
  slug: stepzen-rules
score:
  band: developing
  composite: 48.5
  delta: -3.8
  facets:
    commercial_clarity: 39.5
    contract_quality: 66.9
    developer_ergonomics: 28.3
    discoverability: 64.8
    governance: 58.3
    operational_transparency: 36.8
  previous_composite: 52.3
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 3
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: flat
security:
- kind: authentication
  name: Stepzen Authentication
  slug: stepzen-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Stepzen Domain Security
  slug: stepzen-domain-security
  summary_line: TLSv1.3 · DMARC
slug: stepzen
tags:
- Backend Integration
- GraphQL
- API Gateway
- REST to GraphQL
- IBM
- Data Federation
website: https://stepzen.com/
---
