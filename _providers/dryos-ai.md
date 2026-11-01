---
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
    mcp_server: documented
    openapi_examples: false
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: verified
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: '0.2'
  score: 7.1
  scored_at: '2026-10-31'
api_count: 1
apis:
- description: Dryos API providing energy, weather, and property data
  name: Dryos API
  slug: dryos-api
artifact_total: 4
common:
- group: commercial
  href: https://artifacts.apis.io/dryos-ai/plans/dryos-ai-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/dryos-ai-plans-pricing.yml
- group: design
  href: https://artifacts.apis.io/dryos-ai/conformance/dryos-ai-conformance.yml
  title: ''
  type: Conformance
  url: conformance/dryos-ai-conformance.yml
- group: agent
  href: https://artifacts.apis.io/dryos-ai/llms/dryos-ai-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/dryos-ai-llms.txt
- group: agent
  href: https://artifacts.apis.io/dryos-ai/mcp/dryos-ai-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/dryos-ai-mcp.yml
- group: agent
  href: https://artifacts.apis.io/dryos-ai/well-known/dryos-ai-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/dryos-ai-well-known.yml
- group: other
  href: https://artifacts.apis.io/dryos-ai/hosts/dryos-ai-hosts.yml
  title: ''
  type: Hosts
  url: hosts/dryos-ai-hosts.yml
- group: other
  href: https://artifacts.apis.io/dryos-ai/vendors/dryos-ai-vendors.yml
  title: ''
  type: Vendors
  url: vendors/dryos-ai-vendors.yml
- group: auth
  href: https://artifacts.apis.io/dryos-ai/security/dryos-ai-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/dryos-ai-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.dryos.ai/
- group: docs
  title: ''
  type: Documentation
  url: https://www.dryos.ai/docs
- group: docs
  title: ''
  type: APIReference
  url: https://www.dryos.ai/docs
- group: start
  title: ''
  type: GettingStarted
  url: https://www.dryos.ai/mcp
- group: operate
  title: ''
  type: Support
  url: https://www.dryos.ai/maintainers
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.dryos.ai/privacy
coverage:
  detail: the company serves an API surface but requires credentials before any description of it can be read
  evidence:
  - status: null
    url: https://api.dryos.ai/openapi.json
  - status: null
    url: https://api.dryos.ai/mcp
  - status: 401
    url: https://www.dryos.ai/api/mcp
  - status: 200
    url: https://dryos.ai/
  reason: partner-login
  state: gated
created: '2026-10-30'
description: Dryos AI operates a data marketplace delivering real-time and historical energy, weather, and property datasets via a unified API. It aggregates streams from multiple sources such as ERCOT, MISO, PJM, and SPP, providing over 135 live data streams covering power prices, demand, generation, forecasts, and property information. The platform offers a no‑code workspace, open-source tools, and free public access without requiring accounts, enabling developers and AI agents to integrate and analyze the data effortlessly.
image: https://www.dryos.ai/opengraph-image?9194f83001e65952
layout: provider
mcp_servers:
- description: Remote MCP server at api.dryos.ai.
  name: dryos-ai MCP Server
  slug: dryos-ai-mcp-yml
modified: '2026-10-30'
name: dryos-ai
nav: Providers
network: true
overview: 'dryos-ai is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Energy, Weather, Property, and Data Marketplace.


  dryos-ai''s developer surface includes documentation, API reference, getting-started guide, support, and 10 more developer resources.'
plans:
- name: Dryos Ai Plans Pricing
  plan_count: 1
  slug: dryos-ai-plans-pricing
random_paper: 16
score:
  band: emerging
  composite: 19.9
  coverage:
    artifact_dirs: 11
    catalog_earned: 45.0
    catalog_earned_first_party: 8.0
    catalog_gap: 70.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 31.6
    contract_governance: 4.5
    contract_quality: 0.0
    developer_ergonomics: 33.3
    discoverability: 65.0
    operational_transparency: 0.0
  provenance:
    conformance: derived
    mcp: first-party
  regulatory:
    applies: true
    matched_via: tags
    regime: Energy & Utilities
    regime_id: energy_utilities
    score: 12.3
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Dryos Ai Domain Security
  slug: dryos-ai-domain-security
  summary_line: TLSv1.3 · HSTS
slug: dryos-ai
tags:
- Company
- Energy
- Weather
- Property
- Data Marketplace
website: https://www.dryos.ai/
---
