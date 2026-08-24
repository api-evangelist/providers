---
access_model:
  confidence: high
  label: Paid (free trial) · Self-serve signup
  onboarding: self-serve
  pricing: paid
  public: false
  source:
  - plans
  - authentication
  trial: true
  try_now: true
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: partial
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 32.1
  scored_at: '2026-08-24'
agentic_access:
- acting_count: 10
  human_in_the_loop: 0
  name: Captivate Fm Agentic Access
  operation_count: 28
  slug: captivate-fm-agentic-access
  summary_line: 28 operations · 10 acting
api_count: 6
apis:
- description: Podcast and episode listening analytics (insights).
  name: Captivate Analytics API
  slug: captivate-fm-analytics-api
- description: Exchange a user ID and API token for a Bearer token.
  name: Captivate Authentication API
  slug: captivate-fm-authentication-api
- description: List, read, create, and update episodes.
  name: Captivate Episodes API
  slug: captivate-fm-episodes-api
- description: Upload, read, list, and search a show's audio media.
  name: Captivate Media API
  slug: captivate-fm-media-api
- description: Read and update shows, upload artwork, get the RSS feed URL.
  name: Captivate Shows API
  slug: captivate-fm-shows-api
- description: Read a user and list the shows they can access or manage.
  name: Captivate Users API
  slug: captivate-fm-users-api
artifact_total: 20
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Captivate Analytics API
  slug: open-captivate-fm-analytics-api
- collection_type: open
  name: Captivate Analytics Authentication API
  slug: open-captivate-fm-authentication-api
- collection_type: open
  name: Captivate Analytics Episodes API
  slug: open-captivate-fm-episodes-api
- collection_type: open
  name: Captivate Analytics Media API
  slug: open-captivate-fm-media-api
- collection_type: open
  name: Captivate Analytics Shows API
  slug: open-captivate-fm-shows-api
- collection_type: open
  name: Captivate Analytics Users API
  slug: open-captivate-fm-users-api
- collection_type: open
  name: Captivate API
  slug: open-captivate-fm
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/captivate-fm-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/captivate-fm-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/captivate-fm-authentication.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/captivate-fm
- group: company
  title: ''
  type: Website
  url: https://www.captivate.fm/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.captivate.fm/
- group: docs
  title: ''
  type: SupportDocumentation
  url: https://help.captivate.fm/en/
- group: operate
  title: ''
  type: StatusPage
  url: https://status.captivate.fm
- group: commercial
  title: ''
  type: Plans
  url: plans/captivate-fm-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/captivate-fm-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/captivate-fm-finops.yml
created: '2026-07-05'
description: Captivate is a growth-oriented podcast hosting, distribution, and analytics platform. Its public REST API at https://api.captivate.fm lets developers authenticate a user, read and manage shows and their RSS feeds, create and update episodes, upload and search media (audio) files, and pull detailed listening analytics (insights) at the podcast and episode level. Access is self-serve - any account holder can generate a user ID and API token from the API section of their Captivate account and exchange them for a Bearer token. The API is documented as a public Postman collection at docs.captivate.fm.
finops:
- name: Captivate Fm Finops
  service_category: Media and Podcast Hosting
  slug: captivate-fm-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/captivate-fm.png
layout: provider
modified: '2026-07-05'
name: Captivate
nav: Providers
network: true
overview: 'Captivate publishes 6 APIs on the [APIs.io](https://apis.io/) network, including Analytics API, Authentication API, Episodes API, and 3 more. Tagged areas include Podcasting, Podcast Hosting, Episodes, Media, and Analytics.


  Captivate''s developer surface includes authentication, documentation, and 9 more developer resources.'
plans:
- name: Captivate Fm Plans Pricing
  plan_count: 3
  slug: captivate-fm-plans-pricing
random_paper: 20
rate_limits:
- limit_count: 3
  name: Captivate Fm Rate Limits
  slug: captivate-fm-rate-limits
score:
  band: developing
  composite: 40.6
  delta: 0.0
  facets:
    access_clarity: 39.5
    commercial_clarity: 39.5
    contract_governance: 0.0
    contract_quality: 59.4
    developer_ergonomics: 21.4
    discoverability: 74.1
    governance: 0.0
    operational_transparency: 47.4
  previous_composite: 40.6
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 6
  schema_version: 0.12.1
  scored_at: '2026-08-24'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/captivate-fm/refs/heads/main/screenshots/captivate-fm-2026-07-25T204454.png
security:
- kind: authentication
  name: Captivate Fm Authentication
  slug: captivate-fm-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Captivate Fm Domain Security
  slug: captivate-fm-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: captivate-fm
tags:
- Podcasting
- Podcast Hosting
- Episodes
- Media
- Analytics
- RSS
website: https://www.captivate.fm/
---
