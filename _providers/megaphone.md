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
  schema_version: 0.2
  score: 19.8
  scored_at: '2026-09-05'
agentic_access:
- acting_count: 7
  human_in_the_loop: 0
  name: Megaphone Agentic Access
  operation_count: 22
  slug: megaphone-agentic-access
  summary_line: 22 operations · 7 acting
api_count: 1
apis:
- baseURL: https://cms.megaphone.fm/api
  baseurl_source: declared
  description: Legacy Direct Sales campaigns scoped to an organization.
  name: Megaphone Campaigns API
  slug: megaphone-campaigns-api
- baseURL: https://cms.megaphone.fm/api
  baseurl_source: declared
  description: v2 advertisers, campaigns, orders, assets, advertisements, and targeting (modeled).
  name: Megaphone Direct Sales v2 API
  slug: megaphone-direct-sales-v2-api
- baseURL: https://cms.megaphone.fm/api
  baseurl_source: declared
  description: Episodes within a podcast, including dynamic ad insertion.
  name: Megaphone Episodes API
  slug: megaphone-episodes-api
- baseURL: https://cms.megaphone.fm/api
  baseurl_source: declared
  description: Metrics Export Service and Impressions Export Service (modeled).
  name: Megaphone Exports API
  slug: megaphone-exports-api
- baseURL: https://cms.megaphone.fm/api
  baseurl_source: declared
  description: Top-level account containers that scope podcasts and episodes.
  name: Megaphone Networks API
  slug: megaphone-networks-api
- baseURL: https://cms.megaphone.fm/api
  baseurl_source: declared
  description: Legacy Direct Sales campaign and promo orders and their advertisements.
  name: Megaphone Orders API
  slug: megaphone-orders-api
- baseURL: https://cms.megaphone.fm/api
  baseurl_source: declared
  description: Shows within a network, including feed and monetization settings.
  name: Megaphone Podcasts API
  slug: megaphone-podcasts-api
artifact_total: 23
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Megaphone Campaigns API
  slug: open-megaphone-campaigns-api
- collection_type: open
  name: Megaphone Campaigns Direct Sales v2 API
  slug: open-megaphone-direct-sales-v2-api
- collection_type: open
  name: Megaphone Campaigns Episodes API
  slug: open-megaphone-episodes-api
- collection_type: open
  name: Megaphone Campaigns Exports API
  slug: open-megaphone-exports-api
- collection_type: open
  name: Megaphone Campaigns Networks API
  slug: open-megaphone-networks-api
- collection_type: open
  name: Megaphone Campaigns Orders API
  slug: open-megaphone-orders-api
- collection_type: open
  name: Megaphone Campaigns Podcasts API
  slug: open-megaphone-podcasts-api
- collection_type: open
  name: Megaphone API
  slug: open-megaphone
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/megaphone-agentic-access.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/megaphone-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/megaphone-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/megaphone-authentication.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/megaphonepods
- group: company
  title: ''
  type: Website
  url: https://megaphone.spotify.com/
- group: docs
  title: ''
  type: Documentation
  url: https://developers.megaphone.fm/
- group: docs
  title: ''
  type: APIReference
  url: https://jsapi.apiary.io/apis/megaphoneapi/reference/podcasts.html
- group: commercial
  title: ''
  type: Plans
  url: plans/megaphone-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/megaphone-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/megaphone-finops.yml
- group: commercial
  title: ''
  type: Pricing
  url: https://megaphone.spotify.com/pricing
created: '2026-07-05'
description: Megaphone (Megaphone by Spotify) is an enterprise podcast hosting, distribution, and advertising-monetization platform, owned by Spotify since its 2020 acquisition. Its REST API (base https://cms.megaphone.fm/api) lets podcast producers and partners programmatically manage networks, podcasts, and episodes, run dynamic ad insertion, and operate direct-sales advertising - campaigns, orders, advertisements, advertisers, and targeting - plus pull metrics and impressions via export services. API documentation is public, but an API token requires a paid Megaphone account (Professional from $99/month, or Enterprise).
finops:
- name: Megaphone Finops
  service_category: Media and Podcasting
  slug: megaphone-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/megaphone.png
layout: provider
modified: '2026-07-05'
name: Megaphone
nav: Providers
network: true
overview: 'Megaphone publishes 7 APIs on the [APIs.io](https://apis.io/) network, including Campaigns API, Direct Sales v2 API, Episodes API, and 4 more. Tagged areas include Podcasting, Podcast Hosting, Advertising, Ad Monetization, and Dynamic Ad Insertion.


  Megaphone''s developer surface includes authentication, documentation, API reference, pricing, and 8 more developer resources.'
plans:
- name: Megaphone Plans Pricing
  plan_count: 2
  slug: megaphone-plans-pricing
random_paper: 3
rate_limits:
- limit_count: 3
  name: Megaphone Rate Limits
  slug: megaphone-rate-limits
score:
  band: emerging
  composite: 24.6
  coverage:
    artifact_dirs: 9
    catalog_earned: 60.0
    catalog_earned_first_party: 0.0
    catalog_gap: 55.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 39.5
    commercial_clarity: 39.5
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 28.6
    discoverability: 68.5
    governance: 0.0
    operational_transparency: 31.6
  previous_composite: 24.6
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 7
  schema_version: 0.18.3
  scored_at: '2026-09-05'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/megaphone/refs/heads/main/screenshots/megaphone-2026-08-07T172429.png
security:
- kind: authentication
  name: Megaphone Authentication
  slug: megaphone-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Megaphone Domain Security
  slug: megaphone-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Megaphone Vulnerability Disclosure
  slug: megaphone-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: megaphone
tags:
- Podcasting
- Podcast Hosting
- Advertising
- Ad Monetization
- Dynamic Ad Insertion
- Media
- Spotify
website: https://megaphone.spotify.com/
---
