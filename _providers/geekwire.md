---
access_model:
  confidence: low
  label: Freemium
  onboarding: unknown
  pricing: freemium
  public: false
  source:
  - plans
  - security
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
    mcp_tool_quality: na
    openapi_examples: false
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: derived
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: '0.2'
  score: 0.6
  scored_at: '2026-11-06'
api_count: 2
apis:
- description: GeekWire provides RSS feeds for its main news stream and individual topic categories including Microsoft, Space, Science, Real Estate, Games, Google, Mobile, GeekLife, Podcasts, and Apple. These Atom/
  name: GeekWire RSS Feed
  slug: rss-feed
- description: 'The public WordPress REST API (wp-json) of the GeekWire website at www.geekwire.com: the route index of the site''s content management system, catalogued as one site surface rather than as separate API'
  name: GeekWire Website (WordPress REST)
  slug: geekwire-com-website-wordpress-rest
artifact_total: 6
common:
- group: commercial
  href: https://artifacts.apis.io/geekwire/plans/geekwire-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/geekwire-plans-pricing.yml
- group: operate
  href: https://artifacts.apis.io/geekwire/rate-limits/geekwire-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/geekwire-rate-limits.yml
- group: commercial
  href: https://artifacts.apis.io/geekwire/finops/geekwire-finops.yml
  title: ''
  type: FinOps
  url: finops/geekwire-finops.yml
- group: auth
  href: https://artifacts.apis.io/geekwire/security/geekwire-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/geekwire-domain-security.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/geekwire
- group: company
  title: ''
  type: Website
  url: https://www.geekwire.com/
- group: company
  title: ''
  type: About
  url: https://www.geekwire.com/about-geekwire/
- group: operate
  title: ''
  type: Contact
  url: https://www.geekwire.com/contact-us/
- group: other
  title: ''
  type: RSSFeeds
  url: https://www.geekwire.com/rss-feeds/
- group: other
  title: ''
  type: RSSFeed
  url: https://www.geekwire.com/feed/
- group: company
  title: ''
  type: Newsletter
  url: https://www.geekwire.com/newsletter/
- group: other
  title: ''
  type: JobBoard
  url: https://www.geekwire.com/jobs/
- group: other
  title: ''
  type: Advertising
  url: https://www.geekwire.com/advertise/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.geekwire.com/privacy/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.geekwire.com/termsofuse/
- group: other
  title: ''
  type: Podcast
  url: https://podcasts.apple.com/us/podcast/geekwire/id427374434
- group: other
  title: ''
  type: Podcast
  url: https://open.spotify.com/show/2PPEGel5l0v3XxlD8fVxAh
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/geekwire
- group: other
  title: ''
  type: X
  url: https://x.com/geekwire
created: '2026-03-24'
description: GeekWire is a leading technology news site covering startups, innovation, and the Pacific Northwest tech scene. Founded in Seattle, GeekWire delivers breaking news, analysis, and commentary on technology, business, and entrepreneurship, with a particular focus on companies like Amazon, Microsoft, and the broader Seattle and Pacific Northwest startup ecosystem. GeekWire also operates GeekWork, a technology job board, and produces popular podcasts and weekly radio programming.
finops:
- has_sources: false
  method: generated
  name: Geekwire Finops
  primary_unit: request
  service_category: API
  slug: geekwire-finops
  template: true
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/geekwire.png
layout: provider
modified: '2026-04-28'
name: GeekWire
nav: Providers
network: true
overview: GeekWire is listed with 2 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Media, Startups, and Technology News.
plans:
- name: Geekwire Plans Pricing
  plan_count: 3
  slug: geekwire-plans-pricing
random_paper: 11
rate_limits:
- limit_count: 5
  name: Geekwire Rate Limits
  slug: geekwire-rate-limits
score:
  band: emerging
  composite: 12.8
  coverage:
    artifact_dirs: 8
    catalog_earned: 28.0
    catalog_earned_first_party: 0.0
    catalog_gap: 87.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 28.9
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 9.5
    discoverability: 39.3
    operational_transparency: 10.5
  previous_composite: 12.8
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 13.7
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
screenshot: https://apis.io/screenshots/geekwire/geekwire-2026-06-20T181712.png
security:
- kind: domain-security
  name: Geekwire Domain Security
  slug: geekwire-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
slug: geekwire
tags:
- Media
- Startups
- Technology News
website: https://www.geekwire.com/
---
