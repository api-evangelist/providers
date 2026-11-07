---
access_model:
  confidence: low
  gated: none
  gated_source:
  - onboarding
  label: Open access
  onboarding: open
  pricing: unknown
  public: true
  source:
  - authentication
  - security
  trial: false
  try_now: false
agent_readiness:
  band: human-only
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
    mcp_tool_quality: na
    openapi_examples: false
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: '0.2'
  score: 3.5
  scored_at: '2026-11-06'
api_count: 1
apis:
- description: Provides an ADU eligibility check tool via MCP.
  name: ADU Zoning MCP
  slug: adu-zoning-mcp
artifact_total: 5
common:
- group: agent
  href: https://artifacts.apis.io/adufloridainfo-com/llms/adufloridainfo-com-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/adufloridainfo-com-llms.txt
- group: agent
  href: https://artifacts.apis.io/adufloridainfo-com/mcp/adufloridainfo-com-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/adufloridainfo-com-mcp.yml
- group: other
  href: https://artifacts.apis.io/adufloridainfo-com/hosts/adufloridainfo-com-hosts.yml
  title: ''
  type: Hosts
  url: hosts/adufloridainfo-com-hosts.yml
- group: other
  href: https://artifacts.apis.io/adufloridainfo-com/vendors/adufloridainfo-com-vendors.yml
  title: ''
  type: Vendors
  url: vendors/adufloridainfo-com-vendors.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.adufloridainfo.com/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.adufloridainfo.com/privacy
- group: auth
  href: https://artifacts.apis.io/adufloridainfo-com/security/adufloridainfo-com-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/adufloridainfo-com-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://adufloridainfo.com/
- group: company
  title: ''
  type: Blog
  url: https://www.adufloridainfo.com/blog
- group: start
  title: ''
  type: GettingStarted
  url: https://www.adufloridainfo.com/wizard
created: '2026-10-31'
description: ADU Florida Info is Florida's independent authority on Accessory Dwelling Units (ADUs). It provides instant zoning eligibility checks, detailed local rules by city and county, and connects users with vetted builders across major Florida markets. Homeowners can enter an address to receive a property‑specific report covering permitted ADU types, size limits, setbacks, and other regulations, helping them navigate Florida’s ADU legislation and construction costs.
image: https://www.adufloridainfo.com/logo.png
layout: provider
mcp_servers:
- description: Remote MCP server at www.adufloridainfo.com.
  name: ADU Florida Info MCP Server
  slug: adufloridainfo-com-mcp-yml
modified: '2026-10-31'
name: ADU Florida Info
nav: Providers
network: true
overview: 'ADU Florida Info is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Real Estate, Zoning, Florida, ADU, and Housing.


  ADU Florida Info''s developer surface includes engineering blog, getting-started guide, and 8 more developer resources.'
random_paper: 19
scopes:
- name: Adufloridainfo Com Scopes
  scope_count: 0
  slug: adufloridainfo-com-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: minimal
  composite: 10.7
  coverage:
    artifact_dirs: 18
    catalog_earned: 37.0
    catalog_earned_first_party: 0.0
    catalog_gap: 78.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -4.1
  facets:
    access_clarity: 10.5
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 7.1
    discoverability: 65.0
    operational_transparency: 0.0
  previous_composite: 14.8
  provenance:
    conformance: unknown
    mcp: first-party
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 19.6
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: authentication
  name: Adufloridainfo Com Authentication
  slug: adufloridainfo-com-authentication
  summary_line: 0 schemes
- kind: domain-security
  name: Adufloridainfo Com Domain Security
  slug: adufloridainfo-com-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: adufloridainfo-com
tags:
- Real Estate
- Zoning
- Florida
- ADU
- Housing
website: https://adufloridainfo.com/
---
