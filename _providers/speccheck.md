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
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: documented
    event_surface_described: false
    idempotency: documented
    mcp_server: false
    openapi_examples: verified
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 29.3
  scored_at: '2026-08-26'
agentic_access:
- acting_count: 2
  human_in_the_loop: 0
  name: Speccheck Agentic Access
  operation_count: 8
  slug: speccheck-agentic-access
  summary_line: 8 operations · 2 acting
api_count: 4
apis:
- description: Obtain bearer access tokens.
  name: SpecCheck Authentication API
  slug: speccheck-authentication-api
- description: Lens styles, materials, and add-ons available for a lab.
  name: SpecCheck Catalogs API
  slug: speccheck-catalogs-api
- description: Labs associated with a user and their order settings.
  name: SpecCheck Labs API
  slug: speccheck-labs-api
- description: Create and list optical orders.
  name: SpecCheck Orders API
  slug: speccheck-orders-api
arazzos:
- description: 'End-to-end flow: authenticate with client credentials, resolve the user''s lab and its order settings, walk the lens catalog (styles → materials → add-ons), then submit a prescription order. Every oper'
  name: SpecCheck — Create a prescription (rx) order
  slug: speccheck-create-rx-order
- description: Authenticate, resolve the user's lab, then page recent orders (most recent first) with cursor pagination and an optional created-date filter. Every operationId is verified against openapi/speccheck-op
  name: SpecCheck — List recent orders for a lab
  slug: speccheck-list-recent-orders
artifact_total: 15
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: SpecCheck Authentication API
  slug: open-speccheck-authentication-api
- collection_type: open
  name: SpecCheck Authentication Catalogs API
  slug: open-speccheck-catalogs-api
- collection_type: open
  name: SpecCheck Authentication Labs API
  slug: open-speccheck-labs-api
- collection_type: open
  name: SpecCheck Authentication Orders API
  slug: open-speccheck-orders-api
common:
- group: start
  title: ''
  type: DeveloperPortal
  url: https://docs.speccheckrx.com/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.speccheckrx.com/introduction
- group: docs
  title: ''
  type: APIReference
  url: https://docs.speccheckrx.com/api-reference/endpoint/create_order
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.speccheckrx.com/introduction
- group: start
  title: ''
  type: Login
  url: https://dashboard.speccheckrx.com/
- group: operate
  title: ''
  type: StatusPage
  url: https://status.speccheckrx.com/
- group: docs
  title: ''
  type: OpenAPI
  url: openapi/_original/speccheck-openapi.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/speccheck-authentication.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/speccheck-conventions.yml
- group: design
  title: ''
  type: Idempotency
  url: conventions/speccheck-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/speccheck-problem-types.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/speccheck-lifecycle.yml
- group: start
  title: ''
  type: Sandbox
  url: sandbox/speccheck-sandbox.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/speccheck-data-model.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/speccheck-conformance.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/speccheck-mcp.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/speccheck-llms.txt
- group: other
  title: ''
  type: Overlay
  url: overlays/speccheck-openapi-overlay.yaml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/speccheck-well-known.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/speccheck-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/speccheck-domain-security.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/speccheck-create-rx-order.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/speccheck-list-recent-orders.yml
- group: company
  title: ''
  type: Website
  url: https://speccheckrx.com/
created: '2026-07-17'
description: SpecCheck (speccheckrx.com) is an optical lab ordering platform for eyecare practices and eyewear partners. Its REST API lets integrators authenticate with client credentials, list the labs a user is associated with, retrieve a lab's order settings, browse the lens catalog (styles, materials, and add-on coats, colors, and tints), and create prescription (rx), frame, redo, and multi-pair orders. The API uses 24-hour bearer tokens plus a User-Email actor header, an Idempotency-Key header for safe POST retries, cursor pagination on list endpoints, and a consistent error envelope. SpecCheck was surfaced as a portfolio company of Initialized Capital and enriched by the API Evangelist pipeline from its public documentation at docs.speccheckrx.com.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/speccheck.png
layout: provider
mcp_servers:
- description: ''
  name: SpecCheck MCP Server
  slug: speccheck-mcp-server
modified: '2026-07-21'
name: SpecCheck
nav: Providers
network: true
overview: 'SpecCheck publishes 4 APIs on the [APIs.io](https://apis.io/) network, including Authentication API, Catalogs API, Labs API, and 1 more. Tagged areas include Company, Enterprise Saas, Optical, Eyewear, and Eye Care.


  SpecCheck''s developer surface includes documentation, API reference, getting-started guide, authentication, sandbox, and 20 more developer resources.'
random_paper: 13
score:
  band: thin
  composite: 38.8
  delta: 0.0
  facets:
    access_clarity: 6.6
    commercial_clarity: 6.6
    contract_governance: 16.7
    contract_quality: 60.5
    developer_ergonomics: 58.9
    discoverability: 81.5
    governance: 16.7
    operational_transparency: 0.0
  previous_composite: 38.8
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 4
    mcp: derived
    skills: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Health
    regime_id: health
    score: 21.3
  schema_version: 0.15.0
  scored_at: '2026-08-26'
  trend: flat
security:
- kind: authentication
  name: Speccheck Authentication
  slug: speccheck-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Speccheck Domain Security
  slug: speccheck-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: speccheck
tags:
- Company
- Enterprise Saas
- Optical
- Eyewear
- Eye Care
- Optical Labs
- Prescriptions
- Ordering
- Healthcare
website: https://speccheckrx.com/
---
