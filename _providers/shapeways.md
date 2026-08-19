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
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: derived
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: documented
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 30.6
  scored_at: '2026-08-19'
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
artifact_total: 14
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Shapeways Cart API
  slug: open-shapeways-cart-api
- collection_type: open
  name: Shapeways Cart Materials API
  slug: open-shapeways-materials-api
- collection_type: open
  name: Shapeways Cart Models API
  slug: open-shapeways-models-api
- collection_type: open
  name: Shapeways Cart Orders API
  slug: open-shapeways-orders-api
common:
- group: other
  title: ''
  type: Overlay
  url: overlays/shapeways-overlay.yaml
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


  Shapeways'' developer surface includes documentation, API reference, getting-started guide, support, engineering blog, signup flow, authentication, and 20 more developer resources.'
random_paper: 87
scopes:
- name: Shapeways Scopes
  scope_count: 0
  slug: shapeways-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: thin
  composite: 33.8
  delta: 0.8
  facets:
    access_clarity: 34.2
    commercial_clarity: 34.2
    contract_governance: 16.7
    contract_quality: 13.0
    developer_ergonomics: 66.1
    discoverability: 81.5
    governance: 16.7
    operational_transparency: 2.6
  previous_composite: 33.0
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 4
      marker_coverage: 100.0
      total: 4
    mcp: derived
    skills: derived
  schema_version: 0.12.0
  scored_at: '2026-08-19'
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
