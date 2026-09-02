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
  band_gated_from: agent-native
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: served
    consent_identity: false
    delegated_identity: served
    dry_run_mode: false
    dynamic_client_registration: true
    error_semantics: documented
    event_surface_described: false
    idempotency: false
    mcp_server: verified
    openapi_examples: verified
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 47.3
  scored_at: '2026-09-01'
agentic_access:
- acting_count: 2
  human_in_the_loop: 0
  name: Renesas Agentic Access
  operation_count: 18
  slug: renesas-agentic-access
  summary_line: 18 operations · 2 acting
api_count: 1
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
artifact_total: 17
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Renesas Web Data Board & Kit API
  slug: open-renesas-board-kit-api
- collection_type: open
  name: Renesas Web Data Board & Kit Document API
  slug: open-renesas-document-api
- collection_type: open
  name: Renesas Web Data Board & Kit Package API
  slug: open-renesas-package-api
- collection_type: open
  name: Renesas Web Data Board & Kit Product API
  slug: open-renesas-product-api
- collection_type: open
  name: Renesas Web Data Board & Kit Product Part API
  slug: open-renesas-product-part-api
- collection_type: open
  name: Renesas Web Data Board & Kit Software Tool API
  slug: open-renesas-software-tool-api
common:
- group: other
  title: ''
  type: CapabilityMap
  url: capabilities/renesas-capability-edges.yml
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
  url: openapi/_original/renesas-web-data-openapi-original.yml
- group: other
  title: ''
  type: Overlay
  url: overlays/renesas-web-data-overlay.yaml
- group: build
  title: ''
  type: Examples
  url: openapi/_original/renesas-web-data-openapi-original.yml
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
  name: Renesas Web Data API docs MCP
  slug: renesas-web-data-api-docs-mcp
modified: '2026-07-20'
name: Renesas
nav: Providers
network: true
overview: 'Renesas publishes 6 APIs on the [APIs.io](https://apis.io/) network, including Board & Kit API, Document API, Package API, and 3 more. Tagged areas include Company, Semiconductors, Microcontrollers, Electronics, and Hardware.


  Renesas'' developer surface includes documentation, API reference, getting-started guide, authentication, support, engineering blog, signup flow, and 22 more developer resources.'
random_paper: 18
score:
  band: developing
  composite: 43.5
  coverage:
    artifact_dirs: 20
    catalog_gap: 78.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 34.2
    commercial_clarity: 34.2
    contract_governance: 4.5
    contract_quality: 51.7
    developer_ergonomics: 66.1
    discoverability: 75.9
    governance: 4.5
    operational_transparency: 18.4
  previous_composite: 43.5
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
  schema_version: 0.18.0
  scored_at: '2026-09-01'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/renesas/refs/heads/main/screenshots/renesas-2026-08-17T081518.png
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
