---
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    agentic_commerce: false
    auth_clarity: served
    consent_identity: false
    delegated_identity: served
    dry_run_mode: false
    dynamic_client_registration: true
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
  score: 19.6
  scored_at: '2026-10-31'
api_count: 1
apis:
- description: API providing access to company and trade data via MCP endpoints (e.g., https://thecompanyatlas.com/mcp/australia).
  name: The Company Atlas API
  slug: the-company-atlas-api
artifact_total: 3
common:
- group: agent
  href: https://artifacts.apis.io/thecompanyatlas-com/llms/thecompanyatlas-com-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/thecompanyatlas-com-llms.txt
- group: agent
  href: https://artifacts.apis.io/thecompanyatlas-com/mcp/thecompanyatlas-com-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/thecompanyatlas-com-mcp.yml
- group: agent
  href: https://artifacts.apis.io/thecompanyatlas-com/well-known/thecompanyatlas-com-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/thecompanyatlas-com-well-known.yml
- group: other
  href: https://artifacts.apis.io/thecompanyatlas-com/hosts/thecompanyatlas-com-hosts.yml
  title: ''
  type: Hosts
  url: hosts/thecompanyatlas-com-hosts.yml
- group: other
  href: https://artifacts.apis.io/thecompanyatlas-com/vendors/thecompanyatlas-com-vendors.yml
  title: ''
  type: Vendors
  url: vendors/thecompanyatlas-com-vendors.yml
- group: auth
  href: https://artifacts.apis.io/thecompanyatlas-com/security/thecompanyatlas-com-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/thecompanyatlas-com-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://thecompanyatlas.com/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://thecompanyatlas.com/privacy
- group: commercial
  title: ''
  type: TermsOfService
  url: https://thecompanyatlas.com/terms
- group: commercial
  title: ''
  type: Pricing
  url: https://thecompanyatlas.com/mcp/pricing
coverage:
  checked: '2026-10-29'
  detail: Main website and pricing pages are rendered via JavaScript with no machine‑readable API specification.
  evidence:
  - status: 200
    url: https://thecompanyatlas.com/
  reason: js-rendered-docs
  state: unreadable
created: '2026-10-29'
description: The Company Atlas aggregates customs trade data from 36 international markets, offering tools to look up individual import and export declarations, rank companies behind products or routes, and explore detailed trade records. Data spans from 2012 to 2026 across registries such as Australia ABN, US Colorado, Hong Kong, UK Companies House, and many others, providing comprehensive insights for businesses, researchers, and analysts.
image: https://thecompanyatlas.com/favicon.ico
layout: provider
mcp_servers:
- description: Remote MCP server at thecompanyatlas.com.
  name: thecompanyatlas-com MCP Server
  slug: thecompanyatlas-com-mcp-yml
modified: '2026-10-29'
name: thecompanyatlas-com
nav: Providers
network: true
overview: 'thecompanyatlas-com is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Customs, TradeData, API, and DataPlatform.


  thecompanyatlas-com''s developer surface includes pricing and 9 more developer resources.'
random_paper: 9
score:
  band: emerging
  composite: 12.7
  coverage:
    artifact_dirs: 8
    catalog_earned: 32.0
    catalog_earned_first_party: 0.0
    catalog_gap: 83.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 31.6
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 0.0
    discoverability: 56.7
    operational_transparency: 0.0
  provenance:
    mcp: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 19.6
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Thecompanyatlas Com Domain Security
  slug: thecompanyatlas-com-domain-security
  summary_line: TLSv1.3
slug: thecompanyatlas-com
tags:
- Company
- Customs
- TradeData
- API
- DataPlatform
website: https://thecompanyatlas.com/
---
