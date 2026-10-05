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
    well_known_catalog: true
  schema_version: '0.2'
  score: 2.9
  scored_at: '2026-10-04'
api_count: 1
apis:
- description: API for Akura Medical services (no public contract discovered)
  name: Akura Medical API
  slug: akura-medical-api
artifact_total: 2
common:
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/akuramedical/refs/heads/main/hosts/akuramedical-hosts.yml
  title: ''
  type: Hosts
  url: hosts/akuramedical-hosts.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/akuramedical/refs/heads/main/vendors/akuramedical-vendors.yml
  title: ''
  type: Vendors
  url: vendors/akuramedical-vendors.yml
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.akuramedical.com/privacy/
- group: other
  title: ''
  type: Leadership
  url: https://www.akuramedical.com/leadership/kavi-vyas/
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/akuramedical/refs/heads/main/security/akuramedical-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/akuramedical-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.akuramedical.com
created: '2026-09-24'
description: Akura Medical develops and markets the Katana™ Thrombectomy System, a medical device for treating venous thromboembolism. The company aims to address the high incidence of clot-related conditions in the United States, focusing on innovative solutions for vascular health. Their mission is to improve patient outcomes through advanced technology and dedicated research.
image: https://www.akuramedical.com/wp-content/uploads/2024/10/AKU-logo-header-1.png
layout: provider
modified: '2026-09-24'
name: Akura Medical
nav: Providers
network: true
overview: Akura Medical publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Medical Devices, VascularHealth, Thrombectomy, and Innovation.
random_paper: 19
score:
  band: minimal
  composite: 7.3
  coverage:
    artifact_dirs: 4
    catalog_earned: 32.0
    catalog_earned_first_party: 0.0
    catalog_gap: 83.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.2
  facets:
    access_clarity: 10.5
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 0.0
    discoverability: 58.9
    operational_transparency: 0.0
  previous_composite: 7.1
  regulatory:
    applies: true
    matched_via: tags
    regime: Health
    regime_id: health
    score: 7.8
  schema_version: 0.23.0
  scored_at: '2026-10-04'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Akuramedical Domain Security
  slug: akuramedical-domain-security
  summary_line: TLSv1.3
slug: akuramedical
tags:
- Company
- Medical Devices
- VascularHealth
- Thrombectomy
- Innovation
website: https://www.akuramedical.com
---
