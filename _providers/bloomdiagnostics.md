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
api_count: 0
artifact_total: 1
common:
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/bloomdiagnostics/refs/heads/main/hosts/bloomdiagnostics-hosts.yml
  title: ''
  type: Hosts
  url: hosts/bloomdiagnostics-hosts.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/bloomdiagnostics/refs/heads/main/security/bloomdiagnostics-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/bloomdiagnostics-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://bloomdiagnostics.com
coverage:
  checked: '2026-09-29'
  detail: The company website provides no developer documentation or API reference.
  evidence:
  - status: 200
    url: https://bloomdiagnostics.com
  reason: no-developer-program
  state: none
created: '2026-09-29'
description: Bloomdiagnostics provides a smart diagnostic system that combines laboratory technology with personalized analysis. Their platform offers a range of tests, including inflammation, kidney, ferritin, and ovarian reserve assessments, delivering detailed results through an online portal.
layout: provider
modified: '2026-09-29'
name: Bloomdiagnostics
nav: Providers
network: true
overview: Bloomdiagnostics is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Diagnostics, Healthcare, LabTech, and Personalized Medicine.
random_paper: 19
score:
  band: minimal
  composite: 3.3
  coverage:
    artifact_dirs: 5
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
    mcp: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Health
    regime_id: health
    score: 4.7
  schema_version: 0.23.0
  scored_at: '2026-10-04'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Bloomdiagnostics Domain Security
  slug: bloomdiagnostics-domain-security
  summary_line: TLSv1.3 · DMARC
slug: bloomdiagnostics
tags:
- Company
- Diagnostics
- Healthcare
- LabTech
- Personalized Medicine
website: https://bloomdiagnostics.com
---
