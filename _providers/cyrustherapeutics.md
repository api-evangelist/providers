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
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: true
  schema_version: '0.2'
  score: 2.9
  scored_at: '2026-10-31'
api_count: 0
artifact_total: 1
common:
- group: other
  href: https://artifacts.apis.io/cyrustherapeutics/hosts/cyrustherapeutics-hosts.yml
  title: ''
  type: Hosts
  url: hosts/cyrustherapeutics-hosts.yml
- group: other
  href: https://artifacts.apis.io/cyrustherapeutics/vendors/cyrustherapeutics-vendors.yml
  title: ''
  type: Vendors
  url: vendors/cyrustherapeutics-vendors.yml
- group: auth
  href: https://artifacts.apis.io/cyrustherapeutics/security/cyrustherapeutics-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/cyrustherapeutics-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://equityzen.com/company/cyrustherapeutics
coverage:
  checked: '2026-10-22'
  detail: No public API documentation or machine‑readable contract was found on the company’s website.
  evidence:
  - status: 200
    url: http://cyrustx.com/kr/about/cyabout.php
  reason: no-developer-program
  state: none
created: '2026-10-21'
description: Cyrustherapeutics is a biotechnology company focused on discovering and developing innovative medicines for chronic or life‑threatening diseases with high unmet medical needs. The company aims to address the challenge of undruggable targets by leveraging advanced drug discovery platforms and small‑molecule therapeutics. While detailed public information is limited, the firm is positioned within the biotech sector, seeking to advance novel therapeutic candidates through pre‑clinical and clinical development.
layout: provider
modified: '2026-10-21'
name: Cyrustherapeutics
nav: Providers
network: true
overview: Cyrustherapeutics is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Biotechnology, Drug Discovery, Therapeutics, and Innovation.
random_paper: 15
score:
  band: minimal
  composite: 2.2
  coverage:
    artifact_dirs: 7
    catalog_earned: 20.0
    catalog_earned_first_party: 0.0
    catalog_gap: 95.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 0.0
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 0.0
    discoverability: 35.7
    operational_transparency: 0.0
  provenance:
    mcp: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 5.9
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Cyrustherapeutics Domain Security
  slug: cyrustherapeutics-domain-security
  summary_line: TLSv1.3 · DMARC
slug: cyrustherapeutics
tags:
- Biotechnology
- Drug Discovery
- Therapeutics
- Innovation
website: https://equityzen.com/company/cyrustherapeutics
---
