---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source:
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
- description: The Well provides wellness services and member amenities; API documentation is not publicly machine‑readable.
  name: The Well API
  slug: the-well-api
artifact_total: 2
common:
- group: other
  href: https://artifacts.apis.io/the-well/hosts/the-well-hosts.yml
  title: ''
  type: Hosts
  url: hosts/the-well-hosts.yml
- group: other
  href: https://artifacts.apis.io/the-well/vendors/the-well-vendors.yml
  title: ''
  type: Vendors
  url: vendors/the-well-vendors.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.the-well.com/terms-and-conditions
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.the-well.com/privacy
- group: auth
  href: https://artifacts.apis.io/the-well/security/the-well-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/the-well-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.the-well.com/
coverage:
  checked: '2026-10-23'
  detail: The website serves only rendered HTML with no machine‑readable OpenAPI or other contract files.
  evidence:
  - status: 200
    url: https://www.the-well.com/
  reason: js-rendered-docs
  state: unreadable
created: '2026-10-22'
description: THE WELL is a wellness brand offering clubs, residences, and office spaces that integrate modern medicine, ancient healing, and whole‑person care. It provides members with health‑focused amenities, community programs, and integrated services aimed at improving physical, mental, and emotional wellbeing across its locations.
image: https://the-well.com/the-well.jpeg
layout: provider
modified: '2026-10-22'
name: THE WELL
nav: Providers
network: true
overview: THE WELL is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Wellness, Real Estate, Health, Community, and Lifestyle.
random_paper: 10
score:
  band: minimal
  composite: 7.2
  coverage:
    artifact_dirs: 8
    catalog_earned: 32.0
    catalog_earned_first_party: 0.0
    catalog_gap: 83.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -2.6
  facets:
    access_clarity: 10.5
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 0.0
    discoverability: 57.1
    operational_transparency: 0.0
  needs_work:
    note: Recorded so this provider's gaps can be attributed. Does not affect the composite above.
    owner: catalog
    reasons:
    - owner: catalog
      reason: not_a_repo
  previous_composite: 9.8
  provenance:
    mcp: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Health
    regime_id: health
    score: 7.8
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
screenshot: https://apis.io/screenshots/the-well/the-well-2026-11-03T144558.png
security:
- kind: domain-security
  name: The Well Domain Security
  slug: the-well-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: the-well
tags:
- Wellness
- Real Estate
- Health
- Community
- Lifestyle
website: https://www.the-well.com/
---
