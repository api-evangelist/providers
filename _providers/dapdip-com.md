---
access_model:
  confidence: low
  label: Freemium
  onboarding: unknown
  pricing: freemium
  public: false
  source:
  - plans
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
- description: DapDip provides a creator‑growth analytics platform with public guides and pricing information. No public machine‑readable API contract was found.
  name: DapDip API
  slug: dapdip-api
artifact_total: 4
common:
- group: commercial
  href: https://artifacts.apis.io/dapdip-com/plans/dapdip-com-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/dapdip-com-plans-pricing.yml
- group: agent
  href: https://artifacts.apis.io/dapdip-com/llms/dapdip-com-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/dapdip-com-llms.txt
- group: agent
  href: https://artifacts.apis.io/dapdip-com/mcp/dapdip-com-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/dapdip-com-mcp.yml
- group: other
  href: https://artifacts.apis.io/dapdip-com/hosts/dapdip-com-hosts.yml
  title: ''
  type: Hosts
  url: hosts/dapdip-com-hosts.yml
- group: other
  href: https://artifacts.apis.io/dapdip-com/vendors/dapdip-com-vendors.yml
  title: ''
  type: Vendors
  url: vendors/dapdip-com-vendors.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.dapdip.com/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.dapdip.com/privacy
- group: commercial
  title: ''
  type: Pricing
  url: https://www.dapdip.com/pricing
- group: company
  title: ''
  type: Newsroom
  url: https://www.dapdip.com/news
- group: start
  title: ''
  type: Login
  url: https://www.dapdip.com/signin
- group: docs
  title: ''
  type: Documentation
  url: https://www.dapdip.com/guides
- group: auth
  href: https://artifacts.apis.io/dapdip-com/security/dapdip-com-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/dapdip-com-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://dapdip.com/
coverage:
  checked: '2026-11-05'
  detail: No OpenAPI, AsyncAPI, GraphQL, or other contract was discovered despite public documentation pages.
  evidence:
  - status: 200
    url: https://www.dapdip.com/guides
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-11-04'
description: DapDip is a creator‑growth analytics platform that helps YouTube creators increase audience retention, optimize monetization, and discover AI‑powered tools. The site publishes original guides written by its editorial team, citing official YouTube documentation, and explicitly refuses to share fake‑engagement tactics or speculative metrics.
image: https://www.dapdip.com/opengraph-image
layout: provider
mcp_servers:
- description: Remote MCP server at www.dapdip.com.
  name: DapDip MCP Server
  slug: dapdip-com-mcp-yml
modified: '2026-11-04'
name: DapDip
nav: Providers
network: true
overview: 'DapDip is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include YouTube, CreatorGrowth, Analytics, Artificial Intelligence, and Platform.


  DapDip''s developer surface includes pricing, documentation, and 11 more developer resources.'
plans:
- name: Dapdip Com Plans Pricing
  plan_count: 2
  slug: dapdip-com-plans-pricing
random_paper: 6
score:
  band: emerging
  composite: 20.5
  coverage:
    artifact_dirs: 8
    catalog_earned: 40.0
    catalog_earned_first_party: 8.0
    catalog_gap: 75.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 65.8
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 9.5
    discoverability: 58.3
    operational_transparency: 0.0
  provenance:
    mcp: first-party
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 12.7
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Dapdip Com Domain Security
  slug: dapdip-com-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: dapdip-com
tags:
- YouTube
- CreatorGrowth
- Analytics
- Artificial Intelligence
- Platform
website: https://dapdip.com/
---
