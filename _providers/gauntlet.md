---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source:
  - authentication
  - rate-limits
  - security
  trial: false
  try_now: false
agent_readiness:
  band: agent-ready
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
    error_semantics: verified
    event_surface_described: false
    idempotency: na
    mcp_server: false
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: na
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 30.6
  scored_at: '2026-09-05'
agentic_access:
- acting_count: 0
  human_in_the_loop: 0
  name: Gauntlet Agentic Access
  operation_count: 14
  slug: gauntlet-agentic-access
  summary_line: 14 operations
api_count: 1
apis:
- baseURL: https://api.gauntlet.xyz
  baseurl_source: declared
  description: The Prices API from Gauntlet — 2 operation(s) for prices.
  name: Gauntlet Prices API
  slug: gauntlet-prices-api
- baseURL: https://api.gauntlet.xyz
  baseurl_source: declared
  description: The System API from Gauntlet — 2 operation(s) for system.
  name: Gauntlet System API
  slug: gauntlet-system-api
- baseURL: https://api.gauntlet.xyz
  baseurl_source: declared
  description: The TVL API from Gauntlet — 1 operation(s) for tvl.
  name: Gauntlet TVL API
  slug: gauntlet-tvl-api
- baseURL: https://api.gauntlet.xyz
  baseurl_source: declared
  description: The Users API from Gauntlet — 4 operation(s) for users.
  name: Gauntlet Users API
  slug: gauntlet-users-api
- baseURL: https://api.gauntlet.xyz
  baseurl_source: declared
  description: The Vaults API from Gauntlet — 5 operation(s) for vaults.
  name: Gauntlet Vaults API
  slug: gauntlet-vaults-api
artifact_total: 16
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Gauntlet Prices API
  slug: open-gauntlet-prices-api
- collection_type: open
  name: Gauntlet Prices System API
  slug: open-gauntlet-system-api
- collection_type: open
  name: Gauntlet Prices TVL API
  slug: open-gauntlet-tvl-api
- collection_type: open
  name: Gauntlet Prices Users API
  slug: open-gauntlet-users-api
- collection_type: open
  name: Gauntlet Prices Vaults API
  slug: open-gauntlet-vaults-api
common:
- group: other
  title: ''
  type: Overlay
  url: overlays/gauntlet-openapi-overlay.yaml
- group: company
  title: ''
  type: Website
  url: https://www.gauntlet.xyz
- group: start
  title: ''
  type: DeveloperPortal
  url: https://docs.gauntlet.xyz/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.gauntlet.xyz/
- group: docs
  title: ''
  type: APIReference
  url: https://docs.gauntlet.xyz/api-reference/vaults/list-gauntlet-curated-vaults
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.gauntlet.xyz/onboarding/quickstart
- group: start
  title: ''
  type: Quickstart
  url: https://docs.gauntlet.xyz/onboarding/quickstart
- group: start
  title: ''
  type: SignUp
  url: https://docs.gauntlet.xyz/onboarding/sign-up
- group: operate
  title: ''
  type: Support
  url: https://docs.gauntlet.xyz/onboarding/support
- group: company
  title: ''
  type: Blog
  url: https://www.gauntlet.xyz/resources
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/Gauntlet-xyz
- group: operate
  title: ''
  type: StatusPage
  url: https://status.gauntlet.xyz
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.gauntlet.xyz/tos
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.gauntlet.xyz/privacy-policy
- group: build
  title: ''
  type: Packages
  url: packages/gauntlet-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/gauntlet-packages.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/gauntlet-authentication.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/gauntlet-rate-limits.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/gauntlet-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/gauntlet-problem-types.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/gauntlet-lifecycle.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/gauntlet-conformance.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/gauntlet-data-model.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/gauntlet-llms.txt
- group: agent
  title: ''
  type: X-MCPServerCandidate
  url: mcp/gauntlet-mcp.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/gauntlet-agentic-access.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/gauntlet-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: Security
  url: https://docs.gauntlet.xyz/guides/concepts/security
- group: auth
  title: ''
  type: DomainSecurity
  url: security/gauntlet-domain-security.yml
created: '2026-07-17'
description: 'Gauntlet (Gauntlet Networks, Inc.) is a crypto risk-management and yield-curation firm that runs agent-based economic simulations to optimize risk, incentives, and capital efficiency for DeFi protocols, and curates 80+ institutional-grade yield vaults across Aera, Morpho, Kamino, Drift, and Symbiotic. For developers it ships the Gauntlet Developer Kit: a public read-only REST API at api.gauntlet.xyz (v1) exposing vault metrics, user positions with PnL, wallet activity, TVL, and token prices, plus an official TypeScript SDK (@gauntlet-xyz/sdk) for on-chain deposits, withdrawals, and ERC-8021 attribution. Authentication is a partner-provisioned Bearer API key. Backed by Paradigm, Polychain, and Ribbit Capital.'
image: https://cdn.prod.website-files.com/648bdc0d4b8ce322f27da0af/68013f075b92cb9c2d2c6aef_gauntlet-thumbnail.png
layout: provider
modified: '2026-07-19'
name: Gauntlet
nav: Providers
network: true
overview: 'Gauntlet publishes 5 APIs on the [APIs.io](https://apis.io/) network, including Prices API, System API, TVL API, and 2 more. Tagged areas include Company, Crypto Data, DeFi, Risk Management, and Yield.


  Gauntlet''s developer surface includes documentation, API reference, getting-started guide, quickstart, signup flow, support, engineering blog, and 23 more developer resources.'
random_paper: 7
rate_limits:
- limit_count: 2
  name: Gauntlet Rate Limits
  slug: gauntlet-rate-limits
score:
  band: developing
  composite: 48.1
  coverage:
    artifact_dirs: 19
    catalog_earned: 45.0
    catalog_earned_first_party: 8.0
    catalog_gap: 70.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 34.2
    commercial_clarity: 34.2
    contract_governance: 4.5
    contract_quality: 53.5
    developer_ergonomics: 66.1
    discoverability: 75.9
    governance: 4.5
    operational_transparency: 50.0
  previous_composite: 48.1
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 5
    mcp: derived
    skills: derived
  schema_version: 0.18.3
  scored_at: '2026-09-05'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/gauntlet/refs/heads/main/screenshots/gauntlet-2026-07-25T215504.png
security:
- kind: authentication
  name: Gauntlet Authentication
  slug: gauntlet-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Gauntlet Domain Security
  slug: gauntlet-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
- kind: vulnerability-disclosure
  name: Gauntlet Vulnerability Disclosure
  slug: gauntlet-vulnerability-disclosure
  summary_line: disclosure policy published
slug: gauntlet
tags:
- Company
- Crypto Data
- DeFi
- Risk Management
- Yield
- Vault
- Blockchain
- Web3
- Financial Modeling
website: https://www.gauntlet.xyz
---
