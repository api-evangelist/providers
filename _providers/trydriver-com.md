---
access_model:
  confidence: medium
  gated: none
  gated_source:
  - onboarding
  label: Paid · Open access
  onboarding: open
  pricing: paid
  public: true
  source:
  - plans
  - authentication
  - security
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
    mcp_tool_quality: na
    openapi_examples: false
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: '0.2'
  score: 0.0
  scored_at: '2026-11-06'
api_count: 1
apis:
- description: API for Driver platform, providing dashcam video and analytics.
  name: Driver API
  slug: driver-api
artifact_total: 6
common:
- group: commercial
  href: https://artifacts.apis.io/trydriver-com/plans/trydriver-com-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/trydriver-com-plans-pricing.yml
- group: other
  href: https://artifacts.apis.io/trydriver-com/hosts/trydriver-com-hosts.yml
  title: ''
  type: Hosts
  url: hosts/trydriver-com-hosts.yml
- group: other
  href: https://artifacts.apis.io/trydriver-com/vendors/trydriver-com-vendors.yml
  title: ''
  type: Vendors
  url: vendors/trydriver-com-vendors.yml
- group: auth
  href: https://artifacts.apis.io/trydriver-com/security/trydriver-com-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/trydriver-com-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/trydriver-com/security/trydriver-com-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/trydriver-com-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://drivertechnologies.com/
- group: commercial
  title: ''
  type: Pricing
  url: https://drivertechnologies.com/pricing/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://drivertechnologies.com/privacy-policy/
- group: auth
  title: ''
  type: Security
  url: https://drivertechnologies.com/security/
coverage:
  checked: '2026-10-29'
  detail: OpenAPI spec files were not found at standard locations on the API hosts (e.g., https://api.drivertechnologies.com/openapi.json returned 404).
  evidence:
  - status: 404
    url: https://api.drivertechnologies.com/openapi.json
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-10-29'
description: Driver turns your phone into an AI dash cam with free HD recording that flags risky moments and saves every trip to the cloud on iPhone and Android. The flagship Driver app provides safety coaching, community‑sourced road intelligence, and partners with fleets and mobility platforms to deliver smarter roads. It records every trip, flags risky moments, and stores video in Driver Cloud, offering free plans for drivers and paid options for families, driving schools, and fleets.
image: https://drivertechnologies.com/og/driver.jpg
layout: provider
modified: '2026-10-29'
name: Driver
nav: Providers
network: true
overview: 'Driver is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Artificial Intelligence, Dash Cam, Mobile, and Safety.


  Driver''s developer surface includes pricing and 8 more developer resources.'
plans:
- name: Trydriver Com Plans Pricing
  plan_count: 4
  slug: trydriver-com-plans-pricing
random_paper: 23
scopes:
- name: Trydriver Com Scopes
  scope_count: 0
  slug: trydriver-com-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: emerging
  composite: 16.7
  coverage:
    artifact_dirs: 19
    catalog_earned: 49.0
    catalog_earned_first_party: 12.0
    catalog_gap: 66.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -3.1
  facets:
    access_clarity: 42.1
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 0.0
    discoverability: 66.1
    operational_transparency: 5.3
  needs_work:
    note: Recorded so this provider's gaps can be attributed. Does not affect the composite above.
    owner: catalog
    reasons:
    - owner: catalog
      reason: not_a_repo
  previous_composite: 19.8
  provenance:
    conformance: unknown
    mcp: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 21.8
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
screenshot: https://apis.io/screenshots/trydriver-com/trydriver-com-2026-11-03T145131.png
security:
- kind: authentication
  name: Trydriver Com Authentication
  slug: trydriver-com-authentication
  summary_line: 0 schemes
- kind: domain-security
  name: Trydriver Com Domain Security
  slug: trydriver-com-domain-security
  summary_line: TLSv1.3 · DMARC
- kind: vulnerability-disclosure
  name: Trydriver Com Vulnerability Disclosure
  slug: trydriver-com-vulnerability-disclosure
  summary_line: no policy recorded
slug: trydriver-com
tags:
- Company
- Artificial Intelligence
- Dash Cam
- Mobile
- Safety
- Fleet Management
website: https://drivertechnologies.com/
---
