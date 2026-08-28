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
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: documented
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 22.8
  scored_at: '2026-08-26'
agentic_access:
- acting_count: 7
  human_in_the_loop: 0
  name: Einride Agentic Access
  operation_count: 14
  slug: einride-agentic-access
  summary_line: 14 operations · 7 acting
api_count: 3
apis:
- description: The AuthenticationService API from Einride — 1 operation(s) for authenticationservice.
  name: Einride AuthenticationService API
  slug: einride-authenticationservice-api
- description: The BookingService API from Einride — 7 operation(s) for bookingservice.
  name: Einride BookingService API
  slug: einride-bookingservice-api
- description: The ShipmentService API from Einride — 6 operation(s) for shipmentservice.
  name: Einride ShipmentService API
  slug: einride-shipmentservice-api
artifact_total: 12
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: 'Einride Extend: Authentication AuthenticationService API'
  slug: open-einride-authenticationservice-api
- collection_type: open
  name: 'Einride Extend: Authentication AuthenticationService BookingService API'
  slug: open-einride-bookingservice-api
- collection_type: open
  name: 'Einride Extend: Authentication AuthenticationService ShipmentService API'
  slug: open-einride-shipmentservice-api
common:
- group: other
  title: ''
  type: Overlay
  url: overlays/einride-auth-overlay.yaml
- group: operate
  title: ''
  type: IssueTracker
  url: https://github.com/einride/extend/issues
- group: operate
  title: ''
  type: Releases
  url: https://github.com/einride/extend/releases
- group: auth
  title: ''
  type: SecurityPolicy
  url: https://github.com/einride/extend/blob/master/SECURITY.md
- group: build
  title: ''
  type: CodeOfConduct
  url: https://github.com/einride/extend/blob/master/CODE_OF_CONDUCT.md
- group: commercial
  title: ''
  type: License
  url: https://github.com/einride/extend/blob/master/LICENSE
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/einride-agentic-access.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/einride-authentication.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/einride-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/einride-problem-types.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/einride-data-model.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/einride-lifecycle.yml
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/einride-changelog.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/einride-conformance.yml
- group: build
  title: ''
  type: Packages
  url: packages/einride-packages.yml
- group: build
  title: ''
  type: CLI
  url: cli/einride-cli.yml
- group: design
  title: ''
  type: Components
  url: components/einride-components.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/einride-mcp.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/einride-llms.txt
- group: agent
  title: ''
  type: WellKnown
  url: well-known/einride-well-known.yml
- group: auth
  title: ''
  type: SecurityTxt
  url: well-known/einride-security.txt
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/einride-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: Security
  url: https://www.einride.tech/security/vulnerability-disclosure-policy
- group: auth
  title: ''
  type: DomainSecurity
  url: security/einride-domain-security.yml
- group: start
  title: ''
  type: DeveloperPortal
  url: https://extend.saga.einride.tech
- group: docs
  title: ''
  type: Documentation
  url: https://github.com/einride/extend/blob/master/docs/apis.md
- group: docs
  title: ''
  type: APIReference
  url: https://extend.saga.einride.tech
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/einride
- group: build
  title: ''
  type: SourceCode
  url: https://github.com/einride/extend
- group: company
  title: ''
  type: Blog
  url: https://einride.engineering/blog
- group: start
  title: ''
  type: SignUp
  url: https://forms.gle/Sn3CYSgUgJbJE78X9
- group: operate
  title: ''
  type: Support
  url: https://www.einride.tech/contact
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.einride.tech/privacy/privacy-policy
- group: company
  title: ''
  type: Website
  url: https://www.einride.tech/
created: '2026-07-17'
description: Einride is a Swedish freight technology company delivering an end-to-end platform for electric and autonomous road freight, combining purpose-built autonomous trucks, electric vehicles, smart charging, and the Saga operating software. Its developer-facing product, Einride Extend, exposes open, resource-oriented APIs (designed with Google AIP) over both gRPC and HTTP for booking truck tours and creating, releasing, and tracking shipments. The Extend APIs are alpha (v1beta1) and offered to select developers during an early-access phase, with a saga CLI, Buf Schema Registry proto module, and React UI component library. Einride serves customers including PepsiCo, Heineken, and DP World across Europe, the US, and the Middle East.
image: https://raw.githubusercontent.com/einride/extend/master/docs/img/header.png
layout: provider
mcp_servers:
- description: ''
  name: Einride MCP Server
  slug: einride-mcp-server
modified: '2026-07-19'
name: Einride
nav: Providers
network: true
overview: 'Einride publishes 3 APIs on the [APIs.io](https://apis.io/) network: AuthenticationService API, BookingService API, and ShipmentService API. Tagged areas include Company, Sustainable Transport, Freight, Logistics, and Autonomous Vehicles.


  Einride''s developer surface includes authentication, changelog, CLI, documentation, API reference, engineering blog, signup flow, and 28 more developer resources.'
random_paper: 1
score:
  band: thin
  composite: 38.1
  delta: 1.3
  facets:
    access_clarity: 23.7
    commercial_clarity: 23.7
    contract_governance: 16.7
    contract_quality: 43.5
    developer_ergonomics: 37.5
    discoverability: 92.6
    governance: 16.7
    operational_transparency: 28.9
  previous_composite: 36.8
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 3
    mcp: derived
    skills: derived
  schema_version: 0.15.0
  scored_at: '2026-08-26'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/einride/refs/heads/main/screenshots/einride-2026-07-25T213026.png
security:
- kind: authentication
  name: Einride Authentication
  slug: einride-authentication
  summary_line: bearer · 1 scheme
- kind: domain-security
  name: Einride Domain Security
  slug: einride-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Einride Vulnerability Disclosure
  slug: einride-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: einride
tags:
- Company
- Sustainable Transport
- Freight
- Logistics
- Autonomous Vehicles
- Electric Vehicles
- Shipping
- gRPC
website: https://www.einride.tech/
---
