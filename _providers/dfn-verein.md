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
  href: https://raw.githubusercontent.com/api-evangelist/dfn-verein/refs/heads/main/hosts/dfn-verein-hosts.yml
  title: ''
  type: Hosts
  url: hosts/dfn-verein-hosts.yml
- group: company
  title: ''
  type: Newsroom
  url: https://www.dfn.de/news/
- group: start
  title: ''
  type: Login
  url: https://www.dfn.de/login/
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/dfn-verein/refs/heads/main/security/dfn-verein-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/dfn-verein-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.dfn.de/
coverage:
  checked: '2026-10-13'
  detail: The DFN-Verein website provides no developer program or API documentation.
  evidence:
  - status: 200
    url: https://www.dfn.de/
  - status: 0
    url: https://api.dfn.de/openapi.json
  reason: no-developer-program
  state: none
created: '2026-10-13'
description: DFN-Verein is the association of German research and education networks, providing a collaborative infrastructure for scientific communication, networking, security, and cloud services across Germany. It supports over 360 member institutions, offering tailored communication services, network architecture, and trust services for research and education.
layout: provider
modified: '2026-10-13'
name: DFN-Verein
nav: Providers
network: true
overview: DFN-Verein is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Research, Education, Networking, and Security.
random_paper: 16
score:
  band: minimal
  composite: 5.4
  coverage:
    artifact_dirs: 5
    catalog_earned: 25.0
    catalog_earned_first_party: 0.0
    catalog_gap: 90.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 13.2
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 0.0
    discoverability: 46.4
    operational_transparency: 0.0
  provenance:
    mcp: unknown
  regulatory:
    applies: true
    matched_via: tags
    regime: Education & Research
    regime_id: education
    score: 5.9
  schema_version: 0.24.0
  scored_at: '2026-10-17'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Dfn Verein Domain Security
  slug: dfn-verein-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
slug: dfn-verein
tags:
- Company
- Research
- Education
- Networking
- Security
- Cloud
website: https://www.dfn.de/
---
