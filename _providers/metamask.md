---
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    agentic_commerce: false
    auth_clarity: served
    consent_identity: false
    delegated_identity: served
    dry_run_mode: false
    dynamic_client_registration: true
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
  schema_version: '0.2'
  score: 28.1
  scored_at: '2026-10-17'
api_count: 1
apis:
- description: The Token API from MetaMask — 1 operation(s) for token.
  name: MetaMask Token API
  slug: metamask-token-api
artifact_total: 4
common:
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/metamask/refs/heads/main/rules/metamask-rules.yml
  title: ''
  type: Spectral
  url: rules/metamask-rules.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/metamask/refs/heads/main/cli/metamask-cli.yml
  title: ''
  type: CLI
  url: cli/metamask-cli.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/metamask/refs/heads/main/conformance/metamask-conformance.yml
  title: ''
  type: Conformance
  url: conformance/metamask-conformance.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/metamask/refs/heads/main/llms/metamask-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/metamask-llms.txt
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/metamask/refs/heads/main/well-known/metamask-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/metamask-security.txt
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/metamask/refs/heads/main/well-known/metamask-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/metamask-well-known.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/metamask/refs/heads/main/hosts/metamask-hosts.yml
  title: ''
  type: Hosts
  url: hosts/metamask-hosts.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/metamask/refs/heads/main/vendors/metamask-vendors.yml
  title: ''
  type: Vendors
  url: vendors/metamask-vendors.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/metamask/refs/heads/main/packages/metamask-packages.yml
  title: ''
  type: SDKs
  url: packages/metamask-packages.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/metamask/refs/heads/main/packages/metamask-packages.yml
  title: ''
  type: Packages
  url: packages/metamask-packages.yml
- group: auth
  title: ''
  type: Security
  url: https://metamask.io/security
- group: company
  title: ''
  type: Newsroom
  url: https://metamask.io/news/how-to-buy-crypto
- group: operate
  title: ''
  type: ChangeLog
  url: https://github.com/MetaMask/snaps/releases
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/metamask/refs/heads/main/security/metamask-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/metamask-vulnerability-disclosure.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/metamask/refs/heads/main/security/metamask-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/metamask-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://metamask.io
- group: start
  title: ''
  type: DeveloperPortal
  url: https://metamask.io/developer
- group: docs
  title: ''
  type: Documentation
  url: https://docs.metamask.io
- group: docs
  title: ''
  type: APIReference
  url: https://docs.metamask.io
- group: start
  title: ''
  type: GettingStarted
  url: https://metamask.io/download
- group: operate
  title: ''
  type: Support
  url: https://support.metamask.io/
- group: company
  title: ''
  type: Blog
  url: https://metamask.io/news
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/MetaMask
- group: commercial
  title: ''
  type: TermsOfService
  url: https://metamask.io/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://metamask.io/privacy
- group: build
  title: ''
  type: Postman
  url: https://www.postman.com/metamask/workspace
coverage:
  checked: '2026-10-13'
  detail: Docs at https://docs.metamask.io render via JavaScript and provide no machine‑readable spec.
  evidence:
  - status: 200
    url: https://docs.metamask.io/
  reason: js-rendered-docs
  state: unreadable
created: '2026-10-13'
description: MetaMask is a leading self‑custodial cryptocurrency wallet and Web3 gateway. It enables users to manage crypto assets, interact with decentralized applications, and access a suite of developer tools such as SDKs, embedded wallets, smart accounts, and Snaps. The platform supports multiple blockchains including Ethereum, Solana, and Bitcoin, offering features like token swaps, perps trading, and on‑chain governance.
image: https://images.ctfassets.net/clixtyxoaeas/7Bth2z7E82BB90X6C3YG7m/7ddf5caae232ce3827e19eb2de646fa5/metamask-website-homepage.jpg
layout: provider
modified: '2026-10-13'
name: MetaMask
nav: Providers
network: true
overview: 'MetaMask is listed with 1 API on the [APIs.io](https://apis.io/) network: Token API. Tagged areas include Company, Cryptocurrency, Wallets, Web3, and Developer Tools.


  The MetaMask catalog on APIs.io includes 1 Spectral governance ruleset.


  MetaMask''s developer surface includes CLI, changelog, documentation, API reference, getting-started guide, support, engineering blog, and 19 more developer resources.'
random_paper: 15
rules:
- authorship: generated
  effective_rule_count: 50
  extends:
  - spectral:oas
  name: MetaMask API Rules
  rule_count: 9
  severity_counts:
    error: 7
    hint: 0
    info: 1
    warn: 1
  slug: metamask-rules
score:
  band: thin
  composite: 32.9
  coverage:
    artifact_dirs: 12
    catalog_earned: 36.5
    catalog_earned_first_party: 0.0
    catalog_gap: 78.5
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 21.1
    contract_governance: 18.2
    contract_quality: 9.4
    developer_ergonomics: 64.3
    discoverability: 66.1
    operational_transparency: 31.6
  provenance:
    conformance: derived
    contracts:
      callable: 0.0
      derived: 2
      marker_coverage: 100.0
      total: 2
    mcp: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Payments
    regime_id: payments
    score: 27.7
  schema_version: 0.24.0
  scored_at: '2026-10-17'
  upsert:
    applies: true
    score: 0.0
security:
- kind: domain-security
  name: Metamask Domain Security
  slug: metamask-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
- kind: vulnerability-disclosure
  name: Metamask Vulnerability Disclosure
  slug: metamask-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: metamask
tags:
- Company
- Cryptocurrency
- Wallets
- Web3
- Developer Tools
website: https://metamask.io
---
