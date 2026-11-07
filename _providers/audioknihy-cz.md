---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source:
  - security
  trial: false
  try_now: false
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: unknown
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
    well_known_catalog: true
  schema_version: '0.2'
  score: 9.6
  scored_at: '2026-11-06'
api_count: 1
apis:
- description: Audioknihy.cz provides a price-comparison API for Czech audiobooks.
  name: Audioknihy API
  slug: audioknihy-api
artifact_total: 16
common:
- group: agent
  href: https://artifacts.apis.io/audioknihy-cz/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: agent
  href: https://artifacts.apis.io/audioknihy-cz/llms/audioknihy-cz-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/audioknihy-cz-llms.txt
- group: agent
  href: https://artifacts.apis.io/audioknihy-cz/mcp/audioknihy-cz-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/audioknihy-cz-mcp.yml
- group: agent
  href: https://artifacts.apis.io/audioknihy-cz/well-known/audioknihy-cz-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/audioknihy-cz-well-known.yml
- group: other
  href: https://artifacts.apis.io/audioknihy-cz/hosts/audioknihy-cz-hosts.yml
  title: ''
  type: Hosts
  url: hosts/audioknihy-cz-hosts.yml
- group: other
  href: https://artifacts.apis.io/audioknihy-cz/vendors/audioknihy-cz-vendors.yml
  title: ''
  type: Vendors
  url: vendors/audioknihy-cz-vendors.yml
- group: auth
  href: https://artifacts.apis.io/audioknihy-cz/security/audioknihy-cz-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/audioknihy-cz-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://audioknihy.cz/
- group: company
  title: ''
  type: Blog
  url: https://audioknihy.cz/blog
- group: operate
  title: ''
  type: Support
  url: https://audioknihy.cz/kontakt
- group: commercial
  title: ''
  type: Pricing
  url: https://audioknihy.cz/ceny
- group: commercial
  title: ''
  type: TermsOfService
  url: https://audioknihy.cz/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://audioknihy.cz/privacy
- group: operate
  title: ''
  type: Roadmap
  url: https://audioknihy.cz/roadmap
- group: start
  title: ''
  type: SignUp
  url: https://audioknihy.cz/prihlasit
coverage:
  checked: '2026-11-02'
  detail: MCP endpoint https://audioknihy.cz/api/mcp requires POST JSON-RPC which returns 406 Not Acceptable without authentication.
  evidence:
  - status: 406
    url: https://audioknihy.cz/api/mcp
  reason: auth-required
  state: gated
created: '2026-11-02'
description: 'audioknihy-cz is a company surfaced via the API Evangelist harvest backlog (source: mcp-registry) and added to the network as a stub for full-pipeline profiling.'
image: https://audioknihy.cz/logo-icon-transparent.png
layout: provider
mcp_servers:
- description: Remote MCP server at audioknihy.cz.
  name: Audioknihy.cz MCP Server
  slug: audioknihy-cz-mcp-yml
modified: '2026-11-02'
name: Audioknihy.cz
nav: Providers
network: true
overview: 'Audioknihy.cz is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Audio, Books, Comparison, Czech, and Marketplace.


  Audioknihy.cz''s developer surface includes engineering blog, support, pricing, signup flow, and 11 more developer resources.'
random_paper: 23
score:
  band: emerging
  composite: 11.7
  coverage:
    artifact_dirs: 9
    catalog_earned: 32.0
    catalog_earned_first_party: 0.0
    catalog_gap: 83.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -6.1
  facets:
    access_clarity: 22.4
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 10.0
    discoverability: 56.7
    operational_transparency: 2.6
  previous_composite: 17.8
  provenance:
    mcp: first-party
    skills: unknown
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 9.8
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: falling
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Audioknihy Cz Domain Security
  slug: audioknihy-cz-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC
skill_count: 13
skills:
- name: browse-genres
  slug: audioknihy-cz-browse-genres
- name: compare-all-offers
  slug: audioknihy-cz-compare-all-offers
- name: find-cheapest-offer
  slug: audioknihy-cz-find-cheapest-offer
- name: get-audiobook-rankings
  slug: audioknihy-cz-get-audiobook-rankings
- name: get-audiobook
  slug: audioknihy-cz-get-audiobook
- name: get-author
  slug: audioknihy-cz-get-author
- name: get-narrator
  slug: audioknihy-cz-get-narrator
- name: get-price-index
  slug: audioknihy-cz-get-price-index
- name: get-price-trend
  slug: audioknihy-cz-get-price-trend
- name: get-publisher
  slug: audioknihy-cz-get-publisher
- name: list-partners
  slug: audioknihy-cz-list-partners
- name: search-audiobooks
  slug: audioknihy-cz-search-audiobooks
- name: search-by-filters
  slug: audioknihy-cz-search-by-filters
slug: audioknihy-cz
tags:
- Audio
- Books
- Comparison
- Czech
- Marketplace
website: https://audioknihy.cz/
---
