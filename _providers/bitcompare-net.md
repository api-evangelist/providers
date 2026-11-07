---
access_model:
  confidence: high
  label: Freemium
  onboarding: unknown
  pricing: freemium
  public: false
  source:
  - plans
  - authentication
  - rate-limits
  - security
  trial: false
  try_now: false
agent_readiness:
  band: agent-ready
  band_gated_from: agent-native
  dimensions:
    agent_card: flavored
    agent_skills: derived
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: served
    consent_identity: false
    delegated_identity: served
    dry_run_mode: false
    dynamic_client_registration: true
    error_semantics: derived
    event_surface_described: false
    idempotency: false
    mcp_server: documented
    mcp_tool_quality: na
    openapi_examples: verified
    operation_distinctiveness: distinct
    pagination_ratio: false
    protected_resource_metadata: verified
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 44.5
  scored_at: '2026-11-06'
agentic_access:
- acting_count: 2
  human_in_the_loop: 0
  name: Bitcompare Net Agentic Access
  operation_count: 22
  slug: bitcompare-net-agentic-access
  summary_line: 22 operations · 2 acting
api_count: 1
apis:
- description: Public REST API powering Bitcompare and the Bitcompare MCP server, providing crypto yield data, coin metadata, prices, market stats, and stablecoin information.
  name: Bitcompare API
  slug: bitcompare-api
- baseURL: https://api.bitcompare.net
  baseurl_source: declared
  description: The benchmarks API from Bitcompare — 1 operation(s) for benchmarks.
  name: Bitcompare Benchmarks API
  slug: bitcompare-net-benchmarks-api
- baseURL: https://api.bitcompare.net
  baseurl_source: declared
  description: Coin metadata, market data, and history
  name: Bitcompare Coins API
  slug: bitcompare-net-coins-api
- baseURL: https://api.bitcompare.net
  baseurl_source: declared
  description: The earn API from Bitcompare — 2 operation(s) for earn.
  name: Bitcompare Earn API
  slug: bitcompare-net-earn-api
- baseURL: https://api.bitcompare.net
  baseurl_source: declared
  description: Global market statistics
  name: Bitcompare Market API
  slug: bitcompare-net-market-api
- baseURL: https://api.bitcompare.net
  baseurl_source: declared
  description: Model Context Protocol transport
  name: Bitcompare MCP API
  slug: bitcompare-net-mcp-api
- baseURL: https://api.bitcompare.net
  baseurl_source: declared
  description: Aggregated spot prices from multiple feeds
  name: Bitcompare Prices API
  slug: bitcompare-net-prices-api
- baseURL: https://api.bitcompare.net
  baseurl_source: declared
  description: Crypto yield data across providers
  name: Bitcompare Rates API
  slug: bitcompare-net-rates-api
- baseURL: https://api.bitcompare.net
  baseurl_source: declared
  description: Stablecoin index + peg-stability data
  name: Bitcompare Stablecoins API
  slug: bitcompare-net-stablecoins-api
- baseURL: https://api.bitcompare.net
  baseurl_source: declared
  description: Symbol resolution and normalisation
  name: Bitcompare Symbols API
  slug: bitcompare-net-symbols-api
artifact_total: 19
common:
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.bitcompare.net/quickstart
- group: docs
  title: ''
  type: Documentation
  url: https://docs.bitcompare.net/
- group: agent
  href: https://artifacts.apis.io/bitcompare-net/agentic-access/bitcompare-net-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/bitcompare-net-agentic-access.yml
- group: operate
  href: https://artifacts.apis.io/bitcompare-net/rate-limits/bitcompare-net-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/bitcompare-net-rate-limits.yml
- group: commercial
  href: https://artifacts.apis.io/bitcompare-net/plans/bitcompare-net-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/bitcompare-net-plans-pricing.yml
- group: design
  href: https://artifacts.apis.io/bitcompare-net/rules/bitcompare-net-rules.yml
  title: ''
  type: Spectral
  url: rules/bitcompare-net-rules.yml
- group: design
  href: https://artifacts.apis.io/bitcompare-net/vocabulary/bitcompare-net-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/bitcompare-net-vocabulary.yml
- group: agent
  href: https://artifacts.apis.io/bitcompare-net/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: auth
  title: ''
  type: Security
  url: https://bitcompare.net/terms-of-use
- group: auth
  href: https://artifacts.apis.io/bitcompare-net/authentication/bitcompare-net-authentication.yml
  title: ''
  type: Authentication
  url: authentication/bitcompare-net-authentication.yml
- group: design
  href: https://artifacts.apis.io/bitcompare-net/errors/bitcompare-net-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/bitcompare-net-problem-types.yml
- group: design
  href: https://artifacts.apis.io/bitcompare-net/conformance/bitcompare-net-conformance.yml
  title: ''
  type: Conformance
  url: conformance/bitcompare-net-conformance.yml
- group: agent
  href: https://artifacts.apis.io/bitcompare-net/llms/bitcompare-net-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/bitcompare-net-llms.txt
- group: other
  href: https://artifacts.apis.io/bitcompare-net/a2a/bitcompare-net-a2a.yml
  title: ''
  type: AgentCard
  url: a2a/bitcompare-net-a2a.yml
