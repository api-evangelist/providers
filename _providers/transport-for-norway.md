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
- description: Transport APIs and dataset for Norway
  name: Transport for Norway
  slug: transport-for-norway
artifact_total: 3
common:
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/transport-for-norway-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/transport-for-norway-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://developer.entur.org/
- group: other
  title: ''
  type: PublicAPIsListing
  url: https://github.com/public-apis/public-apis
created: '2026-05-28'
description: Transport APIs and dataset for Norway
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/transport-for-norway.png
layout: provider
modified: '2026-05-28'
name: Transport for Norway
nav: Providers
network: true
overview: Transport for Norway publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Transportation and Public APIs.
random_paper: 15
score:
  band: minimal
  composite: 5.7
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
    developer_ergonomics: 0.0
    discoverability: 57.4
    governance: 0.0
    operational_transparency: 0.0
  previous_composite: 5.7
  schema_version: 0.18.3
  scored_at: '2026-09-04'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/transport-for-norway/refs/heads/main/screenshots/transport-for-norway-2026-06-20T195610.png
security:
- kind: domain-security
  name: Transport For Norway Domain Security
  slug: transport-for-norway-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
- kind: vulnerability-disclosure
  name: Transport For Norway Vulnerability Disclosure
  slug: transport-for-norway-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: transport-for-norway
tags:
- Transportation
- Public APIs
website: https://developer.entur.org/
---
