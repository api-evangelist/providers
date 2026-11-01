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
    mcp_server: documented
    openapi_examples: false
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: '0.2'
  score: 3.1
  scored_at: '2026-10-31'
api_count: 0
artifact_total: 1
common:
- group: other
  href: https://artifacts.apis.io/rotation-medical/hosts/rotation-medical-hosts.yml
  title: ''
  type: Hosts
  url: hosts/rotation-medical-hosts.yml
- group: other
  href: https://artifacts.apis.io/rotation-medical/vendors/rotation-medical-vendors.yml
  title: ''
  type: Vendors
  url: vendors/rotation-medical-vendors.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.medicalrotations.com/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.medicalrotations.com/privacy
- group: start
  title: ''
  type: Login
  url: https://www.medicalrotations.com/login
- group: auth
  href: https://artifacts.apis.io/rotation-medical/security/rotation-medical-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/rotation-medical-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.medicalrotations.com/
coverage:
  detail: the company publishes no developer documentation host and no machine-readable contract on its own domain
  evidence:
  - status: 200
    url: https://www.medicalrotations.com/
  reason: no-developer-program
  state: none
created: '2026-10-26'
description: MedicalRotations provides a premier clinical experience solution connecting medical students, schools, and preceptors with top U.S. clinical facilities. The platform offers tailored rotation opportunities, streamlined sign‑up processes, and support for educational institutions to expand training options, ensuring quality hands‑on experiences for future healthcare professionals.
layout: provider
modified: '2026-10-26'
name: MedicalRotations
nav: Providers
network: true
overview: MedicalRotations is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Healthcare, Education, Clinical Rotations, Medical Students, and Platform.
random_paper: 12
score:
  band: emerging
  composite: 11.1
  coverage:
    artifact_dirs: 8
    catalog_earned: 25.0
    catalog_earned_first_party: 0.0
    catalog_gap: 90.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 34.2
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 0.0
    discoverability: 44.6
    operational_transparency: 0.0
  provenance:
    mcp: unknown
  regulatory:
    applies: true
    matched_via: tags
    regime: Health
    regime_id: health
    score: 10.9
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Rotation Medical Domain Security
  slug: rotation-medical-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: rotation-medical
tags:
- Healthcare
- Education
- Clinical Rotations
- Medical Students
- Platform
website: https://www.medicalrotations.com/
---
