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
    mcp_server: verified
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 13.7
  scored_at: '2026-09-12'
api_count: 1
apis:
- description: A live, unauthenticated Model Context Protocol endpoint served from Active Membranes' own hostname at https://www.activemembrane.com/_api/mcp and advertised by the company in its own llms.txt. An anon
  name: Active Membranes Site MCP Server
  slug: active-membranes-site-mcp
artifact_total: 6
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/active-membranes-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.activemembrane.com/
- group: operate
  title: ''
  type: Support
  url: https://www.activemembrane.com/contact
- group: company
  title: ''
  type: Blog
  url: https://www.activemembrane.com/reverse-osmosis-insights
- group: company
  title: ''
  type: BlogRSS
  url: https://www.activemembrane.com/blog-feed.xml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/active-membranes-inc/
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/active-membranes-llms.txt
- group: agent
  title: ''
  type: MCPServer
  url: mcp/active-membranes-mcp.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/active-membranes-authentication.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/active-membranes-conventions.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/active-membranes-conformance.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/active-membranes-rate-limits.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/active-membranes-plans-pricing.yml
created: '2026-09-06'
description: 'Active Membranes is a California water-technology company, founded in 2022 out of research at the UCLA Samueli School of Engineering, that builds electrically conductive "electro-active" reverse-osmosis membranes for desalination and water reuse. Where a conventional RO membrane filters passively and is cleaned after it fouls, Active Membranes embeds conductive material in the membrane''s polymer matrix and uses a control unit it calls the Active Box to apply a tunable low electrical potential at the membrane surface, electrostatically repelling scale-forming ions and charged organic foulants in real time. The modules ship in the standard 8-inch by 40-inch spiral-wound format so they retrofit into existing pressure vessels, and are aimed at seawater and brackish desalination, produced-water and industrial reuse. The company reports field results including roughly 48% less irreversible fouling in produced-water reuse, up to 70% longer cleaning cycles in brackish water, and a
  Ventura County study citing about 57% lower cost and 64% less footprint. It has raised roughly $3.24M in seed funding from Natural Ventures, Echo River Capital and Pacifica Water Solutions, won the 2023 Global Water Summit Water Technology Idol award, and was selected as a Qualified Team in the XPRIZE Water Scarcity competition. Active Membranes sells capital equipment, not software: it operates no developer program, publishes no OpenAPI, GraphQL or SDK, and lists no pricing. It does, however, serve two machine-readable surfaces from its own hostname — a substantial hand-written /llms.txt, and a live, unauthenticated Model Context Protocol endpoint at /_api/mcp exposing nine tools over the public site content. Both are Wix platform features the company chose to enable and advertise rather than first-party engineering.'
image: https://static.wixstatic.com/media/dd52de_d31c0c0159fe4ea68318db941a61b17f~mv2.png/v1/fill/w_192,h_192,lg_1,usm_0.66_1.00_0.01/dd52de_d31c0c0159fe4ea68318db941a61b17f~mv2.png
layout: provider
mcp_servers:
- description: Active Membranes serves a live, unauthenticated Model Context Protocol endpoint from its own hostname at https://www.activemembrane.com/_api/mcp. It is the Wix Site MCP runtime, not a first-party serv
  name: Active Membranes Site MCP Server
  slug: active-membranes-site-mcp-server
modified: '2026-09-06'
name: Active Membranes
nav: Providers
network: true
overview: 'Active Membranes publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Water, Water Technology, Desalination, and Reverse Osmosis.


  Active Membranes'' developer surface includes support, engineering blog, authentication, and 10 more developer resources.'
plans:
- name: Active Membranes Plans Pricing
  plan_count: 0
  slug: active-membranes-plans-pricing
random_paper: 18
rate_limits:
- limit_count: 0
  name: Active Membranes Rate Limits
  slug: active-membranes-rate-limits
score:
  band: emerging
  composite: 13.6
  coverage:
    artifact_dirs: 9
    catalog_earned: 37.0
    catalog_earned_first_party: 0.0
    catalog_gap: 78.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 0.0
    contract_governance: 18.2
    contract_quality: 0.0
    developer_ergonomics: 19.0
    discoverability: 75.9
    operational_transparency: 0.0
  previous_composite: 13.6
  provenance:
    conformance: first-party
    mcp: first-party
  schema_version: 0.21.0
  scored_at: '2026-09-12'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: authentication
  name: Active Membranes Authentication
  slug: active-membranes-authentication
  summary_line: 2 schemes
- kind: domain-security
  name: Active Membranes Domain Security
  slug: active-membranes-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: active-membranes
tags:
- Company
- Water
- Water Technology
- Desalination
- Reverse Osmosis
- Membranes
- Cleantech
- Sustainability
- Industrial
- Hardware
- MCP
- Agents
website: https://www.activemembrane.com/
---
