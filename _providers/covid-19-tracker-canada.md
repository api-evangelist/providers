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
- description: Details on Covid-19 cases across Canada
  name: COVID-19 Tracker Canada
  slug: covid-19-tracker-canada
artifact_total: 2
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/covid-19-tracker-canada-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://api.covid19tracker.ca/docs/1.0/overview
- group: other
  title: ''
  type: PublicAPIsListing
  url: https://github.com/public-apis/public-apis
created: '2026-05-28'
description: Details on Covid-19 cases across Canada
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/covid-19-tracker-canada.png
layout: provider
modified: '2026-05-28'
name: COVID-19 Tracker Canada
nav: Providers
network: true
overview: COVID-19 Tracker Canada publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Health and Public APIs.
random_paper: 1
score:
  band: minimal
  composite: 5.0
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
    developer_ergonomics: 4.8
    discoverability: 57.4
    governance: 0.0
    operational_transparency: 0.0
  previous_composite: 5.0
  regulatory:
    applies: true
    matched_via: tags
    regime: Health
    regime_id: health
    score: 7.5
  schema_version: 0.18.3
  scored_at: '2026-09-04'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/covid-19-tracker-canada/refs/heads/main/screenshots/covid-19-tracker-canada-2026-06-20T175137.png
security:
- kind: domain-security
  name: Covid 19 Tracker Canada Domain Security
  slug: covid-19-tracker-canada-domain-security
  summary_line: TLSv1.2
slug: covid-19-tracker-canada
tags:
- Health
- Public APIs
website: https://api.covid19tracker.ca/docs/1.0/overview
---
