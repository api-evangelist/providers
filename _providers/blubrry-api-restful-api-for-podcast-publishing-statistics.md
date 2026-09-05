---
access_model:
  confidence: high
  label: Freemium · Self-serve signup
  onboarding: self-serve
  pricing: freemium
  public: false
  source:
  - plans
  - authentication
  trial: false
  try_now: true
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: negotiable
    consent_identity: false
    delegated_identity: documented
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
  score: 24.8
  scored_at: '2026-09-04'
agentic_access:
- acting_count: 8
  human_in_the_loop: 0
  name: Blubrry Api Restful Api For Podcast Publishing Statistics Agentic Access
  operation_count: 27
  slug: blubrry-api-restful-api-for-podcast-publishing-statistics-agentic-access
  summary_line: 27 operations · 8 acting
api_count: 1
apis:
- description: The Blubrry Podcast Media Hosting API enables uploading and managing podcast media files through third-party applications. Supports listing shows, retrieving unpublished media files, deleting media, a
  name: Blubrry Podcast Media Hosting API
  slug: blubrry-podcast-media-hosting-api
- description: The Blubrry Episode Management API supports creating new podcast episodes (publish, schedule, or save as draft) and updating existing episode fields. Enables CMS and podcast production tools to manage
  name: Blubrry Episode Management API
  slug: blubrry-episode-management-api
- description: The Blubrry Podcast Statistics API provides analytics for podcast episodes including download and play counts, overall show download summaries, monthly download breakdowns, and episode-level statistic
  name: Blubrry Podcast Statistics API
  slug: blubrry-podcast-statistics-api
- description: The Blubrry Podcast Network API provides access to user subscriptions with show management, episode metadata storage including playback status and position, show navigation by category and search, and
  name: Blubrry Podcast Network API
  slug: blubrry-podcast-network-api
- baseURL: https://api.blubrry.com/2
  baseurl_source: spec
  description: Read, create, and update episodes for shows hosted on Blubrry.
  name: Blubrry API Episode API
  slug: blubrry-api-restful-api-for-podcast-publishing-statistics-episode-api
- baseURL: https://api.blubrry.com/2
  baseurl_source: spec
  description: Upload and manage media files hosted on Blubrry.
  name: Blubrry API Media API
  slug: blubrry-api-restful-api-for-podcast-publishing-statistics-media-api
- baseURL: https://api.blubrry.com/2
  baseurl_source: spec
  description: Podcast download statistics.
  name: Blubrry API Statistics API
  slug: blubrry-api-restful-api-for-podcast-publishing-statistics-statistics-api
artifact_total: 19
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Blubrry Podcast Hosting & Statistics Episode API
  slug: open-blubrry-api-restful-api-for-podcast-publishing-statistics-episode-api
- collection_type: open
  name: Blubrry Podcast Hosting & Statistics Episode Media API
  slug: open-blubrry-api-restful-api-for-podcast-publishing-statistics-media-api
- collection_type: open
  name: Blubrry Podcast Hosting & Episode Statistics API
  slug: open-blubrry-api-restful-api-for-podcast-publishing-statistics-statistics-api
- collection_type: open
  name: Blubrry Podcast Hosting & Statistics API
  slug: open-blubrry-api-restful-api-for-podcast-publishing-statistics
common:
- group: other
  title: ''
  type: CapabilityMap
  url: capabilities/blubrry-api-restful-api-for-podcast-publishing-statistics-capability-edges.yml
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/blubrry-api-restful-api-for-podcast-publishing-statistics-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/blubrry-api-restful-api-for-podcast-publishing-statistics-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/blubrry-api-restful-api-for-podcast-publishing-statistics-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/blubrry-api-restful-api-for-podcast-publishing-statistics-scopes.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/blubrry
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/rawvoice
- group: company
  title: ''
  type: Website
  url: https://blubrry.com
- group: start
  title: ''
  type: Portal
  url: https://blubrry.com/developer/api/
- group: docs
  title: ''
  type: Documentation
  url: https://blubrry.com/developer/api/
- group: auth
  title: ''
  type: Authentication
  url: https://blubrry.com/developer/api/
- group: company
  title: ''
  type: Blog
  url: https://blubrry.com/podcast-insider/feed/
created: '2025-05-02'
description: Blubrry is a podcast hosting and statistics platform providing a RESTful API for podcast publishing, media management, episode management, audience statistics, and podcast network functionality. The API uses OAuth 2.0 authentication and enables third-party applications to integrate with podcast hosting workflows.
finops:
- name: Blubrry Api Restful Api For Podcast Publishing Statistics Finops
  service_category: API
  slug: blubrry-api-restful-api-for-podcast-publishing-statistics-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/blubrry-api-restful-api-for-podcast-publishing-statistics.png
layout: provider
modified: '2026-04-21'
name: Blubrry API
nav: Providers
network: true
overview: 'Blubrry API publishes 3 APIs on the [APIs.io](https://apis.io/) network: Episode API, Media API, and Statistics API. Tagged areas include Podcasting, Audio, Media, Publishing, and Statistics.


  Blubrry API''s developer surface includes authentication, developer portal, documentation, engineering blog, and 8 more developer resources.'
plans:
- name: Blubrry Api Restful Api For Podcast Publishing Statistics Plans Pricing
  plan_count: 3
  slug: blubrry-api-restful-api-for-podcast-publishing-statistics-plans-pricing
random_paper: 6
rate_limits:
- limit_count: 5
  name: Blubrry Api Restful Api For Podcast Publishing Statistics Rate Limits
  slug: blubrry-api-restful-api-for-podcast-publishing-statistics-rate-limits
scopes:
- name: Blubrry Api Restful Api For Podcast Publishing Statistics Scopes
  scope_count: 0
  slug: blubrry-api-restful-api-for-podcast-publishing-statistics-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: thin
  composite: 29.7
  coverage:
    artifact_dirs: 12
    catalog_earned: 41.0
    catalog_earned_first_party: 0.0
    catalog_gap: 74.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 15.8
    commercial_clarity: 15.8
    contract_governance: 0.0
    contract_quality: 50.3
    developer_ergonomics: 33.3
    discoverability: 59.3
    governance: 0.0
    operational_transparency: 10.5
  previous_composite: 29.7
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 3
  schema_version: 0.18.3
  scored_at: '2026-09-04'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/blubrry-api-restful-api-for-podcast-publishing-statistics/refs/heads/main/screenshots/blubrry-api-restful-api-for-podcast-publishing-statistics-2026-06-20T173526.png
security:
- kind: authentication
  name: Blubrry Api Restful Api For Podcast Publishing Statistics Authentication
  slug: blubrry-api-restful-api-for-podcast-publishing-statistics-authentication
  summary_line: oauth2 · 1 scheme
- kind: domain-security
  name: Blubrry Api Restful Api For Podcast Publishing Statistics Domain Security
  slug: blubrry-api-restful-api-for-podcast-publishing-statistics-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: blubrry-api-restful-api-for-podcast-publishing-statistics
tags:
- Podcasting
- Audio
- Media
- Publishing
- Statistics
website: https://blubrry.com
---
