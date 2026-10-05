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
api_count: 1
apis:
- description: API for Bonum Tx platform providing access to therapeutic data and program information.
  name: Bonum Tx API
  slug: bonum-tx-api
artifact_total: 2
common:
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/bonumtherapeutics/refs/heads/main/hosts/bonumtherapeutics-hosts.yml
  title: ''
  type: Hosts
  url: hosts/bonumtherapeutics-hosts.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/bonumtherapeutics/refs/heads/main/vendors/bonumtherapeutics-vendors.yml
  title: ''
  type: Vendors
  url: vendors/bonumtherapeutics-vendors.yml
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://bonumtx.com/privacy-policy
- group: company
  title: ''
  type: Newsroom
  url: https://bonumtx.com/news/
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/bonumtherapeutics/refs/heads/main/security/bonumtherapeutics-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/bonumtherapeutics-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://bonumtx.com
coverage:
  checked: '2026-10-02'
  detail: Main site loads content via JavaScript, preventing static spec discovery.
  evidence:
  - status: 200
    url: https://bonumtx.com
  reason: js-rendered-docs
  state: unreadable
created: '2026-10-02'
description: Bonumtherapeutics, operating as Bonum Tx, develops antibody‑controlled therapeutics that deliver potent activity only where needed, aiming to improve safety and efficacy across oncology, autoimmunity, metabolic disorders, and pain management. The company leverages a novel regulated protein platform validated by Roche’s acquisition of its predecessor Good Therapeutics in 2022, and is advancing preclinical programs targeting immune cells and tumor microenvironments.
layout: provider
modified: '2026-10-02'
name: Bonumtherapeutics
nav: Providers
network: true
overview: Bonumtherapeutics publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Biotechnology, Therapeutics, Antibody, and Oncology.
random_paper: 16
score:
  band: minimal
  composite: 6.8
  coverage:
    artifact_dirs: 5
    catalog_earned: 30.0
    catalog_earned_first_party: 0.0
    catalog_gap: 85.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 10.5
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 0.0
    discoverability: 55.4
    operational_transparency: 0.0
  provenance:
    mcp: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 9.8
  schema_version: 0.23.0
  scored_at: '2026-10-04'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Bonumtherapeutics Domain Security
  slug: bonumtherapeutics-domain-security
  summary_line: TLSv1.3 · DNSSEC
slug: bonumtherapeutics
tags:
- Company
- Biotechnology
- Therapeutics
- Antibody
- Oncology
website: https://bonumtx.com
---
