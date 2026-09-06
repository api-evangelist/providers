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
  scored_at: '2026-09-05'
api_count: 0
artifact_total: 2
common:
- group: company
  title: ''
  type: Website
  url: https://www.certora.com/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://docs.certora.com/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.certora.com/en/latest/
- group: docs
  title: ''
  type: APIReference
  url: https://docs.certora.com/en/latest/docs/prover/cli/index.html
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.certora.com/en/latest/docs/user-guide/install.html
- group: company
  title: ''
  type: Blog
  url: https://www.certora.com/blog
- group: commercial
  title: ''
  type: Pricing
  url: https://www.certora.com/pricing
- group: start
  title: ''
  type: SignUp
  url: https://prover.certora.com/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.certora.com/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.certora.com/privacy
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/Certora
- group: build
  title: ''
  type: Packages
  url: packages/certora-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/certora-packages.yml
- group: build
  title: ''
  type: CLI
  url: cli/certora-cli.yml
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/certora-changelog.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/certora-authentication.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/certora-lifecycle.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/certora-llms.txt
- group: auth
  title: ''
  type: DomainSecurity
  url: security/certora-domain-security.yml
created: '2026-07-17'
description: Certora is a smart-contract security company whose core product is the Certora Prover, a state-of-the-art automated formal-verification engine that checks every possible contract state and execution path to find critical vulnerabilities in smart contracts running on EVM-based chains, Solana, Stellar (Soroban), and Sui. Developers write rules in the Certora Verification Language (CVL) and submit verification jobs to Certora's cloud from the command line using the open-source certora-cli (certoraRun) tool, which authenticates with a personal access key. Alongside the Prover, Certora offers the Gambit mutation-testing tool, expert manual audits, and verification contests, and reports protecting over $100B in total value locked across major DeFi protocols. This profile was surfaced as an Electric Capital portfolio company and enriched by the API Evangelist pipeline.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/certora.png
layout: provider
modified: '2026-07-18'
name: Certora
nav: Providers
network: true
overview: 'Certora is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Security, Formal Verification, Smart Contracts, and Blockchain.


  Certora''s developer surface includes documentation, API reference, getting-started guide, engineering blog, pricing, signup flow, CLI, and 12 more developer resources.'
random_paper: 17
score:
  band: thin
  composite: 30.4
  coverage:
    artifact_dirs: 10
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 44.7
    commercial_clarity: 44.7
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 66.7
    discoverability: 57.4
    governance: 0.0
    operational_transparency: 18.4
  previous_composite: 30.4
  schema_version: 0.18.3
  scored_at: '2026-09-05'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/certora/refs/heads/main/screenshots/certora-2026-07-25T205007.png
security:
- kind: authentication
  name: Certora Authentication
  slug: certora-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Certora Domain Security
  slug: certora-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
slug: certora
tags:
- Company
- Security
- Formal Verification
- Smart Contracts
- Blockchain
- Developer Tools
- CLI
- Web3
website: https://www.certora.com/
---
