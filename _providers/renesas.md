---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source:
  - authentication
  - security
  - sandbox
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
    mcp_server: platform
    openapi_examples: verified
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 40.8
  scored_at: '2026-09-16'
agentic_access:
- acting_count: 2
  human_in_the_loop: 0
  name: Renesas Agentic Access
  operation_count: 18
  slug: renesas-agentic-access
  summary_line: 18 operations · 2 acting
api_count: 1
apis:
- baseURL: https://api.renesas.com/web-data/v1
  baseurl_source: declared
  description: Endpoints for retrieving boards and kits.
  name: Renesas Board & Kit API
  slug: renesas-board-kit-api
- baseURL: https://api.renesas.com/web-data/v1
  baseurl_source: declared
  description: Endpoint for retrieving documents.
  name: Renesas Document API
  slug: renesas-document-api
- baseURL: https://api.renesas.com/web-data/v1
  baseurl_source: declared
  description: Endpoints for retrieving packages.
  name: Renesas Package API
  slug: renesas-package-api
- baseURL: https://api.renesas.com/web-data/v1
  baseurl_source: declared
  description: Endpoints for retrieving products.
  name: Renesas Product API
  slug: renesas-product-api
- baseURL: https://api.renesas.com/web-data/v1
  baseurl_source: declared
  description: Endpoints for retrieving product parts.
  name: Renesas Product Part API
  slug: renesas-product-part-api
- baseURL: https://api.renesas.com/web-data/v1
  baseurl_source: declared
  description: Endpoints for retrieving software tools.
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
  href: https://raw.githubusercontent.com/api-evangelist/renesas/refs/heads/main/capabilities/renesas-capability-edges.yml
  title: ''
  type: CapabilityMap
  url: capabilities/renesas-capability-edges.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/renesas/refs/heads/main/agentic-access/renesas-agentic-access.yml
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
  href: https://raw.githubusercontent.com/api-evangelist/renesas/refs/heads/main/authentication/renesas-authentication.yml
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
  href: https://raw.githubusercontent.com/api-evangelist/renesas/refs/heads/main/openapi/_original/renesas-web-data-openapi-original.yml
  title: ''
  type: OpenAPI
  url: openapi/_original/renesas-web-data-openapi-original.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/renesas/refs/heads/main/overlays/renesas-web-data-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/renesas-web-data-overlay.yaml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/renesas/refs/heads/main/openapi/_original/renesas-web-data-openapi-original.yml
  title: ''
  type: Examples
  url: openapi/_original/renesas-web-data-openapi-original.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/renesas/refs/heads/main/mcp/renesas-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/renesas-mcp.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/renesas/refs/heads/main/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/renesas/refs/heads/main/llms/renesas-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/renesas-llms.txt
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/renesas/refs/heads/main/well-known/renesas-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/renesas-well-known.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/renesas/refs/heads/main/errors/renesas-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/renesas-problem-types.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/renesas/refs/heads/main/conventions/renesas-conventions.yml
  title: ''
  type: Conventions
  url: conventions/renesas-conventions.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/renesas/refs/heads/main/data-model/renesas-data-model.yml
  title: ''
  type: DataModel
  url: data-model/renesas-data-model.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/renesas/refs/heads/main/lifecycle/renesas-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/renesas-lifecycle.yml
- group: operate
  href: https://raw.githubusercontent.com/api-evangelist/renesas/refs/heads/main/changelog/renesas-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/renesas-changelog.yml
- group: start
  href: https://raw.githubusercontent.com/api-evangelist/renesas/refs/heads/main/sandbox/renesas-sandbox.yml
  title: ''
  type: Sandbox
  url: sandbox/renesas-sandbox.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/renesas/refs/heads/main/conformance/renesas-conformance.yml
  title: ''
  type: Conformance
  url: conformance/renesas-conformance.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/renesas/refs/heads/main/security/renesas-domain-security.yml
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
random_paper: 5
score:
  band: developing
  composite: 43.5
  coverage:
    artifact_dirs: 19
    catalog_earned: 37.0
    catalog_earned_first_party: 0.0
    catalog_gap: 78.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.7
  facets:
    access_clarity: 34.2
    contract_governance: 4.5
    contract_quality: 54.4
    developer_ergonomics: 66.1
    discoverability: 75.9
    operational_transparency: 18.4
  previous_composite: 42.8
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
  schema_version: 0.22.0
  scored_at: '2026-09-16'
  trend: flat
  upsert:
    applies: true
    score: 0.0
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
- Developer Tools
website: https://www.renesas.com
---