- group: build
  href: https://artifacts.apis.io/bitcompare-net/mcp/bitcompare-net-tool-crosswalk.yml
  title: ''
  type: ToolCrosswalk
  url: mcp/bitcompare-net-tool-crosswalk.yml
- group: agent
  href: https://artifacts.apis.io/bitcompare-net/mcp/bitcompare-net-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/bitcompare-net-mcp.yml
- group: auth
  href: https://artifacts.apis.io/bitcompare-net/well-known/bitcompare-net-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/bitcompare-net-security.txt
- group: auth
  href: https://artifacts.apis.io/bitcompare-net/well-known/bitcompare-net-pro-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/bitcompare-net-pro-security.txt
- group: agent
  href: https://artifacts.apis.io/bitcompare-net/well-known/bitcompare-net-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/bitcompare-net-well-known.yml
- group: other
  href: https://artifacts.apis.io/bitcompare-net/hosts/bitcompare-net-hosts.yml
  title: ''
  type: Hosts
  url: hosts/bitcompare-net-hosts.yml
- group: other
  href: https://artifacts.apis.io/bitcompare-net/vendors/bitcompare-net-vendors.yml
  title: ''
  type: Vendors
  url: vendors/bitcompare-net-vendors.yml
- group: build
  href: https://artifacts.apis.io/bitcompare-net/packages/bitcompare-net-packages.yml
  title: ''
  type: SDKs
  url: packages/bitcompare-net-packages.yml
- group: build
  href: https://artifacts.apis.io/bitcompare-net/packages/bitcompare-net-packages.yml
  title: ''
  type: Packages
  url: packages/bitcompare-net-packages.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://bitcompare.net/terms-of-use
- group: operate
  title: ''
  type: StatusPage
  url: https://bitcompare.net/status
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://bitcompare.net/privacy-policy
- group: commercial
  title: ''
  type: Pricing
  url: https://pro.bitcompare.net/pricing
- group: company
  title: ''
  type: Newsroom
  url: https://bitcompare.net/news
- group: start
  title: ''
  type: Login
  url: https://auth.bitcompare.net/pro/login
- group: start
  title: ''
  type: DeveloperPortal
  url: https://bitcompare.net/developers
- group: operate
  title: ''
  type: ChangeLog
  url: https://bitcompare.net/changelog
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/bitcompare
- group: auth
  href: https://artifacts.apis.io/bitcompare-net/security/bitcompare-net-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/bitcompare-net-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/bitcompare-net/security/bitcompare-net-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/bitcompare-net-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://bitcompare.net/
- group: docs
  title: ''
  type: APIReference
  url: https://bitcompare.net/openapi.json
created: '2026-11-02'
description: Bitcompare provides live and historical crypto yield rates across CeFi and DeFi, offering benchmark data for staking, lending, and borrowing markets. Their API delivers normalized yield intelligence, enabling developers to integrate crypto yield data into applications, dashboards, and AI-ready workflows.
image: https://bitcompare-public.sgp1.cdn.digitaloceanspaces.com/og/bitcompare.png
layout: provider
mcp_servers:
- description: Remote MCP server at api.bitcompare.net requiring an API key.
  name: Bitcompare MCP Server
  slug: bitcompare-net-mcp-yml
modified: '2026-11-02'
name: Bitcompare
nav: Providers
network: true
overview: 'Bitcompare publishes 10 API contracts indexed on the [APIs.io](https://apis.io/) network, including Benchmarks API, Coins API, Earn API, and 7 more. Tagged areas include Cryptocurrency, Finance, Data, and Yield.


  The Bitcompare catalog on APIs.io includes 1 Spectral governance ruleset.


  Bitcompare''s developer surface includes getting-started guide, documentation, authentication, pricing, changelog, API reference, and 30 more developer resources.'
plans:
- name: Bitcompare Net Plans Pricing
  plan_count: 5
  slug: bitcompare-net-plans-pricing
random_paper: 18
rate_limits:
- limit_count: 2
  name: Bitcompare Net Rate Limits
  slug: bitcompare-net-rate-limits
rules:
- authorship: generated
  effective_rule_count: 110
  extends:
  - spectral:oas
  name: Bitcompare API Rules
  rule_count: 69
  severity_counts:
    error: 59
    hint: 0
    info: 1
    warn: 9
  slug: bitcompare-net-rules
score:
  band: developing
  composite: 47.9
  coverage:
    artifact_dirs: 20
    catalog_earned: 57.8
    catalog_earned_first_party: 20.0
    catalog_gap: 57.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 53.9
    contract_governance: 22.0
    contract_quality: 52.9
    developer_ergonomics: 39.9
    discoverability: 57.5
    operational_transparency: 44.7
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 9
    mcp: derived
    skills: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 26.5
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: authentication
  name: Bitcompare Net Authentication
  slug: bitcompare-net-authentication
  summary_line: 1 scheme
- kind: domain-security
  name: Bitcompare Net Domain Security
  slug: bitcompare-net-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Bitcompare Net Vulnerability Disclosure
  slug: bitcompare-net-vulnerability-disclosure
  summary_line: security.txt · contact published
skill_count: 1
skills:
- name: rates
  slug: bitcompare-net-rates-skill
slug: bitcompare-net
tags:
- Cryptocurrency
- Finance
- Data
- Yield
website: https://bitcompare.net/
---
