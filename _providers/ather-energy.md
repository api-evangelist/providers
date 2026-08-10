---
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: true
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
    well_known_catalog: true
  schema_version: 0.2
  score: 23.4
  scored_at: '2026-08-10'
agentic_access:
- acting_count: 4
  human_in_the_loop: 0
  name: Ather Energy Agentic Access
  operation_count: 5
  slug: ather-energy-agentic-access
  summary_line: 5 operations · 4 acting
api_count: 1
apis:
- description: The only machine-callable API surface Ather Energy exposes. Ather's commerce host advertises a Universal Commerce Protocol merchant profile at /.well-known/ucp declaring an MCP shopping endpoint under
  name: Ather Shop — UCP Shopping Service (MCP)
  slug: ather-shop-ucp-shopping-service-mcp
artifact_total: 5
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/ather-energy-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.atherenergy.com/
- group: company
  title: ''
  type: About
  url: https://www.atherenergy.com/about
- group: company
  title: ''
  type: Blog
  url: https://www.atherenergy.com/blog
- group: operate
  title: ''
  type: Support
  url: https://www.atherenergy.com/contact
- group: operate
  title: ''
  type: FAQ
  url: https://www.atherenergy.com/faq
- group: operate
  title: ''
  type: Community
  url: https://www.atherenergy.com/community
- group: commercial
  title: ''
  type: Pricing
  url: https://www.atherenergy.com/electric-scooter-all-models
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.atherenergy.com/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.atherenergy.com/policy
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/AtherEnergy
- group: company
  title: ''
  type: Careers
  url: https://careers.atherenergy.com/
- group: company
  title: ''
  type: InvestorRelations
  url: https://www.atherenergy.com/investor-relations
- group: auth
  title: ''
  type: Security
  url: https://www.atherenergy.com/bug-bounty
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/ather-energy-vulnerability-disclosure.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/ather-energy-llms.txt
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/ather-energy-shop-llms.txt
- group: agent
  title: ''
  type: WellKnown
  url: well-known/ather-energy-well-known.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/ather-energy-mcp.yml
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/ather-energy-agentic-access.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/ather-energy-conventions.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/ather-energy-conformance.yml
- group: build
  title: ''
  type: Packages
  url: packages/ather-energy-packages.yml
- group: other
  title: ''
  type: Profile
  url: https://forgeglobal.com/ather-energy_stock/
created: '2026-07-31'
description: 'Ather Energy Limited is a Bengaluru-based Indian electric two-wheeler manufacturer founded in 2013 by Tarun Mehta and Swapnil Jain. It designs and builds connected electric scooters — the Ather 450 series (450S, 450X, 450 Apex) and the family-oriented Rizta — around AtherStack, its proprietary in-house vehicle software architecture delivered to vehicles over the air. Ather also operates Ather Grid, India''s largest two-wheeler fast-charging network, alongside a retail, service, accessories and smart-helmet ecosystem. Ather publishes no public developer API, OpenAPI, GraphQL or MCP surface: its machine-readable public footprint is a curated llms.txt for AI agents, a named-crawler robots.txt allowlist, and an open-source GitHub organisation of embedded and infrastructure libraries (ACAN, ASDK, rumqtt).'
image: https://www.atherenergy.com/images/logo.svg
layout: provider
mcp_servers:
- description: ''
  name: ather-energy-mcp.yml
  slug: ather-energy-mcpyml
modified: '2026-07-31'
name: Ather Energy
nav: Providers
network: true
overview: 'Ather Energy publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Electric Vehicles, Automotive, Transportation, and Manufacturing.


  Ather Energy''s developer surface includes engineering blog, support, FAQ, pricing, and 20 more developer resources.'
random_paper: 67
score:
  band: emerging
  composite: 22.5
  delta: 0.0
  facets:
    commercial_clarity: 31.6
    contract_quality: 0.0
    developer_ergonomics: 15.2
    discoverability: 87.0
    governance: 3.1
    operational_transparency: 15.8
  previous_composite: 22.5
  provenance:
    agentic_access: first-party
    conformance: derived
    mcp: first-party
  regulatory:
    applies: true
    matched_via: tags
    regime: Energy & Utilities
    regime_id: energy_utilities
    score: 33.8
  schema_version: 0.9.1
  scored_at: '2026-08-10'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/ather-energy/refs/heads/main/screenshots/ather-energy-2026-08-07T161835.png
security:
- kind: domain-security
  name: Ather Energy Domain Security
  slug: ather-energy-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
- kind: vulnerability-disclosure
  name: Ather Energy Vulnerability Disclosure
  slug: ather-energy-vulnerability-disclosure
  summary_line: Hackerone · contact published
slug: ather-energy
tags:
- Company
- Electric Vehicles
- Automotive
- Transportation
- Manufacturing
- Energy
- EV Charging
- Mobility
- Internet of Things
- India
website: https://www.atherenergy.com/
---
