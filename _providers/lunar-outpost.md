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
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: documented
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 8.5
  scored_at: '2026-09-01'
api_count: 1
apis:
- description: An unauthenticated remote Model Context Protocol server served from Lunar Outpost's own host and advertised by the company's llms.txt as its "Site MCP Endpoint". It exposes nine tools that let an agen
  name: Lunar Outpost Site MCP Server
  slug: lunar-outpost-site-mcp
artifact_total: 6
common:
- group: company
  title: ''
  type: Website
  url: https://www.lunaroutpost.com/
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/lunar-outpost-llms.txt
- group: agent
  title: ''
  type: MCPServer
  url: mcp/lunar-outpost-mcp.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/lunar-outpost-authentication.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/lunar-outpost-conventions.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/lunar-outpost-conformance.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/lunar-outpost-domain-security.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/lunar-outpost-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/lunar-outpost-rate-limits.yml
- group: company
  title: ''
  type: Blog
  url: https://www.lunaroutpost.com/news
- group: operate
  title: ''
  type: Support
  url: https://www.lunaroutpost.com/contact
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.lunaroutpost.com/terms-of-use
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.lunaroutpost.com/privacy-policy
created: '2026-08-25'
description: 'Lunar Outpost is a space robotics company founded in 2017 and headquartered in Golden, Colorado, with additional operations in Australia and Luxembourg. It builds lunar surface mobility and robotic infrastructure — the MAPP (Mobile Autonomous Prospecting Platform) rover, which operated at the lunar South Pole in 2025 as the first commercial rover on another planetary body, and the Eagle and Pegasus Lunar Terrain Vehicles developed for NASA''s Artemis programme. Alongside the hardware it ships an integrated mission-operations software suite: Stargate, a spaceflight-proven command, control and communication platform that reached TRL 9 with 99.998% uptime on Lunar Voyage 1; Starweave (formerly MARS), a distributed autonomy and mesh-networking layer built under AFRL and AFWERX contract for coordinating heterogeneous robotic fleets in GPS-denied environments; and Spark, an AI mission-operations assistant. None of these products expose a public API, developer portal or machine-readable
  specification — Lunar Outpost sells to government and defence customers rather than through a self-serve developer channel. Its only public machine-readable surfaces are a Wix platform-generated llms.txt and an unauthenticated site MCP endpoint.'
image: https://static.wixstatic.com/media/8a6459_c44b42e2b82b44249f6a3a9fa12cd670~mv2.png/v1/fit/w_2500,h_1330,al_c/8a6459_c44b42e2b82b44249f6a3a9fa12cd670~mv2.png
layout: provider
mcp_servers:
- description: A live, unauthenticated remote MCP server served from Lunar Outpost's own host at https://www.lunaroutpost.com/_api/mcp, advertised by the company's published llms.txt as its "Site MCP Endpoint". Veri
  name: Lunar Outpost Site MCP Server
  slug: lunar-outpost-site-mcp-server
modified: '2026-08-25'
name: Lunar Outpost
nav: Providers
network: true
overview: 'Lunar Outpost publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Space, Robotics, Aerospace, Lunar Exploration, and Autonomous Systems.


  Lunar Outpost''s developer surface includes authentication, engineering blog, support, and 10 more developer resources.'
plans:
- name: Lunar Outpost Plans Pricing
  plan_count: 0
  slug: lunar-outpost-plans-pricing
random_paper: 3
rate_limits:
- limit_count: 0
  name: Lunar Outpost Rate Limits
  slug: lunar-outpost-rate-limits
score:
  band: emerging
  composite: 17.8
  coverage:
    artifact_dirs: 9
    catalog_gap: 78.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 21.1
    commercial_clarity: 21.1
    contract_governance: 18.2
    contract_quality: 0.0
    developer_ergonomics: 19.0
    discoverability: 75.9
    governance: 18.2
    operational_transparency: 0.0
  previous_composite: 17.8
  provenance:
    conformance: first-party
    mcp: first-party
  schema_version: 0.17.2
  scored_at: '2026-09-01'
  trend: flat
security:
- kind: authentication
  name: Lunar Outpost Authentication
  slug: lunar-outpost-authentication
  summary_line: 0 schemes
- kind: domain-security
  name: Lunar Outpost Domain Security
  slug: lunar-outpost-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
slug: lunar-outpost
tags:
- Space
- Robotics
- Aerospace
- Lunar Exploration
- Autonomous Systems
- Mission Control
- Defense
- Satellite
- Artificial Intelligence
- Company
website: https://www.lunaroutpost.com/
---
