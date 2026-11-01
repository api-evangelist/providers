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
- group: auth
  href: https://artifacts.apis.io/docspera/well-known/docspera-status-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/docspera-status-security.txt
- group: agent
  href: https://artifacts.apis.io/docspera/well-known/docspera-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/docspera-well-known.yml
- group: other
  href: https://artifacts.apis.io/docspera/hosts/docspera-hosts.yml
  title: ''
  type: Hosts
  url: hosts/docspera-hosts.yml
- group: other
  href: https://artifacts.apis.io/docspera/vendors/docspera-vendors.yml
  title: ''
  type: Vendors
  url: vendors/docspera-vendors.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://docspera.com/legal/terms
- group: operate
  title: ''
  type: Support
  url: https://docspera.com/support/
- group: operate
  title: ''
  type: StatusPage
  url: https://status.docspera.com/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://docspera.com/legal/privacy
- group: start
  title: ''
  type: Login
  url: https://www.docspera.com/login
- group: other
  title: ''
  type: Leadership
  url: https://www.docspera.com/leadership/
- group: company
  title: ''
  type: Blog
  url: https://www.docspera.com/blog/
- group: auth
  href: https://artifacts.apis.io/docspera/security/docspera-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/docspera-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.docspera.com
coverage:
  checked: '2026-10-23'
  detail: Docs are served as HTML pages with no machine‑readable OpenAPI spec discovered.
  evidence:
  - status: 0
    url: https://api.docspera.com/openapi.json
  reason: js-rendered-docs
  state: unreadable
created: '2026-10-23'
description: DocSpera provides a Surgery Care Operating System, a digital backbone for procedural care that connects the entire procedure-driven care lifecycle—from pre‑op coordination to real‑world evidence. It serves MedTech OEMs, health systems, and payors, offering smart scheduling, patient readiness, analytics, AI engagement, and outcome reporting, with compliance certifications such as GDPR, ISO 27001, and SOC 2 Type II.
layout: provider
modified: '2026-10-23'
name: Docspera
nav: Providers
network: true
overview: 'Docspera is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Healthcare, Software-as-a-Service, Surgery, Medical Technology, and Platform.


  Docspera''s developer surface includes support, engineering blog, and 11 more developer resources.'
random_paper: 9
score:
  band: emerging
  composite: 16.1
  coverage:
    artifact_dirs: 6
    catalog_earned: 25.0
    catalog_earned_first_party: 0.0
    catalog_gap: 90.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 34.2
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 7.1
    discoverability: 46.4
    operational_transparency: 26.3
  provenance:
    mcp: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Health
    regime_id: health
    score: 10.9
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Docspera Domain Security
  slug: docspera-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: docspera
tags:
- Healthcare
- Software-as-a-Service
- Surgery
- Medical Technology
- Platform
- Compliance
website: https://www.docspera.com
---
