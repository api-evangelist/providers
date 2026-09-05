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
- description: Translate between 21 of most used languages, accurate, unlimited requests
  name: Hirak Translation
  slug: hirak-translation
artifact_total: 3
common:
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/hirak-translation-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/hirak-translation-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://translate.hirak.site/
- group: other
  title: ''
  type: PublicAPIsListing
  url: https://github.com/public-apis/public-apis
created: '2026-05-28'
description: Translate between 21 of most used languages, accurate, unlimited requests
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/hirak-translation.png
layout: provider
modified: '2026-05-28'
name: Hirak Translation
nav: Providers
network: true
overview: Hirak Translation publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Text Analysis and Public APIs.
random_paper: 7
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
screenshot: https://raw.githubusercontent.com/api-evangelist/hirak-translation/refs/heads/main/screenshots/hirak-translation-2026-06-20T182755.png
security:
- kind: domain-security
  name: Hirak Translation Domain Security
  slug: hirak-translation-domain-security
  summary_line: TLSv1.3
- kind: vulnerability-disclosure
  name: Hirak Translation Vulnerability Disclosure
  slug: hirak-translation-vulnerability-disclosure
  summary_line: disclosure policy published
slug: hirak-translation
tags:
- Text Analysis
- Public APIs
website: https://translate.hirak.site/
---
