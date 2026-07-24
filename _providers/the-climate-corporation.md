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
- acting_count: 6
  human_in_the_loop: 0
  name: The Climate Corporation Agentic Access
  operation_count: 28
  slug: the-climate-corporation-agentic-access
  summary_line: 28 operations · 6 acting
api_count: 8
apis:
- description: Field Boundary data endpoints.
  name: The Climate Corporation Boundaries API
  slug: the-climate-corporation-boundaries-api
- description: General data export endpoints.
  name: The Climate Corporation Exports API
  slug: the-climate-corporation-exports-api
- description: Farm organization data endpoints.
  name: The Climate Corporation FarmOrganizations API
  slug: the-climate-corporation-farmorganizations-api
- description: Field data endpoints.
  name: The Climate Corporation Fields API
  slug: the-climate-corporation-fields-api
- description: General data retrieval endpoints.
  name: The Climate Corporation Layers API
  slug: the-climate-corporation-layers-api
- description: Operation data endpoints.
  name: The Climate Corporation Operations API
  slug: the-climate-corporation-operations-api
- description: Resource Owner data endpoints.
  name: The Climate Corporation ResourceOwners API
  slug: the-climate-corporation-resourceowners-api
- description: General data upload endpoints.
  name: The Climate Corporation Uploads API
  slug: the-climate-corporation-uploads-api
artifact_total: 13
common:
- group: start
  title: ''
  type: DeveloperPortal
  url: https://dev.fieldview.com/
- group: docs
  title: ''
  type: Documentation
  url: https://dev.fieldview.com/technical-documentation/
- group: docs
  title: ''
  type: APIReference
  url: https://dev.fieldview.com/technical-documentation/
- group: start
  title: ''
  type: SignUp
  url: https://dev.fieldview.com/join-us
- group: operate
  title: ''
  type: Support
  url: https://support.climate.com/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/TheClimateCorporation
- group: commercial
  title: ''
  type: TermsOfService
  url: https://climate.com/legal/end-user-license-agreement
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://climate.com/legal/privacy-policy
- group: auth
  title: ''
  type: Authentication
  url: authentication/the-climate-corporation-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/the-climate-corporation-scopes.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/the-climate-corporation-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/the-climate-corporation-problem-types.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/the-climate-corporation-conformance.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/the-climate-corporation-lifecycle.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/the-climate-corporation-data-model.yml
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/the-climate-corporation-agentic-access.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/the-climate-corporation-mcp.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: start
  title: ''
  type: Sandbox
  url: sandbox/the-climate-corporation-sandbox.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/the-climate-corporation-domain-security.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/the-climate-corporation-llms.txt
created: '2026-07-17'
description: 'The Climate Corporation (Climate LLC, a Bayer company) operates Climate FieldView, one of the world''s largest digital agriculture platforms, spanning 120M+ acres and 100,000+ farmers. Its FieldView Platform APIs let approved partners read and write growers'' data with OAuth2 consent: field boundaries (GeoJSON), farm organizations, operations, resource owners, and agronomic layers (as-planted, as-applied, as-harvested, scouting), plus asynchronous bulk uploads and exports of planting, application, harvest, imagery, seeding prescription (rx), and soil-sample data. Every call requires both a Bearer access token and a partner X-Api-Key. A v5 API surface is in preview.'
image: https://s3-us-west-2.amazonaws.com/climate-com/favicons/android-chrome-192x192.png
layout: provider
mcp_servers:
- description: ''
  name: the-climate-corporation-mcp.yml
  slug: the-climate-corporation-mcpyml
modified: '2026-07-21'
name: The Climate Corporation
nav: Providers
network: true
overview: 'The Climate Corporation publishes 8 APIs on the [APIs.io](https://apis.io/) network, including Boundaries API, Exports API, FarmOrganizations API, and 5 more. Tagged areas include Company, Climate, Agriculture, AgTech, and Digital Agriculture.


  The Climate Corporation''s developer surface includes documentation, API reference, signup flow, support, authentication, sandbox, and 15 more developer resources.'
random_paper: 0
scopes:
- name: The Climate Corporation Scopes
  scope_count: 24
  slug: the-climate-corporation-scopes
  summary_line: 24 scopes · authorizationCode
score:
  band: thin
  composite: 44.8
  delta: 0.0
  facets:
    commercial_clarity: 34.2
    contract_quality: 60.4
    developer_ergonomics: 60.9
    discoverability: 100.0
    governance: 0.0
    operational_transparency: 5.3
  previous_composite: 44.8
  schema_version: 0.5
  scored_at: '2026-07-23'
  trend: flat
security:
- kind: authentication
  name: The Climate Corporation Authentication
  slug: the-climate-corporation-authentication
  summary_line: apiKey/oauth2 · 2 schemes
- kind: domain-security
  name: The Climate Corporation Domain Security
  slug: the-climate-corporation-domain-security
  summary_line: TLSv1.3 · DMARC
slug: the-climate-corporation
tags:
- Company
- Climate
- Agriculture
- AgTech
- Digital Agriculture
- Farm Management
- Geospatial
- APIs
website: https://dev.fieldview.com/
---
