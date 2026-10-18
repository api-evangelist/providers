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
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: '0.2'
  score: 0.0
  scored_at: '2026-10-17'
api_count: 0
artifact_total: 1
common:
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/caredox/refs/heads/main/hosts/caredox-hosts.yml
  title: ''
  type: Hosts
  url: hosts/caredox-hosts.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/caredox/refs/heads/main/vendors/caredox-vendors.yml
  title: ''
  type: Vendors
  url: vendors/caredox-vendors.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://schoolcare.com/terms-of-use
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://schoolcare.com/privacy-policy
- group: company
  title: ''
  type: Newsroom
  url: https://schoolcare.com/newsroom
- group: other
  title: ''
  type: Leadership
  url: https://schoolcare.com/team
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/caredox/refs/heads/main/security/caredox-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/caredox-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://schoolcare.com
created: '2026-10-07'
description: SchoolCare provides a unified Student Health Record Platform for K‑12 schools, parents, and healthcare providers. It enables secure digital charting of student health information, immunizations, medications, and care coordination, complying with HIPAA and FERPA. The solution connects families and school staff to streamline health data management and improve student wellbeing across districts.
image: https://caredox-assets.caredox.com/assets/schoolcareImages/link-preview/artwork-3%403x.png
layout: provider
modified: '2026-10-07'
name: SchoolCare
nav: Providers
network: true
overview: SchoolCare is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Education, Health, Software-as-a-Service, K-12, and StudentRecords.
random_paper: 16
score:
  band: minimal
  composite: 9.2
  coverage:
    artifact_dirs: 6
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 21.1
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
    score: 10.9
  schema_version: 0.24.0
  scored_at: '2026-10-17'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Caredox Domain Security
  slug: caredox-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: caredox
tags:
- Education
- Health
- Software-as-a-Service
- K-12
- StudentRecords
website: https://schoolcare.com
---
