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
api_count: 0
artifact_total: 1
common:
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/calyxo/refs/heads/main/well-known/calyxo-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/calyxo-well-known.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/calyxo/refs/heads/main/hosts/calyxo-hosts.yml
  title: ''
  type: Hosts
  url: hosts/calyxo-hosts.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/calyxo/refs/heads/main/vendors/calyxo-vendors.yml
  title: ''
  type: Vendors
  url: vendors/calyxo-vendors.yml
- group: other
  title: ''
  type: Leadership
  url: https://calyxoinc.com/about-calyxo-inc-old-2/team/
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/calyxo/refs/heads/main/security/calyxo-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/calyxo-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://calyxoinc.com/
- group: company
  title: ''
  type: Blog
  url: https://calyxoinc.com/calyxo-news/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://calyxoinc.com/privacy-policy/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://calyxoinc.com/website-terms-of-use/
coverage:
  checked: '2026-10-06'
  detail: The portal at https://portal.calyxoinc.com returns HTML with no OpenAPI or other machine‑readable contract.
  evidence:
  - status: 200
    url: https://portal.calyxoinc.com/
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-10-06'
description: Calyxo is a medical device company focused on revolutionizing kidney stone care with the world’s first all‑in‑one kidney stone treatment system. Their CVAC System combines ureteroscopy, laser lithotripsy, micro‑jet irrigation, dynamic aspiration and stone collection, delivering minimally invasive, high‑efficacy stone clearance. Founded in 2016, Calyxo operates as a standalone nephrology hospital and has raised significant Series F funding to advance its innovative technologies.
image: https://calyxoinc.com/wp-content/uploads/2026/02/calyxo-aua-2024-og-image.png
layout: provider
modified: '2026-10-06'
name: Calyxo
nav: Providers
network: true
overview: 'Calyxo is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Medical Devices, Kidney Stone Care, Healthcare, Innovation, and Series F.


  Calyxo''s developer surface includes engineering blog and 8 more developer resources.'
random_paper: 18
score:
  band: minimal
  composite: 10.2
  coverage:
    artifact_dirs: 7
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 21.1
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 2.4
    discoverability: 50.0
    operational_transparency: 0.0
  provenance:
    mcp: unknown
  regulatory:
    applies: true
    matched_via: tags
    regime: Health
    regime_id: health
    score: 15.6
  schema_version: 0.24.0
  scored_at: '2026-10-17'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Calyxo Domain Security
  slug: calyxo-domain-security
  summary_line: TLSv1.3 · DMARC
slug: calyxo
tags:
- Medical Devices
- Kidney Stone Care
- Healthcare
- Innovation
- Series F
website: https://calyxoinc.com/
---
