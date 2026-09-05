---
access_model:
  confidence: medium
  label: Open access
  onboarding: open
  pricing: unknown
  public: true
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
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: documented
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 21.0
  scored_at: '2026-09-04'
api_count: 1
apis:
- baseURL: https://quotes.eco.com
  baseurl_source: declared
  description: The Quotes V1 API from Eco — 2 operation(s) for quotes v1.
  name: Eco Quotes V1 API
  slug: eco-quotes-v1-api
- baseURL: https://quotes.eco.com
  baseurl_source: declared
  description: The Quotes V2 API from Eco — 4 operation(s) for quotes v2.
  name: Eco Quotes V2 API
  slug: eco-quotes-v2-api
- baseURL: https://quotes.eco.com
  baseurl_source: declared
  description: The Quotes V3 API from Eco — 9 operation(s) for quotes v3.
  name: Eco Quotes V3 API
  slug: eco-quotes-v3-api
artifact_total: 9
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Eco Routes Quotes V1 API
  slug: open-eco-quotes-v1-api
- collection_type: open
  name: Eco Routes Quotes V1 Quotes V2 API
  slug: open-eco-quotes-v2-api
- collection_type: open
  name: Eco Routes Quotes V1 Quotes V3 API
  slug: open-eco-quotes-v3-api
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/eco-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.eco.com/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://docs.eco.com
- group: docs
  title: ''
  type: Documentation
  url: https://docs.eco.com
- group: docs
  title: ''
  type: APIReference
  url: https://docs.eco.com/api-reference/introduction
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.eco.com/get-started/quickstart
- group: company
  title: ''
  type: Blog
  url: https://eco.com/blog
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/eco
- group: operate
  title: ''
  type: Support
  url: https://www.eco.com/contact
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.eco.com/tos
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.eco.com/privacy-policy
- group: build
  title: ''
  type: Packages
  url: packages/eco-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/eco-packages.yml
- group: build
  title: ''
  type: CLI
  url: cli/eco-cli.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/eco-llms.txt
- group: agent
  title: ''
  type: X-MCPServerCandidate
  url: mcp/eco-mcp.yml
- group: other
  title: ''
  type: Overlay
  url: overlays/eco-routes-overlay.yaml
- group: design
  title: ''
  type: Conformance
  url: conformance/eco-conformance.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/eco-problem-types.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/eco-lifecycle.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/eco-conventions.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/eco-data-model.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/eco-authentication.yml
- group: start
  title: ''
  type: Sandbox
  url: sandbox/eco-sandbox.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
created: '2026-07-17'
description: 'Eco is a developer platform for programmable stablecoin infrastructure — "The Stablecoin Network That Makes Money Programmable." It provides real-time, non-custodial cross-chain stablecoin routing, liquidity, and orchestration across onchain markets through four products: Routes (intent-based cross-chain transfers and swaps fulfilled by competing solvers in 20-40 seconds), Programmable Addresses (deterministic CREATE2 deposit/withdrawal addresses with pre-programmed routing, via Solana Deposit Addresses and Circle Gateway), Programmable Transactions (single-transaction multi-contract "Sauce" execution, beta), and Orchestration (a composition layer over Routes, transactions, and compliance, beta). The Routes REST API exposes quote, intent, and solver operations across V1/V2/V3, requiring no authentication (a dAppID is passed in the request body for attribution). Eco supports 16+ chains and 240+ directional pairs and is used by stablecoin issuers, wallets, exchanges, payment
  platforms, DeFi protocols, treasury managers, and AI agents.'
image: https://cdn.prod.website-files.com/67af51ad91d062ee8ef52137/69c2cc38e52fc86cca6c5320_Stablecoin%20Economy%20OG%20(5)%20(1).jpg
layout: provider
modified: '2026-07-19'
name: Eco
nav: Providers
network: true
overview: 'Eco publishes 3 APIs on the [APIs.io](https://apis.io/) network: Quotes V1 API, Quotes V2 API, and Quotes V3 API. Tagged areas include Company, Stablecoins, Cryptocurrency, Payments, and Blockchain.


  Eco''s developer surface includes documentation, API reference, getting-started guide, engineering blog, support, CLI, authentication, and 18 more developer resources.'
random_paper: 17
score:
  band: developing
  composite: 40.5
  coverage:
    artifact_dirs: 19
    catalog_earned: 37.0
    catalog_earned_first_party: 0.0
    catalog_gap: 78.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 21.1
    commercial_clarity: 21.1
    contract_governance: 4.5
    contract_quality: 43.1
    developer_ergonomics: 80.4
    discoverability: 75.9
    governance: 4.5
    operational_transparency: 2.6
  previous_composite: 40.5
  provenance:
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 3
    mcp: derived
    skills: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Payments
    regime_id: payments
    score: 39.1
  schema_version: 0.18.3
  scored_at: '2026-09-04'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/eco/refs/heads/main/screenshots/eco-2026-07-25T212742.png
security:
- kind: authentication
  name: Eco Authentication
  slug: eco-authentication
  summary_line: none · 0 schemes
- kind: domain-security
  name: Eco Domain Security
  slug: eco-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: eco
tags:
- Company
- Stablecoins
- Cryptocurrency
- Payments
- Blockchain
- Cross-Chain
- DeFi
- Web3
- Infrastructure
- Financial-Services
website: https://www.eco.com/
---
