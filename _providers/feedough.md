---
access_model:
  confidence: medium
  label: Freemium
  onboarding: unknown
  pricing: freemium
  public: false
  source:
  - plans
  trial: false
  try_now: false
agent_readiness:
  band: agent-aware
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
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 15.5
  scored_at: '2026-09-05'
api_count: 2
apis:
- description: Feedough provides an RSS feed for its main content stream, allowing developers and readers to consume articles on startup ideas, business models, and entrepreneurship programmatically using standard f
  name: Feedough RSS Feed
  slug: rss-feed
- description: Feedough is built on WordPress and exposes the standard WordPress REST API, providing JSON endpoints for accessing posts, categories, tags, authors, and other content types. The API is available at th
  name: Feedough WordPress REST API
  slug: wordpress-rest-api
artifact_total: 6
common:
- group: auth
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
- name: Feedough Finops
  service_category: API
  slug: feedough-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/feedough.png
layout: provider
modified: '2026-04-28'
name: Feedough
nav: Providers
network: true
overview: 'Feedough publishes 1 API on the [APIs.io](https://apis.io/) network: WordPress REST API. Tagged areas include Business Models, Entrepreneurship, Media, and Startups.


  Feedough''s developer surface includes developer portal, engineering blog, and 12 more developer resources.'
plans:
- name: Feedough Plans Pricing
  plan_count: 3
  slug: feedough-plans-pricing
random_paper: 20
rate_limits:
- limit_count: 5
  name: Feedough Rate Limits
  slug: feedough-rate-limits
score:
  band: emerging
  composite: 25.3
  coverage:
    artifact_dirs: 6
    catalog_earned: 41.0
    catalog_earned_first_party: 0.0
    catalog_gap: 74.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 36.8
    commercial_clarity: 36.8
    contract_governance: 0.0
    contract_quality: 26.7
    developer_ergonomics: 21.4
    discoverability: 59.3
    governance: 0.0
    operational_transparency: 7.9
  previous_composite: 25.3
  schema_version: 0.18.3
  scored_at: '2026-09-05'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/feedough/refs/heads/main/screenshots/feedough-2026-06-20T181132.png
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
