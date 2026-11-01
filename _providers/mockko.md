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
api_count: 1
apis:
- description: Mockko provides a web-based dashboard mockup builder API (if any). Documentation pages exist but no machine‑readable contract was found.
  name: Mockko API
  slug: mockko-api
artifact_total: 2
common:
- group: operate
  href: https://artifacts.apis.io/mockko/changelog/mockko-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/mockko-changelog.yml
- group: agent
  href: https://artifacts.apis.io/mockko/llms/mockko-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/mockko-llms.txt
- group: other
  href: https://artifacts.apis.io/mockko/hosts/mockko-hosts.yml
  title: ''
  type: Hosts
  url: hosts/mockko-hosts.yml
- group: other
  href: https://artifacts.apis.io/mockko/vendors/mockko-vendors.yml
  title: ''
  type: Vendors
  url: vendors/mockko-vendors.yml
- group: build
  href: https://artifacts.apis.io/mockko/packages/mockko-packages.yml
  title: ''
  type: SDKs
  url: packages/mockko-packages.yml
- group: build
  href: https://artifacts.apis.io/mockko/packages/mockko-packages.yml
  title: ''
  type: Packages
  url: packages/mockko-packages.yml
- group: operate
  title: ''
  type: ChangeLog
  url: https://mockko.com/changelog
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/mockko
- group: auth
  href: https://artifacts.apis.io/mockko/security/mockko-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/mockko-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://mockko.com/
- group: company
  title: ''
  type: Blog
  url: https://mockko.com/blog
- group: commercial
  title: ''
  type: TermsOfService
  url: https://mockko.com/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://mockko.com/privacy
coverage:
  checked: '2026-10-18'
  detail: Documentation pages exist but no OpenAPI, AsyncAPI, GraphQL, gRPC, or WSDL contract could be found.
  evidence:
  - status: 200
    url: https://mockko.com/
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-10-18'
description: Mockko is a web-based dashboard mockup builder that enables designers and analysts to create Power BI, Tableau, and Excel report layouts visually without writing code. It offers drag‑and‑drop design, component library, and export to PNG, PDF, or PowerPoint, with a free tier and paid plans for teams.
image: https://mockko.com/og-image.png
layout: provider
modified: '2026-10-18'
name: Mockko
nav: Providers
network: true
overview: 'Mockko is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Dashboards, Mockup, Power BI, Tableau, and Design.


  Mockko''s developer surface includes changelog, engineering blog, and 11 more developer resources.'
random_paper: 20
score:
  band: emerging
  composite: 14.3
  coverage:
    artifact_dirs: 10
    catalog_earned: 32.0
    catalog_earned_first_party: 0.0
    catalog_gap: 83.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -0.1
  facets:
    access_clarity: 21.1
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 9.5
    discoverability: 57.1
    operational_transparency: 21.1
  previous_composite: 14.4
  provenance:
    mcp: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Energy & Utilities
    regime_id: energy_utilities
    score: 11.5
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Mockko Domain Security
  slug: mockko-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: mockko
tags:
- Dashboards
- Mockup
- Power BI
- Tableau
- Design
website: https://mockko.com/
---
