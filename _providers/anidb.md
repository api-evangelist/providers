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
  scored_at: '2026-09-01'
api_count: 1
apis:
- description: Anime Database
  name: AniDB
  slug: anidb
artifact_total: 3
common:
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/anidb-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/anidb-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://wiki.anidb.net/HTTP_API_Definition
- group: other
  title: ''
  type: PublicAPIsListing
  url: https://github.com/public-apis/public-apis
created: '2026-05-28'
description: Anime Database
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/anidb.png
layout: provider
modified: '2026-05-28'
name: AniDB
nav: Providers
network: true
overview: AniDB publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Anime and Public APIs.
random_paper: 6
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
  scored_at: '2026-09-01'
  trend: flat
security:
- kind: domain-security
  name: Anidb Domain Security
  slug: anidb-domain-security
  summary_line: TLSv1.3 · DMARC
- kind: vulnerability-disclosure
  name: Anidb Vulnerability Disclosure
  slug: anidb-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: anidb
tags:
- Anime
- Public APIs
website: https://wiki.anidb.net/HTTP_API_Definition
---
