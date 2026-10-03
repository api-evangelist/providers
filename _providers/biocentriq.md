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
  href: https://raw.githubusercontent.com/api-evangelist/biocentriq/refs/heads/main/hosts/biocentriq-hosts.yml
  title: ''
  type: Hosts
  url: hosts/biocentriq-hosts.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/biocentriq/refs/heads/main/vendors/biocentriq-vendors.yml
  title: ''
  type: Vendors
  url: vendors/biocentriq-vendors.yml
- group: company
  title: ''
  type: Newsroom
  url: https://madescientific.com/news
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/biocentriq/refs/heads/main/security/biocentriq-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/biocentriq-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://madescientific.com/
- group: docs
  title: ''
  type: Documentation
  url: https://madescientific.com/about
- group: operate
  title: ''
  type: Contact
  url: https://madescientific.com/contact
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://madescientific.com/privacy-policy
- group: commercial
  title: ''
  type: TermsOfService
  url: https://madescientific.com/terms-of-use
coverage:
  checked: '2026-09-28'
  detail: No OpenAPI, AsyncAPI, GraphQL, gRPC, or WSDL contract was discovered on the API host.
  evidence:
  - status: 0
    url: https://api.madescientific.com/openapi.json
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-09-28'
description: Made Scientific, formerly BioCentriq, is a global cell therapy contract development and manufacturing organization (CDMO) based in New Jersey and part of GC Corporation. It offers end‑to‑end services including process development, GMP manufacturing, aseptic fill‑finish, quality control, regulatory consulting, and workforce development, supporting autologous and allogeneic cell therapies. The company rebranded in 2025 to reflect its expanded capabilities and global reach, providing flexible partnership models for biotech innovators.
layout: provider
modified: '2026-09-28'
name: BioCentriq
nav: Providers
network: true
overview: 'BioCentriq is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Cell Therapy, CDMO, Biotechnology, Manufacturing, and USA.


  BioCentriq''s developer surface includes documentation and 8 more developer resources.'
random_paper: 16
score:
  band: minimal
  composite: 10.5
  coverage:
    artifact_dirs: 5
    catalog_earned: 25.0
    catalog_earned_first_party: 0.0
    catalog_gap: 90.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 21.1
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 9.5
    discoverability: 46.4
    operational_transparency: 0.0
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 13.7
  schema_version: 0.23.0
  scored_at: '2026-10-03'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Biocentriq Domain Security
  slug: biocentriq-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: biocentriq
tags:
- Cell Therapy
- CDMO
- Biotechnology
- Manufacturing
- USA
website: https://madescientific.com/
---
