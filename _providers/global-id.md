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
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 9.0
  scored_at: '2026-08-17'
api_count: 0
artifact_total: 2
common:
- group: company
  title: ''
  type: Website
  url: https://global.id
- group: start
  title: ''
  type: DeveloperPortal
  url: https://developer.global.id/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/globalid
- group: auth
  title: ''
  type: Authentication
  url: authentication/global-id-authentication.yml
- group: build
  title: ''
  type: Packages
  url: packages/global-id-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/global-id-packages.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/global-id-well-known.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/global-id-domain-security.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/global-id-llms.txt
created: '2026-07-17'
description: GlobaliD (global.id) is a decentralized digital-identity platform that lets people create a portable, self-sovereign identity and lets developers add "Sign in with GlobaliD" login, issue verifiable credentials, and verify identity claims (such as proof of being 18+) through server-side issuer and verifier toolkits built on Hyperledger Aries. Developers create apps in the invitation-based developer portal to obtain OAuth2 client credentials, then integrate using the official @globalid npm SDKs. Surfaced in the API Evangelist network as a portfolio company of 500 Global.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/global-id.png
layout: provider
modified: '2026-07-19'
name: Global ID
nav: Providers
network: true
overview: 'Global ID is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Identity, Digital Identity, Decentralized Identity, and Self-Sovereign Identity.


  Global ID''s developer surface includes authentication and 8 more developer resources.'
random_paper: 130
score:
  band: minimal
  composite: 11.6
  delta: 0.0
  facets:
    commercial_clarity: 0.0
    contract_quality: 0.0
    developer_ergonomics: 26.1
    discoverability: 57.4
    governance: 0.0
    operational_transparency: 5.3
  previous_composite: 11.6
  schema_version: 0.11.0
  scored_at: '2026-08-17'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/global-id/refs/heads/main/screenshots/global-id-2026-07-25T215912.png
security:
- kind: authentication
  name: Global Id Authentication
  slug: global-id-authentication
  summary_line: oauth2 · 2 schemes
- kind: domain-security
  name: Global Id Domain Security
  slug: global-id-domain-security
  summary_line: TLSv1.3 · DMARC
slug: global-id
tags:
- Company
- Identity
- Digital Identity
- Decentralized Identity
- Self-Sovereign Identity
- Verifiable Credentials
- Authentication
- OAuth
website: https://global.id
---
