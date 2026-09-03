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
  scored_at: '2026-09-02'
api_count: 1
apis:
- description: Anime discovery, streaming & syncing with trackers
  name: AniAPI
  slug: aniapi
artifact_total: 3
common:
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/aniapi-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/aniapi-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://aniapi.com/docs/
- group: other
  title: ''
  type: PublicAPIsListing
  url: https://github.com/public-apis/public-apis
created: '2026-05-28'
description: Anime discovery, streaming & syncing with trackers
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/aniapi.png
layout: provider
modified: '2026-05-28'
name: AniAPI
nav: Providers
network: true
overview: AniAPI publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Anime and Public APIs.
random_paper: 17
score:
  band: minimal
  composite: 7.6
  coverage:
    artifact_dirs: 2
    catalog_gap: 88.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 0.0
    commercial_clarity: 0.0
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 9.5
    discoverability: 57.4
    governance: 0.0
    operational_transparency: 0.0
  previous_composite: 7.6
  schema_version: 0.18.0
  scored_at: '2026-09-02'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/aniapi/refs/heads/main/screenshots/aniapi-2026-06-20T172001.png
security:
- kind: domain-security
  name: Aniapi Domain Security
  slug: aniapi-domain-security
  summary_line: TLSv1.3
- kind: vulnerability-disclosure
  name: Aniapi Vulnerability Disclosure
  slug: aniapi-vulnerability-disclosure
  summary_line: disclosure policy published
slug: aniapi
tags:
- Anime
- Public APIs
website: https://aniapi.com/docs/
---
