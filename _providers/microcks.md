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
    agent_card: false
    agent_skills: false
    agentic_access: derived
    asyncapi_events: false
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    idempotency: false
    mcp_server: true
    openapi_examples: partial
    rate_limit_signal: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 44.6
  scored_at: '2026-07-28'
agentic_access:
- acting_count: 17
  human_in_the_loop: 2
  name: Microcks Agentic Access
  operation_count: 46
  slug: microcks-agentic-access
  summary_line: 46 operations · 17 acting · 2 human-in-the-loop
api_count: 6
apis:
- description: Operations related to configuration
  name: Microcks config API
  slug: microcks-config-api
- description: Operations related to Jobs for discovering mocks and tests
  name: Microcks job API
  slug: microcks-job-api
- description: Operations related to metrics
  name: Microcks metrics API
  slug: microcks-metrics-api
- description: Operations related to API and Services mocks
  name: Microcks mock API
  slug: microcks-mock-api
- description: The Resources API from Microcks — 2 operation(s) for resources.
  name: Microcks Resources API
  slug: microcks-resources-api
- description: Operations related to API and Services tests
  name: Microcks test API
  slug: microcks-test-api
artifact_total: 15
collections:
- collection_type: open
  name: Microcks API v1.14
  slug: open-microcks
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/microcks-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/microcks-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/microcks-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/microcks-scopes.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/microcks
- group: start
  title: ''
  type: Portal
  url: https://microcks.io/
- group: docs
  title: ''
  type: Documentation
  url: https://microcks.io/documentation/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/microcks
- group: operate
  title: ''
  type: Community
  url: https://microcks.io/community/
- group: company
  title: ''
  type: Blog
  url: https://microcks.io/blog/
- group: agent
  title: ''
  type: MCPServer
  url: https://github.com/microcks/microcks-mcp-server
created: '2025-01-08'
description: Microcks is an open source, cloud-native tool for API mocking and testing. It provides a platform for importing API contracts (OpenAPI, AsyncAPI, Postman Collections), generating mock responses, and running test suites. It shortens the feedback loop for API development teams.
finops:
- name: Microcks Finops
  service_category: API
  slug: microcks-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/microcks.png
layout: provider
mcp_servers:
- description: ''
  name: MCP Server
  slug: mcp-server
modified: '2026-05-19'
name: Microcks
nav: Providers
network: true
overview: 'Microcks publishes 6 APIs on the [APIs.io](https://apis.io/) network, including config API, job API, metrics API, and 3 more. Tagged areas include API Testing, Cloud Native, DevOps, Mocking, and Open Source.


  Microcks'' developer surface includes authentication, developer portal, documentation, engineering blog, and 7 more developer resources.'
plans:
- name: Microcks Plans Pricing
  plan_count: 3
  slug: microcks-plans-pricing
random_paper: 69
rate_limits:
- limit_count: 5
  name: Microcks Rate Limits
  slug: microcks-rate-limits
scopes:
- name: Microcks Scopes
  scope_count: 3
  slug: microcks-scopes
  summary_line: 3 scopes · clientCredentials
score:
  band: thin
  composite: 40.0
  delta: -3.3
  facets:
    commercial_clarity: 39.5
    contract_quality: 48.4
    developer_ergonomics: 43.5
    discoverability: 64.8
    governance: 0.0
    operational_transparency: 36.8
  previous_composite: 43.3
  provenance:
    agentic_access: derived
    contracts:
      callable: 0.0
      derived: 0
      marker_coverage: 0.0
      total: 6
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/microcks/refs/heads/main/screenshots/microcks-2026-06-20T185332.png
security:
- kind: authentication
  name: Microcks Authentication
  slug: microcks-authentication
  summary_line: oauth2 · 1 scheme
- kind: domain-security
  name: Microcks Domain Security
  slug: microcks-domain-security
  summary_line: TLSv1.3
slug: microcks
tags:
- API Testing
- Cloud Native
- DevOps
- Mocking
- Open Source
website: https://microcks.io/
---
