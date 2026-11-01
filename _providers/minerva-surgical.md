---
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    agentic_commerce: false
    auth_clarity: served
    consent_identity: false
    delegated_identity: served
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: verified
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: '0.2'
  score: 14.4
  scored_at: '2026-10-31'
api_count: 0
artifact_total: 1
common:
- group: agent
  href: https://artifacts.apis.io/minerva-surgical/well-known/minerva-surgical-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/minerva-surgical-well-known.yml
- group: other
  href: https://artifacts.apis.io/minerva-surgical/hosts/minerva-surgical-hosts.yml
  title: ''
  type: Hosts
  url: hosts/minerva-surgical-hosts.yml
- group: other
  href: https://artifacts.apis.io/minerva-surgical/vendors/minerva-surgical-vendors.yml
  title: ''
  type: Vendors
  url: vendors/minerva-surgical-vendors.yml
- group: auth
  href: https://artifacts.apis.io/minerva-surgical/security/minerva-surgical-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/minerva-surgical-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://minervasurgical.com
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://minervasurgical.com/privacy-policy/
- group: operate
  title: ''
  type: Support
  url: https://minervasurgical.com/request-support/
coverage:
  detail: the company publishes no developer documentation host and no machine-readable contract on its own domain
  evidence:
  - status: 200
    url: https://minervasurgical.com
  reason: no-developer-program
  state: none
created: '2026-10-22'
description: Minerva Surgical develops minimally invasive devices to treat the root causes of abnormal uterine bleeding (AUB). The company provides innovative, patient‑centric solutions for women’s uterine health, focusing on safe, effective, and minimally invasive treatments.
image: https://minervasurgical.com/wp-content/uploads/2023/02/MinervaSurgical.com-featured-Images-1024x1024.png
layout: provider
modified: '2026-10-22'
name: Minerva Surgical
nav: Providers
network: true
overview: 'Minerva Surgical is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Medical Devices, Women''s Health, Minimally Invasive, and Uterine Bleeding.


  Minerva Surgical''s developer surface includes support and 6 more developer resources.'
random_paper: 1
score:
  band: minimal
  composite: 7.9
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
    developer_ergonomics: 4.8
    discoverability: 48.2
    operational_transparency: 0.0
  provenance:
    mcp: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Health
    regime_id: health
    score: 12.5
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Minerva Surgical Domain Security
  slug: minerva-surgical-domain-security
  summary_line: TLSv1.3 · DMARC
slug: minerva-surgical
tags:
- Company
- Medical Devices
- Women's Health
- Minimally Invasive
- Uterine Bleeding
website: https://minervasurgical.com
---
