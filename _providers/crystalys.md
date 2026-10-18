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
  href: https://raw.githubusercontent.com/api-evangelist/crystalys/refs/heads/main/hosts/crystalys-hosts.yml
  title: ''
  type: Hosts
  url: hosts/crystalys-hosts.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/crystalys/refs/heads/main/vendors/crystalys-vendors.yml
  title: ''
  type: Vendors
  url: vendors/crystalys-vendors.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/crystalys/refs/heads/main/security/crystalys-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/crystalys-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://crystalystx.com/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://crystalystx.com/terms-of-use/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://crystalystx.com/privacy-policy/
- group: company
  title: ''
  type: Blog
  url: https://crystalystx.com/news/
- group: company
  title: ''
  type: Investors
  url: https://crystalystx.com/investors/
coverage:
  checked: '2026-10-11'
  detail: No machine‑readable API specification was found on the company's site or API host.
  evidence:
  - status: 200
    url: https://crystalystx.com/
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-10-11'
description: Crystalys Therapeutics is a biopharmaceutical company focused on developing novel treatments for gout. Based in San Diego, CA, the company aims to address significant unmet medical needs through innovative drug development, advancing clinical trials, and securing substantial financing to bring therapies to patients worldwide. Their mission emphasizes improving lives of those suffering from gout and related inflammatory conditions.
image: https://crystalystx.com/favicon.ico
layout: provider
modified: '2026-10-11'
name: Crystalys
nav: Providers
network: true
overview: 'Crystalys is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Biotechnology, Biopharma, Gout, Therapeutics, and San Diego.


  Crystalys'' developer surface includes engineering blog and 7 more developer resources.'
random_paper: 16
score:
  band: minimal
  composite: 9.3
  coverage:
    artifact_dirs: 5
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
    discoverability: 48.2
    operational_transparency: 0.0
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 13.7
  schema_version: 0.24.0
  scored_at: '2026-10-17'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Crystalys Domain Security
  slug: crystalys-domain-security
  summary_line: TLSv1.3 · DMARC
slug: crystalys
tags:
- Biotechnology
- Biopharma
- Gout
- Therapeutics
- San Diego
website: https://crystalystx.com/
---
