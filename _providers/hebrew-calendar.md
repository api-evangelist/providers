---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source: []
  trial: false
  try_now: false
agent_readiness:
  band: human-only
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    auth_clarity: false
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 0.0
  scored_at: '2026-08-12'
api_count: 1
apis:
- description: Convert between Gregorian and Hebrew, fetch Shabbat and Holiday times, etc
  name: Hebrew Calendar
  slug: hebrew-calendar
artifact_total: 3
common:
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/hebrew-calendar-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/hebrew-calendar-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.hebcal.com/home/developer-apis
- group: other
  title: ''
  type: PublicAPIsListing
  url: https://github.com/public-apis/public-apis
created: '2026-05-28'
description: Convert between Gregorian and Hebrew, fetch Shabbat and Holiday times, etc
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/hebrew-calendar.png
layout: provider
modified: '2026-05-28'
name: Hebrew Calendar
nav: Providers
network: true
overview: Hebrew Calendar publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Calendar and Public APIs.
random_paper: 68
score:
  band: minimal
  composite: 5.7
  delta: 0.0
  facets:
    commercial_clarity: 0.0
    contract_quality: 0.0
    developer_ergonomics: 0.0
    discoverability: 57.4
    governance: 0.0
    operational_transparency: 0.0
  previous_composite: 5.7
  schema_version: 0.11.0
  scored_at: '2026-08-12'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/hebrew-calendar/refs/heads/main/screenshots/hebrew-calendar-2026-06-20T182608.png
security:
- kind: domain-security
  name: Hebrew Calendar Domain Security
  slug: hebrew-calendar-domain-security
  summary_line: TLSv1.3 · DMARC
- kind: vulnerability-disclosure
  name: Hebrew Calendar Vulnerability Disclosure
  slug: hebrew-calendar-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: hebrew-calendar
tags:
- Calendar
- Public APIs
website: https://www.hebcal.com/home/developer-apis
---
