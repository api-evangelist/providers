---
access_model:
  confidence: medium
  gated: none
  gated_source:
  - onboarding
  label: Freemium · Self-serve signup
  onboarding: self-serve
  pricing: freemium
  public: false
  source:
  - plans
  - authentication
  - security
  trial: false
  try_now: true
agent_readiness:
  band: agent-ready
  band_gated_from: agent-native
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: served
    consent_identity: false
    delegated_identity: served
    dry_run_mode: false
    dynamic_client_registration: true
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: verified
    mcp_tool_quality: na
    openapi_examples: false
    operation_distinctiveness: distinct
    pagination_ratio: na
    protected_resource_metadata: verified
    rate_limit_signal: derived
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 43.9
  scored_at: '2026-11-06'
agentic_access:
- acting_count: 6
  human_in_the_loop: 0
  name: Podbean Agentic Access
  operation_count: 16
  slug: podbean-agentic-access
  summary_line: 16 operations · 6 acting
api_count: 1
apis:
- baseURL: https://api.podbean.com/v1
  baseurl_source: declared
  description: Download, engagement, and advertising reports.
  name: Podbean Analytics API
  slug: podbean-analytics-api
- baseURL: https://api.podbean.com/v1
  baseurl_source: declared
  description: OAuth 2.0 login dialog, token exchange, inspection, and multi-podcast tokens.
  name: Podbean Authentication API
  slug: podbean-authentication-api
- baseURL: https://api.podbean.com/v1
  baseurl_source: declared
  description: List, read, publish, update, and delete podcast episodes.
  name: Podbean Episode API
  slug: podbean-episode-api
- baseURL: https://api.podbean.com/v1
  baseurl_source: declared
  description: Authorize a media/image upload and list uploaded media files.
  name: Podbean File Upload API
  slug: podbean-file-upload-api
- baseURL: https://api.podbean.com/v1
  baseurl_source: declared
  description: Read the authorized podcast profile and settings.
  name: Podbean Podcast API
  slug: podbean-podcast-api
- baseURL: https://api.podbean.com/v1
  baseurl_source: declared
  description: Embeddable player markup and metadata for a podcast or episode URL.
  name: Podbean o Embed API
  slug: podbean-o-embed-api
artifact_total: 22
collections:
- collection_type: open
  name: Podbean Analytics API
  slug: open-podbean-analytics-api
- collection_type: open
  name: Podbean Analytics Authentication API
  slug: open-podbean-authentication-api
- collection_type: open
  name: Podbean Analytics Episode API
  slug: open-podbean-episode-api
- collection_type: open
  name: Podbean Analytics File Upload API
  slug: open-podbean-file-upload-api
- collection_type: open
  name: Podbean Analytics oEmbed API
  slug: open-podbean-oembed-api
- collection_type: open
  name: Podbean Analytics Podcast API
  slug: open-podbean-podcast-api
- collection_type: open
  name: Podbean API
  slug: open-podbean
common:
- group: company
  title: ''
  type: BlogRSS
  url: https://blog.podbean.com/feed/
- group: other
  href: https://artifacts.apis.io/podbean/capabilities/podbean-capability-edges.yml
  title: ''
  type: CapabilityMap
  url: capabilities/podbean-capability-edges.yml
- group: agent
  href: https://artifacts.apis.io/podbean/agentic-access/podbean-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/podbean-agentic-access.yml
- group: auth
  href: https://artifacts.apis.io/podbean/security/podbean-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/podbean-domain-security.yml
- group: auth
  href: https://artifacts.apis.io/podbean/authentication/podbean-authentication.yml
  title: ''
  type: Authentication
  url: authentication/podbean-authentication.yml
- group: auth
  href: https://artifacts.apis.io/podbean/scopes/podbean-scopes.yml
  title: ''
  type: OAuthScopes
  url: scopes/podbean-scopes.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/podbean
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/podbean
- group: company
  title: ''
  type: Website
  url: https://www.podbean.com
- group: docs
  title: ''
  type: Documentation
  url: https://developers.podbean.com/podbean-api-docs/
- group: commercial
  href: https://artifacts.apis.io/podbean/plans/podbean-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/podbean-plans-pricing.yml
- group: operate
  href: https://artifacts.apis.io/podbean/rate-limits/podbean-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/podbean-rate-limits.yml
- group: commercial
  href: https://artifacts.apis.io/podbean/finops/podbean-finops.yml
  title: ''
  type: FinOps
  url: finops/podbean-finops.yml
- group: start
  title: ''
  type: SignUp
  url: https://developers.podbean.com/
- group: company
  title: ''
  type: Blog
  url: https://www.podbean.com/podcast-news
created: '2026-07-05'
description: Podbean is a podcast hosting, distribution, and monetization platform for creators, businesses, and networks. Its public REST API (base https://api.podbean.com/v1) uses OAuth 2.0 and lets third-party apps and integrations manage a user's podcast programmatically - read podcast profiles, list and publish/update/delete episodes, authorize media file uploads, embed players via oEmbed, and pull download, engagement, and advertising analytics reports. Apps can act on behalf of a single podcast (Client Credentials) or across many podcasts (Multiple Podcasts tokens) for agencies and networks.
finops:
- has_sources: true
  method: generated
  name: Podbean Finops
  primary_unit: ''
  service_category: Media and Content Hosting
  slug: podbean-finops
  template: false
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/podbean.png
layout: provider
mcp_servers:
- description: Remote MCP server at mcp.podbean.com over HTTP.
  name: Podbean MCP Server
  slug: podbean
modified: '2026-10-06'
name: Podbean
nav: Providers
network: true
overview: 'Podbean publishes 6 API contracts indexed on the [APIs.io](https://apis.io/) network, including Analytics API, Authentication API, Episode API, and 3 more. Tagged areas include Podcasts, Podcast Hosting, Media, Audio, and Episodes.


  The Podbean catalog on APIs.io includes 1 Spectral governance ruleset.


  Podbean''s developer surface includes authentication, documentation, signup flow, engineering blog, and 11 more developer resources.'
plans:
- name: Podbean Plans Pricing
  plan_count: 5
  slug: podbean-plans-pricing
random_paper: 9
rate_limits:
- limit_count: 4
  name: Podbean Rate Limits
  slug: podbean-rate-limits
rules:
- authorship: generated
  effective_rule_count: 109
  extends:
  - spectral:oas
  name: Podbean API Rules
  rule_count: 68
  severity_counts:
    error: 66
    hint: 0
    info: 1
    warn: 1
  slug: podbean-rules
scopes:
- name: Podbean Scopes
  scope_count: 3
  slug: podbean-scopes
  summary_line: 3 scopes · authorizationCode/clientCredentials
score:
  band: thin
  composite: 33.0
  coverage:
    artifact_dirs: 20
    catalog_earned: 47.5
    catalog_earned_first_party: 0.0
    catalog_gap: 67.5
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 21.1
    contract_governance: 13.6
    contract_quality: 48.9
    developer_ergonomics: 32.1
    discoverability: 68.3
    operational_transparency: 10.5
  previous_composite: 33.0
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 6
    mcp: first-party
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 21.6
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: true
    score: 0.0
screenshot: https://apis.io/screenshots/podbean/podbean-2026-08-17T081313.png
security:
- kind: authentication
  name: Podbean Authentication
  slug: podbean-authentication
  summary_line: oauth2 · 1 scheme
- kind: domain-security
  name: Podbean Domain Security
  slug: podbean-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
slug: podbean
tags:
- Podcasts
- Podcast Hosting
- Media
- Audio
- Episodes
- Analytics
- Monetization
website: https://www.podbean.com
---
