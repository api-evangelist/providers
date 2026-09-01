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
  scored_at: '2026-09-01'
api_count: 0
artifact_total: 2
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/violet-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.violet.co/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.violet.co
- group: start
  title: ''
  type: Portal
  url: https://app.violet.co
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.violet.co/general-introduction/getting-started
- group: docs
  title: ''
  type: APIReference
  url: https://docs.violet.co/integration-walkthrough/introduction
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/violetprotocol
- group: operate
  title: ''
  type: Support
  url: https://discord.com/invite/hRJpPQtKSh
- group: start
  title: ''
  type: SignUp
  url: https://app.violet.co
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.violet.co/terms-of-use
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.violet.co/privacy-notice
- group: build
  title: ''
  type: Packages
  url: packages/violet-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/violet-packages.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/violet-llms.txt
- group: design
  title: ''
  type: Conformance
  url: conformance/violet-conformance.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/violet-authentication.yml
created: '2026-07-17'
description: 'Violet Protocol provides privacy-preserving, reusable on-chain compliance and identity infrastructure for decentralized finance (DeFi). Its products — VioletID, Full AML/KYC screening, GeoFencing, and Sybil resistance — let crypto businesses meet regulatory requirements such as anti-money-laundering, sanctions screening, geo-blocking, accredited-investor verification, and proof of unique personhood. Integration is SDK and smart-contract based: Violet issues Ethereum Access Tokens (EATs) — OAuth 2.0-compliant, EIP-712-signed compliance assertions that carry no PII — and maintains the on-chain VioletID Registry that maps wallet addresses to verified compliance statuses, all built on W3C Decentralized Identifier and Verifiable Credential standards.'
image: https://www.violet.co/og-image.jpg
layout: provider
modified: '2026-07-21'
name: Violet
nav: Providers
network: true
overview: 'Violet is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Compliance, Identity, DeFi, and Blockchain.


  Violet''s developer surface includes documentation, developer portal, getting-started guide, API reference, support, signup flow, authentication, and 9 more developer resources.'
random_paper: 8
score:
  band: thin
  composite: 26.2
  coverage:
    artifact_dirs: 5
    catalog_gap: 88.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 27.6
    commercial_clarity: 27.6
    contract_governance: 18.2
    contract_quality: 0.0
    developer_ergonomics: 61.9
    discoverability: 57.4
    governance: 18.2
    operational_transparency: 2.6
  previous_composite: 26.2
  provenance:
    conformance: first-party
  schema_version: 0.17.2
  scored_at: '2026-09-01'
  trend: flat
security:
- kind: authentication
  name: Violet Authentication
  slug: violet-authentication
  summary_line: oauth2/onchain-registry · 2 schemes
- kind: domain-security
  name: Violet Domain Security
  slug: violet-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: violet
tags:
- Company
- Compliance
- Identity
- DeFi
- Blockchain
- KYC
- AML
- Web3
- Decentralized Identity
- Sanctions Screening
- Authentication
website: https://www.violet.co/
---
