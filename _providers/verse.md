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
    agentic_access: false
    asyncapi_events: false
    auth_clarity: false
    consent_identity: true
    dry_run_mode: false
    error_semantics: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: false
    spec_presence: false
    well_known_catalog: true
  schema_version: 0.2
  score: 6.3
  scored_at: '2026-07-28'
api_count: 1
apis:
- description: Authenticated backend API for Verse, served at api.verse.inc over the Connect RPC protocol (gRPC-compatible; advertises Connect-Protocol-Version and Authorization headers, and OPTIONS/GET/POST/PATCH/D
  name: Verse API
  slug: verse-api
artifact_total: 3
common:
- group: company
  title: ''
  type: Website
  url: https://verse.inc/
- group: auth
  title: ''
  type: SecurityTxt
  url: well-known/verse-security.txt
- group: agent
  title: ''
  type: WellKnown
  url: well-known/verse-well-known.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/verse-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: Security
  url: well-known/verse-security.txt
- group: auth
  title: ''
  type: DomainSecurity
  url: security/verse-domain-security.yml
created: '2026-07-17'
description: 'Verse (verse.inc) is a private company backed by Bessemer Venture Partners, surfaced into the API Evangelist network from Bessemer''s portfolio. Its public marketing site is served entirely behind a Cloudflare bot challenge, so the product and sector could not be independently characterized from the site itself during enrichment. What is verifiable: Verse operates a live, authenticated backend API at api.verse.inc built on the Connect RPC protocol (a gRPC-compatible framework — the host advertises the Connect-Protocol-Version header and OPTIONS/GET/POST/PATCH/DELETE methods), fronted by Google infrastructure, and it publishes an RFC 9116 security.txt naming a security contact. No public OpenAPI, developer docs, SDKs, or MCP server were discoverable. Sector remains undetermined pending further research.'
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/verse.png
layout: provider
modified: '2026-07-21'
name: Verse
nav: Providers
network: true
overview: Verse publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, API, Connect RPC, gRPC, and Bessemer Portfolio.
random_paper: 75
score:
  band: minimal
  composite: 9.3
  delta: -1.3
  facets:
    commercial_clarity: 0.0
    contract_quality: 0.0
    developer_ergonomics: 0.0
    discoverability: 79.6
    governance: 0.0
    operational_transparency: 10.5
  previous_composite: 10.6
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: flat
security:
- kind: domain-security
  name: Verse Domain Security
  slug: verse-domain-security
  summary_line: TLSv1.3 · DNSSEC · DMARC
- kind: vulnerability-disclosure
  name: Verse Vulnerability Disclosure
  slug: verse-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: verse
tags:
- Company
- API
- Connect RPC
- gRPC
- Bessemer Portfolio
- Cloudflare
- Unknown
website: https://verse.inc/
---
