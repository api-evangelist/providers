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
api_count: 0
artifact_total: 2
common:
- group: company
  title: ''
  type: Website
  url: https://www.kobaltmusic.com
- group: start
  title: ''
  type: Login
  url: https://portal.kobaltmusic.com
- group: agent
  title: ''
  type: WellKnown
  url: well-known/kobalt-well-known.yml
- group: auth
  title: ''
  type: SecurityTxt
  url: well-known/kobalt-security.txt
- group: auth
  title: ''
  type: Security
  url: https://www.kobaltmusic.com/.well-known/security.txt
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/kobalt-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/kobalt-domain-security.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/kobalt-llms.txt
created: '2026-07-17'
description: 'Kobalt Music Group is an independent music rights management and administrative publishing company founded in 2000 by Willard Ahdritz, operating from New York and London. Unlike traditional publishers it administers copyrights rather than owning them, running Kobalt Music Publishing, a neighbouring rights division, and AMRA, the digital-first collection society it acquired in 2014. Royalty and rights processing runs on KTech, the rights and content management platform built to independently serve both Kobalt Music Publishing and AMRA at the scale of billions of music micro-transactions, with songwriters and rightsholders viewing statements and analytics through the authenticated Kobalt Portal. Kobalt publishes no public developer program: a 2026-07-19 probe found no developer portal, no API documentation, no OpenAPI or AsyncAPI description, and no API discovery documents under /.well-known/. Integration is arranged commercially through Kobalt or KTech rather than through a
  self-service API.'
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/kobalt.png
layout: provider
modified: '2026-07-19'
name: Kobalt
nav: Providers
network: true
overview: Kobalt is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Music, Music Publishing, Rights Management, and Royalties.
random_paper: 5
score:
  band: minimal
  composite: 10.9
  delta: 0.1
  facets:
    commercial_clarity: 13.2
    contract_quality: 0.0
    developer_ergonomics: 0.0
    discoverability: 68.5
    governance: 0.0
    operational_transparency: 10.5
  previous_composite: 10.8
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/kobalt/refs/heads/main/screenshots/kobalt-2026-07-25T224028.png
security:
- kind: domain-security
  name: Kobalt Domain Security
  slug: kobalt-domain-security
  summary_line: TLSv1.3 · DMARC
- kind: vulnerability-disclosure
  name: Kobalt Vulnerability Disclosure
  slug: kobalt-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: kobalt
tags:
- Company
- Music
- Music Publishing
- Rights Management
- Royalties
- Copyright
- Media and Entertainment
- Enterprise
website: https://www.kobaltmusic.com
---
