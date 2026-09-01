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
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: documented
    event_surface_described: true
    idempotency: false
    mcp_server: false
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 22.7
  scored_at: '2026-09-01'
api_count: 3
apis:
- description: REST API for institutional custody (Taurus-PROTECT) and tokenization / digital asset issuance (Taurus-CAPITAL). Bearer + HMAC request signing, versioned under /api/rest/v1/, cursor-based pagination, g
  name: Taurus-PROTECT & Taurus-CAPITAL API
  slug: taurus-protect-taurus-capital-api
- description: Blockchain node and indexing services providing normalized access to on-chain data across dozens of supported protocols.
  name: Taurus-EXPLORER API
  slug: taurus-explorer-api
- description: Institutional trading infrastructure with deep liquidity and institutional-grade execution, accessible over both a REST API and the FIX protocol.
  name: Taurus-PRIME API
  slug: taurus-prime-api
artifact_total: 8
asyncapis:
- description: ''
  name: Taurus Protect Webhooks
  slug: taurus-protect-webhooks
common:
- group: start
  title: ''
  type: DeveloperPortal
  url: https://docs.taurushq.com/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.taurushq.com/
- group: docs
  title: ''
  type: APIReference
  url: https://docs.taurushq.com/protect-capital/reference
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.taurushq.com/protect-capital/docs/introduction
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/taurushq-io
- group: auth
  title: ''
  type: Authentication
  url: authentication/taurus-authentication.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/taurus-conventions.yml
- group: build
  title: ''
  type: SDKs
  url: packages/taurus-packages.yml
- group: build
  title: ''
  type: Packages
  url: packages/taurus-packages.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/taurus-problem-types.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/taurus-lifecycle.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/taurus-conformance.yml
- group: auth
  title: ''
  type: Compliance
  url: security/taurus-trust-center.yml
- group: auth
  title: ''
  type: TrustCenter
  url: security/taurus-trust-center.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/taurus-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: Security
  url: https://www.taurushq.com/security
- group: auth
  title: ''
  type: SecurityTxt
  url: well-known/taurus-security.txt
- group: agent
  title: ''
  type: WellKnown
  url: well-known/taurus-well-known.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/taurus-domain-security.yml
- group: design
  title: ''
  type: Webhooks
  url: asyncapi/taurus-protect-webhooks.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/taurus-llms.txt
- group: company
  title: ''
  type: LinkedIn
  url: https://ch.linkedin.com/company/taurus-sa
- group: company
  title: ''
  type: Twitter
  url: https://twitter.com/taurus_hq
created: '2026-07-17'
description: 'Taurus SA (Taurus HQ) is a Geneva-based digital asset infrastructure provider for banks and financial institutions. Its platform spans four institutional products exposed through APIs: Taurus-PROTECT (bank-grade custody of cryptocurrencies, digital assets, and private keys secured in FIPS 140-2 Level 3 HSMs), Taurus-CAPITAL (issuance and lifecycle management of tokenized securities and digital assets), Taurus-EXPLORER (blockchain node and indexing services across dozens of protocols), and Taurus-PRIME (institutional trading connectivity with deep liquidity via REST and FIX). The Taurus-PROTECT REST API (versioned /api/rest/v1/) uses bearer plus HMAC request signing, cursor-based pagination, and governance rules enforced by digital signatures, with first-party Java, Go, Python, and TypeScript SDKs, OIDC/SAML SSO, and SCIM provisioning.'
image: https://taurushq.com/img/brand@2x.png
layout: provider
modified: '2026-07-21'
name: Taurus
nav: Providers
network: true
overview: 'Taurus publishes 3 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Digital Assets, Cryptocurrency, Custody, and Tokenization.


  The Taurus catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  Taurus'' developer surface includes documentation, API reference, getting-started guide, authentication, and 19 more developer resources.'
random_paper: 4
score:
  band: thin
  composite: 35.7
  coverage:
    artifact_dirs: 10
    catalog_gap: 75.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 15.8
    commercial_clarity: 15.8
    contract_governance: 18.2
    contract_quality: 42.7
    developer_ergonomics: 32.1
    discoverability: 81.5
    governance: 18.2
    operational_transparency: 10.5
  previous_composite: 35.7
  provenance:
    conformance: first-party
  regulatory:
    applies: true
    matched_via: weak_tags
    regime: Securities & Market Data
    regime_id: securities_market_data
    score: 60.0
  schema_version: 0.17.2
  scored_at: '2026-09-01'
  trend: flat
security:
- kind: authentication
  name: Taurus Authentication
  slug: taurus-authentication
  summary_line: http/hmac/openIdConnect/saml · 3 schemes
- kind: domain-security
  name: Taurus Domain Security
  slug: taurus-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Taurus Vulnerability Disclosure
  slug: taurus-vulnerability-disclosure
  summary_line: security.txt · contact published
- kind: trust-center
  name: Taurus Trust Center
  slug: taurus-trust-center
  summary_line: ISAE 3402 Type II, FIPS 140-2 Level 3, CMTA DACS, ISO 27001
slug: taurus
tags:
- Company
- Digital Assets
- Cryptocurrency
- Custody
- Tokenization
- Blockchain
- Trading
- Financial-Services
- Fintech
- Institutional
website: https://docs.taurushq.com/
---
