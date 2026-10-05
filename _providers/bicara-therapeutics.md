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
  href: https://raw.githubusercontent.com/api-evangelist/bicara-therapeutics/refs/heads/main/hosts/bicara-therapeutics-hosts.yml
  title: ''
  type: Hosts
  url: hosts/bicara-therapeutics-hosts.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/bicara-therapeutics/refs/heads/main/vendors/bicara-therapeutics-vendors.yml
  title: ''
  type: Vendors
  url: vendors/bicara-therapeutics-vendors.yml
- group: company
  title: ''
  type: Newsroom
  url: https://www.bicara.com/news/
- group: other
  title: ''
  type: Leadership
  url: https://www.bicara.com/team/ricky-joshi/
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/bicara-therapeutics/refs/heads/main/security/bicara-therapeutics-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/bicara-therapeutics-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.bicara.com
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.bicara.com/terms-of-use/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.bicara.com/privacy-policy/
- group: company
  title: ''
  type: Careers
  url: https://www.bicara.com/careers/
- group: company
  title: ''
  type: About
  url: https://www.bicara.com/about/
- group: other
  title: ''
  type: Science
  url: https://www.bicara.com/science/
- group: other
  title: ''
  type: Patients
  url: https://www.bicara.com/patients/
- group: operate
  title: ''
  type: Contact
  url: https://www.bicara.com/contact/
- group: company
  title: ''
  type: InvestorRelations
  url: https://ir.bicara.com
coverage:
  checked: '2026-09-28'
  detail: No OpenAPI, AsyncAPI, GraphQL, or other machine‑readable contract was found on the provider's API host.
  evidence:
  - status: connection_failed
    url: https://api.bicara.com/openapi.json
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-09-28'
description: Bicara Therapeutics is a biotechnology company focused on developing gene‑editing therapies for serious diseases. The firm advances innovative approaches to treat patients with rare genetic disorders and oncology indications, leveraging its proprietary platform to create precise, durable therapeutic solutions. Through collaborations with academic institutions and industry partners, Bicara aims to translate scientific breakthroughs into clinical candidates that address unmet medical needs.
image: https://www.bicara.com/wp-content/uploads/2024/06/Home-Hero.jpg
layout: provider
modified: '2026-09-28'
name: Bicara Therapeutics
nav: Providers
network: true
overview: Bicara Therapeutics is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Biotechnology, Gene Editing, Therapeutics, and Rare Disease.
random_paper: 16
score:
  band: minimal
  composite: 9.1
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
    developer_ergonomics: 0.0
    discoverability: 51.8
    operational_transparency: 0.0
  provenance:
    mcp: unknown
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 13.7
  schema_version: 0.23.0
  scored_at: '2026-10-04'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Bicara Therapeutics Domain Security
  slug: bicara-therapeutics-domain-security
  summary_line: TLSv1.3 · HSTS
slug: bicara-therapeutics
tags:
- Company
- Biotechnology
- Gene Editing
- Therapeutics
- Rare Disease
- Oncology
website: https://www.bicara.com
---
