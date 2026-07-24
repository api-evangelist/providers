---
access_model:
  confidence: medium
  label: Self-serve signup
  onboarding: self-serve
  pricing: unknown
  public: false
  source:
  - authentication
  trial: false
  try_now: false
agent_readiness:
  band: agent-native
  dimensions:
    agent_skills: true
    agentic_access: true
    asyncapi_events: false
    auth_clarity: true
    consent_identity: false
    error_semantics: true
    idempotency: false
    mcp_server: true
    openapi_examples: false
    rate_limit_signal: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.1
  score: 65.4
  scored_at: '2026-07-23'
agentic_access:
- acting_count: 3
  human_in_the_loop: 0
  name: Shapeways Agentic Access
  operation_count: 10
  slug: shapeways-agentic-access
  summary_line: 10 operations · 3 acting
api_count: 4
apis:
- description: Shipping options for a destination.
  name: Shapeways Cart API
  slug: shapeways-cart-api
- description: The Shapeways material catalog (40+ materials).
  name: Shapeways Materials API
  slug: shapeways-materials-api
- description: Upload, list, retrieve, and delete 3D models.
  name: Shapeways Models API
  slug: shapeways-models-api
- description: Place and track manufacturing orders.
  name: Shapeways Orders API
  slug: shapeways-orders-api
artifact_total: 9
common:
- group: start
  title: ''
  type: DeveloperPortal
  url: https://developers.shapeways.com/
- group: docs
  title: ''
  type: Documentation
  url: https://developers.shapeways.com/getting-started
- group: docs
  title: ''
  type: APIReference
  url: https://developers.shapeways.com/api-reference
- group: start
  title: ''
  type: GettingStarted
  url: https://developers.shapeways.com/quick-start
- group: operate
  title: ''
  type: Support
  url: https://support.shapeways.com/
- group: company
  title: ''
  type: Blog
  url: https://www.shapeways.com/blog
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/Shapeways
- group: start
  title: ''
  type: SignUp
  url: https://auth.shapeways.com/register
- group: start
  title: ''
  type: Login
  url: https://auth.shapeways.com/login
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.shapeways.com/terms-and-conditions
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.shapeways.com/privacy-statement
- group: auth
  title: ''
  type: Authentication
  url: authentication/shapeways-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/shapeways-scopes.yml
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/shapeways-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/shapeways-domain-security.yml
- group: build
  title: ''
  type: Packages
  url: packages/shapeways-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/shapeways-packages.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/shapeways-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/shapeways-problem-types.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/shapeways-mcp.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/shapeways-llms.txt
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/shapeways-lifecycle.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/shapeways-conformance.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/shapeways-data-model.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: company
  title: ''
  type: Website
  url: https://www.shapeways.com
created: '2026-07-17'
description: Shapeways is an on-demand 3D printing and additive-manufacturing platform that turns digital 3D models into physical parts across 12 additive technologies and 40+ materials, serving over one million customers in 180+ countries as a turnkey manufacturing partner for prototyping, production, and lifecycle support. Its OAuth 2.0 REST API (base URL https://api.shapeways.com) lets applications browse the material catalog, upload and manage 3D models, retrieve shipping options, and place and track manufacturing orders. Endpoints are versioned with a trailing /v1 path segment; official client libraries are published for PHP, Python, JavaScript, Go, and C++.
image: http://www.shapeways.com/wp-content/uploads/2021/03/SW-Thumbnail-Horizontal-1.jpg
layout: provider
mcp_servers:
- description: ''
  name: shapeways-mcp.yml
  slug: shapeways-mcpyml
modified: '2026-07-21'
name: Shapeways
nav: Providers
network: true
overview: 'Shapeways publishes 4 APIs on the [APIs.io](https://apis.io/) network, including Cart API, Materials API, Models API, and 1 more. Tagged areas include Company, 3D Printing, Additive Manufacturing, Manufacturing, and Prototyping.


  Shapeways'' developer surface includes documentation, API reference, getting-started guide, support, engineering blog, signup flow, authentication, and 19 more developer resources.'
random_paper: 12
scopes:
- name: Shapeways Scopes
  scope_count: 0
  slug: shapeways-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: developing
  composite: 45.9
  delta: 0.0
  facets:
    commercial_clarity: 34.2
    contract_quality: 54.4
    developer_ergonomics: 73.9
    discoverability: 100.0
    governance: 0.0
    operational_transparency: 5.3
  previous_composite: 45.9
  schema_version: 0.5
  scored_at: '2026-07-23'
  trend: flat
security:
- kind: authentication
  name: Shapeways Authentication
  slug: shapeways-authentication
  summary_line: oauth2 · 1 scheme
- kind: domain-security
  name: Shapeways Domain Security
  slug: shapeways-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: shapeways
tags:
- Company
- 3D Printing
- Additive Manufacturing
- Manufacturing
- Prototyping
- Hardware
- Fulfillment
- eCommerce
website: https://www.shapeways.com
---
