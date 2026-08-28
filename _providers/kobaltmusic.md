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
  band: human-only
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    agentic_commerce: false
    auth_clarity: false
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
  score: 0.0
  scored_at: '2026-08-26'
api_count: 0
artifact_total: 2
common:
- group: company
  title: ''
  type: Website
  url: https://www.kobaltmusic.com/
- group: agent
  title: ''
  type: WellKnown
  url: well-known/kobaltmusic-well-known.yml
- group: auth
  title: ''
  type: SecurityTxt
  url: well-known/kobaltmusic-security.txt
- group: auth
  title: ''
  type: Security
  url: https://www.kobaltmusic.com/.well-known/security.txt
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/kobaltmusic-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/kobaltmusic-domain-security.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/kobaltmusic-llms.txt
created: '2026-07-17'
description: Kobalt Music Group is a music services company providing publishing administration, neighbouring rights and recordings services for songwriters, artists, publishers and rights holders. It collects, matches and accounts for royalties across streaming and digital platforms, reporting to clients through its own portals rather than a public developer program. Kobalt's rights and content management platform is operated by KTech, its technology arm, which processes the micro-transaction royalty data behind Kobalt Music Publishing and AMRA, the global digital collection society. As of the July 2026 enrichment pass Kobalt publishes no public API, API documentation, or machine-readable API specification; the only public machine-readable surface found was an RFC 9116 security.txt.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/kobaltmusic.png
layout: provider
modified: '2026-07-19'
name: Kobalt Music
nav: Providers
network: true
overview: Kobalt Music is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Music, Music Publishing, Royalties, and Rights Management.
random_paper: 6
score:
  band: minimal
  composite: 6.8
  delta: 0.0
  facets:
    access_clarity: 0.0
    commercial_clarity: 0.0
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 0.0
    discoverability: 61.1
    governance: 0.0
    operational_transparency: 5.3
  previous_composite: 6.8
  schema_version: 0.15.0
  scored_at: '2026-08-26'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/kobaltmusic/refs/heads/main/screenshots/kobaltmusic-2026-07-25T224033.png
security:
- kind: domain-security
  name: Kobaltmusic Domain Security
  slug: kobaltmusic-domain-security
  summary_line: TLSv1.3 · DMARC
- kind: vulnerability-disclosure
  name: Kobaltmusic Vulnerability Disclosure
  slug: kobaltmusic-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: kobaltmusic
tags:
- Company
- Music
- Music Publishing
- Royalties
- Rights Management
- Media
- Entertainment
website: https://www.kobaltmusic.com/
---
