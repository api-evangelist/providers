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
    error_semantics: verified
    event_surface_described: derived
    idempotency: false
    mcp_server: false
    mcp_tool_quality: na
    openapi_examples: false
    operation_distinctiveness: mostly
    pagination_ratio: partial
    protected_resource_metadata: false
    rate_limit_signal: derived
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 26.1
  scored_at: '2026-11-06'
agentic_access:
- acting_count: 30
  human_in_the_loop: 4
  name: Bunny Net Agentic Access
  operation_count: 47
  slug: bunny-net-agentic-access
  summary_line: 47 operations · 30 acting · 4 human-in-the-loop
api_count: 2
apis:
- description: REST API for managing account-level bunny.net resources - Pull Zones, Storage Zones, DNS Zones, Stream Video Libraries, statistics, billing, purge, API keys, and reference data (countries, regions).
  name: Bunny.net Core Platform API
  slug: core
- description: Endpoints for creating and configuring CDN Pull Zones - origin configuration, edge rules, hostnames, SSL certificates, cache settings, and security headers.
  name: Bunny.net Pull Zones API
  slug: pull-zones
- description: Endpoints for creating and managing edge Storage Zones, replication regions, and access keys used by the Edge Storage data-plane.
  name: Bunny.net Storage Zones API
  slug: storage-zones
- description: Object-storage data-plane API for uploading, downloading, listing, and deleting files inside a Storage Zone. Regional hosts are derived from the zone's primary region (e.g. ny.storage.bunnycdn.com, la
  name: Bunny.net Edge Storage API
  slug: edge-storage
- description: Endpoints for managing DNS zones and records on the Bunny.net DNS platform, including geo-steering and load-balancing record types.
  name: Bunny.net DNS API
  slug: dns
- description: Video streaming API for managing Video Libraries, videos, collections, captions, chapters, transcoding profiles, and DRM. Upload and playback are served via dedicated video.bunnycdn.com endpoints; lib
  name: Bunny.net Stream API
  slug: stream
