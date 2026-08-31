---
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
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
    openapi_examples: documented
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 9.2
  scored_at: '2026-08-30'
api_count: 1
apis:
- description: Electra's Open Charge Point Interface implementation in the Charge Point Operator role — the roaming interface an e-mobility service provider calls to read Electra's locations and tariffs, authorise i
  name: Electra OCPI CPO API
  slug: go-electra-ocpi-cpo-api
artifact_total: 10
common:
- group: company
  title: ''
  type: Website
  url: https://www.go-electra.com/
- group: company
  title: ''
  type: About
  url: https://www.go-electra.com/en/about/
- group: commercial
  title: ''
  type: Pricing
  url: https://www.go-electra.com/en/price/
- group: start
  title: ''
  type: SignUp
  url: https://business.go-electra.com/register
- group: start
  title: ''
  type: Login
  url: https://business.go-electra.com/sign-in
- group: operate
  title: ''
  type: Support
  url: https://intercom.help/go-electra/en/
- group: operate
  title: ''
  type: Contact
  url: https://www.go-electra.com/en/contact/
- group: company
  title: ''
  type: Blog
  url: https://www.go-electra.com/en/newsroom/all-categories/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.go-electra.com/en/tos/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.go-electra.com/en/privacy/
- group: commercial
  title: ''
  type: Legal
  url: https://www.go-electra.com/en/legal/
- group: auth
  title: ''
  type: TrustCenter
  url: https://trust.go-electra.com/
- group: other
  title: ''
  type: Ethics
  url: https://www.go-electra.com/en/whistleblowing-and-grievance/
- group: other
  title: ''
  type: Sustainability
  url: https://www.go-electra.com/en/sustainability/
- group: other
  title: ''
  type: Application
  url: https://app.go-electra.com/
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/electra-charge
- group: company
  title: ''
  type: Careers
  url: https://careers.go-electra.com/en
- group: auth
  title: ''
  type: Authentication
  url: authentication/go-electra-authentication.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/go-electra-conformance.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/go-electra-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/go-electra-problem-types.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/go-electra-lifecycle.yml
- group: build
  title: ''
  type: Examples
  url: examples/_index.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/go-electra-domain-security.yml
- group: build
  title: ''
  type: Packages
  url: packages/go-electra-packages.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/go-electra-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/go-electra-rate-limits.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/go-electra-mcp.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/go-electra-llms.txt
created: '2026-08-17'
description: 'Electra is a European operator of ultra-fast electric-vehicle charging, headquartered at 104 rue de Richelieu in the 2nd arrondissement of Paris and led by co-founder and CEO Aurelien de Meaux. It designs, finances, installs and operates its own DC fast-charging stations rather than reselling someone else''s hardware, advertising 770+ live stations with 68 more under construction, charge rates up to 400 kW, and a target of 2,200 stations / 15,000 charge points across Europe by 2030. Its own pricing and station pages cover France, Belgium, Spain, Italy, Germany, Austria, the Netherlands and Switzerland, with city hubs in Paris, Lyon, Marseille, Brussels, Antwerp, Liege, Milan, Bologna, Turin, Madrid, Barcelona and Zurich. The commercial surface is consumer- and fleet-facing: a mobile app, an Electra+ subscription that cuts up to 0.20 EUR/kWh, an RFID charging card, Autocharge and Plug&Charge, and a fleet dashboard at business.go-electra.com. It is a Serena portfolio company
  and has raised a 160 MEUR round, a 304 MEUR Series B and a 433 MEUR debt facility. Electra publishes NO developer portal, NO API documentation, NO OpenAPI, NO llms.txt, NO MCP server and NO A2A agent card — every one of those was probed and missed on 2026-08-17. What it does run, and what almost nobody looking at the marketing site would find, is a real machine-readable API: a live Open Charge Point Interface implementation in the Charge Point Operator role at https://ocpi.go-electra.com/ocpi/cpo, serving BOTH OCPI 2.1.1 and OCPI 2.2.1 concurrently. Its version-negotiation endpoints answer anonymously with HTTP 200 and enumerate the full module inventory — cdrs, commands, credentials, locations, sessions, tariffs and tokens, with SENDER/RECEIVER roles declared on the 2.2.1 surface — while every data module itself returns HTTP 401 with `WWW-Authenticate: Token realm="Application"`, OCPI''s own bilateral token scheme. That is a documented open industry standard, fully implemented, discoverable
  without credentials and readable only with a roaming agreement; its production use is evidenced by the 180+ e-mobility service provider cards Electra''s own help centre lists as accepted at its chargers.'
examples:
- key_count: 4
  name: Go Electra Ocpi Cpo 2.1.1 Endpoints
  slug: go-electra-ocpi-cpo-2.1.1-endpoints
- key_count: 4
  name: Go Electra Ocpi Cpo 2.2.1 Endpoints
  slug: go-electra-ocpi-cpo-2.2.1-endpoints
- key_count: 4
  name: Go Electra Ocpi Cpo Versions
  slug: go-electra-ocpi-cpo-versions
image: https://www.go-electra.com/favicons/apple-touch-icon-1024x1024.png
layout: provider
mcp_servers:
- description: 'Electra publishes NO MCP server. This file is a candidate design, not a provider claim. Every search and probe missed: no mcp subdomain resolves, no MCP endpoint is documented, no npm or PyPI package '
  name: Electra MCP Server
  slug: electra-mcp-server
modified: '2026-08-17'
name: Electra
nav: Providers
network: true
overview: 'Electra publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Climate Tech, EV Charging, Energy, and Mobility.


  Electra''s developer surface includes pricing, signup flow, support, engineering blog, legal docs, authentication, code examples, and 22 more developer resources.'
plans:
- name: Go Electra Plans Pricing
  plan_count: 4
  slug: go-electra-plans-pricing
random_paper: 8
rate_limits:
- limit_count: 0
  name: Go Electra Rate Limits
  slug: go-electra-rate-limits
score:
  band: thin
  composite: 33.2
  coverage:
    artifact_dirs: 14
    catalog_gap: 66.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 77.6
    commercial_clarity: 77.6
    contract_governance: 18.2
    contract_quality: 6.7
    developer_ergonomics: 19.0
    discoverability: 68.5
    governance: 18.2
    operational_transparency: 0.0
  previous_composite: 33.2
  provenance:
    conformance: first-party
    mcp: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Energy & Utilities
    regime_id: energy_utilities
    score: 40.5
  schema_version: 0.17.2
  scored_at: '2026-08-30'
  trend: flat
security:
- kind: authentication
  name: Go Electra Authentication
  slug: go-electra-authentication
  summary_line: ocpi-token · 1 scheme
- kind: domain-security
  name: Go Electra Domain Security
  slug: go-electra-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: trust-center
  name: Go Electra Trust Center
  slug: go-electra-trust-center
  summary_line: trust center published
slug: go-electra
tags:
- Company
- Climate Tech
- EV Charging
- Energy
- Mobility
- OCPI
- Roaming
- Charge Point Operator
- Electric Vehicles
- Fast Charging
- Charging Sessions
- Tariffs
- Electrification
- France
- Europe
website: https://www.go-electra.com/
---
