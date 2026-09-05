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
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 0.0
  scored_at: '2026-09-04'
api_count: 1
apis:
- description: Take programmatic screenshots of web pages from any website
  name: Screenshot
  slug: screenshot
artifact_total: 2
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/screenshot-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.abstractapi.com/website-screenshot-api
- group: other
  title: ''
  type: PublicAPIsListing
  url: https://github.com/public-apis/public-apis
created: '2026-05-28'
description: Take programmatic screenshots of web pages from any website
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/screenshot.png
layout: provider
modified: '2026-05-28'
name: Screenshot
nav: Providers
network: true
overview: Screenshot publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Development and Public APIs.
random_paper: 15
score:
  band: minimal
  composite: 7.6
  coverage:
    artifact_dirs: 2
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 0.0
    commercial_clarity: 0.0
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 9.5
    discoverability: 57.4
    governance: 0.0
    operational_transparency: 0.0
  previous_composite: 7.6
  schema_version: 0.18.3
  scored_at: '2026-09-04'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/screenshot/refs/heads/main/screenshots/screenshot-2026-06-20T193602.png
security:
- kind: domain-security
  name: Screenshot Domain Security
  slug: screenshot-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: screenshot
tags:
- Development
- Public APIs
website: https://www.abstractapi.com/website-screenshot-api
---
