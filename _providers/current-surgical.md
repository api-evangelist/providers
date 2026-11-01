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
  href: https://artifacts.apis.io/current-surgical/hosts/current-surgical-hosts.yml
  title: ''
  type: Hosts
  url: hosts/current-surgical-hosts.yml
- group: other
  href: https://artifacts.apis.io/current-surgical/vendors/current-surgical-vendors.yml
  title: ''
  type: Vendors
  url: vendors/current-surgical-vendors.yml
- group: auth
  href: https://artifacts.apis.io/current-surgical/security/current-surgical-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/current-surgical-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://currentsurgical.com
coverage:
  checked: '2026-10-24'
  detail: No public API documentation or machine-readable contract was found for Current Surgical.
  evidence:
  - status: 404
    url: https://developer.current-surgical.com
  reason: not-a-software-company
  state: none
created: '2026-10-24'
description: Current Surgical develops a digital surgery platform that combines real‑time imaging, precision focused ultrasound and AI‑driven algorithms to enable millimeter‑level control of tissue treatment. The technology is aimed at surgeons and medical facilities for applications such as solid tumor ablation, cardiac arrhythmias, chronic pain, hypertension and epilepsy. By providing closed‑loop control and automated precision, the platform seeks to improve outcomes and reduce risk in minimally invasive procedures.
layout: provider
modified: '2026-10-24'
name: Current Surgical
nav: Providers
network: true
overview: Current Surgical is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Surgery, Medical Devices, Focused Ultrasound, Digital Surgery, and Minimally Invasive Surgery.
random_paper: 18
score:
  band: minimal
  composite: 3.4
  coverage:
    artifact_dirs: 6
    catalog_earned: 25.0
    catalog_earned_first_party: 0.0
    catalog_gap: 90.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 0.0
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
    score: 4.7
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Current Surgical Domain Security
  slug: current-surgical-domain-security
  summary_line: TLSv1.3 · HSTS
slug: current-surgical
tags:
- Surgery
- Medical Devices
- Focused Ultrasound
- Digital Surgery
- Minimally Invasive Surgery
website: https://currentsurgical.com
---
