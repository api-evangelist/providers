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
    mcp_tool_quality: na
    openapi_examples: false
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: '0.2'
  score: 6.0
  scored_at: '2026-11-06'
api_count: 1
apis:
- description: Advertising MCP for AI agents as documented on the /agents page.
  name: BestBid MCP
  slug: bestbid-mcp
artifact_total: 7
common:
- group: agent
  href: https://artifacts.apis.io/bestbid-lol/llms/bestbid-lol-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/bestbid-lol-llms.txt
- group: agent
  href: https://artifacts.apis.io/bestbid-lol/mcp/bestbid-lol-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/bestbid-lol-mcp.yml
- group: other
  href: https://artifacts.apis.io/bestbid-lol/hosts/bestbid-lol-hosts.yml
  title: ''
  type: Hosts
  url: hosts/bestbid-lol-hosts.yml
- group: other
  href: https://artifacts.apis.io/bestbid-lol/vendors/bestbid-lol-vendors.yml
  title: ''
  type: Vendors
  url: vendors/bestbid-lol-vendors.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://bestbid.lol/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://bestbid.lol/privacy
- group: company
  title: ''
  type: Newsroom
  url: https://bestbid.lol/press
- group: auth
  href: https://artifacts.apis.io/bestbid-lol/security/bestbid-lol-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/bestbid-lol-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://bestbid.lol/
created: '2026-11-02'
description: BestBid.lol is a transparent paid‑ranking advertising platform for products, brands, and creators. It lets users discover and save public profiles, explore transparent paid rankings, and introduce their own work, with rankings based on total completed paid bids rather than quality or endorsement. The site offers discover, rankings, saved items, and an advertising disclosure explaining how the rankings work.
image: https://bestbid.lol/opengraph-image.png
layout: provider
mcp_servers:
- description: Remote MCP server at bestbid.lol.
  name: BestBid.lol MCP Server
  slug: bestbid-lol-mcp-yml
modified: '2026-11-02'
name: BestBid.lol
nav: Providers
network: true
overview: BestBid.lol is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Advertising, Marketplace, Rankings, Transparency, and Community.
plans:
- name: Bestbid Lol Plans Pricing
  plan_count: 0
  slug: bestbid-lol-plans-pricing
random_paper: 1
rate_limits:
- limit_count: 0
  name: Bestbid Lol Rate Limits
  slug: bestbid-lol-rate-limits
scopes:
- name: Bestbid Lol Scopes
  scope_count: 0
  slug: bestbid-lol-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: minimal
  composite: 8.5
  coverage:
    artifact_dirs: 20
    catalog_earned: 32.0
    catalog_earned_first_party: 0.0
    catalog_gap: 83.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 10.5
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 0.0
    discoverability: 57.5
    operational_transparency: 0.0
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
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: authentication
  name: Bestbid Lol Authentication
  slug: bestbid-lol-authentication
  summary_line: 0 schemes
- kind: domain-security
  name: Bestbid Lol Domain Security
  slug: bestbid-lol-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: bestbid-lol
tags:
- Advertising
- Marketplace
- Rankings
- Transparency
- Community
website: https://bestbid.lol/
---
