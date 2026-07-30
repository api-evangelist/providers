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
    asyncapi_events: false
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: documented
    idempotency: false
    mcp_server: true
    openapi_examples: verified
    rate_limit_signal: false
    spec_presence: true
    well_known_catalog: true
  schema_version: 0.2
  score: 52.9
  scored_at: '2026-07-28'
agentic_access:
- acting_count: 2
  human_in_the_loop: 0
  name: Renesas Agentic Access
  operation_count: 18
  slug: renesas-agentic-access
  summary_line: 18 operations · 2 acting
api_count: 6
apis:
- description: Endpoints for retrieving boards and kits.
  name: Renesas Board & Kit API
  slug: renesas-board-kit-api
- description: Endpoint for retrieving documents.
  name: Renesas Document API
  slug: renesas-document-api
- description: Endpoints for retrieving packages.
  name: Renesas Package API
  slug: renesas-package-api
- description: Endpoints for retrieving products.
  name: Renesas Product API
  slug: renesas-product-api
- description: Endpoints for retrieving product parts.
  name: Renesas Product Part API
  slug: renesas-product-part-api
- description: Endpoints for retrieving software tools.
  name: Renesas Software Tool API
  slug: renesas-software-tool-api
artifact_total: 10
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/renesas-agentic-access.yml
- group: company
  title: ''
  type: Website
  url: https://www.renesas.com
- group: start
  title: ''
  type: DeveloperPortal
  url: https://developer.renesas.com
- group: docs
  title: ''
  type: Documentation
  url: https://developer.renesas.com/docs/web-data-api
- group: docs
  title: ''
  type: APIReference
  url: https://developer.renesas.com/docs/web-data-api/apis/web-data
- group: start
  title: ''
  type: GettingStarted
  url: https://developer.renesas.com/docs/web-data-api/guides/quickstart
- group: auth
  title: ''
  type: Authentication
  url: authentication/renesas-authentication.yml
- group: operate
  title: ''
  type: Support
  url: https://www.renesas.com/en/support
- group: company
  title: ''
  type: Blog
  url: https://www.renesas.com/en/blogs
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/renesas
- group: start
  title: ''
  type: SignUp
  url: https://www.renesas.com/en/form/web-data-api-access-request
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.renesas.com/legal-notices
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.renesas.com/privacy
- group: docs
  title: ''
  type: OpenAPI
  url: openapi/renesas-web-data-openapi-original.yml
- group: other
  title: ''
  type: Overlay
  url: overlays/renesas-web-data-overlay.yaml
- group: build
  title: ''
  type: Examples
  url: openapi/renesas-web-data-openapi-original.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/renesas-mcp.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/renesas-llms.txt
- group: agent
  title: ''
  type: WellKnown
  url: well-known/renesas-well-known.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/renesas-problem-types.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/renesas-conventions.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/renesas-data-model.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/renesas-lifecycle.yml
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/renesas-changelog.yml
- group: start
  title: ''
  type: Sandbox
  url: sandbox/renesas-sandbox.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/renesas-conformance.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/renesas-domain-security.yml
created: '2026-07-17'
description: 'Renesas Electronics Corporation (TYO: 6723) is a global semiconductor manufacturer producing microcontrollers and microprocessors (RA, RX, RL78, RH850, RZ, Synergy families), analog, power, sensor, timing, connectivity, and memory products for automotive, industrial, infrastructure, and consumer electronics applications. On the developer side Renesas operates a public developer portal at developer.renesas.com whose flagship programmable interface is the Renesas Web Data API — a REST API that lets approved partners and integrators retrieve Renesas product metadata (products, product parts, documents, boards & kits, packages, and software tools) in real time instead of relying on manual CSV downloads or periodic feed refreshes. The API is documented on a Redocly Realm site, ships an OpenAPI 3.0.0 description, an auto-generated Model Context Protocol (MCP) server, a browser Try-It console, and a semantic-versioned changelog.'
image: https://www.renesas.com/themes/kachow/images/renesas-logo.png
layout: provider
mcp_servers:
- description: ''
  name: renesas-mcp.yml
  slug: renesas-mcpyml
modified: '2026-07-20'
name: Renesas
nav: Providers
network: true
overview: 'Renesas publishes 6 APIs on the [APIs.io](https://apis.io/) network, including Board & Kit API, Document API, Package API, and 3 more. Tagged areas include Company, Semiconductors, Microcontrollers, Electronics, and Hardware.


  Renesas'' developer surface includes documentation, API reference, getting-started guide, authentication, support, engineering blog, signup flow, and 21 more developer resources.'
random_paper: 15
score:
  band: developing
  composite: 46.8
  delta: 0.2
  facets:
    commercial_clarity: 34.2
    contract_quality: 51.1
    developer_ergonomics: 69.0
    discoverability: 92.6
    governance: 11.5
    operational_transparency: 21.1
  previous_composite: 46.6
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 6
    mcp: first-party
    skills: derived
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: flat
security:
- kind: authentication
  name: Renesas Authentication
  slug: renesas-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Renesas Domain Security
  slug: renesas-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: renesas
tags:
- Company
- Semiconductors
- Microcontrollers
- Electronics
- Hardware
- Product Data
- Developer Portal
- Automotive
- Industrial
- Embedded
website: https://www.renesas.com
---
