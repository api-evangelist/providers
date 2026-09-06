---
access_model:
  confidence: medium
  label: Self-serve signup
  onboarding: self-serve
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
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 15.1
  scored_at: '2026-09-05'
api_count: 1
apis:
- description: Open-source NaCl-based cryptographic relay operated as asynchronous "dead drops" for end-to-end-encrypted device-to-device communication. Clients establish anonymous session keys via a proof-of-work h
  name: Vault12 Zax Cryptographic Relay API
  slug: vault12-zax-cryptographic-relay-api
artifact_total: 4
common:
- group: operate
  title: ''
  type: IssueTracker
  url: https://github.com/vault12/zax/issues
- group: operate
  title: ''
  type: Releases
  url: https://github.com/vault12/zax/releases
- group: docs
  title: ''
  type: ContributionGuide
  url: https://github.com/vault12/zax/blob/main/CONTRIBUTING.md
- group: commercial
  title: ''
  type: License
  url: https://github.com/vault12/zax/blob/main/LICENSE
- group: auth
  title: ''
  type: DomainSecurity
  url: security/vault12-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://vault12.com
- group: company
  title: ''
  type: Blog
  url: https://vault12.com/blog/
- group: operate
  title: ''
  type: Support
  url: https://vault12.com/help/
- group: commercial
  title: ''
  type: Pricing
  url: https://vault12.com/pricing/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://vault12.com/terms/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://vault12.com/privacy/
- group: operate
  title: ''
  type: StatusPage
  url: https://status.vault12.com/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/vault12
- group: build
  title: ''
  type: Packages
  url: packages/vault12-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/vault12-packages.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/vault12-well-known.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/vault12-scopes.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/vault12-authentication.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/vault12-conformance.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/vault12-llms.txt
- group: start
  title: ''
  type: Sandbox
  url: sandbox/vault12-sandbox.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/vault12-lifecycle.yml
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/vault12-changelog.yml
created: '2026-07-17'
description: Vault12 is a non-custodial crypto asset security company whose Vault12 Guard mobile app backs up wallet seed phrases and private keys using Shamir's Secret Sharing across a decentralized network of appointed Guardians, with designated legacy contacts for crypto inheritance — no cloud storage and no custody of funds. Its developer surface is open source, centered on the Zax NaCl-based cryptographic relay (asynchronous end-to-end-encrypted device-to-device messaging and file exchange), the glow.ts client library, and native Shamir's Secret Sharing implementations, plus RFC 8414 OAuth 2.0 authorization-server metadata published on vault12.com and a public Zax test relay at zt.vault12.com.
image: https://assets.rbl.ms/27528763/origin.png
layout: provider
modified: '2026-07-21'
name: Vault12
nav: Providers
network: true
overview: 'Vault12 publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Cryptocurrency, Security, Backup, and Inheritance.


  Vault12''s developer surface includes engineering blog, support, pricing, authentication, sandbox, changelog, and 17 more developer resources.'
random_paper: 4
scopes:
- name: Vault12 Scopes
  scope_count: 4
  slug: vault12-scopes
  summary_line: 4 scopes · authorizationCode/implicit/password/refresh_token
score:
  band: thin
  composite: 34.9
  coverage:
    artifact_dirs: 12
    catalog_earned: 37.0
    catalog_earned_first_party: 0.0
    catalog_gap: 78.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.9
  facets:
    access_clarity: 31.6
    commercial_clarity: 31.6
    contract_governance: 18.2
    contract_quality: 0.0
    developer_ergonomics: 50.0
    discoverability: 75.9
    governance: 18.2
    operational_transparency: 26.3
  open_source:
    applies: true
    score: 50.0
  previous_composite: 34.0
  provenance:
    conformance: first-party
  regulatory:
    applies: true
    matched_via: tags
    regime: Payments
    regime_id: payments
    score: 54.7
  schema_version: 0.18.3
  scored_at: '2026-09-05'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/vault12/refs/heads/main/screenshots/vault12-2026-09-02T165503.png
security:
- kind: authentication
  name: Vault12 Authentication
  slug: vault12-authentication
  summary_line: oauth2/session-handshake · 2 schemes
- kind: domain-security
  name: Vault12 Domain Security
  slug: vault12-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
slug: vault12
tags:
- Company
- Cryptocurrency
- Security
- Backup
- Inheritance
- Wallets
- Cryptography
- Secret Sharing
- Key Management
website: https://vault12.com
---
