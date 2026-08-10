---
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
api_count: 0
artifact_total: 2
common:
- group: company
  title: ''
  type: Website
  url: https://www.atompower.com/
- group: company
  title: ''
  type: Blog
  url: https://www.atompower.com/blog
- group: company
  title: ''
  type: BlogRSS
  url: https://www.atompower.com/blog-feed.xml
- group: operate
  title: ''
  type: Support
  url: https://www.atompower.com/contact-us
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.atompower.com/privacy-policy
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.atompower.com/terms-conditions
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/atom-power-llms.txt
- group: agent
  title: ''
  type: MCPServer
  url: mcp/atom-power-mcp.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/atom-power-domain-security.yml
coverage:
  checked: '2026-08-06'
  detail: Atom Power's "Atom Cloud" developer portal and API gateway are decommissioned — developers.atompower.com and api.atompower.com are still published as CNAMEs to Azure API Management, but both targets (apim-obsidian-prod-01.developer.azure-api.net and api-atompower.azure-api.net) return NXDOMAIN, so there is no reachable API, reference, or spec; the live Wix marketing site links no developer program at all.
  evidence:
  - note: 'DNS resolution failed: CNAME target apim-obsidian-prod-01.developer.azure-api.net returns NXDOMAIN'
    status: 0
    url: https://developers.atompower.com/apis
  - note: 'DNS resolution failed: CNAME target api-atompower.azure-api.net returns NXDOMAIN'
    status: 0
    url: https://api.atompower.com/
  - status: 400
    url: https://www.atompower.com/openapi.json
  - status: 400
    url: https://www.atompower.com/.well-known/agent-card.json
  - status: 200
    url: https://www.atompower.com/llms.txt
  reason: no-developer-program
  state: none
created: '2026-08-06'
description: Atom Power, Inc. is a Charlotte, North Carolina electrical technology company founded in 2014 that invented the Atom Switch, the world's first commercial UL-listed digital solid-state circuit breaker. The company builds SiC (silicon carbide) power modules, solid-state switchgear and panel-level Level 2 electric-vehicle charging hardware for commercial, industrial, data-center and grid-edge deployments, paired with cloud software for energy management, load balancing and charger operations. Atom Power previously ran an "Atom Cloud" developer portal on Azure API Management at developers.atompower.com with a gateway at api.atompower.com; both hostnames are now dangling CNAMEs to deleted Azure API Management instances, so no public API contract is currently reachable.
image: https://static.wixstatic.com/media/9b626a_6de3d6548956428a831983d5b6c5ef13%7Emv2.png/v1/fit/w_2500,h_1330,al_c/9b626a_6de3d6548956428a831983d5b6c5ef13%7Emv2.png
layout: provider
mcp_servers:
- description: ''
  name: atom-power-mcp.yml
  slug: atom-power-mcpyml
modified: '2026-08-06'
name: Atom Power
nav: Providers
network: true
overview: 'Atom Power is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Energy, Electric Vehicle Charging, EV Charging, and Circuit Protection.


  Atom Power''s developer surface includes engineering blog, support, and 7 more developer resources.'
random_paper: 107
score:
  band: emerging
  composite: 14.8
  delta: 0.0
  facets:
    commercial_clarity: 21.1
    contract_quality: 0.0
    developer_ergonomics: 15.2
    discoverability: 68.5
    governance: 0.0
    operational_transparency: 0.0
  previous_composite: 14.8
  provenance:
    mcp: first-party
  regulatory:
    applies: true
    matched_via: tags
    regime: Energy & Utilities
    regime_id: energy_utilities
    score: 18.9
  schema_version: 0.9.1
  scored_at: '2026-08-10'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/atom-power/refs/heads/main/screenshots/atom-power-2026-08-07T161854.png
security:
- kind: domain-security
  name: Atom Power Domain Security
  slug: atom-power-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: atom-power
tags:
- Company
- Energy
- Electric Vehicle Charging
- EV Charging
- Circuit Protection
- Solid State Circuit Breaker
- Electrical Equipment
- Energy Management
- Hardware
website: https://www.atompower.com/
---
