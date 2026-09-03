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
    agentic_commerce: false
    auth_clarity: false
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
  score: 8.6
  scored_at: '2026-09-02'
api_count: 0
artifact_total: 2
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/dronamics-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.dronamics.com/
- group: company
  title: ''
  type: Blog
  url: https://www.dronamics.com/newsroom
- group: operate
  title: ''
  type: Support
  url: https://www.dronamics.com/contact
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.dronamics.com/privacy-policy
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/dronamics-llms.txt
- group: agent
  title: ''
  type: MCPServer
  url: mcp/dronamics-mcp.yml
created: '2026-07-17'
description: Dronamics is a European deep-tech company that designs, builds, and operates autonomous long-range cargo drones for middle-mile logistics. Its flagship aircraft, The Black Swan, is a remotely piloted UAV that carries up to 350 kg (770 lb) of cargo over distances up to 2,500 km (1,550 mi), enabling same-day, cross-border, point-to-point deliveries that are faster, cheaper, and lower in CO2 emissions than traditional air freight. Founded in 2014 in Sofia, Bulgaria by brothers Svilen and Konstantin Rangelov and operating as Dronamics Group Limited, the company is building the world's first cargo drone airline, operating a proprietary drone fleet from a network of low-cost droneports. The public dronamics.com marketing site is built on Wix and exposes a Wix Site MCP endpoint for agentic access; Dronamics does not publish a developer-facing logistics API, OpenAPI, or SDKs at this time.
image: https://static.wixstatic.com/media/ffb852_9b241796c89941089c6ff49b87cdfc3d~mv2.jpg/v1/fill/w_2500,h_1406,al_c/ffb852_9b241796c89941089c6ff49b87cdfc3d~mv2.jpg
layout: provider
mcp_servers:
- description: ''
  name: Dronamics MCP Server
  slug: dronamics-mcp-server
modified: '2026-07-18'
name: Dronamics
nav: Providers
network: true
overview: 'Dronamics is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Drones, UAV, Cargo, and Logistics.


  Dronamics'' developer surface includes engineering blog, support, and 5 more developer resources.'
random_paper: 15
score:
  band: minimal
  composite: 9.3
  coverage:
    artifact_dirs: 5
    catalog_gap: 88.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 10.5
    commercial_clarity: 10.5
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 7.1
    discoverability: 57.4
    governance: 0.0
    operational_transparency: 0.0
  previous_composite: 9.3
  provenance:
    mcp: first-party
  schema_version: 0.18.0
  scored_at: '2026-09-02'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/dronamics/refs/heads/main/screenshots/dronamics-2026-07-25T212420.png
security:
- kind: domain-security
  name: Dronamics Domain Security
  slug: dronamics-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: dronamics
tags:
- Company
- Drones
- UAV
- Cargo
- Logistics
- Air Freight
- Middle Mile
- Delivery
- Aerospace
- Deep Tech
website: https://www.dronamics.com/
---
