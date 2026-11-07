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
- description: Feedough provides an RSS feed for its main content stream, allowing developers and readers to consume articles on startup ideas, business models, and entrepreneurship programmatically using standard f
  name: Feedough RSS Feed
  slug: rss-feed
- description: 'The public WordPress REST API (wp-json) of the Feedough website at www.feedough.com: the route index of the site''s content management system, catalogued as one site surface rather than as separate API'
  name: Feedough Website (WordPress REST)
  slug: feedough-com-website-wordpress-rest
artifact_total: 6
common:
- group: commercial
  href: https://artifacts.apis.io/feedough/plans/feedough-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/feedough-plans-pricing.yml
- group: operate
  href: https://artifacts.apis.io/feedough/rate-limits/feedough-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/feedough-rate-limits.yml
- group: commercial
  href: https://artifacts.apis.io/feedough/finops/feedough-finops.yml
  title: ''
  type: FinOps
  url: finops/feedough-finops.yml
- group: auth
  href: https://artifacts.apis.io/feedough/security/feedough-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/feedough-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.feedough.com/
- group: company
  title: ''
  type: About
  url: https://www.feedough.com/about-us/
- group: company
  title: ''
  type: Newsletter
  url: https://www.feedough.com/subscribe/
- group: other
  title: ''
  type: Advertising
  url: https://www.feedough.com/partner-with-feedough/
- group: other
  title: ''
  type: RSSFeed
  url: https://www.feedough.com/feed/
- group: start
  title: ''
  type: Portal
  url: https://www.feedough.com/startup-resources/
- group: company
  title: ''
  type: Blog
  url: https://www.feedough.com/daily/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.feedough.com/legal/privacy-policy/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.feedough.com/legal/terms/
- group: other
  title: ''
  type: CookiePolicy
  url: https://www.feedough.com/legal/cookie-policy/
- group: other
  title: ''
  type: Disclaimer
  url: https://www.feedough.com/disclaimer/
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/feedough
- group: other
  title: ''
  type: X
  url: https://x.com/FeedoughCom
created: '2026-03-24'
description: Feedough is a media platform and entrepreneurship resource covering startup ideas, business models, and entrepreneurship. Founded in December 2013 by Aashish Pahwa to bridge the information gap in the startup industry, Feedough explains startup concepts in plain language without the fluff. The platform is ranked among the top twenty startup websites globally and is cited as a resource by institutions including Harvard Business School and the University of Washington.
finops:
- has_sources: false
  method: generated
  name: Feedough Finops
  primary_unit: request
  service_category: API
  slug: feedough-finops
  template: true
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/feedough.png
layout: provider
modified: '2026-04-28'
name: Feedough
nav: Providers
network: true
overview: 'Feedough is listed with 2 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Business Models, Entrepreneurship, Media, and Startups.


  Feedough''s developer surface includes developer portal, engineering blog, and 15 more developer resources.'
plans:
- name: Feedough Plans Pricing
  plan_count: 3
  slug: feedough-plans-pricing
random_paper: 23
rate_limits:
- limit_count: 5
  name: Feedough Rate Limits
  slug: feedough-rate-limits
score:
  band: emerging
  composite: 13.9
  coverage:
    artifact_dirs: 9
    catalog_earned: 28.0
    catalog_earned_first_party: 0.0
    catalog_gap: 87.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -0.9
  facets:
    access_clarity: 28.9
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 16.7
    discoverability: 39.3
    operational_transparency: 7.9
  previous_composite: 14.8
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
screenshot: https://apis.io/screenshots/feedough/feedough-2026-06-20T181132.png
security:
- kind: domain-security
  name: Feedough Domain Security
  slug: feedough-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
slug: feedough
tags:
- Business Models
- Entrepreneurship
- Media
- Startups
website: https://www.feedough.com/
---
