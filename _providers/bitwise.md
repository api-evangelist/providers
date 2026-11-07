---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source:
  - authentication
  - security
  trial: false
  try_now: false
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: na
    dynamic_client_registration: false
    error_semantics: derived
    event_surface_described: false
    idempotency: na
    mcp_server: false
    mcp_tool_quality: na
    openapi_examples: false
    operation_distinctiveness: distinct
    pagination_ratio: false
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: na
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 22.9
  scored_at: '2026-11-06'
agentic_access:
- acting_count: 0
  human_in_the_loop: 0
  name: Bitwise Agentic Access
  operation_count: 6
  slug: bitwise-agentic-access
  summary_line: 6 operations
api_count: 1
apis:
- baseURL: https://api.bitwiseinvestments.com
  baseurl_source: declared
  description: Per-fund market data (NAV, AUM, holdings, performance).
  name: Bitwise Funds API
  slug: bitwise-funds-api
- baseURL: https://api.bitwiseinvestments.com
  baseurl_source: declared
  description: Bitwise crypto index metadata, history, and constituents.
  name: Bitwise Indexes API
  slug: bitwise-indexes-api
- baseURL: https://api.bitwiseinvestments.com
  baseurl_source: declared
  description: Bitwise exchange-traded fund listings and details.
  name: Bitwise ET Fs API
  slug: bitwise-etfs-api
artifact_total: 12
collections:
- collection_type: open
  name: Bitwise ETFs API
  slug: open-bitwise-etfs-api
- collection_type: open
  name: Bitwise ETFs Funds API
  slug: open-bitwise-funds-api
- collection_type: open
  name: Bitwise ETFs Indexes API
  slug: open-bitwise-indexes-api
common:
- group: agent
  href: https://artifacts.apis.io/bitwise/mcp/bitwise-mcp.yml
  title: ''
  type: X-MCPServerCandidate
  url: mcp/bitwise-mcp.yml
- group: other
  href: https://artifacts.apis.io/bitwise/overlays/bitwise-openapi-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/bitwise-openapi-overlay.yaml
- group: agent
  href: https://artifacts.apis.io/bitwise/agentic-access/bitwise-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/bitwise-agentic-access.yml
- group: auth
  href: https://artifacts.apis.io/bitwise/security/bitwise-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/bitwise-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://bitwiseinvestments.com/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://developers.bitwiseinvestments.com/
- group: docs
  title: ''
  type: Documentation
  url: https://developers.bitwiseinvestments.com/
- group: docs
  title: ''
  type: APIReference
  url: https://developers.bitwiseinvestments.com/
- group: start
  title: ''
  type: GettingStarted
  url: https://developers.bitwiseinvestments.com/
- group: build
  title: ''
  type: Postman
  url: https://developers.bitwiseinvestments.com/
- group: operate
  title: ''
  type: Support
  url: mailto:api@bitwiseinvestments.com
- group: company
  title: ''
  type: Blog
  url: https://bitwiseinvestments.com/crypto-market-insights
- group: start
  title: ''
  type: SignUp
  url: https://experts.bitwiseinvestments.com/sign-up
- group: start
  title: ''
  type: Login
  url: https://app.bitwiseinvestments.com/investor-portal
- group: commercial
  title: ''
  type: TermsOfService
  url: https://bitwiseinvestments.com/terms-of-service
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://bitwiseinvestments.com/privacy-policy
- group: agent
  href: https://artifacts.apis.io/bitwise/llms/bitwise-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/bitwise-llms.txt
- group: agent
  href: https://artifacts.apis.io/bitwise/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
created: '2026-07-17'
description: Bitwise Asset Management is a crypto-focused investment manager (founded 2017, offices in San Francisco, New York, London, and Frankfurt) offering crypto index funds, ETFs, separately managed accounts, private funds, and staking products across 70+ vehicles including the Bitwise 10 Crypto Index (BITW) and spot Bitcoin (BITB) and Ethereum (ETHW) ETFs. Bitwise publishes a read-only market-data API for its indexes, ETFs, and fund data via a public Postman developer portal, covering index metadata, historical daily index values, index constituents (prices/supplies/weights), and per-fund data (NAV, AUM, holdings, crypto-per-share, performance). API keys are issued on request. This profile was enriched by the API Evangelist pipeline from the provider's public developer surface.
image: https://bitwiseinvestments.com/favicon.ico
layout: provider
modified: '2026-07-18'
name: Bitwise
nav: Providers
network: true
overview: 'Bitwise publishes 3 API contracts indexed on the [APIs.io](https://apis.io/) network: Funds API, Indexes API, and ET Fs API. Tagged areas include Company, Fintech, Cryptocurrency, Asset Management, and Market Data.


  The Bitwise catalog on APIs.io includes 1 Spectral governance ruleset.


  Bitwise''s developer surface includes documentation, API reference, getting-started guide, support, engineering blog, signup flow, and 12 more developer resources.'
random_paper: 15
rules:
- authorship: generated
  effective_rule_count: 105
  extends:
  - spectral:oas
  name: Bitwise API Rules
  rule_count: 64
  severity_counts:
    error: 62
    hint: 0
    info: 1
    warn: 1
  slug: bitwise-rules
score:
  band: thin
  composite: 33.0
  coverage:
    artifact_dirs: 22
    catalog_earned: 41.5
    catalog_earned_first_party: 0.0
    catalog_gap: 73.5
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 34.2
    contract_governance: 18.2
    contract_quality: 14.3
    developer_ergonomics: 63.7
    discoverability: 73.2
    operational_transparency: 0.0
  previous_composite: 33.0
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 3
      marker_coverage: 100.0
      total: 3
    mcp: derived
    skills: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Securities & Market Data
    regime_id: securities_market_data
    score: 23.1
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: this provider''s published contracts declare no write operations, and a read-only API cannot create-or-update. Excluded from the denominator, not zeroed.'
    reason: read_only
screenshot: https://apis.io/screenshots/bitwise/bitwise-2026-07-25T203218.png
security:
- kind: authentication
  name: Bitwise Authentication
  slug: bitwise-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Bitwise Domain Security
  slug: bitwise-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
skill_count: 2
skills:
- name: Look up Bitwise fund and ETF data
  slug: bitwise-fund-and-etf-data
- name: Pull a Bitwise index's value history and constituents
  slug: bitwise-index-analytics
slug: bitwise
tags:
- Company
- Fintech
- Cryptocurrency
- Asset Management
- Market Data
- Index Funds
- ETFs
- Financial Services
website: https://bitwiseinvestments.com/
---
