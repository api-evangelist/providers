---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source: []
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
    mcp_server: false
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 12.9
  scored_at: '2026-09-04'
api_count: 1
apis:
- description: GraphQL API for querying Compound Finance v2 protocol data via The Graph subgraph, including markets, accounts, borrows, repays, liquidations, and token transfers.
  name: Compound Finance GraphQL API
  slug: compound-finance-graphql-api
artifact_total: 4
common:
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/compound-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/compound-domain-security.yml
created: '2026-06-14'
description: Compound is a decentralized, blockchain-based protocol that allows users to lend and borrow cryptocurrencies (DeFi lending protocol) built on Ethereum.
graphqls:
- description: Compound Finance is a decentralized, blockchain-based DeFi lending protocol built on Ethereum. It allows users to supply assets to earn interest or borrow assets against supplied collateral. The proto
  name: Compound Finance GraphQL API
  slug: compound-graphql
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/compound.png
layout: provider
modified: '2026-06-14'
name: Compound Finance
nav: Providers
network: true
overview: Compound Finance publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include DeFi, Lending, Borrowing, Ethereum, and Blockchain.
random_paper: 8
score:
  band: emerging
  composite: 17.6
  coverage:
    artifact_dirs: 3
    catalog_earned: 32.0
    catalog_earned_first_party: 0.0
    catalog_gap: 83.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 0.0
    commercial_clarity: 0.0
    contract_governance: 0.0
    contract_quality: 36.2
    developer_ergonomics: 9.5
    discoverability: 59.3
    governance: 0.0
    operational_transparency: 5.3
  previous_composite: 17.6
  schema_version: 0.18.3
  scored_at: '2026-09-04'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/compound/refs/heads/main/screenshots/compound-2026-06-20T174841.png
security:
- kind: domain-security
  name: Compound Domain Security
  slug: compound-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
- kind: vulnerability-disclosure
  name: Compound Vulnerability Disclosure
  slug: compound-vulnerability-disclosure
  summary_line: disclosure policy published
slug: compound
tags:
- DeFi
- Lending
- Borrowing
- Ethereum
- Blockchain
- Finance
- Cryptocurrency
---
