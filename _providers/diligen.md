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
  href: https://raw.githubusercontent.com/api-evangelist/diligen/refs/heads/main/hosts/diligen-hosts.yml
  title: ''
  type: Hosts
  url: hosts/diligen-hosts.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/diligen/refs/heads/main/vendors/diligen-vendors.yml
  title: ''
  type: Vendors
  url: vendors/diligen-vendors.yml
- group: docs
  title: ''
  type: Documentation
  url: https://developer.diligen.com/
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/diligen/refs/heads/main/security/diligen-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/diligen-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.diligen.com/
- group: company
  title: ''
  type: Blog
  url: https://www.diligen.com/blog
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.diligen.com/privacypolicy
- group: operate
  title: ''
  type: Contact
  url: https://www.diligen.com/contact
- group: start
  title: ''
  type: Demo
  url: https://www.diligen.com/demo
coverage:
  checked: '2026-10-12'
  detail: Developer portal pages are rendered client‑side JavaScript with no machine‑readable OpenAPI spec.
  evidence:
  - status: 200
    url: https://developer.diligen.com/
  reason: js-rendered-docs
  state: unreadable
created: '2026-10-12'
description: Diligen provides machine‑learning powered contract analysis software that helps law firms, legal service providers, and corporations streamline review, extract key provisions, generate summaries, and manage projects at scale. Its AI‑driven platform automates insight extraction, improves review efficiency, and supports regulatory change response, delivering faster, higher‑quality outcomes for legal teams.
layout: provider
modified: '2026-10-12'
name: Diligen
nav: Providers
network: true
overview: 'Diligen is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Legal Tech, Artificial Intelligence, ContractAnalysis, and Automation.


  Diligen''s developer surface includes documentation, engineering blog, and 7 more developer resources.'
random_paper: 6
score:
  band: minimal
  composite: 8.0
  coverage:
    artifact_dirs: 7
    catalog_earned: 25.0
    catalog_earned_first_party: 0.0
    catalog_gap: 90.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 10.5
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 11.9
    discoverability: 44.6
    operational_transparency: 0.0
  provenance:
    mcp: unknown
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 9.1
  schema_version: 0.24.0
  scored_at: '2026-10-17'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Diligen Domain Security
  slug: diligen-domain-security
  summary_line: TLSv1.3 · DMARC
slug: diligen
tags:
- Company
- Legal Tech
- Artificial Intelligence
- ContractAnalysis
- Automation
website: https://www.diligen.com/
---