- description: Signed HTTP POST webhooks delivered by Bunny Stream to the WebhookUrl configured on a Video Library whenever a video transitions to a new processing state (Queued, Processing, Encoding, Finished, Reso
  name: Bunny.net Stream Webhooks
  slug: stream-webhooks
- description: Security and WAF configuration API for Bunny Shield - managed rules, custom rules, bot detection, rate-limiting policies, and DDoS mitigation settings attached to Pull Zones.
  name: Bunny.net Shield API
  slug: shield
- description: 'Image and front-end optimisation service attached to Pull Zones - image resizing, format conversion (WebP/AVIF), quality controls, and automatic CSS/JS minification. Configured via Pull Zone settings '
  name: Bunny.net Optimizer
  slug: optimizer
- description: Edge-compute API for deploying and managing Bunny Edge Scripts - JavaScript/TypeScript functions that run on the Bunny.net edge network to mutate requests and responses, with associated routes, enviro
  name: Bunny.net Scripting / Edge Compute API
  slug: scripting
- description: Cache purge endpoints for invalidating cached content by URL, by Pull Zone, or by tag across the Bunny.net global edge network.
  name: Bunny.net Purge API
  slug: purge
- description: Endpoints returning bandwidth, request, status-code, and geographic traffic statistics for the account and per Pull Zone or Storage Zone.
  name: Bunny.net Statistics API
  slug: statistics
- description: Billing endpoints for retrieving account balance, monthly usage and invoices, and applying promo codes.
  name: Bunny.net Billing API
  slug: billing
- description: Endpoints for managing API keys (AccessKey) issued for the account.
  name: Bunny.net API Keys API
  slug: api-keys
- description: Reference endpoint returning the list of countries Bunny.net supports for geo-targeting in Pull Zone and DNS rules.
  name: Bunny.net Countries API
  slug: countries
- description: Reference endpoint returning the list of Bunny.net edge and storage regions for use in zone configuration.
  name: Bunny.net Regions API
  slug: regions
- baseURL: https://api.bunny.net
  baseurl_source: declared
  description: The Billing API from Bunny.net — 3 operation(s) for billing.
  name: Bunny.net Billing API
  slug: bunny-net-billing-api
- baseURL: https://api.bunny.net
  baseurl_source: declared
  description: The Countries API from Bunny.net — 1 operation(s) for countries.
  name: Bunny.net Countries API
  slug: bunny-net-countries-api
- baseURL: https://api.bunny.net
  baseurl_source: declared
  description: The PullZones API from Bunny.net — 12 operation(s) for pullzones.
  name: Bunny.net PullZones API
  slug: bunny-net-pullzones-api
- baseURL: https://api.bunny.net
  baseurl_source: declared
  description: The Purge API from Bunny.net — 1 operation(s) for purge.
  name: Bunny.net Purge API
  slug: bunny-net-purge-api
- baseURL: https://api.bunny.net
  baseurl_source: declared
  description: The Regions API from Bunny.net — 1 operation(s) for regions.
  name: Bunny.net Regions API
  slug: bunny-net-regions-api
- baseURL: https://api.bunny.net
  baseurl_source: declared
  description: The Statistics API from Bunny.net — 3 operation(s) for statistics.
  name: Bunny.net Statistics API
  slug: bunny-net-statistics-api
- baseURL: https://api.bunny.net
  baseurl_source: declared
  description: The StorageZones API from Bunny.net — 4 operation(s) for storagezones.
  name: Bunny.net StorageZones API
  slug: bunny-net-storagezones-api
- baseURL: https://api.bunny.net
  baseurl_source: declared
  description: The Stream API from Bunny.net — 2 operation(s) for stream.
  name: Bunny.net Stream API
  slug: bunny-net-stream-api
- baseURL: https://api.bunny.net
  baseurl_source: declared
  description: The API Keys API from Bunny.net — 1 operation(s) for api keys.
  name: Bunny.net API Keys API
  slug: bunny-net-api-keys-api
- baseURL: https://api.bunny.net
  baseurl_source: declared
  description: The DNS Zone API from Bunny.net — 12 operation(s) for dns zone.
  name: Bunny.net DNS Zone API
  slug: bunny-net-dns-zone-api
- baseURL: https://api.bunny.net
  baseurl_source: declared
  description: The Pull Zone API from Bunny.net — 24 operation(s) for pull zone.
  name: Bunny.net Pull Zone API
  slug: bunny-net-pull-zone-api
- baseURL: https://api.bunny.net
  baseurl_source: declared
  description: The Region API from Bunny.net — 1 operation(s) for region.
  name: Bunny.net Region API
  slug: bunny-net-region-api
- baseURL: https://api.bunny.net
  baseurl_source: declared
  description: The Search API from Bunny.net — 1 operation(s) for search.
  name: Bunny.net Search API
  slug: bunny-net-search-api
- baseURL: https://api.bunny.net
  baseurl_source: declared
  description: The Storage Zone API from Bunny.net — 6 operation(s) for storage zone.
  name: Bunny.net Storage Zone API
  slug: bunny-net-storage-zone-api
- baseURL: https://api.bunny.net
  baseurl_source: declared
  description: The Stream Video Library API from Bunny.net — 16 operation(s) for stream video library.
  name: Bunny.net Stream Video Library API
  slug: bunny-net-stream-video-library-api
- baseURL: https://api.bunny.net
  baseurl_source: declared
  description: The User API from Bunny.net — 2 operation(s) for user.
  name: Bunny.net User API
  slug: bunny-net-user-api
- baseURL: https://api.bunny.net
  baseurl_source: declared
  description: The DNS Zones API from Bunny.net — 6 operation(s) for dns zones.
  name: Bunny.net DNS Zones API
  slug: bunny-net-dns-zones-api
artifact_total: 53
asyncapis:
- description: AsyncAPI definition of the Bunny Stream webhook surface. Bunny Stream sends a signed HTTP POST callback to the `WebhookUrl` configured on a Video Library whenever the state of a video changes (upload,
  name: Bunny.net Stream Webhooks
  slug: bunny-net-stream-webhooks-asyncapi
collections:
- collection_type: open
  name: Bunny.net Core Platform APIKeys API
  slug: open-bunny-net-apikeys-api
- collection_type: open
  name: Bunny.net Core Platform APIKeys Billing API
  slug: open-bunny-net-billing-api
- collection_type: open
  name: Bunny.net Core Platform APIKeys Countries API
  slug: open-bunny-net-countries-api
- collection_type: open
  name: Bunny.net Core Platform APIKeys DNSZones API
  slug: open-bunny-net-dnszones-api
- collection_type: open
  name: Bunny.net Core Platform APIKeys PullZones API
  slug: open-bunny-net-pullzones-api
- collection_type: open
  name: Bunny.net Core Platform APIKeys Purge API
  slug: open-bunny-net-purge-api
- collection_type: open
  name: Bunny.net Core Platform APIKeys Regions API
  slug: open-bunny-net-regions-api
- collection_type: open
  name: Bunny.net Core Platform APIKeys Statistics API
  slug: open-bunny-net-statistics-api
- collection_type: open
  name: Bunny.net Core Platform APIKeys StorageZones API
  slug: open-bunny-net-storagezones-api
- collection_type: open
  name: Bunny.net Core Platform APIKeys Stream API
  slug: open-bunny-net-stream-api
- collection_type: open
  name: Bunny.net Core Platform API
  slug: open-bunny-net
common:
- group: other
  href: https://artifacts.apis.io/bunny-net/vendor-facets/bunny-net-vendor-facets.yml
  title: ''
  type: VendorFacets
  url: vendor-facets/bunny-net-vendor-facets.yml
- group: other
  href: https://artifacts.apis.io/bunny-net/capabilities/bunny-net-capability-edges.yml
  title: ''
  type: CapabilityMap
  url: capabilities/bunny-net-capability-edges.yml
- group: agent
  href: https://artifacts.apis.io/bunny-net/agentic-access/bunny-net-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/bunny-net-agentic-access.yml
- group: auth
  href: https://artifacts.apis.io/bunny-net/security/bunny-net-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/bunny-net-domain-security.yml
- group: auth
  href: https://artifacts.apis.io/bunny-net/authentication/bunny-net-authentication.yml
  title: ''
  type: Authentication
  url: authentication/bunny-net-authentication.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/bunny-net
- group: company
  title: ''
  type: Website
  url: https://bunny.net/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.bunny.net/
- group: build
  title: ''
  type: GitHub
  url: https://github.com/BunnyWay
- group: operate
  title: ''
  type: Status
  url: https://status.bunny.net/
- group: commercial
  title: ''
  type: Pricing
  url: https://bunny.net/pricing/
- group: commercial
  href: https://artifacts.apis.io/bunny-net/plans/bunny-net-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/bunny-net-plans-pricing.yml
- group: operate
  href: https://artifacts.apis.io/bunny-net/rate-limits/bunny-net-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/bunny-net-rate-limits.yml
- group: commercial
  href: https://artifacts.apis.io/bunny-net/finops/bunny-net-finops.yml
  title: ''
  type: FinOps
  url: finops/bunny-net-finops.yml
- group: agent
  title: ''
  type: LlmsText
  url: https://docs.bunny.net/llms.txt
- group: company
  title: ''
  type: Blog
  url: https://bunny.net/blog/
created: '2026-05-23'
description: 'Bunny.net is a content-delivery and edge platform offering a global CDN, edge storage, video streaming, DNS, image optimisation, edge scripting, and WAF / security shielding. The Bunny.net Core Platform REST API at api.bunny.net manages account-level resources - Pull Zones, Storage Zones, DNS Zones, Stream video libraries, statistics, billing, purge, API keys, and reference data (countries, regions). Product-specific data-plane APIs sit on dedicated hosts: Edge Storage at storage.bunnycdn.com, Stream uploads at video.bunnycdn.com, Shield (WAF), Optimizer, and the Scripting / Magic Containers edge-compute API. All APIs use the AccessKey header for authentication, with API keys issued from the bunny.net dashboard.'
finops:
- has_sources: false
  method: generated
  name: Bunny Net Finops
  primary_unit: ''
  service_category: API
  slug: bunny-net-finops
  template: true
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/bunny-net.png
layout: provider
modified: '2026-05-30'
name: Bunny.net
nav: Providers
network: true
overview: 'Bunny.net publishes 33 API contracts indexed on the [APIs.io](https://apis.io/) network, including Stream Webhooks, Billing API, Countries API, and 30 more. Tagged areas include CDN, Edge, Video, Storage, and DNS.


  The Bunny.net catalog on APIs.io includes 1 event-driven AsyncAPI specification and 1 Spectral governance ruleset.


  Bunny.net''s developer surface includes authentication, documentation, GitHub presence, status page, pricing, engineering blog, and 10 more developer resources.'
plans:
- name: Bunny Net Plans Pricing
  plan_count: 9
  slug: bunny-net-plans-pricing
- name: Bunny Net Price Estimates
  plan_count: 0
  slug: bunny-net-price-estimates
random_paper: 16
rate_limits:
- limit_count: 2
  name: Bunny Net Rate Limits
  slug: bunny-net-rate-limits
rules:
- authorship: generated
  effective_rule_count: 31
  extends:
  - spectral:asyncapi
  name: Bunny.net — asyncapi rules
  rule_count: 4
  severity_counts:
    error: 1
    hint: 0
    info: 1
    warn: 2
  slug: bunny-net-asyncapi-spectral-rules
score:
  band: thin
  composite: 39.1
  coverage:
    artifact_dirs: 19
    catalog_earned: 50.5
    catalog_earned_first_party: 12.0
    catalog_gap: 64.5
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.9
  facets:
    access_clarity: 42.1
    contract_governance: 13.6
    contract_quality: 61.9
    developer_ergonomics: 23.8
    discoverability: 64.3
    operational_transparency: 10.5
  previous_composite: 38.2
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 28
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 11.8
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: true
    score: 22.2
screenshot: https://apis.io/screenshots/bunny-net/bunny-net-2026-06-20T173805.png
security:
- kind: authentication
  name: Bunny Net Authentication
  slug: bunny-net-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Bunny Net Domain Security
  slug: bunny-net-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: bunny-net
tags:
- CDN
- Edge
- Video
- Storage
- DNS
- WAF
- Edge Compute
- Image Optimization
website: https://bunny.net/
---
