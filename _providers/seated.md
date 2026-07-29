---
access_model:
  confidence: medium
  label: Freemium · Requires approval
  onboarding: approval
  pricing: freemium
  public: false
  source:
  - plans
  trial: false
  try_now: false
agent_readiness:
  band: human-only
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    asyncapi_events: false
    auth_clarity: false
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: documented
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 3.2
  scored_at: '2026-07-28'
api_count: 1
apis:
- description: The Seated Artist API enables developers and artist teams to build custom integrations with the Seated platform. The API provides access to tour date listings and event data, supporting use cases such
  name: Seated Artist API
  slug: artist-api
artifact_total: 5
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/seated-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.seated.com/
- group: docs
  title: ''
  type: Documentation
  url: https://support.seated.com
- group: start
  title: ''
  type: GettingStarted
  url: https://www.seated.com/artists
- group: commercial
  title: ''
  type: TermsOfService
  url: https://support.seated.com/hc/en-us/articles/115006017267-Terms-Conditions
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://support.seated.com/hc/en-us/articles/115006196728-Privacy-Policy
- group: company
  title: ''
  type: Blog
  url: https://blog.seated.com
- group: start
  title: ''
  type: FanPortal
  url: https://go.seated.com
- group: commercial
  title: ''
  type: Plans
  url: plans/seated-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/seated-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/seated-finops.yml
created: '2026-06-13'
description: Seated is a live event discovery and direct ticketing platform that connects fans with artists through a frictionless ticketing experience. The platform enables artists to publish tour dates via a single embed line or a custom API integration, manage fan presales and waitlists, capture and sync fan data with marketing tools, and generate additional revenue through merchandise and digital content bundled into the ticket purchase flow. Fans can follow favorite artists to receive text or notification alerts for nearby shows, purchase tickets via mobile without downloading an app, and access live event information for music and entertainment. Seated serves independent artists and major touring acts including Noah Kahan, Shawn Mendes, Brandi Carlile, Post Malone, and Billie Eilish, operating as an independent founder-led company focused on direct artist-to-fan ticketing.
finops:
- name: Seated Finops
  service_category: ''
  slug: seated-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/seated.png
layout: provider
modified: '2026-06-13'
name: Seated
nav: Providers
network: true
overview: 'Seated publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include live events, concerts, ticketing, artists, and venues.


  Seated''s developer surface includes documentation, getting-started guide, engineering blog, and 8 more developer resources.'
plans:
- name: Seated Plans Pricing
  plan_count: 3
  slug: seated-plans-pricing
random_paper: 70
rate_limits:
- limit_count: 2
  name: Seated Rate Limits
  slug: seated-rate-limits
score:
  band: emerging
  composite: 26.0
  delta: -2.4
  facets:
    commercial_clarity: 60.5
    contract_quality: 0.0
    developer_ergonomics: 21.7
    discoverability: 68.5
    governance: 0.0
    operational_transparency: 21.1
  previous_composite: 28.4
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/seated/refs/heads/main/screenshots/seated-2026-06-20T193617.png
security:
- kind: domain-security
  name: Seated Domain Security
  slug: seated-domain-security
  summary_line: TLSv1.3 · DMARC
slug: seated
tags:
- live events
- concerts
- ticketing
- artists
- venues
- tour dates
- fan notifications
- presales
- music
- entertainment
website: https://www.seated.com/
---
