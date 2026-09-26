---
access_model:
  confidence: medium
  label: Paid
  onboarding: unknown
  pricing: paid
  public: false
  source:
  - plans
  - authentication
  - security
  trial: false
  try_now: false
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: bearer
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
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 19.8
  scored_at: '2026-09-25'
agentic_access:
- acting_count: 12
  human_in_the_loop: 0
  name: Iconik Agentic Access
  operation_count: 26
  slug: iconik-agentic-access
  summary_line: 26 operations · 12 acting
api_count: 1
apis:
- baseURL: https://app.iconik.io/API/assets/v1
  baseurl_source: declared
  description: Core media asset containers.
  name: iconik Assets API
  slug: iconik-assets-api
- baseURL: https://app.iconik.io/API/assets/v1
  baseurl_source: declared
  description: Folder-like grouping of assets and sub-collections.
  name: iconik Collections API
  slug: iconik-collections-api
- baseURL: https://app.iconik.io/API/assets/v1
  baseurl_source: declared
  description: Files, proxies, formats, and storages attached to assets.
  name: iconik Files API
  slug: iconik-files-api
- baseURL: https://app.iconik.io/API/assets/v1
  baseurl_source: declared
  description: Asynchronous job tracking and orchestration.
  name: iconik Jobs API
  slug: iconik-jobs-api
- baseURL: https://app.iconik.io/API/assets/v1
  baseurl_source: declared
  description: Custom metadata fields, views, and values.
  name: iconik Metadata API
  slug: iconik-metadata-api
- baseURL: https://app.iconik.io/API/assets/v1
  baseurl_source: declared
  description: Full-text and metadata search across the catalog.
  name: iconik Search API
  slug: iconik-search-api
artifact_total: 21
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: iconik Assets API
  slug: open-iconik-assets-api
- collection_type: open
  name: iconik Assets Collections API
  slug: open-iconik-collections-api
- collection_type: open
  name: iconik Assets Files API
  slug: open-iconik-files-api
- collection_type: open
  name: iconik Assets Jobs API
  slug: open-iconik-jobs-api
- collection_type: open
  name: iconik Assets Metadata API
  slug: open-iconik-metadata-api
- collection_type: open
  name: iconik Assets Search API
  slug: open-iconik-search-api
- collection_type: open
  name: iconik API
  slug: open-iconik
common:
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/iconik/refs/heads/main/capabilities/iconik-capability-edges.yml
  title: ''
  type: CapabilityMap
  url: capabilities/iconik-capability-edges.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/iconik/refs/heads/main/agentic-access/iconik-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/iconik-agentic-access.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/iconik/refs/heads/main/security/iconik-trust-center.yml
  title: ''
  type: TrustCenter
  url: security/iconik-trust-center.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/iconik/refs/heads/main/security/iconik-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/iconik-domain-security.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/iconik/refs/heads/main/authentication/iconik-authentication.yml
  title: ''
  type: Authentication
  url: authentication/iconik-authentication.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/iconik-io
- group: company
  title: ''
  type: Website
  url: https://www.iconik.io
- group: docs
  title: ''
  type: Documentation
  url: https://app.iconik.io/docs/
- group: commercial
  href: https://raw.githubusercontent.com/api-evangelist/iconik/refs/heads/main/plans/iconik-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/iconik-plans-pricing.yml
- group: operate
  href: https://raw.githubusercontent.com/api-evangelist/iconik/refs/heads/main/rate-limits/iconik-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/iconik-rate-limits.yml
- group: commercial
  href: https://raw.githubusercontent.com/api-evangelist/iconik/refs/heads/main/finops/iconik-finops.yml
  title: ''
  type: FinOps
  url: finops/iconik-finops.yml
created: '2026-07-05'
description: 'iconik is a hybrid cloud media asset management (MAM) platform for video and media teams, letting organizations ingest, organize, search, collaborate on, and distribute media across cloud and on-premise storage without vendor lock-in. iconik is API-first: nearly everything in the product is exposed through a set of versioned REST microservice APIs - Assets, Collections, Metadata, Search, Files, and Jobs - so integrators can automate ingest, enrich metadata, drive search and discovery, manage files and formats across connected storages, and orchestrate asynchronous work. The API is authenticated with an application ID and an auth token generated by an administrator in the web UI, and event notifications are delivered as HTTP webhooks.'
finops:
- name: Iconik Finops
  service_category: Media and Content Management
  slug: iconik-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/iconik.png
layout: provider
modified: '2026-07-05'
name: iconik
nav: Providers
network: true
overview: 'iconik publishes 6 APIs on the [APIs.io](https://apis.io/) network, including Assets API, Collections API, Files API, and 3 more. Tagged areas include Media Asset Management, MAM, Video, Media, and Cloud Storage.


  iconik''s developer surface includes authentication, documentation, and 9 more developer resources.'
plans:
- name: Iconik Plans Pricing
  plan_count: 3
  slug: iconik-plans-pricing
random_paper: 21
rate_limits:
- limit_count: 3
  name: Iconik Rate Limits
  slug: iconik-rate-limits
score:
  band: thin
  composite: 37.5
  coverage:
    artifact_dirs: 11
    catalog_earned: 61.6
    catalog_earned_first_party: 0.0
    catalog_gap: 53.4
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -2.4
  facets:
    access_clarity: 44.2
    contract_governance: 0.0
    contract_quality: 51.6
    developer_ergonomics: 29.8
    discoverability: 66.1
    operational_transparency: 28.4
  previous_composite: 39.9
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 6
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 16.7
  schema_version: 0.23.0
  scored_at: '2026-09-25'
  trend: flat
  upsert:
    applies: true
    score: 0.0
screenshot: https://raw.githubusercontent.com/api-evangelist/iconik/refs/heads/main/screenshots/iconik-2026-07-25T222037.png
security:
- kind: authentication
  name: Iconik Authentication
  slug: iconik-authentication
  summary_line: apiKey · 2 schemes
- kind: domain-security
  name: Iconik Domain Security
  slug: iconik-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
- kind: trust-center
  name: Iconik Trust Center
  slug: iconik-trust-center
  summary_line: SOC 2
slug: iconik
tags:
- Media Asset Management
- MAM
- Video
- Media
- Cloud Storage
- Metadata
- Search
- Assets
website: https://www.iconik.io
---
