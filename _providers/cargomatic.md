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
    agentic_access: false
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: verified
    event_surface_described: false
    idempotency: false
    mcp_server: derived
    openapi_examples: false
    rate_limit_signal: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 36.3
  scored_at: '2026-08-03'
api_count: 5
apis:
- description: Endpoints dealing with authenticating to the API
  name: Cargomatic Authorization API
  slug: cargomatic-authorization-api
- description: Endpoints for Cargomatic Carriers and Drivers
  name: Cargomatic Carrier API
  slug: cargomatic-carrier-api
- description: The Document API from Cargomatic — 2 operation(s) for document.
  name: Cargomatic Document API
  slug: cargomatic-document-api
- description: Endpoints for Cargomatic Shippers
  name: Cargomatic Shipper API
  slug: cargomatic-shipper-api
- description: Endpoints for managing shipment stops
  name: Cargomatic Stops API
  slug: cargomatic-stops-api
artifact_total: 8
common:
- group: company
  title: ''
  type: Website
  url: https://cargomatic.com/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://api-docs.cargomatic.com/#/
- group: docs
  title: ''
  type: Documentation
  url: https://api-docs.cargomatic.com/#/
- group: docs
  title: ''
  type: APIReference
  url: https://api-docs.cargomatic.com/#/
- group: operate
  title: ''
  type: Support
  url: https://cargomatic.com/support/
- group: operate
  title: ''
  type: SupportContact
  url: https://cargomatic.com/support/contact-us/
- group: operate
  title: ''
  type: FAQ
  url: https://cargomatic.com/support/faq/
- group: company
  title: ''
  type: Blog
  url: https://cargomatic.com/blog/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/cargomatic
- group: start
  title: ''
  type: SignUp
  url: https://cargomatic.com/sign-up/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://cargomatic.com/terms-of-service/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://cargomatic.com/privacy-policy/
- group: company
  title: ''
  type: Careers
  url: https://cargomatic.com/about/careers/
- group: company
  title: ''
  type: About
  url: https://cargomatic.com/about/
- group: operate
  title: ''
  type: SupportEmail
  url: mailto:apisupport@cargomatic.com
- group: docs
  title: ''
  type: OpenAPI
  url: openapi/cargomatic-openapi-original.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/cargomatic-authentication.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/cargomatic-problem-types.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/cargomatic-conventions.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/cargomatic-conformance.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/cargomatic-data-model.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/cargomatic-lifecycle.yml
- group: start
  title: ''
  type: Sandbox
  url: sandbox/cargomatic-sandbox.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/cargomatic-mcp.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/cargomatic-llms.txt
- group: auth
  title: ''
  type: DomainSecurity
  url: security/cargomatic-domain-security.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
created: '2026-07-17'
description: Cargomatic is a technology-enabled marketplace for local freight and drayage that connects shippers with a network of more than 35,000 professional truck drivers across the top 20 ports in the continental United States. Its platform automates quoting, booking, dispatch, tracking, and document exchange for drayage, intermodal, less-than-truckload (LTL), full-truckload (FTL), and white-glove final-mile delivery. Cargomatic exposes a public REST API (the Cargomatic Public API) so shippers and carriers can automate the same quoting, order-creation, shipment-status, stop-management, driver-assignment, and document workflows available in the Cargomatic portal, authenticating with JWT bearer tokens issued from an authentication endpoint. The company is headquartered in Long Beach, California and is backed by Canaan Partners and the SoftBank Vision Fund.
image: https://cargomatic.com/wp-content/uploads/2021/01/cargomatic-logo.png
layout: provider
mcp_servers:
- description: ''
  name: Cargomatic MCP Server manifest (candidate)
  slug: cargomatic-mcp-server-manifest-candidate
modified: '2026-07-18'
name: Cargomatic
nav: Providers
network: true
overview: 'Cargomatic publishes 5 APIs on the [APIs.io](https://apis.io/) network, including Authorization API, Carrier API, Document API, and 2 more. Tagged areas include Company, Logistics, Freight, Drayage, and Transportation.


  Cargomatic''s developer surface includes documentation, API reference, support, FAQ, engineering blog, signup flow, authentication, and 20 more developer resources.'
random_paper: 5
score:
  band: thin
  composite: 41.9
  delta: 0.0
  facets:
    commercial_clarity: 34.2
    contract_quality: 58.1
    developer_ergonomics: 51.6
    discoverability: 81.5
    governance: 11.5
    operational_transparency: 5.3
  previous_composite: 41.9
  provenance:
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 5
    mcp: derived
    skills: derived
  schema_version: 0.9
  scored_at: '2026-08-03'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/cargomatic/refs/heads/main/screenshots/cargomatic-2026-07-25T204608.png
security:
- kind: authentication
  name: Cargomatic Authentication
  slug: cargomatic-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Cargomatic Domain Security
  slug: cargomatic-domain-security
  summary_line: TLSv1.3 · DMARC
slug: cargomatic
tags:
- Company
- Logistics
- Freight
- Drayage
- Transportation
- Supply Chain
- Shipping
- Trucking
- Marketplace
- Intermodal
website: https://cargomatic.com/
---
