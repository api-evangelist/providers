---
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
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: '0.2'
  score: 0.0
  scored_at: '2026-10-31'
api_count: 0
artifact_total: 1
common:
- group: other
  href: https://artifacts.apis.io/senseonics/hosts/senseonics-hosts.yml
  title: ''
  type: Hosts
  url: hosts/senseonics-hosts.yml
- group: other
  href: https://artifacts.apis.io/senseonics/vendors/senseonics-vendors.yml
  title: ''
  type: Vendors
  url: vendors/senseonics-vendors.yml
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.senseonics.com/investor-relations/privacy-notice
- group: company
  title: ''
  type: Newsroom
  url: https://www.senseonics.com/~/media/Files/S/Senseonics-IR/reports-and-presentations/promise-final-publication-dia-2021-0182.pdf
- group: auth
  href: https://artifacts.apis.io/senseonics/security/senseonics-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/senseonics-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.senseonics.com/
- group: company
  title: ''
  type: InvestorRelations
  url: https://www.senseonics.com/investor-relations
- group: company
  title: ''
  type: Careers
  url: https://www.senseonics.com/careers
- group: other
  title: ''
  type: Leadership
  url: https://www.senseonics.com/leadership
coverage:
  detail: the company publishes no developer documentation host and no machine-readable contract on its own domain
  evidence:
  - status: 200
    url: https://www.senseonics.com/
  reason: no-developer-program
  state: none
created: '2026-10-22'
description: Senseonics is a medical technology company that develops and commercializes the Eversense continuous glucose monitoring (CGM) system, an implantable sensor providing up to 365 days of glucose data for people with diabetes. The company’s website offers product information, clinical study results, investor relations, and corporate leadership details, reflecting its focus on innovative diabetes management solutions.
image: https://www.senseonics.com/~/media/Images/S/Senseonics-IR/logo/logo-social-media.jpg
layout: provider
modified: '2026-10-22'
name: Senseonics
nav: Providers
network: true
overview: Senseonics is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Medical, Diabetes, HealthTech, ImplantableDevices, and CGM.
random_paper: 2
score:
  band: minimal
  composite: 6.6
  coverage:
    artifact_dirs: 7
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 10.5
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 0.0
    discoverability: 51.8
    operational_transparency: 0.0
  provenance:
    mcp: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Health
    regime_id: health
    score: 7.8
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Senseonics Domain Security
  slug: senseonics-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: senseonics
tags:
- Medical
- Diabetes
- HealthTech
- ImplantableDevices
- CGM
website: https://www.senseonics.com/
---
