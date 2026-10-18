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
  href: https://raw.githubusercontent.com/api-evangelist/clinomic/refs/heads/main/well-known/clinomic-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/clinomic-well-known.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/clinomic/refs/heads/main/hosts/clinomic-hosts.yml
  title: ''
  type: Hosts
  url: hosts/clinomic-hosts.yml
- group: company
  title: ''
  type: Newsroom
  url: https://www.clinomic.ai/press/
- group: other
  title: ''
  type: Leadership
  url: https://www.clinomic.ai/team/
- group: company
  title: ''
  type: Blog
  url: https://www.clinomic.ai/blog/
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/clinomic/refs/heads/main/security/clinomic-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/clinomic-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.clinomic.ai
coverage:
  detail: the company publishes no developer documentation host and no machine-readable contract on its own domain
  evidence:
  - status: 200
    url: https://www.clinomic.ai
  - status: 403
    url: https://equityzen.com/company/clinomic
  reason: no-developer-program
  state: none
created: '2026-10-08'
description: Clinomic provides data intelligence and network medicine solutions for critical care, offering platforms such as Mona PDMS, Mona OS, and cloud services to streamline patient management, interoperability, and analytics in intensive care settings. Their suite includes teleICU, webICU, and AI tool integration, aiming to improve clinical outcomes through standardized, automated data workflows.
image: https://www.clinomic.ai/wp-content/uploads/2024/07/Clinomic-Mona-Apps-Anna-Montage-1024x560.png
layout: provider
modified: '2026-10-08'
name: Clinomic
nav: Providers
network: true
overview: 'Clinomic is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Healthcare, Data Intelligence, Critical-Care, and Platform.


  Clinomic''s developer surface includes engineering blog and 6 more developer resources.'
random_paper: 10
score:
  band: minimal
  composite: 5.3
  coverage:
    artifact_dirs: 6
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 0.0
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 2.4
    discoverability: 51.8
    operational_transparency: 0.0
  provenance:
    mcp: unknown
  regulatory:
    applies: true
    matched_via: tags
    regime: Health
    regime_id: health
    score: 9.4
  schema_version: 0.24.0
  scored_at: '2026-10-17'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Clinomic Domain Security
  slug: clinomic-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: clinomic
tags:
- Company
- Healthcare
- Data Intelligence
- Critical-Care
- Platform
- Network-Medicine
website: https://www.clinomic.ai
---
