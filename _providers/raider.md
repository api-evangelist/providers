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
    auth_clarity: false
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 0.0
  scored_at: '2026-08-19'
api_count: 1
apis:
- description: Provides detailed character and guild rankings for Raiding and Mythic+ content in World of Warcraft
  name: Raider
  slug: raider
artifact_total: 3
common:
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/raider-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/raider-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://raider.io/api
- group: other
  title: ''
  type: PublicAPIsListing
  url: https://github.com/public-apis/public-apis
- group: company
  title: ''
  type: Blog
  url: https://raider.io/rss.xml
created: '2026-05-28'
description: Provides detailed character and guild rankings for Raiding and Mythic+ content in World of Warcraft
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/raider.png
layout: provider
modified: '2026-05-28'
name: Raider
nav: Providers
network: true
overview: 'Raider publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Games And Comics and Public APIs.


  Raider''s developer surface includes engineering blog and 4 more developer resources.'
random_paper: 35
score:
  band: minimal
  composite: 6.2
  delta: 0.0
  facets:
    access_clarity: 0.0
    commercial_clarity: 0.0
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 2.4
    discoverability: 57.4
    governance: 0.0
    operational_transparency: 0.0
  previous_composite: 6.2
  schema_version: 0.12.0
  scored_at: '2026-08-19'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/raider/refs/heads/main/screenshots/raider-2026-06-20T192530.png
security:
- kind: domain-security
  name: Raider Domain Security
  slug: raider-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
- kind: vulnerability-disclosure
  name: Raider Vulnerability Disclosure
  slug: raider-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: raider
tags:
- Games And Comics
- Public APIs
website: https://raider.io/api
---
