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
  scored_at: '2026-09-25'
api_count: 0
artifact_total: 1
common:
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/accelus/refs/heads/main/security/accelus-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/accelus-domain-security.yml
coverage:
  checked: '2026-09-06'
  detail: Accelus Inc. divested its whole product line — Remi robotic navigation to Alphatec in April 2023, the FlareHawk/Toro/LineSider implants to Highridge Medical in September 2025 — and its only host accelusinc.com is now a suspended cPanel account that 302s every path, including the root and a negative-control path, to an "Account Suspended" page behind a TLS certificate that expired 2026-05-13.
  evidence:
  - status: 302
    url: https://accelusinc.com/
  - status: 200
    url: https://accelusinc.com/cgi-sys/suspendedpage.cgi
  - status: 302
    url: https://accelusinc.com/openapi.json
  - status: 302
    url: https://accelusinc.com/.well-known/agent-card.json
  - status: 302
    url: https://accelusinc.com/.well-known/accelus-negative-control-7f3ab91c.json
  - status: 200
    url: https://equityzen.com/company/accelus/
  reason: defunct
  state: none
created: '2026-09-06'
description: Accelus was a Palm Beach Gardens, Florida medical device company formed in 2021 by the combination of Integrity Implants and Fusion Robotics, built around an "Adaptive Geometry" expandable-implant platform for minimally invasive spine surgery. Its products were the FlareHawk and Toro expandable interbody fusion systems for transforaminal, posterior and lateral lumbar interbody fusion, the LineSider minimally invasive pedicle screw system, and the Remi Robotic Navigation System, a table-mounted intra-operative navigation and robotics platform that guided instrumentation from 2D fluoroscopic or 3D imaging. The company raised roughly $32M from investors including Concord Health Partners, Symbiotic Capital, Eastward Capital Partners and Trog Hawley Capital. It sold the Remi robotic navigation assets to Alphatec Holdings for $55M in April 2023 and its remaining implant products and intellectual property — FlareHawk, Toro and LineSider — to Highridge Medical on 2 September 2025. Accelus
  sold surgical hardware and single-use implants to hospitals and surgeons, never operated a developer program, and published no public API, SDK, webhook surface or machine-readable specification. Its only host, the WordPress marketing site accelusinc.com, is now a suspended cPanel hosting account that returns an "Account Suspended" page on every path behind a TLS certificate that expired on 2026-05-13, and no accelusinc.com subdomain resolves. This profile is retained as a historical record; there is no API surface to enrich.
image: https://web.archive.org/web/20241002124548id_/https://accelusinc.com/wp-content/uploads/2021/07/accelus-logo_4c.png
layout: provider
modified: '2026-09-06'
name: Accelus
nav: Providers
network: true
overview: Accelus is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Medical Devices, Medical Technology, Healthcare, and Spine Surgery.
random_paper: 10
score:
  band: minimal
  composite: 0.0
  coverage:
    artifact_dirs: 2
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
    discoverability: 0.0
    operational_transparency: 0.0
  lifecycle: defunct
  needs_work:
    note: Recorded so this provider's gaps can be attributed. Does not affect the composite above.
    owner: catalog
    reasons:
    - owner: catalog
      reason: no_resolvable_host
  regulatory:
    applies: true
    matched_via: tags
    regime: Health
    regime_id: health
    score: 4.7
  schema_version: 0.23.0
  scored_at: '2026-09-25'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Accelus Domain Security
  slug: accelus-domain-security
  summary_line: TLSv1.3 · DMARC
slug: accelus
tags:
- Company
- Medical Devices
- Medical Technology
- Healthcare
- Spine Surgery
- Surgical Robotics
- Implants
- Defunct
---
