---
access_model:
  confidence: high
  label: Freemium · Self-serve signup
  onboarding: self-serve
  pricing: freemium
  public: false
  source:
  - plans
  - authentication
  trial: false
  try_now: true
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 30.6
  scored_at: '2026-08-17'
agentic_access:
- acting_count: 0
  human_in_the_loop: 0
  name: Openwallet Foundation Agentic Access
  operation_count: 6
  slug: openwallet-foundation-agentic-access
  summary_line: 6 operations
api_count: 11
apis:
- description: Aries Cloud Agent Python (ACA-Py) exposes an OpenAPI-documented REST Admin API used by controller applications to manage agent behavior, issue and verify credentials, exchange messages, and orchestrat
  name: ACA-Py Admin API
  slug: aca-py-admin-api
- description: Credo (formerly Aries Framework JavaScript) is a TypeScript framework for building decentralized identity and verifiable credential applications. It exposes programmatic interfaces for issuing, verify
  name: Credo API
  slug: credo-api
- description: Askar is a secure storage backend for digital wallets that manages cryptographic keys, secrets, and credential records. It provides language bindings (Python, Rust, JavaScript, Kotlin, Swift) for read
  name: Askar API
  slug: askar-api
- description: VC API is an implementation of the W3C Verifiable Credentials API draft standard, exposing REST endpoints for verifiable credential issuance, verification, and presentation exchange.
  name: VC API
  slug: vc-api
- description: OpenWallet Foundation maintains Selective Disclosure for JSON Web Tokens (SD-JWT) libraries across multiple languages including JavaScript, Python, Rust, Kotlin, and .NET. These libraries expose progr
  name: SD-JWT Libraries
  slug: sd-jwt-api
- description: The Basicmessages API from OpenWallet Foundation — 1 operation(s) for basicmessages.
  name: OpenWallet Foundation Basicmessages API
  slug: openwallet-foundation-basicmessages-api
- description: The Connections API from OpenWallet Foundation — 1 operation(s) for connections.
  name: OpenWallet Foundation Connections API
  slug: openwallet-foundation-connections-api
- description: The Forward API from OpenWallet Foundation — 1 operation(s) for forward.
  name: OpenWallet Foundation Forward API
  slug: openwallet-foundation-forward-api
- description: The Issue Credential API from OpenWallet Foundation — 1 operation(s) for issue credential.
  name: OpenWallet Foundation Issue Credential API
  slug: openwallet-foundation-issue-credential-api
- description: The Present Proof API from OpenWallet Foundation — 1 operation(s) for present proof.
  name: OpenWallet Foundation Present Proof API
  slug: openwallet-foundation-present-proof-api
- description: The Ws API from OpenWallet Foundation — 1 operation(s) for ws.
  name: OpenWallet Foundation Ws API
  slug: openwallet-foundation-ws-api
artifact_total: 25
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: ACA-Py Admin Basicmessages API
  slug: open-openwallet-foundation-basicmessages-api
- collection_type: open
  name: ACA-Py Admin Basicmessages Connections API
  slug: open-openwallet-foundation-connections-api
- collection_type: open
  name: ACA-Py Admin Basicmessages Forward API
  slug: open-openwallet-foundation-forward-api
- collection_type: open
  name: ACA-Py Admin Basicmessages Issue Credential API
  slug: open-openwallet-foundation-issue-credential-api
- collection_type: open
  name: ACA-Py Admin Basicmessages Present Proof API
  slug: open-openwallet-foundation-present-proof-api
- collection_type: open
  name: ACA-Py Admin Basicmessages Ws API
  slug: open-openwallet-foundation-ws-api
- collection_type: open
  name: ACA-Py Admin API
  slug: open-openwallet-foundation
common:
- group: commercial
  title: ''
  type: License
  url: https://github.com/openwallet-foundation/acapy/blob/main/LICENSE
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/openwallet-foundation-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/openwallet-foundation-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/openwallet-foundation-authentication.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/open-wallet-foundation
- group: company
  title: ''
  type: Website
  url: https://openwallet.foundation/
- group: docs
  title: ''
  type: Documentation
  url: https://openwallet.foundation/projects/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/openwallet-foundation
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/openwallet-foundation-labs
- group: company
  title: ''
  type: Blog
  url: https://openwallet.foundation/blog/
- group: operate
  title: ''
  type: Community
  url: https://openwallet.foundation/community/
- group: other
  title: ''
  type: Mailing List
  url: https://lists.openwallet.foundation/
- group: company
  title: ''
  type: About
  url: https://openwallet.foundation/about/
- group: commercial
  title: ''
  type: Privacy
  url: https://openwallet.foundation/privacy-policy/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://openwallet.foundation/terms-of-use/
created: '2026-03-16'
description: The OpenWallet Foundation is a Linux Foundation Europe project that brings developers and standards organizations together to facilitate global interoperability of verifiable credentials and digital wallet technology. It develops open source engines for secure, privacy-preserving digital identity solutions.
finops:
- name: Openwallet Foundation Finops
  service_category: API
  slug: openwallet-foundation-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/openwallet-foundation.png
layout: provider
modified: '2026-04-28'
name: OpenWallet Foundation
nav: Providers
network: true
overview: 'OpenWallet Foundation publishes 6 APIs on the [APIs.io](https://apis.io/) network, including Basicmessages API, Connections API, Forward API, and 3 more. Tagged areas include Credentials, Digital Wallet, Identity, and Linux Foundation.


  OpenWallet Foundation''s developer surface includes authentication, documentation, engineering blog, privacy policy, and 11 more developer resources.'
plans:
- name: Openwallet Foundation Plans Pricing
  plan_count: 3
  slug: openwallet-foundation-plans-pricing
random_paper: 121
rate_limits:
- limit_count: 5
  name: Openwallet Foundation Rate Limits
  slug: openwallet-foundation-rate-limits
score:
  band: thin
  composite: 33.3
  delta: 0.0
  facets:
    commercial_clarity: 36.8
    contract_quality: 55.3
    developer_ergonomics: 26.1
    discoverability: 55.6
    governance: 0.0
    operational_transparency: 13.2
  previous_composite: 33.3
  provenance:
    agentic_access: derived
    contracts:
      callable: 0.0
      derived: 0
      marker_coverage: 0.0
      total: 6
  regulatory:
    applies: true
    matched_via: tags
    regime: Payments
    regime_id: payments
    score: 31.3
  schema_version: 0.11.0
  scored_at: '2026-08-17'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/openwallet-foundation/refs/heads/main/screenshots/openwallet-foundation-2026-06-20T191051.png
security:
- kind: authentication
  name: Openwallet Foundation Authentication
  slug: openwallet-foundation-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Openwallet Foundation Domain Security
  slug: openwallet-foundation-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: openwallet-foundation
tags:
- Credentials
- Digital Wallet
- Identity
- Linux Foundation
website: https://openwallet.foundation/
---
