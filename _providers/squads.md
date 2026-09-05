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
  band: human-only
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    agentic_commerce: false
    auth_clarity: bearer
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
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 2.5
  scored_at: '2026-09-04'
api_count: 2
apis:
- description: TypeScript and Rust SDKs plus a CLI for creating and operating Squads multisigs (smart accounts) on Solana — creating multisigs, proposing, approving and executing transactions, and managing program-u
  name: Squads Multisig SDK
  slug: squads-multisig-sdk
- description: Grid is Squads' stablecoin API for accounts, payments, cards, and yield — letting developers build neobank-style fintech products on stablecoin rails with API-key authentication, multi-rail payouts (s
  name: Grid API
  slug: grid-api
artifact_total: 6
common:
- group: operate
  title: ''
  type: IssueTracker
  url: https://github.com/Squads-Protocol/v4/issues
- group: auth
  title: ''
  type: SecurityPolicy
  url: https://github.com/Squads-Protocol/v4/blob/main/SECURITY.md
- group: commercial
  title: ''
  type: License
  url: https://github.com/Squads-Protocol/v4/blob/main/LICENSE
- group: auth
  title: ''
  type: TrustCenter
  url: security/squads-trust-center.yml
- group: auth
  title: ''
  type: Compliance
  url: https://trust.squads.xyz/
- group: company
  title: ''
  type: Website
  url: https://squads.xyz/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://docs.squads.so/main
- group: docs
  title: ''
  type: Documentation
  url: https://docs.squads.so/main
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.squads.so/main/getting-started/quickstart-guide
- group: docs
  title: ''
  type: APIReference
  url: https://docs.squads.so/main/development
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/Squads-Protocol
- group: company
  title: ''
  type: Blog
  url: https://squads.xyz/blog
- group: commercial
  title: ''
  type: Pricing
  url: https://docs.squads.so/main/getting-started/pricing
- group: start
  title: ''
  type: SignUp
  url: https://grid.squads.xyz/welcome
- group: commercial
  title: ''
  type: TermsOfService
  url: https://squads.xyz/legal/terms-of-service
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://squads.xyz/legal/privacy-policy
- group: operate
  title: ''
  type: Support
  url: https://discord.com/invite/squadsprotocol
- group: build
  title: ''
  type: Packages
  url: packages/squads-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/squads-packages.yml
- group: build
  title: ''
  type: CLI
  url: cli/squads-cli.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/squads-llms.txt
- group: auth
  title: ''
  type: Authentication
  url: authentication/squads-authentication.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/squads-lifecycle.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/squads-conformance.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/squads-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: Security
  url: https://docs.squads.so/main/security/bug-bounty.md
- group: auth
  title: ''
  type: DomainSecurity
  url: security/squads-domain-security.yml
created: '2026-07-17'
description: Squads Labs builds smart-account and stablecoin infrastructure on Solana. Its flagship Squads Protocol is an open-source, formally-verified, immutable multisig program (v3 and v4) that secures over $10 billion in on-chain assets for 350+ teams, exposed to developers through the @sqds/multisig TypeScript SDK, a Rust crate, and the @sqds/cli command-line tool. Squads also operates Grid, a stablecoin API for accounts, payments, cards, and yield that lets fintech developers build neobank-style products on stablecoin rails with sub-second settlement. This profile was seeded as a VC-portfolio lead and enriched by the API Evangelist pipeline from Squads' public developer surface.
image: https://avatars.githubusercontent.com/u/84348534
layout: provider
modified: '2026-07-21'
name: Squads
nav: Providers
network: true
overview: 'Squads publishes 2 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Infrastructure, Blockchain, Solana, and Multisig.


  Squads'' developer surface includes documentation, getting-started guide, API reference, engineering blog, pricing, signup flow, support, and 20 more developer resources.'
random_paper: 6
score:
  band: developing
  composite: 41.2
  coverage:
    artifact_dirs: 10
    catalog_earned: 37.0
    catalog_earned_first_party: 0.0
    catalog_gap: 78.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 60.5
    commercial_clarity: 60.5
    contract_governance: 18.2
    contract_quality: 0.0
    developer_ergonomics: 71.4
    discoverability: 75.9
    governance: 18.2
    operational_transparency: 13.2
  open_source:
    applies: true
    score: 35.0
  previous_composite: 41.2
  provenance:
    conformance: first-party
  regulatory:
    applies: true
    matched_via: tags
    regime: Payments
    regime_id: payments
    score: 56.3
  schema_version: 0.18.3
  scored_at: '2026-09-04'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/squads/refs/heads/main/screenshots/squads-2026-09-02T160642.png
security:
- kind: authentication
  name: Squads Authentication
  slug: squads-authentication
  summary_line: apiKey/wallet-signature · 0 schemes
- kind: domain-security
  name: Squads Domain Security
  slug: squads-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Squads Vulnerability Disclosure
  slug: squads-vulnerability-disclosure
  summary_line: contact published
- kind: trust-center
  name: Squads Trust Center
  slug: squads-trust-center
  summary_line: SOC 2, ISO 27001
slug: squads
tags:
- Company
- Infrastructure
- Blockchain
- Solana
- Multisig
- Smart Accounts
- Stablecoins
- Payments
- Wallets
- Web3
website: https://squads.xyz/
---
