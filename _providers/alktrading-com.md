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
  href: https://artifacts.apis.io/alktrading-com/llms/alktrading-com-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/alktrading-com-llms.txt
- group: agent
  href: https://artifacts.apis.io/alktrading-com/mcp/alktrading-com-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/alktrading-com-mcp.yml
- group: other
  href: https://artifacts.apis.io/alktrading-com/hosts/alktrading-com-hosts.yml
  title: ''
  type: Hosts
  url: hosts/alktrading-com-hosts.yml
- group: other
  href: https://artifacts.apis.io/alktrading-com/vendors/alktrading-com-vendors.yml
  title: ''
  type: Vendors
  url: vendors/alktrading-com-vendors.yml
- group: company
  title: ''
  type: Newsroom
  url: https://alktrading.com/news
- group: other
  title: ''
  type: Leadership
  url: https://alktrading.com/TEAM
- group: auth
  href: https://artifacts.apis.io/alktrading-com/security/alktrading-com-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/alktrading-com-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://alktrading.com/
- group: company
  title: ''
  type: Blog
  url: https://alktrading.com/blog
- group: commercial
  title: ''
  type: Pricing
  url: https://alktrading.com/pricing
- group: start
  title: ''
  type: SignUp
  url: https://alktrading.com/signup
coverage:
  checked: '2026-11-01'
  detail: All attempted OpenAPI spec URLs on api.alktrading.com and alktrading.com returned 404, indicating no machine‑readable API contract is published.
  evidence:
  - status: 404
    url: https://api.alktrading.com/openapi.json
  - status: 404
    url: https://alktrading.com/openapi.json
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-11-01'
description: ALK Trading provides free, rules‑based trading charts and signals focused on US mega‑cap stocks. Each card shows the side, entry and stop, and the service is educational‑only, not a broker. The platform also offers a paid mentorship program for $199 per month, featuring daily group sessions of one to two hours and a weekly one‑on‑one with instructor Ravi, limited to fifteen members. All content is intended for education and not financial advice.
image: https://alktrading.com/alk-card-2610c.jpg
layout: provider
mcp_servers:
- description: Remote MCP server at alktrading.com.
  name: ALK Trading MCP Server
  slug: alktrading-com-mcp-yml
modified: '2026-11-01'
name: ALK Trading
nav: Providers
network: true
overview: 'ALK Trading is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Trading, Education, Mentorship, Stocks, and US Mega-Caps.


  ALK Trading''s developer surface includes engineering blog, pricing, signup flow, and 8 more developer resources.'
plans:
- name: Alktrading Com Plans Pricing
  plan_count: 0
  slug: alktrading-com-plans-pricing
random_paper: 5
rate_limits:
- limit_count: 0
  name: Alktrading Com Rate Limits
  slug: alktrading-com-rate-limits
scopes:
- name: Alktrading Com Scopes
  scope_count: 0
  slug: alktrading-com-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: minimal
  composite: 7.2
  coverage:
    artifact_dirs: 21
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -2.8
  facets:
    access_clarity: 11.8
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 1.2
    discoverability: 50.0
    operational_transparency: 0.0
  previous_composite: 10.0
  provenance:
    conformance: unknown
    mcp: first-party
  regulatory:
    applies: true
    matched_via: tags
    regime: Education & Research
    regime_id: education
    score: 15.7
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: authentication
  name: Alktrading Com Authentication
  slug: alktrading-com-authentication
  summary_line: 0 schemes
- kind: domain-security
  name: Alktrading Com Domain Security
  slug: alktrading-com-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: alktrading-com
tags:
- Trading
- Education
- Mentorship
- Stocks
- US Mega-Caps
website: https://alktrading.com/
---
