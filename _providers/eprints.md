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
  href: https://raw.githubusercontent.com/api-evangelist/eprints/refs/heads/main/hosts/eprints-hosts.yml
  title: ''
  type: Hosts
  url: hosts/eprints-hosts.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/eprints/refs/heads/main/packages/eprints-packages.yml
  title: ''
  type: SDKs
  url: packages/eprints-packages.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/eprints/refs/heads/main/packages/eprints-packages.yml
  title: ''
  type: Packages
  url: packages/eprints-packages.yml
- group: company
  title: ''
  type: Newsroom
  url: https://community.eprints.org/news/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/eprints
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/eprints/refs/heads/main/security/eprints-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/eprints-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.eprints.org
coverage:
  checked: '2026-10-13'
  detail: EPrints provides a repository platform but offers no public developer program or API documentation.
  evidence:
  - status: 200
    url: https://www.eprints.org
  reason: no-developer-program
  state: none
created: '2026-10-13'
description: EPrints provides a world‑leading open‑source digital repository platform used by research institutions worldwide. With over 24 years of experience, EPrints Services offers stable, innovative repository solutions, hosting, support, and customization for diverse scholarly communities, enabling open access, data preservation, and institutional repositories.
layout: provider
modified: '2026-10-13'
name: EPrints
nav: Providers
network: true
overview: EPrints is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Open Source, DigitalRepository, Research Infrastructure, and OpenAccess.
random_paper: 3
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
    access_clarity: 0.0
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 7.1
    discoverability: 46.4
    operational_transparency: 5.3
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 5.9
  schema_version: 0.24.0
  scored_at: '2026-10-17'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Eprints Domain Security
  slug: eprints-domain-security
  summary_line: TLSv1.3 · DMARC
slug: eprints
tags:
- Company
- Open Source
- DigitalRepository
- Research Infrastructure
- OpenAccess
website: https://www.eprints.org
---
