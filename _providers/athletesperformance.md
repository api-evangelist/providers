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
api_count: 1
apis:
- description: Athletesperformance provides a human performance coaching platform; API details are not publicly documented.
  name: Athletesperformance API
  slug: athletesperformance-api
artifact_total: 2
common:
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/athletesperformance/refs/heads/main/hosts/athletesperformance-hosts.yml
  title: ''
  type: Hosts
  url: hosts/athletesperformance-hosts.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/athletesperformance/refs/heads/main/vendors/athletesperformance-vendors.yml
  title: ''
  type: Vendors
  url: vendors/athletesperformance-vendors.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://legal-docs.teamexos.com/terms-of-service?_gl=1*alm51s*_ga*MjA3MTE2ODIzOS4xNzI5MzI2NDU0*_ga_D3D03WYX8T*MTczMDQwNTcxNS4xNy4xLjE3MzA0MDcwODkuMTYuMC4w*_gcl_au*MzU5MTYzNzc3LjE3MjkzMjY0NTg.
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://legal-docs.teamexos.com/privacy-policy?_gl=1*j3dme7*_ga*MjA3MTE2ODIzOS4xNzI5MzI2NDU0*_ga_D3D03WYX8T*MTczMDQwNTcxNS4xNy4xLjE3MzA0MDcwODkuMTYuMC4w*_gcl_au*MzU5MTYzNzc3LjE3MjkzMjY0NTg.
- group: company
  title: ''
  type: Newsroom
  url: https://www.teamexos.com/newsroom
- group: other
  title: ''
  type: Leadership
  url: https://www.teamexos.com/resources/leadership/i-in-team
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/teamexos
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/athletesperformance/refs/heads/main/security/athletesperformance-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/athletesperformance-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.teamexos.com
coverage:
  checked: 2026-09-26
  detail: No public API documentation or developer program is available for Athletesperformance.
  evidence:
  - status: blocked
    url: https://api.teamexos.com/openapi.json
  reason: no-developer-program
  state: none
created: '2026-09-26'
description: Athletesperformance, now part of EXOS, provides human performance coaching, training, and consulting services for athletes and organizations. Their offerings include strength, speed, nutrition, and movement programs, as well as corporate wellness solutions, facility design, and virtual coaching platforms. The company focuses on optimizing performance across sports, education, military, and corporate sectors, leveraging data-driven methods and expert coaching to reduce injury risk and enhance results.
layout: provider
modified: '2026-09-26'
name: Athletesperformance
nav: Providers
network: true
overview: Athletesperformance publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, HumanPerformance, Coaching, Wellness, and Sports.
random_paper: 4
score:
  band: minimal
  composite: 10.3
  coverage:
    artifact_dirs: 5
    catalog_earned: 30.0
    catalog_earned_first_party: 0.0
    catalog_gap: 85.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 21.1
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 0.0
    discoverability: 57.1
    operational_transparency: 5.3
  provenance:
    mcp: derived
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
  name: Athletesperformance Domain Security
  slug: athletesperformance-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: athletesperformance
tags:
- Company
- HumanPerformance
- Coaching
- Wellness
- Sports
website: https://www.teamexos.com
---
