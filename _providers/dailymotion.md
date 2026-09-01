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
    agentic_commerce: false
    auth_clarity: false
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: false
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
  score: 17.3
  scored_at: '2026-09-01'
api_count: 1
apis:
- description: Dailymotion Developer API
  name: Dailymotion
  slug: dailymotion
artifact_total: 4
common:
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/dailymotion-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/dailymotion-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://developer.dailymotion.com/
- group: other
  title: ''
  type: PublicAPIsListing
  url: https://github.com/public-apis/public-apis
- group: design
  title: ''
  type: Webhooks
  url: https://developers.dailymotion.com/docs/webhooks
created: '2026-05-28'
description: Dailymotion Developer API
graphqls:
- description: Dailymotion is a video sharing platform. The API covers video search, channel management, playlists, user profiles, content moderation, advertising configuration, analytics, and live streaming.
  name: Dailymotion GraphQL API
  slug: dailymotion-graphql
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/dailymotion.png
layout: provider
modified: '2026-05-30'
name: Dailymotion
nav: Providers
network: true
overview: Dailymotion publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Video and Public APIs.
random_paper: 17
score:
  band: emerging
  composite: 17.4
  coverage:
    artifact_dirs: 3
    catalog_gap: 88.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 0.0
    commercial_clarity: 0.0
    contract_governance: 0.0
    contract_quality: 37.2
    developer_ergonomics: 9.5
    discoverability: 57.4
    governance: 0.0
    operational_transparency: 3.9
  previous_composite: 17.4
  schema_version: 0.17.2
  scored_at: '2026-09-01'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/dailymotion/refs/heads/main/screenshots/dailymotion-2026-06-20T175448.png
security:
- kind: domain-security
  name: Dailymotion Domain Security
  slug: dailymotion-domain-security
  summary_line: TLSv1.3 · DMARC
- kind: vulnerability-disclosure
  name: Dailymotion Vulnerability Disclosure
  slug: dailymotion-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: dailymotion
tags:
- Video
- Public APIs
website: https://developer.dailymotion.com/
---
