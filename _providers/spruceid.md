---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source: []
  trial: false
  try_now: false
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
    auth_clarity: false
    consent_identity: false
    dry_run_mode: false
    error_semantics: verified
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: partial
    rate_limit_signal: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 28.8
  scored_at: '2026-08-03'
agentic_access:
- acting_count: 8
  human_in_the_loop: 0
  name: Spruceid Agentic Access
  operation_count: 11
  slug: spruceid-agentic-access
  summary_line: 11 operations · 8 acting
api_count: 10
apis:
- description: Sign-In with Ethereum (SIWE) enables Ethereum accounts to authenticate with off-chain services by signing a standardized message format (EIP-4361). SpruceID's SIWE library provides client and server i
  name: SpruceID Sign-In with Ethereum (SIWE) API
  slug: spruceid-sign-in-with-ethereum-siwe-api
- description: 'The SpruceID SSI (Self-Sovereign Identity) core library provides a comprehensive Rust API for signing, issuing, and verifying W3C Verifiable Credentials and JSON Web Tokens. It supports VC Data Model '
  name: SpruceID SSI Core Library API
  slug: spruceid-ssi-core-library-api
- description: 'SpruceID''s OID4VCI (OpenID for Verifiable Credential Issuance) Rust library implements the OpenID4VC credential issuance protocol, enabling credential issuers to deliver W3C Verifiable Credentials to '
  name: SpruceID OID4VCI Credential Issuance API
  slug: spruceid-oid4vci-credential-issuance-api
- description: SpruceID's OID4VP (OpenID for Verifiable Presentations) Rust library implements the OpenID4VC credential presentation protocol, enabling verifier applications to request and receive verifiable credent
  name: SpruceID OID4VP Verifiable Presentations API
  slug: spruceid-oid4vp-verifiable-presentations-api
- description: SpruceID's isomdl library provides a Rust implementation of the ISO/IEC 18013-5 standard for mobile driver's licenses (mDL). It enables issuers to create standards-compliant mDL credentials and verifi
  name: SpruceID isomdl Mobile Driver's License API
  slug: spruceid-isomdl-mobile-drivers-license-api
- description: Issue and verify W3C Verifiable Credentials using the VC API specification. Supports both legacy (/issue/credentials, /verify/credentials) and current (/credentials/issue, /credentials/verify) path st
  name: SpruceID Credentials API
  slug: spruceid-credentials-api
- description: Health check endpoints
  name: SpruceID Health API
  slug: spruceid-health-api
- description: DID resolution implementing the W3C DID Resolution HTTP binding.
  name: SpruceID Identifiers API
  slug: spruceid-identifiers-api
- description: Issue and verify W3C Verifiable Presentations. Supports both legacy (/issue/presentations, /verify/presentations) and current (/presentations/issue, /presentations/verify) path styles.
  name: SpruceID Presentations API
  slug: spruceid-presentations-api
- description: Bitstring Status List credential endpoint for credential revocation status.
  name: SpruceID Status API
  slug: spruceid-status-api
artifact_total: 12
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/spruceid-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/spruceid-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://spruceid.com
- group: other
  title: ''
  type: Developer
  url: https://www.sprucekit.dev/
- group: company
  title: ''
  type: Blog
  url: https://blog.spruceid.com
- group: build
  title: ''
  type: GitHub
  url: https://github.com/spruceid
- group: other
  title: ''
  type: KnowledgeBase
  url: https://learn.spruceid.com
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://spruceid.com/privacy
- group: operate
  title: ''
  type: Contact
  url: https://spruceid.com/contact
- group: operate
  title: ''
  type: Discord
  url: https://discord.gg/spruceid
created: '2026-06-14'
description: SpruceID is a decentralized identity company providing open-source tools and infrastructure for governments and enterprises to issue, verify, and manage digital identity credentials. Their platform supports W3C Verifiable Credentials, Decentralized Identifiers (DIDs), OpenID for Verifiable Credential Issuance (OID4VCI), OpenID for Verifiable Presentations (OID4VP), Sign-In with Ethereum (SIWE), and ISO/IEC 18013-5 mobile driver's licenses (mDL). SpruceID's SpruceKit toolkit enables developers to build wallet apps, credential issuers, and verifier integrations using standards-based identity protocols.
image: https://spruceid.com/favicon.ico
layout: provider
modified: '2026-06-14'
name: SpruceID
nav: Providers
network: true
overview: 'SpruceID publishes 5 APIs on the [APIs.io](https://apis.io/) network, including Credentials API, Health API, Identifiers API, and 2 more. Tagged areas include Decentralized Identity, Verifiable Credentials, DIDs, Sign-In with Ethereum, and Identity Wallet.


  SpruceID''s developer surface includes engineering blog, GitHub presence, and 8 more developer resources.'
random_paper: 8
score:
  band: emerging
  composite: 21.9
  delta: 0.0
  facets:
    commercial_clarity: 10.5
    contract_quality: 51.2
    developer_ergonomics: 2.2
    discoverability: 64.8
    governance: 0.0
    operational_transparency: 5.3
  previous_composite: 21.9
  provenance:
    agentic_access: derived
    contracts:
      callable: 0.0
      derived: 0
      marker_coverage: 0.0
      total: 5
  regulatory:
    applies: true
    matched_via: tags
    regime: Government & Public Sector
    regime_id: government
    score: 18.5
  schema_version: 0.9
  scored_at: '2026-08-03'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/spruceid/refs/heads/main/screenshots/spruceid-2026-06-20T194421.png
security:
- kind: domain-security
  name: Spruceid Domain Security
  slug: spruceid-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: spruceid
tags:
- Decentralized Identity
- Verifiable Credentials
- DIDs
- Sign-In with Ethereum
- Identity Wallet
- Government
- OpenID Connect
- W3C Standards
website: https://spruceid.com
---
