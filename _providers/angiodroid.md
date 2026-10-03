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
  scored_at: '2026-10-03'
api_count: 1
apis:
- description: API for Angiodroid services (no public contract discovered)
  name: Angiodroid API
  slug: angiodroid-api
artifact_total: 2
common:
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/angiodroid/refs/heads/main/hosts/angiodroid-hosts.yml
  title: ''
  type: Hosts
  url: hosts/angiodroid-hosts.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/angiodroid/refs/heads/main/vendors/angiodroid-vendors.yml
  title: ''
  type: Vendors
  url: vendors/angiodroid-vendors.yml
- group: company
  title: ''
  type: Newsroom
  url: https://www.angiodroid.com/newsroom
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/angiodroid/refs/heads/main/security/angiodroid-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/angiodroid-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.angiodroid.com
coverage:
  checked: 2026-09-24
  detail: No public API documentation or contract was found for Angiodroid.
  evidence:
  - status: 0
    url: https://api.angiodroid.com/openapi.json
  reason: no-developer-program
  state: none
created: '2026-09-24'
description: Angiodroid SpA is a medical technology company specializing in CO₂-based solutions for vascular surgery, interventional radiology, cardiology, and angiology. It aims to improve patient outcomes by providing innovative, contrast‑free imaging technologies, reducing the risk of contrast‑induced nephropathy. The company offers products such as CO₂ injectors, disposables, and synchronization tools, and emphasizes innovation, passion, and quality in its mission.
image: https://www.angiodroid.com/hubfs/anteprima.png
layout: provider
modified: '2026-09-24'
name: Angiodroid
nav: Providers
network: true
overview: Angiodroid publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Medical Technology, CO2 Imaging, Vascular Surgery, and Interventional Radiology.
random_paper: 0
score:
  band: minimal
  composite: 4.7
  coverage:
    artifact_dirs: 5
    catalog_earned: 32.0
    catalog_earned_first_party: 0.0
    catalog_gap: 83.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 0.0
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 0.0
    discoverability: 58.9
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
  scored_at: '2026-10-03'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Angiodroid Domain Security
  slug: angiodroid-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: angiodroid
tags:
- Company
- Medical Technology
- CO2 Imaging
- Vascular Surgery
- Interventional Radiology
website: https://www.angiodroid.com
---
