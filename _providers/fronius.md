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
  scored_at: '2026-09-25'
api_count: 0
artifact_total: 1
common:
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/fronius/refs/heads/main/hosts/fronius-hosts.yml
  title: ''
  type: Hosts
  url: hosts/fronius-hosts.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/fronius/refs/heads/main/packages/fronius-packages.yml
  title: ''
  type: SDKs
  url: packages/fronius-packages.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/fronius/refs/heads/main/packages/fronius-packages.yml
  title: ''
  type: Packages
  url: packages/fronius-packages.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.fronius.com/en/terms-and-conditions
- group: company
  title: ''
  type: Newsroom
  url: https://www.fronius.com/-/media/international/c/code-of-conduct/c_terms_code_of_conduct_en.pdf
- group: company
  title: ''
  type: Blog
  url: https://blog.fronius.com
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/Fronius
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/fronius/refs/heads/main/security/fronius-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/fronius-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.fronius.com/
- group: docs
  title: ''
  type: Documentation
  url: https://www.fronius.com/en/help-center
- group: operate
  title: ''
  type: Support
  url: https://www.fronius.com/en/contact
created: '2026-09-22'
description: Fronius International is a global corporation founded in 1945, specializing in welding technology, photovoltaics, battery charging solutions, and energy management systems. With over 6,500 employees across 37 subsidiaries, Fronius delivers innovative, reliable products for solar energy, electric mobility, and industrial welding, emphasizing sustainability and quality. The company connects people, materials, and energy to build a safe, sustainable world.
image: https://www.fronius.com/-/media/oneweb/others/c-fallback-connecting-what-matters-1540x866.webp?97886
layout: provider
modified: '2026-09-22'
name: Fronius
nav: Providers
network: true
overview: 'Fronius is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Energy, Welding, Solar, and Technology.


  Fronius'' developer surface includes engineering blog, documentation, support, and 8 more developer resources.'
random_paper: 4
score:
  band: emerging
  composite: 11.8
  coverage:
    artifact_dirs: 7
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.1
  facets:
    access_clarity: 10.5
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 23.8
    discoverability: 50.0
    operational_transparency: 5.3
  previous_composite: 11.7
  provenance:
    mcp: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Energy & Utilities
    regime_id: energy_utilities
    score: 8.2
  schema_version: 0.23.0
  scored_at: '2026-09-25'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Fronius Domain Security
  slug: fronius-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: fronius
tags:
- Company
- Energy
- Welding
- Solar
- Technology
- Innovation
website: https://www.fronius.com/
---
