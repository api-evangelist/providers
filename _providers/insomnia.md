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
  name: Insomnia Agentic Access
  operation_count: 10
  slug: insomnia-agentic-access
  summary_line: 10 operations · 6 acting
api_count: 1
apis:
- description: Insomnia is an open-source, cross-platform API development platform by Kong for designing, debugging, and testing HTTP, REST, GraphQL, gRPC, SOAP, WebSockets, SSE, and Socket.IO APIs. It includes an I
  name: Insomnia
  slug: insomnia
- description: View request logs for mock servers.
  name: Insomnia Mock Logs API
  slug: insomnia-mock-logs-api
- description: Manage individual routes within a mock server.
  name: Insomnia Mock Routes API
  slug: insomnia-mock-routes-api
- description: Manage mock server instances.
  name: Insomnia Mock Servers API
  slug: insomnia-mock-servers-api
artifact_total: 21
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Insomnia Mock Server Mock Logs API
  slug: open-insomnia-mock-logs-api
- collection_type: open
  name: Insomnia Mock Server Mock Logs Mock Routes API
  slug: open-insomnia-mock-routes-api
- collection_type: open
  name: Insomnia Mock Server API
  slug: open-insomnia-mock-server
- collection_type: open
  name: Insomnia Mock Server Mock Logs Mock Servers API
  slug: open-insomnia-mock-servers-api
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/insomnia-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/insomnia-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/insomnia-authentication.yml
- group: docs
  title: ''
  type: Documentation
  url: https://docs.insomnia.rest/
- group: build
  title: ''
  type: GitHubRepository
  url: https://github.com/Kong/insomnia
- group: build
  title: ''
  type: Plugins
  url: https://insomnia.rest/plugins
- group: operate
  title: ''
  type: ChangeLog
  url: https://insomnia.rest/changelog
- group: company
  title: ''
  type: Blog
  url: https://konghq.com/blog
- group: commercial
  title: ''
  type: Pricing
  url: https://insomnia.rest/pricing
- group: build
  title: ''
  type: CLI
  url: https://docs.insomnia.rest/inso-cli/introduction/
- group: company
  title: ''
  type: Website
  url: https://konghq.com/products/kong-insomnia
created: '2025-01-08'
description: Insomnia is an open-source, cross-platform API development platform by Kong for designing, debugging, and testing HTTP, REST, GraphQL, gRPC, SOAP, WebSockets, SSE, and Socket.IO APIs. It includes an Inso CLI for CI/CD integration, cloud-hosted and self-hosted mock servers, OpenAPI spec design tools, and collaborative features with cloud sync, local vault, and Git storage options.
finops:
- name: Insomnia Finops
  service_category: API
  slug: insomnia-finops
graphqls:
- description: ''
  name: Insomnia GraphQL API
  slug: insomnia-graphql
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/insomnia.png
json_schemas:
- name: Insomnia Environment
  property_count: 11
  slug: environment
- name: Insomnia Request
  property_count: 17
  slug: request
- name: Insomnia Workspace
  property_count: 9
  slug: workspace
jsonld:
- class_count: 2
  name: Insomnia Context
  property_count: 5
  slug: insomnia-context
layout: provider
modified: '2026-05-19'
name: Insomnia
nav: Providers
network: true
overview: 'Insomnia publishes 3 APIs on the [APIs.io](https://apis.io/) network: Mock Logs API, Mock Routes API, and Mock Servers API. Tagged areas include API Design, CLI, Clients, Mocking, and Platform.


  The Insomnia catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  Insomnia''s developer surface includes authentication, documentation, changelog, engineering blog, pricing, CLI, and 5 more developer resources.'
plans:
- name: Insomnia Plans Pricing
  plan_count: 3
  slug: insomnia-plans-pricing
random_paper: 1
rate_limits:
- limit_count: 5
  name: Insomnia Rate Limits
  slug: insomnia-rate-limits
rules:
- effective_rule_count: 5
  extends: []
  name: Insomnia API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 3
  slug: insomnia-jsonschema-spectral-rules
score:
  band: developing
  composite: 39.5
  coverage:
    artifact_dirs: 14
    catalog_gap: 55.8
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: -0.5
  facets:
    access_clarity: 26.3
    commercial_clarity: 26.3
    contract_governance: 9.8
    contract_quality: 68.7
    developer_ergonomics: 31.0
    discoverability: 59.3
    governance: 9.8
    operational_transparency: 28.9
  previous_composite: 40.0
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 3
  schema_version: 0.17.2
  scored_at: '2026-08-30'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/insomnia/refs/heads/main/screenshots/insomnia-2026-06-20T183403.png
security:
- kind: authentication
  name: Insomnia Authentication
  slug: insomnia-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Insomnia Domain Security
  slug: insomnia-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
slug: insomnia
tags:
- API Design
- CLI
- Clients
- Mocking
- Platform
- Testing
website: https://konghq.com/products/kong-insomnia
---
