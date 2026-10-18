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
api_count: 1
apis:
- description: Scania Developer Portal for connected transport APIs.
  name: Scania Developer Portal
  slug: scania-developer-portal
artifact_total: 3
common:
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/scania/refs/heads/main/well-known/scania-scania-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/scania-scania-security.txt
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/scania/refs/heads/main/security/scania-vulnerability-disclosure.yml
  title: ''
  type: Security
  url: security/scania-vulnerability-disclosure.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/scania/refs/heads/main/well-known/scania-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/scania-security.txt
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/scania/refs/heads/main/well-known/scania-developer-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/scania-developer-security.txt
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/scania/refs/heads/main/well-known/scania-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/scania-well-known.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/scania/refs/heads/main/hosts/scania-hosts.yml
  title: ''
  type: Hosts
  url: hosts/scania-hosts.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/scania/refs/heads/main/vendors/scania-vendors.yml
  title: ''
  type: Vendors
  url: vendors/scania-vendors.yml
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.scania.com/group/en/home/admin/misc/privacy-statement.html
- group: company
  title: ''
  type: Newsroom
  url: https://www.scania.com/group/en/home/newsroom/news.html
- group: docs
  title: ''
  type: Documentation
  url: https://developer.scania.com/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/scania
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/scania/refs/heads/main/security/scania-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/scania-vulnerability-disclosure.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/scania/refs/heads/main/security/scania-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/scania-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://scania.com/
coverage:
  checked: '2026-10-15'
  detail: Developer portal returns a JavaScript shell with no machine‑readable OpenAPI spec.
  evidence:
  - status: 200
    url: https://developer.scania.com
  reason: js-rendered-docs
  state: unreadable
created: '2026-10-14'
description: Scania AB is a leading global manufacturer of heavy trucks, buses, and engines, providing sustainable transport solutions and services. Founded in 1891 in Sweden, Scania designs, manufactures, and sells a full range of trucks and buses, as well as engines for marine and industrial applications. The company focuses on innovation, safety, and environmental responsibility, offering digital services and connectivity solutions for fleet management and logistics. Scania operates worldwide, delivering high-quality vehicles and services to customers across various industries, supporting efficient and eco-friendly transportation.
image: https://www.scania.com/content/dam/group/startpage/teasers/scania-dynamic-trucks.jpg.transform/Rend_1200X630/image.jpg
layout: provider
modified: '2026-10-14'
name: Scania
nav: Providers
network: true
overview: 'Scania is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Trucking, Transportation, Manufacturing, and Sustainability.


  Scania''s developer surface includes documentation and 13 more developer resources.'
random_paper: 7
score:
  band: emerging
  composite: 12.0
  coverage:
    artifact_dirs: 7
    catalog_earned: 32.0
    catalog_earned_first_party: 0.0
    catalog_gap: 83.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 10.5
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 9.5
    discoverability: 58.9
    operational_transparency: 15.8
  provenance:
    mcp: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 15.7
  schema_version: 0.24.0
  scored_at: '2026-10-17'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Scania Domain Security
  slug: scania-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
- kind: vulnerability-disclosure
  name: Scania Vulnerability Disclosure
  slug: scania-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: scania
tags:
- Company
- Trucking
- Transportation
- Manufacturing
- Sustainability
website: https://scania.com/
---
