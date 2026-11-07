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
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: na
    dynamic_client_registration: false
    error_semantics: false
    event_surface_described: false
    idempotency: na
    mcp_server: verified
    mcp_tool_quality: half
    openapi_examples: false
    operation_distinctiveness: distinct
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: derived
    reversibility_documented: na
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 31.3
  scored_at: '2026-11-06'
api_count: 1
apis:
- description: Free, lower-rate-limit public API exposing basic account, transaction, and token endpoints used by the Solscan UI.
  name: Solscan Public API
  slug: public-api
- description: Commercial Pro API with full account, transaction, token, NFT, DeFi, and analytics endpoints. Higher rate limits, decoded events, and historical depth. Authentication via token header.
  name: Solscan Pro API
  slug: pro-api
- baseURL: https://public-api.solscan.io
  baseurl_source: declared
  description: Solana account data
  name: Solscan Account API
  slug: solscan-account-api
- baseURL: https://public-api.solscan.io
  baseurl_source: declared
  description: Block lookups
  name: Solscan Block API
  slug: solscan-block-api
- baseURL: https://public-api.solscan.io
  baseurl_source: declared
  description: NFT collection data
  name: Solscan NFT API
  slug: solscan-nft-api
- baseURL: https://public-api.solscan.io
  baseurl_source: declared
  description: SPL token data
  name: Solscan Token API
  slug: solscan-token-api
- baseURL: https://public-api.solscan.io
  baseurl_source: declared
  description: Transaction lookups
  name: Solscan Transaction API
  slug: solscan-transaction-api
artifact_total: 18
collections:
- collection_type: open
  name: Solscan Pro Account API
  slug: open-solscan-account-api
- collection_type: open
  name: Solscan Pro Block API
  slug: open-solscan-block-api
- collection_type: open
  name: Solscan Pro NFT API
  slug: open-solscan-nft-api
- collection_type: open
  name: Solscan Pro Token API
  slug: open-solscan-token-api
- collection_type: open
  name: Solscan Pro Transaction API
  slug: open-solscan-transaction-api
common:
- group: company
  title: ''
  type: Website
  url: https://solscan.io
- group: auth
  href: https://artifacts.apis.io/solscan/security/solscan-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/solscan-domain-security.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/solscanofficial
- group: start
  title: ''
  type: Portal
  url: https://solscan.io/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.solscan.io/
- group: commercial
  title: ''
  type: Pricing
  url: https://solscan.io/apis
- group: commercial
  href: https://artifacts.apis.io/solscan/plans/solscan-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/solscan-plans-pricing.yml
- group: operate
  href: https://artifacts.apis.io/solscan/rate-limits/solscan-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/solscan-rate-limits.yml
- group: commercial
  href: https://artifacts.apis.io/solscan/finops/solscan-finops.yml
  title: ''
  type: FinOps
  url: finops/solscan-finops.yml
- group: agent
  title: ''
  type: LlmsText
  url: https://docs.solscan.io/llms.txt
created: '2026-05-08'
description: Solscan is a leading Solana block explorer with a Public API (free, basic) and a Pro API (paid, with full account, transaction, token, NFT, and DeFi endpoints). The Pro API serves decoded on-chain data and is the primary commercial product. Authentication uses a token (Bearer or query parameter) and is required for all Pro endpoints.
finops:
- has_sources: true
  method: generated
  name: Solscan Finops
  primary_unit: ''
  service_category: Crypto Explorer
  slug: solscan-finops
  template: false
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/solscan.png
layout: provider
mcp_servers:
- description: Remote MCP server at mcp.solscan.io over HTTP; 55 tools listed.
  name: Solscan MCP Server
  slug: solscan
modified: '2026-09-16'
name: Solscan
nav: Providers
network: true
overview: 'Solscan publishes 7 API contracts indexed on the [APIs.io](https://apis.io/) network, including Account API, Block API, NFT API, and 4 more. Tagged areas include Web3, Solana, Explorer, Onchain, and Tokens.


  The Solscan catalog on APIs.io includes 1 Spectral governance ruleset.


  Solscan''s developer surface includes developer portal, documentation, pricing, and 7 more developer resources.'
plans:
- name: Solscan Plans Pricing
  plan_count: 5
  slug: solscan-plans-pricing
random_paper: 11
rate_limits:
- limit_count: 5
  name: Solscan Rate Limits
  slug: solscan-rate-limits
rules:
- authorship: generated
  effective_rule_count: 91
  extends:
  - spectral:oas
  name: Solscan API Rules
  rule_count: 50
  severity_counts:
    error: 47
    hint: 0
    info: 1
    warn: 2
  slug: solscan-rules
score:
  band: thin
  composite: 27.9
  coverage:
    artifact_dirs: 14
    catalog_earned: 47.5
    catalog_earned_first_party: 0.0
    catalog_gap: 67.5
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 18.4
    contract_governance: 13.6
    contract_quality: 45.3
    developer_ergonomics: 19.0
    discoverability: 75.0
    operational_transparency: 10.5
  previous_composite: 27.9
  provenance:
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 5
    mcp: first-party
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 5.9
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: this provider''s published contracts declare no write operations, and a read-only API cannot create-or-update. Excluded from the denominator, not zeroed.'
    reason: read_only
screenshot: https://apis.io/screenshots/solscan/solscan-2026-06-20T194154.png
security:
- kind: domain-security
  name: Solscan Domain Security
  slug: solscan-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
slug: solscan
tags:
- Web3
- Solana
- Explorer
- Onchain
- Tokens
- NFT
website: https://solscan.io
---
