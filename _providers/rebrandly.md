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
- description: Custom URL shortener for sharing branded links
  name: Rebrandly
  slug: rebrandly
artifact_total: 4
common:
- group: auth
  title: ''
  type: TrustCenter
  url: security/rebrandly-trust-center.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/rebrandly-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/rebrandly-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://developers.rebrandly.com/v1/docs
- group: other
  title: ''
  type: PublicAPIsListing
  url: https://github.com/public-apis/public-apis
created: '2026-05-28'
description: Custom URL shortener for sharing branded links
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/rebrandly.png
layout: provider
modified: '2026-05-28'
name: Rebrandly
nav: Providers
network: true
overview: Rebrandly publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include URL Shorteners and Public APIs.
random_paper: 18
score:
  band: minimal
  composite: 8.3
  coverage:
    artifact_dirs: 2
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 7.9
    commercial_clarity: 7.9
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 4.8
    discoverability: 57.4
    governance: 0.0
    operational_transparency: 0.0
  previous_composite: 8.3
  schema_version: 0.18.3
  scored_at: '2026-09-04'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/rebrandly/refs/heads/main/screenshots/rebrandly-2026-06-20T192656.png
security:
- kind: domain-security
  name: Rebrandly Domain Security
  slug: rebrandly-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
- kind: vulnerability-disclosure
  name: Rebrandly Vulnerability Disclosure
  slug: rebrandly-vulnerability-disclosure
  summary_line: security.txt · contact published
- kind: trust-center
  name: Rebrandly Trust Center
  slug: rebrandly-trust-center
  summary_line: SOC 2, HIPAA, GDPR
slug: rebrandly
tags:
- URL Shorteners
- Public APIs
website: https://developers.rebrandly.com/v1/docs
---
