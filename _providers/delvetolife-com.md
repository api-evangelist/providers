---
access_model:
  confidence: medium
  gated: none
  gated_source:
  - onboarding
  label: Free · Open access
  onboarding: open
  pricing: free
  public: true
  source:
  - plans
  - authentication
  - security
  trial: false
  try_now: true
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
  score: 8.5
  scored_at: '2026-11-06'
api_count: 1
apis:
- description: 'Free, read-only remote MCP server (Streamable HTTP, no account, API key or sign-in) exposing Delve to Life dress-code guides, outfit formulas, colour combinations and guide search to MCP clients such '
  name: Delve to Life MCP Server
  slug: delve-to-life-mcp-server
artifact_total: 12
common:
- group: commercial
  href: https://artifacts.apis.io/delvetolife-com/plans/delvetolife-com-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/delvetolife-com-plans-pricing.yml
- group: design
  href: https://artifacts.apis.io/delvetolife-com/conventions/delvetolife-com-conventions.yml
  title: ''
  type: Conventions
  url: conventions/delvetolife-com-conventions.yml
- group: auth
  href: https://artifacts.apis.io/delvetolife-com/authentication/delvetolife-com-authentication.yml
  title: ''
  type: Authentication
  url: authentication/delvetolife-com-authentication.yml
- group: agent
  href: https://artifacts.apis.io/delvetolife-com/llms/delvetolife-com-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/delvetolife-com-llms.txt
- group: agent
  href: https://artifacts.apis.io/delvetolife-com/mcp/delvetolife-com-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/delvetolife-com-mcp.yml
- group: agent
  href: https://artifacts.apis.io/delvetolife-com/well-known/delvetolife-com-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/delvetolife-com-well-known.yml
- group: other
  href: https://artifacts.apis.io/delvetolife-com/hosts/delvetolife-com-hosts.yml
  title: ''
  type: Hosts
  url: hosts/delvetolife-com-hosts.yml
- group: other
  href: https://artifacts.apis.io/delvetolife-com/vendors/delvetolife-com-vendors.yml
  title: ''
  type: Vendors
  url: vendors/delvetolife-com-vendors.yml
- group: auth
  href: https://artifacts.apis.io/delvetolife-com/security/delvetolife-com-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/delvetolife-com-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://delvetolife.com/
- group: docs
  title: ''
  type: Documentation
  url: https://delvetolife.com/ai/
- group: company
  title: ''
  type: About
  url: https://delvetolife.com/about/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://delvetolife.com/privacy
created: '2026-11-05'
description: Delve to Life (delvetolife.com) is an independent English-language style reference project that explains clothing names with side-by-side illustrated pictures, converts clothing and shoe sizes across US, UK, EU, Japan, Korea and China, explains dress codes from casual to white tie, and suggests what to wear by weather and occasion. It publishes a free, read-only remote MCP server (Streamable HTTP, no account or API key) exposing its dress-code guides, outfit formulas and colour combinations to AI assistants.
examples:
- key_count: 3
  name: Delvetolife Com Mcp Tools List
  slug: delvetolife-com-mcp-tools-list
image: https://delvetolife.com/assets/everyday-style-editorial-1200.jpg
json_schemas:
- name: Delvetolife Com Colour Combinations Input
  property_count: 1
  slug: delvetolife-com-colour-combinations-input
- name: Delvetolife Com Explain Dress Code Input
  property_count: 1
  slug: delvetolife-com-explain-dress-code-input
- name: Delvetolife Com List Dress Codes Input
  property_count: 0
  slug: delvetolife-com-list-dress-codes-input
- name: Delvetolife Com Search Guides Input
  property_count: 2
  slug: delvetolife-com-search-guides-input
- name: Delvetolife Com Suggest Outfit Input
  property_count: 3
  slug: delvetolife-com-suggest-outfit-input
layout: provider
mcp_servers:
- description: Remote MCP server at mcp.delvetolife.com over streamable HTTP; 5 tools listed.
  name: Delve to Life MCP Server
  slug: delve-to-life
modified: '2026-11-05'
name: Delve to Life
nav: Providers
network: true
overview: 'Delve to Life is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Fashion, Clothing, Size Charts, and Dress Codes.


  Delve to Life''s developer surface includes authentication, documentation, and 11 more developer resources.'
plans:
- name: Delvetolife Com Plans Pricing
  plan_count: 1
  slug: delvetolife-com-plans-pricing
random_paper: 23
rate_limits:
- limit_count: 0
  name: Delvetolife Com Rate Limits
  slug: delvetolife-com-rate-limits
score:
  band: emerging
  composite: 19.8
  coverage:
    artifact_dirs: 15
    catalog_earned: 54.0
    catalog_earned_first_party: 8.0
    catalog_gap: 61.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 31.6
    contract_governance: 0.0
    contract_quality: 12.0
    developer_ergonomics: 21.4
    discoverability: 65.0
    operational_transparency: 0.0
  provenance:
    mcp: first-party
  regulatory:
    applies: true
    matched_via: residual_tags
    regime: AI & Biometrics
    regime_id: ai_biometrics
    score: 15.7
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: authentication
  name: Delvetolife Com Authentication
  slug: delvetolife-com-authentication
  summary_line: 1 scheme
- kind: domain-security
  name: Delvetolife Com Domain Security
  slug: delvetolife-com-domain-security
  summary_line: TLSv1.3
slug: delvetolife-com
tags:
- Company
- Fashion
- Clothing
- Size Charts
- Dress Codes
- Style Guides
- MCP
- AI Assistant
website: https://delvetolife.com/
---
