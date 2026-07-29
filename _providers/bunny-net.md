---
access_model:
  confidence: high
  label: Free · Self-serve signup
  onboarding: self-serve
  pricing: free
  public: false
  source:
  - plans
  - authentication
  trial: false
  try_now: true
agent_readiness:
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
    asyncapi_events: true
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 36.0
  scored_at: '2026-07-28'
agentic_access:
- acting_count: 30
  human_in_the_loop: 4
  name: Bunny Net Agentic Access
  operation_count: 47
  slug: bunny-net-agentic-access
  summary_line: 47 operations · 30 acting · 4 human-in-the-loop
api_count: 26
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
- description: The APIKeys API from Bunny.net — 1 operation(s) for apikeys.
  name: Bunny.net APIKeys API
  slug: bunny-net-apikeys-api
- description: The Billing API from Bunny.net — 3 operation(s) for billing.
  name: Bunny.net Billing API
  slug: bunny-net-billing-api
- description: The Countries API from Bunny.net — 1 operation(s) for countries.
  name: Bunny.net Countries API
  slug: bunny-net-countries-api
- description: The DNSZones API from Bunny.net — 6 operation(s) for dnszones.
  name: Bunny.net DNSZones API
  slug: bunny-net-dnszones-api
- description: The PullZones API from Bunny.net — 12 operation(s) for pullzones.
  name: Bunny.net PullZones API
  slug: bunny-net-pullzones-api
- description: The Purge API from Bunny.net — 1 operation(s) for purge.
  name: Bunny.net Purge API
  slug: bunny-net-purge-api
- description: The Regions API from Bunny.net — 1 operation(s) for regions.
  name: Bunny.net Regions API
  slug: bunny-net-regions-api
- description: The Statistics API from Bunny.net — 3 operation(s) for statistics.
  name: Bunny.net Statistics API
  slug: bunny-net-statistics-api
- description: The StorageZones API from Bunny.net — 4 operation(s) for storagezones.
  name: Bunny.net StorageZones API
  slug: bunny-net-storagezones-api
- description: The Stream API from Bunny.net — 2 operation(s) for stream.
  name: Bunny.net Stream API
  slug: bunny-net-stream-api
artifact_total: 36
asyncapis:
- description: AsyncAPI definition of the Bunny Stream webhook surface. Bunny Stream sends a signed HTTP POST callback to the `WebhookUrl` configured on a Video Library whenever the state of a video changes (upload,
  name: Bunny.net Stream Webhooks
  slug: bunny-net-stream-webhooks-asyncapi
collections:
- collection_type: open
  name: Bunny.net Core Platform API
  slug: open-bunny-net
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/bunny-net-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/bunny-net-domain-security.yml
- group: auth
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
  title: ''
  type: Plans
  url: plans/bunny-net-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/bunny-net-rate-limits.yml
- group: commercial
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
- name: Bunny Net Finops
  service_category: API
  slug: bunny-net-finops
graphqls:
- description: This is a conceptual GraphQL schema for the Bunny.net platform, representing the data model underlying Bunny.net's CDN, edge storage, video streaming, DNS, security (Shield/WAF), image optimization, e
  name: Bunny.net GraphQL Schema
  slug: bunny-net-graphql
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/bunny-net.png
layout: provider
modified: '2026-05-30'
name: Bunny.net
nav: Providers
network: true
overview: 'Bunny.net publishes 11 APIs on the [APIs.io](https://apis.io/) network, including Stream Webhooks, APIKeys API, Billing API, and 8 more. Tagged areas include CDN, Edge, Video, Storage, and DNS.


  The Bunny.net catalog on APIs.io includes 1 event-driven AsyncAPI specification and 1 Spectral governance ruleset.


  Bunny.net''s developer surface includes authentication, documentation, GitHub presence, status page, pricing, engineering blog, and 8 more developer resources.'
plans:
- name: Bunny Net Plans Pricing
  plan_count: 1
  slug: bunny-net-plans-pricing
random_paper: 59
rate_limits:
- limit_count: 2
  name: Bunny Net Rate Limits
  slug: bunny-net-rate-limits
rules:
- name: Bunny.net API Rules
  rule_count: 4
  severity_counts:
    error: 1
    hint: 0
    info: 1
    warn: 2
  slug: bunny-net-asyncapi-spectral-rules
score:
  band: thin
  composite: 41.7
  delta: -2.3
  facets:
    commercial_clarity: 39.5
    contract_quality: 65.4
    developer_ergonomics: 21.7
    discoverability: 64.8
    governance: 27.1
    operational_transparency: 26.3
  previous_composite: 44.0
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 10
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/bunny-net/refs/heads/main/screenshots/bunny-net-2026-06-20T173805.png
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
