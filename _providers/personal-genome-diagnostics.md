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
    well_known_catalog: false
  schema_version: '0.2'
  score: 0.0
  scored_at: '2026-10-31'
api_count: 0
artifact_total: 1
common:
- group: agent
  href: https://artifacts.apis.io/personal-genome-diagnostics/llms/personal-genome-diagnostics-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/personal-genome-diagnostics-llms.txt
- group: other
  href: https://artifacts.apis.io/personal-genome-diagnostics/hosts/personal-genome-diagnostics-hosts.yml
  title: ''
  type: Hosts
  url: hosts/personal-genome-diagnostics-hosts.yml
- group: other
  href: https://artifacts.apis.io/personal-genome-diagnostics/vendors/personal-genome-diagnostics-vendors.yml
  title: ''
  type: Vendors
  url: vendors/personal-genome-diagnostics-vendors.yml
- group: operate
  title: ''
  type: Support
  url: https://www.labcorp.com/patients/help
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.labcorp.com/compliance/privacy/privacy-notice
- group: company
  title: ''
  type: Newsroom
  url: https://www.labcorp.com/newsroom
- group: other
  title: ''
  type: Leadership
  url: https://www.labcorp.com/about/our-story/leadership
- group: auth
  href: https://artifacts.apis.io/personal-genome-diagnostics/security/personal-genome-diagnostics-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/personal-genome-diagnostics-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.labcorp.com/oncology/providers/testing-solutions/kitted-solutions
coverage:
  checked: '2026-10-26'
  detail: Provider docs are heavily JavaScript-rendered and no machine‑readable OpenAPI or other contract could be discovered.
  evidence:
  - status: 200
    url: https://www.labcorp.com/oncology/providers/testing-solutions/kitted-solutions
  reason: js-rendered-docs
  state: unreadable
created: '2026-10-26'
description: Personal Genome Diagnostics (PGDx) provides comprehensive genomic profiling services for oncology, delivering advanced cancer testing solutions through its partnership with Labcorp. The company offers kitted solutions that enable rapid, reliable clinical genomic profiling, supporting precision medicine initiatives worldwide. PGDx leverages proprietary bioinformatics to interpret tumor DNA, helping clinicians make informed treatment decisions.
image: https://www.labcorp.com/content/dam/labcorp/logos/labcorp-logos/labcorp-logo@2x.png
layout: provider
modified: '2026-10-26'
name: Personal Genome Diagnostics
nav: Providers
network: true
overview: 'Personal Genome Diagnostics is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Genomics, Oncology, Diagnostics, and PrecisionMedicine.


  Personal Genome Diagnostics'' developer surface includes support and 8 more developer resources.'
random_paper: 9
score:
  band: minimal
  composite: 7.4
  coverage:
    artifact_dirs: 7
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 10.5
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 4.8
    discoverability: 51.8
    operational_transparency: 0.0
  provenance:
    mcp: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 9.8
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Personal Genome Diagnostics Domain Security
  slug: personal-genome-diagnostics-domain-security
  summary_line: TLSv1.3 · DMARC
slug: personal-genome-diagnostics
tags:
- Company
- Genomics
- Oncology
- Diagnostics
- PrecisionMedicine
website: https://www.labcorp.com/oncology/providers/testing-solutions/kitted-solutions
---
