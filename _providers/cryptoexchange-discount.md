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
    agent_skills: false
    agentic_access: derived
    agentic_commerce: self
    auth_clarity: served
    consent_identity: false
    delegated_identity: served
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
    protected_resource_metadata: verified
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: true
  schema_version: '0.2'
  score: 26.1
  scored_at: '2026-11-06'
agentic_access:
- acting_count: 0
  human_in_the_loop: 0
  name: Cryptoexchange Discount Agentic Access
  operation_count: 1
  slug: cryptoexchange-discount-agentic-access
  summary_line: 1 operation
api_count: 1
apis:
- description: Public discovery API for exchange discount lookups.
  name: CryptoExchange Discount API
  slug: cryptoexchange-discount-api
artifact_total: 5
common:
- group: agent
  href: https://artifacts.apis.io/cryptoexchange-discount/agentic-access/cryptoexchange-discount-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/cryptoexchange-discount-agentic-access.yml
- group: design
  href: https://artifacts.apis.io/cryptoexchange-discount/rules/cryptoexchange-discount-rules.yml
  title: ''
  type: Spectral
  url: rules/cryptoexchange-discount-rules.yml
- group: design
  href: https://artifacts.apis.io/cryptoexchange-discount/conformance/cryptoexchange-discount-conformance.yml
  title: ''
  type: Conformance
  url: conformance/cryptoexchange-discount-conformance.yml
- group: agent
  href: https://artifacts.apis.io/cryptoexchange-discount/llms/cryptoexchange-discount-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/cryptoexchange-discount-llms.txt
- group: build
  href: https://artifacts.apis.io/cryptoexchange-discount/mcp/cryptoexchange-discount-tool-crosswalk.yml
  title: ''
  type: ToolCrosswalk
  url: mcp/cryptoexchange-discount-tool-crosswalk.yml
- group: agent
  href: https://artifacts.apis.io/cryptoexchange-discount/mcp/cryptoexchange-discount-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/cryptoexchange-discount-mcp.yml
- group: agent
  href: https://artifacts.apis.io/cryptoexchange-discount/well-known/cryptoexchange-discount-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/cryptoexchange-discount-well-known.yml
- group: other
  href: https://artifacts.apis.io/cryptoexchange-discount/hosts/cryptoexchange-discount-hosts.yml
  title: ''
  type: Hosts
  url: hosts/cryptoexchange-discount-hosts.yml
- group: other
  href: https://artifacts.apis.io/cryptoexchange-discount/vendors/cryptoexchange-discount-vendors.yml
  title: ''
  type: Vendors
  url: vendors/cryptoexchange-discount-vendors.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://cryptoexchange.discount/terms-of-service
- group: start
  title: ''
  type: GettingStarted
  url: https://cryptoexchange.discount/blog/binance-copy-trading
- group: docs
  title: ''
  type: APIReference
  url: https://cryptoexchange.discount/.well-known/api-catalog
- group: auth
  href: https://artifacts.apis.io/cryptoexchange-discount/security/cryptoexchange-discount-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/cryptoexchange-discount-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://cryptoexchange.discount/
- group: docs
  title: ''
  type: Documentation
  url: https://cryptoexchange.discount/guides
- group: company
  title: ''
  type: Blog
  url: https://cryptoexchange.discount/blog
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://cryptoexchange.discount/privacy-policy
created: '2026-11-04'
description: Crypto Exchange Discount aggregates the best cryptocurrency exchange promo codes and referral bonuses, offering users up to 20% lifetime fee discounts on major platforms such as Binance, OKX, Kraken, Bybit and more. The site provides curated discount codes, detailed guides, and up-to-date offers for crypto traders seeking savings across multiple exchanges.
image: https://cryptoexchange.discount/og-image.jpg
layout: provider
mcp_servers:
- description: Remote MCP server at cryptoexchange.discount.
  name: Crypto Exchange Discount MCP Server
  slug: cryptoexchange-discount-mcp-yml
modified: '2026-11-04'
name: Crypto Exchange Discount
nav: Providers
network: true
overview: 'Crypto Exchange Discount is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Cryptocurrency, Discounts, Exchange, Referrals, and Promotions.


  The Crypto Exchange Discount catalog on APIs.io includes 1 Spectral governance ruleset.


  Crypto Exchange Discount''s developer surface includes getting-started guide, API reference, documentation, engineering blog, and 13 more developer resources.'
random_paper: 2
rules:
- authorship: generated
  effective_rule_count: 56
  extends:
  - spectral:oas
  name: Crypto Exchange Discount API Rules
  rule_count: 15
  severity_counts:
    error: 13
    hint: 0
    info: 1
    warn: 1
  slug: cryptoexchange-discount-rules
score:
  band: emerging
  composite: 21.1
  coverage:
    artifact_dirs: 11
    catalog_earned: 41.5
    catalog_earned_first_party: 0.0
    catalog_gap: 73.5
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 21.1
    contract_governance: 31.8
    contract_quality: 0.0
    developer_ergonomics: 31.0
    discoverability: 65.0
    operational_transparency: 0.0
  provenance:
    agentic_access: derived
    conformance: first-party
    mcp: first-party
  regulatory:
    applies: true
    jurisdictions:
    - jurisdiction: EU
      standard: gdpr
    - jurisdiction: US
      standard: ccpa
    jurisdictions_satisfied: 2
    matched_via: weak_tags
    regime: Securities & Market Data
    regime_id: securities_market_data
    score: 23.1
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Cryptoexchange Discount Domain Security
  slug: cryptoexchange-discount-domain-security
  summary_line: TLSv1.3 · HSTS
slug: cryptoexchange-discount
tags:
- Cryptocurrency
- Discounts
- Exchange
- Referrals
- Promotions
website: https://cryptoexchange.discount/
---
