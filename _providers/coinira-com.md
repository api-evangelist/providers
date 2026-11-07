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
  - security
  trial: false
  try_now: false
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: false
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: derived
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
  score: 8.8
  scored_at: '2026-11-06'
agentic_access:
- acting_count: 0
  human_in_the_loop: 0
  name: Coinira Com Agentic Access
  operation_count: 2
  slug: coinira-com-agentic-access
  summary_line: 2 operations
api_count: 1
apis:
- description: Read-only calculation endpoints for hypothetical retirement growth and historical cryptocurrency investment results.
  name: Coin IRA Calculator API
  slug: coin-ira-calculator-api
artifact_total: 5
common:
- group: agent
  href: https://artifacts.apis.io/coinira-com/agentic-access/coinira-com-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/coinira-com-agentic-access.yml
- group: design
  href: https://artifacts.apis.io/coinira-com/rules/coinira-com-rules.yml
  title: ''
  type: Spectral
  url: rules/coinira-com-rules.yml
- group: design
  href: https://artifacts.apis.io/coinira-com/errors/coinira-com-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/coinira-com-problem-types.yml
- group: design
  href: https://artifacts.apis.io/coinira-com/conformance/coinira-com-conformance.yml
  title: ''
  type: Conformance
  url: conformance/coinira-com-conformance.yml
- group: agent
  href: https://artifacts.apis.io/coinira-com/llms/coinira-com-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/coinira-com-llms.txt
- group: agent
  href: https://artifacts.apis.io/coinira-com/mcp/coinira-com-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/coinira-com-mcp.yml
- group: agent
  href: https://artifacts.apis.io/coinira-com/well-known/coinira-com-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/coinira-com-well-known.yml
- group: other
  href: https://artifacts.apis.io/coinira-com/hosts/coinira-com-hosts.yml
  title: ''
  type: Hosts
  url: hosts/coinira-com-hosts.yml
- group: other
  href: https://artifacts.apis.io/coinira-com/vendors/coinira-com-vendors.yml
  title: ''
  type: Vendors
  url: vendors/coinira-com-vendors.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://coinira.com/terms-and-conditions/
- group: auth
  title: ''
  type: Security
  url: https://coinira.com/security/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://coinira.com/privacy-policy/
- group: commercial
  title: ''
  type: Pricing
  url: https://coinira.com/pricing/
- group: start
  title: ''
  type: Login
  url: https://secure.coinira.com/Authentication/Login
- group: company
  title: ''
  type: Blog
  url: https://coinira.com/blog/
- group: auth
  href: https://artifacts.apis.io/coinira-com/security/coinira-com-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/coinira-com-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://coinira.com/
created: '2026-11-04'
description: Coin IRA offers a $0‑fee self‑directed cryptocurrency IRA, allowing investors to hold Bitcoin, Ethereum, XRP and other digital assets alongside traditional holdings like fractional gold and silver. The platform provides free cold storage, no account fees, and tools for tax‑advantaged crypto investing, targeting both individual and retirement accounts. It emphasizes security, compliance, and easy access through a web portal and mobile app.
image: https://coinira.com/static/img/social/home-og.4333075c2d3b.webp
layout: provider
mcp_servers:
- description: Remote MCP server at coinira.com.
  name: Coin IRA MCP Server
  slug: coinira-com-mcp-yml
modified: '2026-11-04'
name: Coin IRA
nav: Providers
network: true
overview: 'Coin IRA is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Finance, Cryptocurrency, IRA, and Investment.


  The Coin IRA catalog on APIs.io includes 1 Spectral governance ruleset.


  Coin IRA''s developer surface includes pricing, engineering blog, and 15 more developer resources.'
random_paper: 1
rules:
- authorship: generated
  effective_rule_count: 73
  extends:
  - spectral:oas
  name: Coin IRA API Rules
  rule_count: 32
  severity_counts:
    error: 30
    hint: 0
    info: 1
    warn: 1
  slug: coinira-com-rules
score:
  band: emerging
  composite: 20.0
  coverage:
    artifact_dirs: 13
    catalog_earned: 41.5
    catalog_earned_first_party: 0.0
    catalog_gap: 73.5
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 44.7
    contract_governance: 18.2
    contract_quality: 0.0
    developer_ergonomics: 2.4
    discoverability: 65.0
    operational_transparency: 10.5
  provenance:
    agentic_access: derived
    conformance: derived
    mcp: first-party
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 18.6
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Coinira Com Domain Security
  slug: coinira-com-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: coinira-com
tags:
- Company
- Finance
- Cryptocurrency
- IRA
- Investment
- Retirement
website: https://coinira.com/
---
