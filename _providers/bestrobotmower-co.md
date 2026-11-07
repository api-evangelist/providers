---
access_model:
  confidence: low
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
api_count: 0
artifact_total: 6
common:
- group: agent
  href: https://artifacts.apis.io/bestrobotmower-co/llms/bestrobotmower-co-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/bestrobotmower-co-llms.txt
- group: agent
  href: https://artifacts.apis.io/bestrobotmower-co/mcp/bestrobotmower-co-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/bestrobotmower-co-mcp.yml
- group: other
  href: https://artifacts.apis.io/bestrobotmower-co/hosts/bestrobotmower-co-hosts.yml
  title: ''
  type: Hosts
  url: hosts/bestrobotmower-co-hosts.yml
- group: other
  href: https://artifacts.apis.io/bestrobotmower-co/vendors/bestrobotmower-co-vendors.yml
  title: ''
  type: Vendors
  url: vendors/bestrobotmower-co-vendors.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://bestrobotmower.co/legal/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://bestrobotmower.co/legal/privacy
- group: company
  title: ''
  type: Newsroom
  url: https://bestrobotmower.co/news
- group: company
  title: ''
  type: Blog
  url: https://bestrobotmower.co/blog
- group: auth
  href: https://artifacts.apis.io/bestrobotmower-co/security/bestrobotmower-co-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/bestrobotmower-co-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://bestrobotmower.co/
coverage:
  checked: '2026-11-02'
  detail: MCP endpoint requires POST and returns 405 to GET, preventing contract discovery.
  evidence:
  - status: 405
    url: https://bestrobotmower.co/api/mcp
  reason: auth-required
  state: gated
created: '2026-11-02'
description: BestRobotMower.co provides comprehensive reviews and specifications of the best robot lawn mowers on the market. The site compares wire‑free and RTK models from leading brands such as Segway, Mammotion, and Ecovacs, covering lawn size, slope, price, and navigation features. It serves homeowners, landscaping professionals, and gardening enthusiasts looking to automate lawn care with reliable, high‑performance robotic mowers.
image: https://bestrobotmower.co/brand/icon.svg
layout: provider
mcp_servers:
- description: Remote MCP server at bestrobotmower.co.
  name: BestRobotMower.co MCP Server
  slug: bestrobotmower-co-mcp-yml
modified: '2026-11-02'
name: BestRobotMower.co
nav: Providers
network: true
overview: 'BestRobotMower.co is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Robotics, Lawn Care, Reviews, and Comparison.


  BestRobotMower.co''s developer surface includes engineering blog and 9 more developer resources.'
plans:
- name: Bestrobotmower Co Plans Pricing
  plan_count: 0
  slug: bestrobotmower-co-plans-pricing
random_paper: 13
rate_limits:
- limit_count: 0
  name: Bestrobotmower Co Rate Limits
  slug: bestrobotmower-co-rate-limits
scopes:
- name: Bestrobotmower Co Scopes
  scope_count: 0
  slug: bestrobotmower-co-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: minimal
  composite: 7.9
  coverage:
    artifact_dirs: 21
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 10.5
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 1.2
    discoverability: 49.2
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
  name: Bestrobotmower Co Authentication
  slug: bestrobotmower-co-authentication
  summary_line: 0 schemes
- kind: domain-security
  name: Bestrobotmower Co Domain Security
  slug: bestrobotmower-co-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: bestrobotmower-co
tags:
- Company
- Robotics
- Lawn Care
- Reviews
- Comparison
website: https://bestrobotmower.co/
---
