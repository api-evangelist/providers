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
api_count: 0
artifact_total: 1
common:
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/aulos-bioscience/refs/heads/main/hosts/aulos-bioscience-hosts.yml
  title: ''
  type: Hosts
  url: hosts/aulos-bioscience-hosts.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/aulos-bioscience/refs/heads/main/vendors/aulos-bioscience-vendors.yml
  title: ''
  type: Vendors
  url: vendors/aulos-bioscience-vendors.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/aulos-bioscience/refs/heads/main/security/aulos-bioscience-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/aulos-bioscience-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.aulosbioscience.com
coverage:
  checked: 2026-09-26
  detail: The main site returns a JavaScript shell and no machine‑readable API spec could be found.
  evidence:
  - status: 200
    url: https://www.aulosbioscience.com
  reason: js-rendered-docs
  state: unreadable
created: '2026-09-26'
description: Aulos Bioscience is a biotechnology company focused on developing innovative solutions for early disease detection and personalized medicine. Leveraging advanced genomics and proteomics platforms, the company aims to provide clinicians with actionable insights to improve patient outcomes. Founded with a mission to bridge the gap between cutting‑edge research and practical healthcare applications, Aulos Bioscience offers a suite of APIs for data access, sample management, and analytical results, supporting integration into electronic health record systems and research pipelines.
layout: provider
modified: '2026-09-26'
name: Aulos Bioscience
nav: Providers
network: true
overview: Aulos Bioscience is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Biotechnology, Genomics, Diagnostics, and Healthcare.
random_paper: 9
score:
  band: minimal
  composite: 3.3
  coverage:
    artifact_dirs: 4
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
  name: Aulos Bioscience Domain Security
  slug: aulos-bioscience-domain-security
  summary_line: TLSv1.3 · HSTS
slug: aulos-bioscience
tags:
- Company
- Biotechnology
- Genomics
- Diagnostics
- Healthcare
website: https://www.aulosbioscience.com
---
