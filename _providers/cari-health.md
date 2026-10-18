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
    protected_resource_metadata: verified
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: '0.2'
  score: 14.4
  scored_at: '2026-10-17'
api_count: 1
apis:
- description: API for Cari Health providing clinical data and personalized methadone dosing information.
  name: Cari Health API
  slug: cari-health-api
artifact_total: 2
common:
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/cari-health/refs/heads/main/well-known/cari-health-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/cari-health-well-known.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/cari-health/refs/heads/main/hosts/cari-health-hosts.yml
  title: ''
  type: Hosts
  url: hosts/cari-health-hosts.yml
- group: company
  title: ''
  type: Newsroom
  url: https://carihealth.com/news/
- group: other
  title: ''
  type: Leadership
  url: https://carihealth.com/team/
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/cari-health/refs/heads/main/security/cari-health-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/cari-health-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://carihealth.com/
coverage:
  checked: '2026-10-07'
  detail: Main site renders content via JavaScript, preventing retrieval of a machine‑readable OpenAPI spec.
  evidence:
  - status: 200
    url: https://carihealth.com/
  reason: js-rendered-docs
  state: unreadable
created: '2026-10-07'
description: Cari Health empowers clinicians with rapid, personalized methadone dosing data, delivering actionable clinical insights at the point of care. By bridging the data gap, CARI Health improves patient outcomes, supports clinicians with real-time metabolite measurements, and advances opioid use disorder treatment through innovative, data‑driven technology backed by NIH, NSF, and leading accelerators.
image: https://carihealth.com/wp-content/uploads/2025/07/cari-health-smiling-doctor.webp
layout: provider
modified: '2026-10-07'
name: Cari Health
nav: Providers
network: true
overview: Cari Health is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Health Tech, ClinicalData, OpioidTreatment, and Personalized Medicine.
random_paper: 12
score:
  band: minimal
  composite: 4.8
  coverage:
    artifact_dirs: 6
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 0.0
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 0.0
    discoverability: 51.8
    operational_transparency: 0.0
  provenance:
    mcp: unknown
  regulatory:
    applies: true
    matched_via: tags
    regime: Health
    regime_id: health
    score: 9.4
  schema_version: 0.24.0
  scored_at: '2026-10-17'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Cari Health Domain Security
  slug: cari-health-domain-security
  summary_line: TLSv1.3
slug: cari-health
tags:
- Health Tech
- ClinicalData
- OpioidTreatment
- Personalized Medicine
website: https://carihealth.com/
---
