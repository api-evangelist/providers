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
- description: API documentation portal for CareTaker Medical
  name: CareTaker Medical API
  slug: caretaker-medical-api
artifact_total: 2
common:
- group: other
  href: https://artifacts.apis.io/caretaker-medical/hosts/caretaker-medical-hosts.yml
  title: ''
  type: Hosts
  url: hosts/caretaker-medical-hosts.yml
- group: other
  href: https://artifacts.apis.io/caretaker-medical/vendors/caretaker-medical-vendors.yml
  title: ''
  type: Vendors
  url: vendors/caretaker-medical-vendors.yml
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://caretakermedical.net/privacy-policy/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://portal.caretakermedical.net/
- group: company
  title: ''
  type: Blog
  url: https://caretakermedical.net/blog/category/er/
- group: auth
  href: https://artifacts.apis.io/caretaker-medical/security/caretaker-medical-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/caretaker-medical-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://caretakermedical.net/
coverage:
  checked: '2026-10-07'
  detail: Documentation portal returns HTML without any machine‑readable OpenAPI, AsyncAPI, GraphQL or WSDL files.
  evidence:
  - status: 200
    url: https://portal.caretakermedical.net/
  reason: js-rendered-docs
  state: unreadable
created: '2026-10-07'
description: Caretaker Medical provides the VitalStream platform, a device that delivers continuous, beat‑to‑beat hemodynamic monitoring both invasively and non‑invasively. The system is sold to hospitals and other care settings for use in pre‑operative, operating‑room, ICU, step‑down and ambulatory surgery environments, integrating with existing GE Carescape and Philips Intellivue monitors.
image: https://caretakermedical.net/wp-content/uploads/2024/03/cropped-favicon.png
layout: provider
modified: '2026-10-07'
name: CareTaker Medical
nav: Providers
network: true
overview: 'CareTaker Medical is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Hemodynamic Monitoring, ICU Monitoring, Non‑invasive Monitoring, and Clinical Monitoring.


  CareTaker Medical''s developer surface includes engineering blog and 6 more developer resources.'
random_paper: 6
score:
  band: minimal
  composite: 6.2
  coverage:
    artifact_dirs: 9
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -2.5
  facets:
    access_clarity: 5.3
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 6.0
    discoverability: 48.2
    operational_transparency: 0.0
  previous_composite: 8.7
  provenance:
    mcp: unknown
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
screenshot: https://apis.io/screenshots/caretaker-medical/caretaker-medical-2026-11-03T123351.png
security:
- kind: domain-security
  name: Caretaker Medical Domain Security
  slug: caretaker-medical-domain-security
  summary_line: TLSv1.3 · DNSSEC · DMARC
slug: caretaker-medical
tags:
- Hemodynamic Monitoring
- ICU Monitoring
- Non‑invasive Monitoring
- Clinical Monitoring
website: https://caretakermedical.net/
---
