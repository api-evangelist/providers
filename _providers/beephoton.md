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
  scored_at: '2026-10-04'
api_count: 0
artifact_total: 1
common:
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/beephoton/refs/heads/main/hosts/beephoton-hosts.yml
  title: ''
  type: Hosts
  url: hosts/beephoton-hosts.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/beephoton/refs/heads/main/security/beephoton-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/beephoton-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://beephoton.com
coverage:
  checked: '2026-09-27'
  detail: No public developer program or API documentation was found for beephoton.
  evidence:
  - status: 404
    url: https://api.beephoton.com/openapi.json
  reason: no-developer-program
  state: none
created: '2026-09-27'
description: Beephoton (芯晟捷创光电科技) is a high‑tech enterprise founded in June 2017, specializing in photon detection technology and product development. It offers X‑ray detector modules and line‑array cameras for medical imaging, security screening, and industrial applications. The company operates modern clean‑room facilities, holds multiple patents, and is ISO‑9001 certified, serving customers worldwide with advanced photonic solutions.
layout: provider
modified: '2026-09-27'
name: Beephoton
nav: Providers
network: true
overview: Beephoton is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, PhotonDetection, Medical Imaging, Industrial, and Security.
random_paper: 18
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
  name: Beephoton Domain Security
  slug: beephoton-domain-security
  summary_line: TLSv1.2 · DNSSEC
slug: beephoton
tags:
- Company
- PhotonDetection
- Medical Imaging
- Industrial
- Security
website: https://beephoton.com
---
