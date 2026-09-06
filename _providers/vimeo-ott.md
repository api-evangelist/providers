---
access_model:
  confidence: medium
  label: Paid (free trial) · Self-serve signup
  onboarding: self-serve
  pricing: paid
  public: false
  source:
  - plans
  - authentication
  - security
  trial: true
  try_now: true
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
  schema_version: 0.2
  score: 19.8
  scored_at: '2026-09-05'
agentic_access:
- acting_count: 16
  human_in_the_loop: 1
  name: Vimeo Ott Agentic Access
  operation_count: 30
  slug: vimeo-ott-agentic-access
  summary_line: 30 operations · 16 acting · 1 human-in-the-loop
api_count: 1
apis:
- baseURL: https://api.vhx.tv
  baseurl_source: declared
  description: Performance reports for the OTT service.
  name: Vimeo OTT Analytics API
  slug: vimeo-ott-analytics-api
- baseURL: https://api.vhx.tv
  baseurl_source: declared
  description: Short-lived tokens granting a customer access to the embeddable player.
  name: Vimeo OTT Authorizations API
  slug: vimeo-ott-authorizations-api
- baseURL: https://api.vhx.tv
  baseurl_source: declared
  description: Categories, series, seasons, movies, and playlists, and their items.
  name: Vimeo OTT Collections API
  slug: vimeo-ott-collections-api
- baseURL: https://api.vhx.tv
  baseurl_source: declared
  description: Subscribers, their product access, watchlists, and in-progress viewing.
  name: Vimeo OTT Customers API
  slug: vimeo-ott-customers-api
- baseURL: https://api.vhx.tv
  baseurl_source: declared
  description: Access agreements (subscription, rental, purchase) and their prices.
  name: Vimeo OTT Products API
  slug: vimeo-ott-products-api
- baseURL: https://api.vhx.tv
  baseurl_source: declared
  description: Transcoded content items and their playable file URLs.
  name: Vimeo OTT Videos API
  slug: vimeo-ott-videos-api
artifact_total: 21
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Vimeo OTT Analytics API
  slug: open-vimeo-ott-analytics-api
- collection_type: open
  name: Vimeo OTT Analytics Authorizations API
  slug: open-vimeo-ott-authorizations-api
- collection_type: open
  name: Vimeo OTT Analytics Collections API
  slug: open-vimeo-ott-collections-api
- collection_type: open
  name: Vimeo OTT Analytics Customers API
  slug: open-vimeo-ott-customers-api
- collection_type: open
  name: Vimeo OTT Analytics Products API
  slug: open-vimeo-ott-products-api
- collection_type: open
  name: Vimeo OTT Analytics Videos API
  slug: open-vimeo-ott-videos-api
- collection_type: open
  name: Vimeo OTT API
  slug: open-vimeo-ott
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/vimeo-ott-agentic-access.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/vimeo-ott-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/vimeo-ott-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/vimeo-ott-authentication.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/vimeo
- group: company
  title: ''
  type: Website
  url: https://vimeo.com/ott
- group: docs
  title: ''
  type: Documentation
  url: https://dev.vhx.tv/docs/api/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/vhx
- group: commercial
  title: ''
  type: Plans
  url: plans/vimeo-ott-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/vimeo-ott-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/vimeo-ott-finops.yml
created: '2026-07-11'
description: Vimeo OTT (formerly VHX) is a subscription video / over-the-top (OTT) platform for launching branded SVOD, TVOD, and live streaming services across web, mobile, and connected-TV apps. Its documented REST API at api.vhx.tv lets media companies programmatically manage customers, products (subscription, rental, and purchase access agreements), videos, and collections (categories, series, seasons, movies, playlists), plus watchlists, player authorizations, comments, live events, and analytics. The API is publicly documented at dev.vhx.tv and uses HTTP Basic authentication with an API key generated from the Vimeo OTT CMS; the platform itself is a paid product (Starter and Enterprise plans).
finops:
- name: Vimeo Ott Finops
  service_category: Media and Streaming
  slug: vimeo-ott-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/vimeo-ott.png
layout: provider
modified: '2026-07-11'
name: Vimeo OTT
nav: Providers
network: true
overview: 'Vimeo OTT publishes 6 APIs on the [APIs.io](https://apis.io/) network, including Analytics API, Authorizations API, Collections API, and 3 more. Tagged areas include OTT, Video, SVOD, Streaming, and Media.


  Vimeo OTT''s developer surface includes authentication, documentation, and 9 more developer resources.'
plans:
- name: Vimeo Ott Plans Pricing
  plan_count: 2
  slug: vimeo-ott-plans-pricing
random_paper: 8
rate_limits:
- limit_count: 5
  name: Vimeo Ott Rate Limits
  slug: vimeo-ott-rate-limits
score:
  band: emerging
  composite: 23.7
  coverage:
    artifact_dirs: 9
    catalog_earned: 60.0
    catalog_earned_first_party: 0.0
    catalog_gap: 55.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 28.9
    commercial_clarity: 28.9
    contract_governance: 0.0
    contract_quality: 2.6
    developer_ergonomics: 29.8
    discoverability: 68.5
    governance: 0.0
    operational_transparency: 34.2
  previous_composite: 23.7
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 6
  schema_version: 0.18.3
  scored_at: '2026-09-05'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/vimeo-ott/refs/heads/main/screenshots/vimeo-ott-2026-09-02T165929.png
security:
- kind: authentication
  name: Vimeo Ott Authentication
  slug: vimeo-ott-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Vimeo Ott Domain Security
  slug: vimeo-ott-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Vimeo Ott Vulnerability Disclosure
  slug: vimeo-ott-vulnerability-disclosure
  summary_line: Hackerone · security.txt · contact published
slug: vimeo-ott
tags:
- OTT
- Video
- SVOD
- Streaming
- Media
- Subscription
- VHX
website: https://vimeo.com/ott
---
