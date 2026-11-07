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
- description: Credo Health provides a platform for value‑based care integration, but no public machine‑readable API contract was found.
  name: Credo Health API
  slug: credo-health-api
artifact_total: 2
common:
- group: other
  href: https://artifacts.apis.io/credo-health/hosts/credo-health-hosts.yml
  title: ''
  type: Hosts
  url: hosts/credo-health-hosts.yml
- group: other
  href: https://artifacts.apis.io/credo-health/vendors/credo-health-vendors.yml
  title: ''
  type: Vendors
  url: vendors/credo-health-vendors.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.credohealth.com/terms-of-service
- group: operate
  title: ''
  type: Support
  url: https://support.credohealth.com/hc/en-us
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.credohealth.com/privacy-policy?hsLang=en
- group: auth
  href: https://artifacts.apis.io/credo-health/security/credo-health-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/credo-health-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.credohealth.com/
- group: company
  title: ''
  type: Blog
  url: https://www.credohealth.com/blog
- group: company
  title: ''
  type: About
  url: https://www.credohealth.com/about
- group: operate
  title: ''
  type: Contact
  url: https://www.credohealth.com/working-at-credo
- group: start
  title: ''
  type: ScheduleDemo
  url: https://www.credohealth.com/schedule-a-demo
coverage:
  checked: '2026-10-11'
  detail: OpenAPI endpoint returned HTML of a JavaScript app, no machine‑readable spec could be retrieved.
  evidence:
  - status: 200
    url: https://app.credohealth.com/openapi.json
  reason: js-rendered-docs
  state: unreadable
created: '2026-10-11'
description: Credo Health is an AI‑powered SaaS platform that enables physicians, health plans, MSOs, and ACOs to deliver value‑based care. It integrates with leading EHRs, provides analytics, and supports patient diagnosis and treatment workflows. The platform offers solutions such as Acquire, Inspect, Engage, and Optimize, and serves a broad range of healthcare organizations to improve outcomes and efficiency.
image: https://www.credohealth.com/hubfs/raw_assets/2/public/@projects/smart-growth-project/smart-growth-app/assets/images/Credo.jpg
layout: provider
modified: '2026-10-11'
name: Credo Health
nav: Providers
network: true
overview: 'Credo Health is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Healthcare, Artificial Intelligence, Software-as-a-Service, and Value-Based Care.


  Credo Health''s developer surface includes support, engineering blog, and 9 more developer resources.'
random_paper: 0
score:
  band: minimal
  composite: 7.8
  coverage:
    artifact_dirs: 9
    catalog_earned: 32.0
    catalog_earned_first_party: 0.0
    catalog_gap: 83.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -3.3
  facets:
    access_clarity: 10.5
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 3.6
    discoverability: 57.1
    operational_transparency: 0.0
  previous_composite: 11.1
  provenance:
    mcp: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Health
    regime_id: health
    score: 7.4
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
screenshot: https://apis.io/screenshots/credo-health/credo-health-2026-11-03T125551.png
security:
- kind: domain-security
  name: Credo Health Domain Security
  slug: credo-health-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: credo-health
tags:
- Company
- Healthcare
- Artificial Intelligence
- Software-as-a-Service
- Value-Based Care
website: https://www.credohealth.com/
---
