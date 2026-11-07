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
- group: agent
  href: https://artifacts.apis.io/lungpacer-medical/llms/lungpacer-medical-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/lungpacer-medical-llms.txt
- group: other
  href: https://artifacts.apis.io/lungpacer-medical/hosts/lungpacer-medical-hosts.yml
  title: ''
  type: Hosts
  url: hosts/lungpacer-medical-hosts.yml
- group: other
  href: https://artifacts.apis.io/lungpacer-medical/vendors/lungpacer-medical-vendors.yml
  title: ''
  type: Vendors
  url: vendors/lungpacer-medical-vendors.yml
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://lungpacer.com/privacy-policy/
- group: auth
  href: https://artifacts.apis.io/lungpacer-medical/security/lungpacer-medical-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/lungpacer-medical-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.lungpacer.com
coverage:
  detail: the company publishes no developer documentation host and no machine-readable contract on its own domain
  evidence:
  - status: 200
    url: https://www.lungpacer.com
  reason: no-developer-program
  state: none
created: '2026-10-26'
description: Lungpacer Medical provides the AeroPace® temporary transvenous diaphragm neurostimulation system, a catheter‑based device that stimulates the phrenic nerves to activate the diaphragm. The system is indicated for patients 18 years or older who have been on mechanical ventilation for at least 96 hours and have not weaned, aiming to improve weaning success, reduce ventilator days, and lower reintubation risk. It is marketed to hospitals and critical‑care providers for use in intensive care settings.
image: https://lungpacer.com/wp-content/uploads/2025/12/Lungpacer_OG_1200x630.png
layout: provider
modified: '2026-10-26'
name: Lungpacer Medical
nav: Providers
network: true
overview: Lungpacer Medical is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Diaphragm Pacing, Neurostimulation, Ventilator Weaning, Critical Care, and Medical Devices.
random_paper: 21
score:
  band: minimal
  composite: 5.7
  coverage:
    artifact_dirs: 7
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -1.3
  facets:
    access_clarity: 5.3
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 0.0
    discoverability: 55.4
    operational_transparency: 0.0
  needs_work:
    note: Recorded so this provider's gaps can be attributed. Does not affect the composite above.
    owner: catalog
    reasons:
    - owner: catalog
      reason: not_a_repo
  previous_composite: 7.0
  regulatory:
    applies: true
    matched_via: tags
    regime: Health
    regime_id: health
    score: 6.3
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
screenshot: https://apis.io/screenshots/lungpacer-medical/lungpacer-medical-2026-11-03T135127.png
security:
- kind: domain-security
  name: Lungpacer Medical Domain Security
  slug: lungpacer-medical-domain-security
  summary_line: TLSv1.3 · DMARC
slug: lungpacer-medical
tags:
- Diaphragm Pacing
- Neurostimulation
- Ventilator Weaning
- Critical Care
- Medical Devices
website: https://www.lungpacer.com
---
