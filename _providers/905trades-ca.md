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
api_count: 0
artifact_total: 2
common:
- group: agent
  href: https://artifacts.apis.io/905trades-ca/llms/905trades-ca-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/905trades-ca-llms.txt
- group: agent
  href: https://artifacts.apis.io/905trades-ca/mcp/905trades-ca-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/905trades-ca-mcp.yml
- group: other
  href: https://artifacts.apis.io/905trades-ca/hosts/905trades-ca-hosts.yml
  title: ''
  type: Hosts
  url: hosts/905trades-ca-hosts.yml
- group: other
  href: https://artifacts.apis.io/905trades-ca/vendors/905trades-ca-vendors.yml
  title: ''
  type: Vendors
  url: vendors/905trades-ca-vendors.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://905trades.ca/terms/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://905trades.ca/privacy/
- group: auth
  href: https://artifacts.apis.io/905trades-ca/security/905trades-ca-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/905trades-ca-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://905trades.ca/
coverage:
  checked: '2026-10-31'
  detail: MCP endpoint only accepts POST, no GET spec available
  evidence:
  - status: 405
    url: https://905trades.ca/mcp
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-10-31'
description: 905 Trades is a Canadian platform that connects homeowners in the Greater Toronto Area with vetted residential trade professionals such as flooring installers, garage door specialists, carpet cleaners, and renovation contractors. The service operates on a referral fee model where contractors pay for leads, ensuring homeowners receive quotes directly from the tradespeople without additional charges from the platform. The site provides detailed service area coverage, partner information, and transparent terms and privacy policies.
image: https://905trades.ca/img/og-905-trades.png
layout: provider
mcp_servers:
- description: Remote MCP server at 905trades.ca.
  name: 905 Trades MCP Server
  slug: 905trades-ca-mcp-yml
modified: '2026-10-31'
name: 905 Trades
nav: Providers
network: true
overview: 905 Trades is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Home Services, Trade, Canada, and GTA.
random_paper: 10
score:
  band: minimal
  composite: 6.1
  coverage:
    artifact_dirs: 7
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -2.7
  facets:
    access_clarity: 10.5
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 0.0
    discoverability: 48.3
    operational_transparency: 0.0
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    countries:
    - canada
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
    regions:
    - north-america
  previous_composite: 8.8
  provenance:
    mcp: first-party
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 9.8
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: 905Trades Ca Domain Security
  slug: 905trades-ca-domain-security
  summary_line: TLSv1.3
slug: 905trades-ca
tags:
- Company
- Home Services
- Trade
- Canada
- GTA
website: https://905trades.ca/
---
