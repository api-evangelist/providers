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
    mcp_server: verified
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 12.1
  scored_at: '2026-09-01'
api_count: 1
apis:
- description: The public Model Context Protocol endpoint served by LIFT Aircraft's Wix-hosted site. Exposes nine tools that let an agent read business details, search the site, read the installed Wix business-solut
  name: LIFT Aircraft Site MCP
  slug: site-mcp
artifact_total: 4
common:
- group: company
  title: ''
  type: Website
  url: https://www.liftaircraft.com
- group: agent
  title: ''
  type: MCPServer
  url: mcp/lift-mcp.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/lift-llms.txt
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/lift-authentication.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/lift-domain-security.yml
- group: company
  title: ''
  type: Blog
  url: https://www.liftaircraft.com/news
- group: operate
  title: ''
  type: Support
  url: https://www.liftaircraft.com/faq
- group: commercial
  title: ''
  type: Pricing
  url: https://www.liftaircraft.com/plans-pricing
created: '2026-07-17'
description: LIFT Aircraft is an Austin, Texas experiential aviation company founded by former Boeing engineer Matt Chasen, built around HEXA — an amphibious electric vertical take-off and landing aircraft with eighteen independent electric motors and propellers, a 432lb carbon fibre airframe, a triply redundant autopilot flown with a single three-axis joystick, an autonomous ballistic parachute, and enough redundancy to fly and land safely with up to six motors disabled. Because HEXA is compliant with the FAA's powered ultralight classification, no pilot's licence is required, and LIFT sells flight as a paid experience rather than selling aircraft — a short training session followed by a solo flight from waterfront bases in Austin and other US cities. The company has raised over $25 million from venture capital, accredited investors and US government grants, has worked with the US Air Force Agility Prime programme and the US Army, and has begun the FAA type certification process for a commercial
  edition. LIFT publishes no developer REST API or OpenAPI; its only machine-readable surface is a live, unauthenticated Model Context Protocol endpoint and an llms.txt served by its Wix-hosted site.
image: https://static.wixstatic.com/media/9f6a5c_257a4a5e996e4aa5bccb028fdb90388b%7Emv2.png/v1/fill/w_192%2Ch_192%2Clg_1%2Cusm_0.66_1.00_0.01/9f6a5c_257a4a5e996e4aa5bccb028fdb90388b%7Emv2.png
layout: provider
mcp_servers:
- description: ''
  name: LIFT Aircraft MCP Server
  slug: lift-aircraft-mcp-server
modified: '2026-07-19'
name: LIFT Aircraft
nav: Providers
network: true
overview: 'LIFT Aircraft publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Aviation, eVTOL, Electric Aircraft, and Urban Air Mobility.


  LIFT Aircraft''s developer surface includes authentication, engineering blog, support, pricing, and 5 more developer resources.'
random_paper: 11
score:
  band: emerging
  composite: 13.9
  coverage:
    artifact_dirs: 7
    catalog_gap: 78.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 10.5
    commercial_clarity: 10.5
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 20.8
    discoverability: 75.9
    governance: 0.0
    operational_transparency: 0.0
  previous_composite: 13.9
  provenance:
    mcp: first-party
    skills: derived
  schema_version: 0.18.0
  scored_at: '2026-09-01'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/lift/refs/heads/main/screenshots/lift-2026-07-25T225052.png
security:
- kind: authentication
  name: Lift Authentication
  slug: lift-authentication
  summary_line: none/bearer · 2 schemes
- kind: domain-security
  name: Lift Domain Security
  slug: lift-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: lift
tags:
- Company
- Aviation
- eVTOL
- Electric Aircraft
- Urban Air Mobility
- Aerospace
- Transportation
- Experiential Entertainment
- Booking
- MCP
website: https://www.liftaircraft.com
---
