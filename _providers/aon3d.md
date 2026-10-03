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
api_count: 1
apis:
- description: API documentation for AON3D 3D printers and services, as listed in the developer docs.
  name: AON3D API
  slug: aon3d-api
artifact_total: 2
common:
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/aon3d
- group: operate
  href: https://raw.githubusercontent.com/api-evangelist/aon3d/refs/heads/main/changelog/aon3d-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/aon3d-changelog.yml
- group: company
  title: ''
  type: Newsroom
  url: https://www.aon3d.com/category/press/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.aon3d.com/
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/aon3d/refs/heads/main/hosts/aon3d-hosts.yml
  title: ''
  type: Hosts
  url: hosts/aon3d-hosts.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/aon3d/refs/heads/main/vendors/aon3d-vendors.yml
  title: ''
  type: Vendors
  url: vendors/aon3d-vendors.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/aon3d/refs/heads/main/security/aon3d-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/aon3d-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.aon3d.com/
- group: start
  title: ''
  type: GettingStarted
  url: https://www.aon3d.com/get-quote/
- group: operate
  title: ''
  type: Support
  url: https://www.aon3d.com/contact/
- group: company
  title: ''
  type: Blog
  url: https://www.aon3d.com/category/blog/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.aon3d.com/terms-of-use/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.aon3d.com/privacy-policy
- group: start
  title: ''
  type: DeveloperPortal
  url: https://docs.aon3d.com/
- group: docs
  title: ''
  type: APIReference
  url: https://docs.aon3d.com/
coverage:
  checked: 2026-09-25/
  detail: Documentation site https://docs.aon3d.com/ returns HTML shells and no machine‑readable spec despite probing common OpenAPI paths.
  evidence:
  - status: 404
    url: https://docs.aon3d.com/openapi.json
  reason: js-rendered-docs
  state: unreadable
created: '2026-09-25'
description: AON3D provides industrial additive manufacturing solutions, offering high‑temperature 3D printers such as Hylo™ and Basis™, a range of advanced materials including carbon‑fiber PEEK, ULTEM™ and PEKK, and software tools for print preparation. The company serves aerospace, defense, and manufacturing sectors, delivering turnkey hardware, material science resources, and consulting services through its website.
image: https://www.aon3d.com/wp-content/uploads/2023/09/Hylo-URL-Preview.jpg
layout: provider
modified: '2026-09-25'
name: AON3D
nav: Providers
network: true
overview: 'AON3D publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Additive Manufacturing, 3D Printing, Industrial Solutions, and Materials.


  AON3D''s developer surface includes changelog, documentation, getting-started guide, support, engineering blog, API reference, and 9 more developer resources.'
random_paper: 7
score:
  band: emerging
  composite: 21.6
  coverage:
    artifact_dirs: 7
    catalog_earned: 32.0
    catalog_earned_first_party: 0.0
    catalog_gap: 83.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 21.1
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 45.2
    discoverability: 58.9
    operational_transparency: 21.1
  provenance:
    mcp: derived
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
  name: Aon3D Domain Security
  slug: aon3d-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: aon3d
tags:
- Company
- Additive Manufacturing
- 3D Printing
- Industrial Solutions
- Materials
website: https://www.aon3d.com/
---
