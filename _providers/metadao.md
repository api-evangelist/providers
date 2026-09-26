---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source:
  - authentication
  trial: false
  try_now: false
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: false
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: na
    dynamic_client_registration: false
    error_semantics: documented
    event_surface_described: false
    idempotency: na
    mcp_server: false
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: na
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 25.2
  scored_at: '2026-09-25'
api_count: 4
apis:
- baseURL: https://market-api.metadao.fi
  baseurl_source: declared
  description: API information and health
  name: MetaDAO Meta API
  slug: metadao-meta-api
- baseURL: https://market-api.metadao.fi
  baseurl_source: declared
  description: Token supply breakdown and allocation
  name: MetaDAO Supply API
  slug: metadao-supply-api
- baseURL: https://market-api.metadao.fi
  baseurl_source: declared
  description: DAO trading pairs, pricing, and volume
  name: MetaDAO Tickers API
  slug: metadao-tickers-api
- baseURL: https://market-api.metadao.fi
  baseurl_source: declared
  description: Aggregate trading volume
  name: MetaDAO Volume API
  slug: metadao-volume-api
artifact_total: 12
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: MetaDAO Futarchy DEX Meta API
  slug: open-metadao-meta-api
- collection_type: open
  name: MetaDAO Futarchy DEX Meta Supply API
  slug: open-metadao-supply-api
- collection_type: open
  name: MetaDAO Futarchy DEX Meta Tickers API
  slug: open-metadao-tickers-api
- collection_type: open
  name: MetaDAO Futarchy DEX Meta Volume API
  slug: open-metadao-volume-api
common:
- group: company
  title: ''
  type: Website
  url: https://metadao.fi
- group: start
  title: ''
  type: DeveloperPortal
  url: https://api-docs.metadao.fi/introduction
- group: docs
  title: ''
  type: Documentation
  url: https://api-docs.metadao.fi/introduction
- group: docs
  title: ''
  type: APIReference
  url: https://api-docs.metadao.fi/api-reference/overview
- group: start
  title: ''
  type: GettingStarted
  url: https://api-docs.metadao.fi/quickstart
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/metaDAOproject
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/metadao/refs/heads/main/authentication/metadao-authentication.yml
  title: ''
  type: Authentication
  url: authentication/metadao-authentication.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/metadao/refs/heads/main/errors/metadao-error-codes.yml
  title: ''
  type: ErrorCatalog
  url: errors/metadao-error-codes.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/metadao/refs/heads/main/lifecycle/metadao-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/metadao-lifecycle.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/metadao/refs/heads/main/conventions/metadao-conventions.yml
  title: ''
  type: Conventions
  url: conventions/metadao-conventions.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/metadao/refs/heads/main/conformance/metadao-conformance.yml
  title: ''
  type: Conformance
  url: conformance/metadao-conformance.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/metadao/refs/heads/main/security/metadao-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/metadao-domain-security.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/metadao/refs/heads/main/data-model/metadao-data-model.yml
  title: ''
  type: DataModel
  url: data-model/metadao-data-model.yml
- group: operate
  href: https://raw.githubusercontent.com/api-evangelist/metadao/refs/heads/main/rate-limits/metadao-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/metadao-rate-limits.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/metadao/refs/heads/main/mcp/metadao-mcp.yml
  title: ''
  type: X-MCPServerCandidate
  url: mcp/metadao-mcp.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/metadao/refs/heads/main/skills/metadao-market-data.md
  title: ''
  type: AgentSkill
  url: skills/metadao-market-data.md
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/metadao/refs/heads/main/skills/metadao-token-supply.md
  title: ''
  type: AgentSkill
  url: skills/metadao-token-supply.md
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/metadao/refs/heads/main/llms/metadao-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/metadao-llms.txt
created: '2026-07-17'
description: MetaDAO is a fundraising and governance platform for high-quality founders and their communities, built on the Solana Futarchy protocol. It runs early fair token launches (high-float ICOs) and market-driven ("futarchy") governance where decision markets control treasury and intellectual property, with performance-aligned insider token unlocks. For developers, MetaDAO operates the public Futarchy DEX API — a CoinGecko-compatible, read-only market-data API at market-api.metadao.fi that automatically discovers every DAO on the protocol and exposes real-time pricing, trading volume, liquidity, and token supply. Surfaced as a Paradigm portfolio company and enriched by the API Evangelist pipeline from MetaDAO's own published documentation.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/metadao.png
layout: provider
modified: '2026-07-20'
name: MetaDAO
nav: Providers
network: true
overview: 'MetaDAO publishes 4 APIs on the [APIs.io](https://apis.io/) network, including Meta API, Supply API, Tickers API, and 1 more. Tagged areas include Company, Crypto Tools, DeFi, Solana, and DEX.


  MetaDAO''s developer surface includes documentation, API reference, getting-started guide, authentication, and 14 more developer resources.'
random_paper: 5
rate_limits:
- limit_count: 1
  name: Metadao Rate Limits
  slug: metadao-rate-limits
score:
  band: thin
  composite: 33.7
  coverage:
    artifact_dirs: 15
    catalog_earned: 48.0
    catalog_earned_first_party: 8.0
    catalog_gap: 67.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -1.3
  facets:
    access_clarity: 0.0
    contract_governance: 18.2
    contract_quality: 44.1
    developer_ergonomics: 51.8
    discoverability: 78.6
    operational_transparency: 23.7
  previous_composite: 35.0
  provenance:
    conformance: first-party
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 5
    mcp: derived
    skills: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Securities & Market Data
    regime_id: securities_market_data
    score: 15.7
  schema_version: 0.23.0
  scored_at: '2026-09-25'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: this provider''s published contracts declare no write operations, and a read-only API cannot create-or-update. Excluded from the denominator, not zeroed.'
    reason: read_only
screenshot: https://raw.githubusercontent.com/api-evangelist/metadao/refs/heads/main/screenshots/metadao-2026-08-07T172641.png
security:
- kind: authentication
  name: Metadao Authentication
  slug: metadao-authentication
  summary_line: none · 0 schemes
- kind: domain-security
  name: Metadao Domain Security
  slug: metadao-domain-security
  summary_line: DNSSEC · DMARC
slug: metadao
tags:
- Company
- Crypto Tools
- DeFi
- Solana
- DEX
- Governance
- Market Data
- Futarchy
website: https://metadao.fi
---
