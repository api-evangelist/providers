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
api_count: 0
artifact_total: 1
common:
- group: other
  href: https://artifacts.apis.io/alphaeon/hosts/alphaeon-hosts.yml
  title: ''
  type: Hosts
  url: hosts/alphaeon-hosts.yml
- group: other
  href: https://artifacts.apis.io/alphaeon/vendors/alphaeon-vendors.yml
  title: ''
  type: Vendors
  url: vendors/alphaeon-vendors.yml
- group: start
  title: ''
  type: Login
  url: https://goalphaeon.com/login
- group: auth
  href: https://artifacts.apis.io/alphaeon/security/alphaeon-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/alphaeon-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.goalphaeon.com/
coverage:
  checked: '2026-10-05'
  detail: The website returns HTML but provides no machine‑readable API documentation.
  evidence:
  - status: 200
    url: https://www.goalphaeon.com/
  reason: js-rendered-docs
  state: unreadable
created: '2026-09-24'
description: Alphaeon provides consumer financing solutions for healthcare procedures, allowing patients to spread the cost of medical, dental, vision, and cosmetic treatments over time. Through its credit platform, Alphaeon offers flexible payment plans, pre‑qualification without impacting credit scores, and a seamless online application process. The company partners with providers to make elective and necessary care more affordable, aiming to improve access to health services while supporting financial wellbeing.
image: http://static1.squarespace.com/static/583ef043f5e2313f41d80cf0/t/662045a77eeddd5bef18e610/1713391015741/Alphaeon_Credit_logo_registered_RGB.png?format=1500w
layout: provider
modified: '2026-09-24'
name: Alphaeon
nav: Providers
network: true
overview: Alphaeon is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Finance, Healthcare, Consumer Credit, and Payments.
random_paper: 0
score:
  band: minimal
  composite: 5.0
  coverage:
    artifact_dirs: 8
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -1.4
  facets:
    access_clarity: 6.6
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 0.0
    discoverability: 48.2
    operational_transparency: 0.0
  previous_composite: 6.4
  provenance:
    mcp: unknown
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
screenshot: https://apis.io/screenshots/alphaeon/alphaeon-2026-11-03T120713.png
security:
- kind: domain-security
  name: Alphaeon Domain Security
  slug: alphaeon-domain-security
  summary_line: TLSv1.3 · HSTS
slug: alphaeon
tags:
- Company
- Finance
- Healthcare
- Consumer Credit
- Payments
website: https://www.goalphaeon.com/
---
