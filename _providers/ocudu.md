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
    rate_limit_signal: derived
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: '0.2'
  score: 0.6
  scored_at: '2026-10-17'
api_count: 1
apis:
- description: API for the OCUDU Ecosystem Foundation, providing programmatic access to the open collaboration platform for Radio Access Network reference implementations and AI-based RAN algorithms.
  name: OCUDU Ecosystem Foundation API
  slug: ocudu-api
artifact_total: 6
common:
- group: commercial
  href: https://raw.githubusercontent.com/api-evangelist/ocudu/refs/heads/main/plans/ocudu-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/ocudu-plans-pricing.yml
- group: operate
  href: https://raw.githubusercontent.com/api-evangelist/ocudu/refs/heads/main/rate-limits/ocudu-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/ocudu-rate-limits.yml
- group: commercial
  href: https://raw.githubusercontent.com/api-evangelist/ocudu/refs/heads/main/finops/ocudu-finops.yml
  title: ''
  type: FinOps
  url: finops/ocudu-finops.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/ocudu/refs/heads/main/security/ocudu-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/ocudu-vulnerability-disclosure.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/ocudu/refs/heads/main/security/ocudu-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/ocudu-domain-security.yml
- group: docs
  title: ''
  type: Documentation
  url: https://www.linuxfoundation.org/
- group: build
  title: ''
  type: GitHubOrg
  url: https://github.com/ocudu
- group: company
  title: ''
  type: Blog
  url: https://ocudu.org/feed/
created: '2026-03-16'
description: The OCUDU Ecosystem Foundation is a Linux Foundation project announced at MWC Barcelona in March 2026. It is an open collaboration hub dedicated to building a foundational reference platform for Radio Access Networks including AI-based algorithms, with founding members AMD, AT&T, Ericsson, Nokia, NVIDIA, and Verizon.
finops:
- has_sources: false
  method: generated
  name: Ocudu Finops
  primary_unit: ''
  service_category: API
  slug: ocudu-finops
  template: true
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/ocudu.png
layout: provider
modified: '2026-07-25'
name: OCUDU Ecosystem Foundation
nav: Providers
network: true
overview: 'OCUDU Ecosystem Foundation is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Artificial Intelligence, Linux Foundation, RAN, and Telecommunications.


  OCUDU Ecosystem Foundation''s developer surface includes documentation, engineering blog, and 6 more developer resources.'
plans:
- name: Ocudu Plans Pricing
  plan_count: 3
  slug: ocudu-plans-pricing
random_paper: 16
rate_limits:
- limit_count: 5
  name: Ocudu Rate Limits
  slug: ocudu-rate-limits
score:
  band: minimal
  composite: 8.8
  coverage:
    artifact_dirs: 6
    catalog_earned: 33.0
    catalog_earned_first_party: 0.0
    catalog_gap: 82.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -1.7
  facets:
    access_clarity: 7.9
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 11.9
    discoverability: 48.2
    operational_transparency: 13.2
  previous_composite: 10.5
  regulatory:
    applies: true
    matched_via: tags
    regime: Telecommunications
    regime_id: telecommunications
    score: 9.4
  schema_version: 0.24.0
  scored_at: '2026-10-17'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
screenshot: https://raw.githubusercontent.com/api-evangelist/ocudu/refs/heads/main/screenshots/ocudu-2026-06-20T190617.png
security:
- kind: domain-security
  name: Ocudu Domain Security
  slug: ocudu-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Ocudu Vulnerability Disclosure
  slug: ocudu-vulnerability-disclosure
  summary_line: no policy recorded
slug: ocudu
tags:
- Artificial Intelligence
- Linux Foundation
- RAN
- Telecommunications
---
