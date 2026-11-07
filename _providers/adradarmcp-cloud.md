---
access_model:
  confidence: medium
  label: Paid
  onboarding: unknown
  pricing: paid
  public: false
  source:
  - plans
  - authentication
  - security
  trial: false
  try_now: false
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
    mcp_tool_quality: na
    openapi_examples: false
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: verified
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: '0.2'
  score: 22.2
  scored_at: '2026-11-06'
api_count: 1
apis:
- description: AdRadar MCP provides tools to search the public Meta Ad Library and TikTok Creative Center, classify ads, and check credit balance.
  name: AdRadar MCP
  slug: adradar-mcp
artifact_total: 6
common:
- group: commercial
  href: https://artifacts.apis.io/adradarmcp-cloud/plans/adradarmcp-cloud-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/adradarmcp-cloud-plans-pricing.yml
- group: auth
  href: https://artifacts.apis.io/adradarmcp-cloud/authentication/adradarmcp-cloud-authentication.yml
  title: ''
  type: Authentication
  url: authentication/adradarmcp-cloud-authentication.yml
- group: agent
  href: https://artifacts.apis.io/adradarmcp-cloud/llms/adradarmcp-cloud-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/adradarmcp-cloud-llms.txt
- group: agent
  href: https://artifacts.apis.io/adradarmcp-cloud/mcp/adradarmcp-cloud-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/adradarmcp-cloud-mcp.yml
- group: agent
  href: https://artifacts.apis.io/adradarmcp-cloud/well-known/adradarmcp-cloud-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/adradarmcp-cloud-well-known.yml
- group: other
  href: https://artifacts.apis.io/adradarmcp-cloud/hosts/adradarmcp-cloud-hosts.yml
  title: ''
  type: Hosts
  url: hosts/adradarmcp-cloud-hosts.yml
- group: other
  href: https://artifacts.apis.io/adradarmcp-cloud/vendors/adradarmcp-cloud-vendors.yml
  title: ''
  type: Vendors
  url: vendors/adradarmcp-cloud-vendors.yml
- group: auth
  href: https://artifacts.apis.io/adradarmcp-cloud/security/adradarmcp-cloud-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/adradarmcp-cloud-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://adradarmcp.cloud/
- group: commercial
  title: ''
  type: Pricing
  url: https://adradarmcp.cloud/en/pay
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://adradarmcp.cloud/privacy
created: '2026-10-31'
description: Ad Radar (AdRadar MCP) is a remote Model Context Protocol server that lets AI agents search the public Meta Ad Library and TikTok Creative Center Top Ads, classify sales angles, and compute a 0-100 Winning Score.
examples:
- key_count: 3
  name: Adradarmcp Cloud Mcp Tools
  slug: adradarmcp-cloud-mcp-tools
image: https://adradarmcp.cloud/assets/hero-bg.png
layout: provider
mcp_servers:
- description: Remote MCP server at adradarmcp.cloud.
  name: AdRadar MCP Server
  slug: adradarmcp-cloud-mcp-yml
modified: '2026-10-31'
name: AdRadar
nav: Providers
network: true
overview: 'AdRadar is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include AdTech, Artificial Intelligence, Advertising, Meta, and TikTok.


  AdRadar''s developer surface includes authentication, pricing, and 9 more developer resources.'
plans:
- name: Adradarmcp Cloud Plans Pricing
  plan_count: 6
  slug: adradarmcp-cloud-plans-pricing
random_paper: 11
score:
  band: emerging
  composite: 16.9
  coverage:
    artifact_dirs: 13
    catalog_earned: 49.0
    catalog_earned_first_party: 12.0
    catalog_gap: 66.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -2.4
  facets:
    access_clarity: 42.1
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 11.9
    discoverability: 65.0
    operational_transparency: 0.0
  previous_composite: 19.3
  provenance:
    conformance: unknown
    mcp: first-party
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 12.7
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: authentication
  name: Adradarmcp Cloud Authentication
  slug: adradarmcp-cloud-authentication
  summary_line: 2 schemes
- kind: domain-security
  name: Adradarmcp Cloud Domain Security
  slug: adradarmcp-cloud-domain-security
  summary_line: TLSv1.3 · HSTS
slug: adradarmcp-cloud
tags:
- AdTech
- Artificial Intelligence
- Advertising
- Meta
- TikTok
website: https://adradarmcp.cloud/
---
