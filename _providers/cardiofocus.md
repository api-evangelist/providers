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
  href: https://raw.githubusercontent.com/api-evangelist/cardiofocus/refs/heads/main/hosts/cardiofocus-hosts.yml
  title: ''
  type: Hosts
  url: hosts/cardiofocus-hosts.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/cardiofocus/refs/heads/main/vendors/cardiofocus-vendors.yml
  title: ''
  type: Vendors
  url: vendors/cardiofocus-vendors.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://cardiofocus.com/terms-&-conditions
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://cardiofocus.com/privacy-policy
- group: company
  title: ''
  type: Newsroom
  url: https://cardiofocus.com/news
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/cardiofocus/refs/heads/main/security/cardiofocus-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/cardiofocus-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://cardiofocus.com
coverage:
  checked: '2026-10-07'
  detail: Attempts to fetch OpenAPI spec at https://api.cardiofocus.com/* returned no response, indicating no machine‑readable contract is publicly available.
  evidence:
  - status: 0
    url: https://api.cardiofocus.com/openapi.json
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-10-07'
description: Cardiofocus is a medical technology company specializing in pulsed field ablation (PFA) solutions for cardiac arrhythmia treatment. The firm develops integrated catheter and waveform generator systems, including the Centauri, QuickShot, OptiShot, and CardioWave platforms, to provide electrophysiologists with precise, controlled therapy. CardioFocus advances its technology through extensive research, clinical trials, and regulatory approvals, serving physicians and patients worldwide.
image: https://framerusercontent.com/assets/TA4KXta36JxqH5opyvFdYeIyi0.png
layout: provider
modified: '2026-10-07'
name: Cardiofocus
nav: Providers
network: true
overview: Cardiofocus is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Medical, Technology, Cardiology, and PFA.
random_paper: 4
score:
  band: minimal
  composite: 9.0
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
    discoverability: 50.0
    operational_transparency: 0.0
  provenance:
    mcp: unknown
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
  name: Cardiofocus Domain Security
  slug: cardiofocus-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: cardiofocus
tags:
- Company
- Medical
- Technology
- Cardiology
- PFA
website: https://cardiofocus.com
---
