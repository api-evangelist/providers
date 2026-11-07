---
access_model:
  confidence: low
  label: Requires approval
  onboarding: approval
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
api_count: 0
artifact_total: 1
common:
- group: other
  href: https://artifacts.apis.io/cartwheelcare-org/hosts/cartwheelcare-org-hosts.yml
  title: ''
  type: Hosts
  url: hosts/cartwheelcare-org-hosts.yml
- group: other
  href: https://artifacts.apis.io/cartwheelcare-org/vendors/cartwheelcare-org-vendors.yml
  title: ''
  type: Vendors
  url: vendors/cartwheelcare-org-vendors.yml
- group: company
  title: ''
  type: Newsroom
  url: https://www.cartwheel.org/category/press
- group: auth
  href: https://artifacts.apis.io/cartwheelcare-org/security/cartwheelcare-org-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/cartwheelcare-org-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.cartwheel.org
coverage:
  detail: the company publishes no developer documentation host and no machine-readable contract on its own domain
  evidence:
  - status: 200
    url: https://cartwheelcare.org
  reason: no-developer-program
  state: none
created: '2026-10-22'
description: Cartwheel provides evidence‑based mental health care for K‑12 students, offering licensed clinicians, bilingual coordinators, and a digital portal that eliminates waitlists. Partnering with school districts, they deliver personalized support, insurance handling, and rapid appointment scheduling, aiming to improve student wellbeing and academic outcomes.
image: https://cdn.prod.website-files.com/652d3415e3dc44a9873b9dd5/656f84e722dda2983177b8a0_Group%2051.png
layout: provider
modified: '2026-10-22'
name: Cartwheel
nav: Providers
network: true
overview: Cartwheel is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Mental Health, Education, B2B, Software-as-a-Service, and Healthcare.
random_paper: 15
score:
  band: minimal
  composite: 3.8
  coverage:
    artifact_dirs: 7
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -0.1
  facets:
    access_clarity: 0.0
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 0.0
    discoverability: 49.1
    operational_transparency: 0.0
  needs_work:
    note: Recorded so this provider's gaps can be attributed. Does not affect the composite above.
    owner: catalog
    reasons:
    - owner: catalog
      reason: not_a_repo
  previous_composite: 3.9
  provenance:
    mcp: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Health
    regime_id: health
    score: 4.7
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
screenshot: https://apis.io/screenshots/cartwheelcare-org/cartwheelcare-org-2026-11-03T123427.png
security:
- kind: domain-security
  name: Cartwheelcare Org Domain Security
  slug: cartwheelcare-org-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
slug: cartwheelcare-org
tags:
- Mental Health
- Education
- B2B
- Software-as-a-Service
- Healthcare
website: https://www.cartwheel.org
---
