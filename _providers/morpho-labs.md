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
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: documented
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 8.8
  scored_at: '2026-09-04'
api_count: 1
apis:
- description: Morpho's public GraphQL API providing real-time and historical onchain and offchain data across Morpho Blue markets, Morpho Vaults (V1 and V2), Midnight fixed-rate markets, user positions, curators, o
  name: Morpho API
  slug: morpho-api
artifact_total: 5
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/morpho-labs-domain-security.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/morpho-labs-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: Security
  url: https://docs.morpho.org/morpho/concepts/security/bug-bounty/
- group: company
  title: ''
  type: Website
  url: https://morpho.org/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://docs.morpho.org/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.morpho.org/
- group: docs
  title: ''
  type: APIReference
  url: https://docs.morpho.org/tools/offchain/api/morpho/
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.morpho.org/tools/offchain/api/get-started/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/morpho-org
- group: company
  title: ''
  type: Blog
  url: https://morpho.org/blog/category/101-content/
- group: operate
  title: ''
  type: Support
  url: https://morpho.org/faq/
- group: operate
  title: ''
  type: StatusPage
  url: https://status.morpho.org/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://morpho.org/terms-of-use/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://morpho.org/privacy-policy/
- group: build
  title: ''
  type: SDKs
  url: packages/morpho-labs-packages.yml
- group: build
  title: ''
  type: Packages
  url: packages/morpho-labs-packages.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/morpho-labs-llms.txt
- group: auth
  title: ''
  type: Authentication
  url: authentication/morpho-labs-authentication.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/morpho-labs-conventions.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/morpho-labs-rate-limits.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/morpho-labs-lifecycle.yml
- group: operate
  title: ''
  type: Deprecation
  url: lifecycle/morpho-labs-lifecycle.yml
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/morpho-labs-changelog.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/morpho-labs-problem-types.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/morpho-labs-conformance.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/morpho-labs-data-model.yml
- group: agent
  title: ''
  type: X-MCPServerCandidate
  url: mcp/morpho-labs-mcp.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
created: '2026-07-17'
description: Morpho Labs builds Morpho, an open, non-custodial onchain credit network for the Ethereum Virtual Machine. The protocol pairs Morpho Blue (a trustless, oracle-agnostic, permissionless lending primitive with isolated markets), Morpho Vaults (permissionless, curator-managed yield vaults that allocate deposits across markets), and Midnight (fixed-rate markets). For developers, Morpho publishes a public GraphQL API at api.morpho.org that indexes onchain and offchain data for markets, vaults, positions, curators, oracles, assets, rewards, and transactions, plus a suite of TypeScript SDKs for building and simulating transactions, and detailed documentation at docs.morpho.org.
image: https://evcop6xwrqrpqrf9.public.blob.vercel-storage.com/globals/morpho-thumbnail.1l1vc.png
layout: provider
modified: '2026-07-20'
name: Morpho Labs
nav: Providers
network: true
overview: 'Morpho Labs publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, DeFi, Lending, Blockchain, and Ethereum.


  Morpho Labs'' developer surface includes documentation, API reference, getting-started guide, engineering blog, support, authentication, changelog, and 21 more developer resources.'
random_paper: 11
rate_limits:
- limit_count: 2
  name: Morpho Labs Rate Limits
  slug: morpho-labs-rate-limits
score:
  band: thin
  composite: 33.8
  coverage:
    artifact_dirs: 17
    catalog_earned: 45.0
    catalog_earned_first_party: 8.0
    catalog_gap: 70.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 21.1
    commercial_clarity: 21.1
    contract_governance: 4.5
    contract_quality: 0.0
    developer_ergonomics: 69.6
    discoverability: 75.9
    governance: 4.5
    operational_transparency: 57.9
  previous_composite: 33.8
  provenance:
    conformance: derived
    mcp: derived
    skills: derived
  schema_version: 0.18.3
  scored_at: '2026-09-04'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/morpho-labs/refs/heads/main/screenshots/morpho-labs-2026-08-07T184313.png
security:
- kind: authentication
  name: Morpho Labs Authentication
  slug: morpho-labs-authentication
  summary_line: none · 0 schemes
- kind: domain-security
  name: Morpho Labs Domain Security
  slug: morpho-labs-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
- kind: vulnerability-disclosure
  name: Morpho Labs Vulnerability Disclosure
  slug: morpho-labs-vulnerability-disclosure
  summary_line: disclosure policy published
slug: morpho-labs
tags:
- Company
- DeFi
- Lending
- Blockchain
- Ethereum
- GraphQL
- On-Chain Data
- Financial-Services
- Web3
- Crypto
website: https://morpho.org/
---
