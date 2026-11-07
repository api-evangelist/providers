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
  href: https://artifacts.apis.io/dozee/hosts/dozee-hosts.yml
  title: ''
  type: Hosts
  url: hosts/dozee-hosts.yml
- group: other
  href: https://artifacts.apis.io/dozee/vendors/dozee-vendors.yml
  title: ''
  type: Vendors
  url: vendors/dozee-vendors.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.dozeehealth.ai/terms-of-use
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.dozeehealth.ai/privacypolicy
- group: company
  title: ''
  type: Newsroom
  url: https://www.dozeehealth.ai/media
- group: auth
  href: https://artifacts.apis.io/dozee/security/dozee-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/dozee-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.dozeehealth.ai
coverage:
  detail: the company publishes no developer documentation host and no machine-readable contract on its own domain
  evidence:
  - status: 200
    url: https://www.dozeehealth.ai
  - status: 403
    url: https://equityzen.com/company/dozee
  reason: no-developer-program
  state: none
created: '2026-10-24'
description: Dozee provides contactless remote patient monitoring solutions using ballistocardiography and AI. Their platform captures micro‑vibrations from a sensor sheet under a mattress to deliver vital signs, alerts, and health insights for hospitals and home care, aiming to improve patient safety and reduce nursing workload.
layout: provider
modified: '2026-10-24'
name: Dozee
nav: Providers
network: true
overview: Dozee is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Healthcare, Remote Monitoring, Artificial Intelligence, and Ballistocardiography.
random_paper: 7
score:
  band: minimal
  composite: 5.9
  coverage:
    artifact_dirs: 9
    catalog_earned: 25.0
    catalog_earned_first_party: 0.0
    catalog_gap: 90.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -2.7
  facets:
    access_clarity: 10.5
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 0.0
    discoverability: 45.5
    operational_transparency: 0.0
  previous_composite: 8.6
  provenance:
    mcp: unknown
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
screenshot: https://apis.io/screenshots/dozee/dozee-2026-11-03T131013.png
security:
- kind: domain-security
  name: Dozee Domain Security
  slug: dozee-domain-security
  summary_line: TLSv1.3 · HSTS
slug: dozee
tags:
- Company
- Healthcare
- Remote Monitoring
- Artificial Intelligence
- Ballistocardiography
website: https://www.dozeehealth.ai
---
