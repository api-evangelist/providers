---
access_model:
  confidence: high
  label: Paid
  onboarding: unknown
  pricing: paid
  public: false
  source:
  - plans
  - authentication
  - rate-limits
  - security
  trial: false
  try_now: false
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
    openapi_examples: partial
    operation_distinctiveness: mostly
    pagination_ratio: false
    protected_resource_metadata: verified
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 45.6
  scored_at: '2026-11-06'
agentic_access:
- acting_count: 11
  human_in_the_loop: 0
  name: Transistor Agentic Access
  operation_count: 23
  slug: transistor-agentic-access
  summary_line: 23 operations · 11 acting
api_count: 1
apis:
- baseURL: https://api.transistor.fm/v1
  baseurl_source: declared
  description: The authenticated user account.
  name: Transistor Account API
  slug: transistor-account-api
- baseURL: https://api.transistor.fm/v1
  baseurl_source: declared
  description: Download analytics for shows and episodes.
  name: Transistor Analytics API
  slug: transistor-analytics-api
- baseURL: https://api.transistor.fm/v1
  baseurl_source: declared
  description: Podcast episodes, drafts, uploads, and publishing.
  name: Transistor Episodes API
  slug: transistor-episodes-api
- baseURL: https://api.transistor.fm/v1
  baseurl_source: declared
  description: Podcasts (shows) in your Transistor account.
  name: Transistor Shows API
  slug: transistor-shows-api
- baseURL: https://api.transistor.fm/v1
  baseurl_source: declared
  description: Private (subscriber-only) podcast subscribers.
  name: Transistor Subscribers API
  slug: transistor-subscribers-api
- baseURL: https://api.transistor.fm/v1
  baseurl_source: declared
  description: Event webhook subscriptions.
  name: Transistor Webhooks API
  slug: transistor-webhooks-api
artifact_total: 24
collections:
- collection_type: open
  name: Transistor Account API
  slug: open-transistor-account-api
- collection_type: open
  name: Transistor Account Analytics API
  slug: open-transistor-analytics-api
- collection_type: open
  name: Transistor Account Episodes API
  slug: open-transistor-episodes-api
- collection_type: open
  name: Transistor Account Shows API
  slug: open-transistor-shows-api
- collection_type: open
  name: Transistor Account Subscribers API
  slug: open-transistor-subscribers-api
- collection_type: open
  name: Transistor Account Webhooks API
  slug: open-transistor-webhooks-api
- collection_type: open
  name: Transistor API
  slug: open-transistor
common:
- group: company
  title: ''
  type: Blog
  url: https://transistor.fm/blog/
- group: company
  title: ''
  type: BlogRSS
  url: https://transistor.fm/blog/feed/
- group: commercial
  title: ''
  type: Pricing
  url: https://transistor.fm/pricing/
- group: other
  href: https://artifacts.apis.io/transistor/capabilities/transistor-capability-edges.yml
  title: ''
  type: CapabilityMap
  url: capabilities/transistor-capability-edges.yml
- group: agent
  href: https://artifacts.apis.io/transistor/agentic-access/transistor-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/transistor-agentic-access.yml
- group: auth
  href: https://artifacts.apis.io/transistor/security/transistor-trust-center.yml
  title: ''
  type: TrustCenter
  url: security/transistor-trust-center.yml
- group: auth
  href: https://artifacts.apis.io/transistor/security/transistor-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/transistor-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/transistor/security/transistor-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/transistor-domain-security.yml
- group: auth
  href: https://artifacts.apis.io/transistor/authentication/transistor-authentication.yml
  title: ''
  type: Authentication
  url: authentication/transistor-authentication.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/transistorfm
- group: company
  title: ''
  type: Website
  url: https://transistor.fm
- group: docs
  title: ''
  type: Documentation
  url: https://developers.transistor.fm/
- group: commercial
  href: https://artifacts.apis.io/transistor/plans/transistor-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/transistor-plans-pricing.yml
- group: operate
  href: https://artifacts.apis.io/transistor/rate-limits/transistor-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/transistor-rate-limits.yml
- group: commercial
  href: https://artifacts.apis.io/transistor/finops/transistor-finops.yml
  title: ''
  type: FinOps
  url: finops/transistor-finops.yml
created: '2026-07-05'
description: Transistor is a podcast hosting and analytics platform that lets teams host unlimited shows, distribute episodes to Apple Podcasts, Spotify, and YouTube, run private (subscriber-only) podcasts, and measure downloads with advanced analytics. Transistor exposes a documented public REST API at https://api.transistor.fm/v1 that follows the JSON:API specification, is authenticated with an x-api-key header, and covers shows, episodes, analytics, private podcast subscribers, and event webhooks.
finops:
- has_sources: true
  method: generated
  name: Transistor Finops
  primary_unit: ''
  service_category: Media and Podcast Hosting
  slug: transistor-finops
  template: false
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/transistor.png
layout: provider
mcp_servers:
- description: Remote MCP server at mcp.transistor.fm over HTTP.
  name: Transistor MCP Server
  slug: transistor
modified: '2026-10-06'
name: Transistor
nav: Providers
network: true
overview: 'Transistor publishes 6 API contracts indexed on the [APIs.io](https://apis.io/) network, including Account API, Analytics API, Episodes API, and 3 more. Tagged areas include Podcasts, Podcast Hosting, Analytics, Media, and Audio.


  The Transistor catalog on APIs.io includes 1 Spectral governance ruleset.


  Transistor''s developer surface includes engineering blog, pricing, authentication, documentation, and 11 more developer resources.'
plans:
- name: Transistor Plans Pricing
  plan_count: 4
  slug: transistor-plans-pricing
- name: Transistor Price Estimates
  plan_count: 0
  slug: transistor-price-estimates
random_paper: 9
rate_limits:
- limit_count: 2
  name: Transistor Rate Limits
  slug: transistor-rate-limits
rules:
- authorship: generated
  effective_rule_count: 109
  extends:
  - spectral:oas
  name: Transistor API Rules
  rule_count: 68
  severity_counts:
    error: 63
    hint: 0
    info: 3
    warn: 2
  slug: transistor-rules
score:
  band: developing
  composite: 41.1
  coverage:
    artifact_dirs: 19
    catalog_earned: 61.5
    catalog_earned_first_party: 20.0
    catalog_gap: 53.5
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -1.0
  facets:
    access_clarity: 44.7
    contract_governance: 13.6
    contract_quality: 53.8
    developer_ergonomics: 28.6
    discoverability: 68.3
    operational_transparency: 31.6
  previous_composite: 42.1
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
    score: 22.5
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: true
    score: 0.0
screenshot: https://apis.io/screenshots/transistor/transistor-2026-09-02T164127.png
security:
- kind: authentication
  name: Transistor Authentication
  slug: transistor-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Transistor Domain Security
  slug: transistor-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Transistor Vulnerability Disclosure
  slug: transistor-vulnerability-disclosure
  summary_line: no policy recorded
- kind: trust-center
  name: Transistor Trust Center
  slug: transistor-trust-center
  summary_line: SOC 2, ISO 27001
slug: transistor
tags:
- Podcasts
- Podcast Hosting
- Analytics
- Media
- Audio
- JSON:API
website: https://transistor.fm
---
