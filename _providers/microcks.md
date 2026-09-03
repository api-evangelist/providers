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
    agentic_commerce: false
    auth_clarity: negotiable
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: documented
    openapi_examples: partial
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 28.6
  scored_at: '2026-09-03'
agentic_access:
- acting_count: 17
  human_in_the_loop: 2
  name: Microcks Agentic Access
  operation_count: 46
  slug: microcks-agentic-access
  summary_line: 46 operations · 17 acting · 2 human-in-the-loop
api_count: 1
apis:
- baseURL: http://microcks.example.com/api
  baseurl_source: spec
  description: Operations related to configuration
  name: Microcks config API
  slug: microcks-config-api
- baseURL: http://microcks.example.com/api
  baseurl_source: spec
  description: Operations related to Jobs for discovering mocks and tests
  name: Microcks job API
  slug: microcks-job-api
- baseURL: http://microcks.example.com/api
  baseurl_source: spec
  description: Operations related to metrics
  name: Microcks metrics API
  slug: microcks-metrics-api
- baseURL: http://microcks.example.com/api
  baseurl_source: spec
  description: Operations related to API and Services mocks
  name: Microcks mock API
  slug: microcks-mock-api
- baseURL: http://microcks.example.com/api
  baseurl_source: spec
  description: The Resources API from Microcks — 2 operation(s) for resources.
  name: Microcks Resources API
  slug: microcks-resources-api
- baseURL: http://microcks.example.com/api
  baseurl_source: spec
  description: Operations related to API and Services tests
  name: Microcks test API
  slug: microcks-test-api
artifact_total: 22
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Microcks API v1.14 config API
  slug: open-microcks-config-api
- collection_type: open
  name: Microcks API v1.14 config job API
  slug: open-microcks-job-api
- collection_type: open
  name: Microcks API v1.14 config metrics API
  slug: open-microcks-metrics-api
- collection_type: open
  name: Microcks API v1.14 config mock API
  slug: open-microcks-mock-api
- collection_type: open
  name: Microcks API v1.14 config Resources API
  slug: open-microcks-resources-api
- collection_type: open
  name: Microcks API v1.14 config test API
  slug: open-microcks-test-api
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
overview: 'Microcks publishes 6 APIs on the [APIs.io](https://apis.io/) network, including config API, job API, metrics API, and 3 more. Tagged areas include API Testing, Cloud-Native, DevOps, Mocking, and Open-Source.


  Microcks'' developer surface includes authentication, developer portal, documentation, engineering blog, and 7 more developer resources.'
plans:
- name: Microcks Plans Pricing
  plan_count: 3
  slug: microcks-plans-pricing
random_paper: 19
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
  composite: 30.4
  coverage:
    artifact_dirs: 12
    catalog_gap: 74.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 15.8
    commercial_clarity: 15.8
    contract_governance: 0.0
    contract_quality: 51.1
    developer_ergonomics: 35.7
    discoverability: 59.3
    governance: 0.0
    operational_transparency: 10.5
  previous_composite: 30.4
  provenance:
    agentic_access: derived
    contracts:
      callable: 0.0
      derived: 0
      marker_coverage: 0.0
      total: 6
  schema_version: 0.18.2
  scored_at: '2026-09-03'
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
- Cloud-Native
- DevOps
- Mocking
- Open-Source
website: https://microcks.io/
---
