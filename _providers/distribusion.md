---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source: []
  trial: false
  try_now: false
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    auth_clarity: false
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: true
    openapi_examples: false
    rate_limit_signal: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 10.8
  scored_at: '2026-08-10'
api_count: 1
apis:
- description: 'B2B API for retailers to search ground-transportation inventory (bus, train, ferry, tram) across 2,000+ carriers, create and manage bookings, take payment, and handle after-sales. Reference is behind '
  name: Distribusion Retailer API
  slug: distribusion-retailer-api
artifact_total: 3
common:
- group: start
  title: ''
  type: DeveloperPortal
  url: https://docs.distribusion.com/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.distribusion.com/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/distribusion
- group: operate
  title: ''
  type: Support
  url: https://www.distribusion.com/contact
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.distribusion.com/terms-and-conditions
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.distribusion.com/privacy-policy
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/distribusion-llms.txt
- group: agent
  title: ''
  type: MCPServer
  url: mcp/distribusion-mcp.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/distribusion-conformance.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/distribusion-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://distribusion.com/
created: '2026-07-17'
description: 'Distribusion is a Berlin-based ground transportation technology company that operates a global distribution system (GDS) for ground travel. Its B2B platform connects 2,000+ carriers - buses, trains, trams, and ferries - with 250+ retailers and travel platforms including Google Maps, Expedia, Booking, and Trainline. The Distribusion Retailer API handles the full transaction lifecycle from search to settlement: inventory search, booking, payment, unified invoicing, channel management, real-time disruption management, and after-sales services. The platform supports the OSDM (Open Sales and Distribution Model) rail distribution standard and aims to make ground travel as accessible and bookable as flights. Backed by Creandum and Northzone.'
image: https://static.wixstatic.com/media/b2a9dd_08785717d62a4229b84538fa61a583eb~mv2.png/v1/fit/w_2500,h_1330,al_c/b2a9dd_08785717d62a4229b84538fa61a583eb~mv2.png
layout: provider
mcp_servers:
- description: ''
  name: distribusion-mcp.yml
  slug: distribusion-mcpyml
modified: '2026-07-18'
name: Distribusion
nav: Providers
network: true
overview: 'Distribusion publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Transportation, Travel, Mobility, and Ground Travel.


  Distribusion''s developer surface includes documentation, support, and 9 more developer resources.'
random_paper: 35
score:
  band: emerging
  composite: 20.1
  delta: 0.0
  facets:
    commercial_clarity: 21.1
    contract_quality: 0.0
    developer_ergonomics: 30.4
    discoverability: 75.9
    governance: 12.5
    operational_transparency: 5.3
  previous_composite: 20.1
  provenance:
    conformance: first-party
    mcp: first-party
  schema_version: 0.9.1
  scored_at: '2026-08-10'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/distribusion/refs/heads/main/screenshots/distribusion-2026-07-25T212115.png
security:
- kind: domain-security
  name: Distribusion Domain Security
  slug: distribusion-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: distribusion
tags:
- Company
- Transportation
- Travel
- Mobility
- Ground Travel
- Booking
- Distribution
- API
website: https://distribusion.com/
---
