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
  scored_at: '2026-08-11'
api_count: 1
apis:
- description: API explorer that gives a query URL with a JSON response of locations and cities
  name: Ducks Unlimited
  slug: ducks-unlimited
artifact_total: 3
common:
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/ducks-unlimited-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/ducks-unlimited-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://gis.ducks.org/datasets/du-university-chapters/api
- group: other
  title: ''
  type: PublicAPIsListing
  url: https://github.com/public-apis/public-apis
- group: company
  title: ''
  type: Blog
  url: https://www.ducks.org/newsroom
created: '2026-05-28'
description: API explorer that gives a query URL with a JSON response of locations and cities
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/ducks-unlimited.png
layout: provider
modified: '2026-05-28'
name: Ducks Unlimited
nav: Providers
network: true
overview: 'Ducks Unlimited publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Geocoding and Public APIs.


  Ducks Unlimited''s developer surface includes engineering blog and 4 more developer resources.'
random_paper: 46
score:
  band: minimal
  composite: 6.2
  delta: 0.0
  facets:
    commercial_clarity: 0.0
    contract_quality: 0.0
    developer_ergonomics: 2.2
    discoverability: 57.4
    governance: 0.0
    operational_transparency: 0.0
  previous_composite: 6.2
  schema_version: 0.11.0
  scored_at: '2026-08-11'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/ducks-unlimited/refs/heads/main/screenshots/ducks-unlimited-2026-06-20T180309.png
security:
- kind: domain-security
  name: Ducks Unlimited Domain Security
  slug: ducks-unlimited-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Ducks Unlimited Vulnerability Disclosure
  slug: ducks-unlimited-vulnerability-disclosure
  summary_line: disclosure policy published
slug: ducks-unlimited
tags:
- Geocoding
- Public APIs
website: https://gis.ducks.org/datasets/du-university-chapters/api
---
