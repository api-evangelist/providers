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
    mcp_server: documented
    openapi_examples: false
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: '0.2'
  score: 13.9
  scored_at: '2026-10-31'
api_count: 1
apis:
- description: API documentation exists but no machine-readable contract was found.
  name: Transconnect API
  slug: transconnect-api
artifact_total: 2
common:
- group: agent
  href: https://artifacts.apis.io/transconnect-online/well-known/transconnect-online-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/transconnect-online-well-known.yml
- group: other
  href: https://artifacts.apis.io/transconnect-online/hosts/transconnect-online-hosts.yml
  title: ''
  type: Hosts
  url: hosts/transconnect-online-hosts.yml
- group: other
  href: https://artifacts.apis.io/transconnect-online/vendors/transconnect-online-vendors.yml
  title: ''
  type: Vendors
  url: vendors/transconnect-online-vendors.yml
- group: auth
  href: https://artifacts.apis.io/transconnect-online/security/transconnect-online-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/transconnect-online-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://transconnect-online.de/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://portal.transconnect.io
- group: docs
  title: ''
  type: Documentation
  url: https://transconnect.io/de/
- group: docs
  title: ''
  type: APIReference
  url: https://transconnect.io/de/
- group: start
  title: ''
  type: GettingStarted
  url: https://transconnect.io/de/
- group: company
  title: ''
  type: Blog
  url: https://transconnect.io/blog
- group: operate
  title: ''
  type: Support
  url: https://transconnect.io/support?hsLang=de
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/transconnect-platform
coverage:
  detail: the company publishes developer documentation but serves no machine-readable contract from it
  evidence:
  - status: 401
    url: https://portal.transconnect.io/mcp
  - status: 403
    url: https://transconnect.io/mcp
  - status: 200
    url: https://transconnect-online.de/
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-10-19'
description: SQL Projekt, operating under the brand TRANSCONNECT, provides a low‑code business integration platform for German enterprises. It connects existing systems and processes, enabling digital transformation across industry, public administration, utilities, and media sectors. The platform offers master data management, digital twins, product passports, and IoT monitoring, supporting both on‑premise and cloud environments. With a focus on secure, scalable integration, TRANSCONNECT helps customers automate workflows, improve efficiency, and comply with regulations such as the Online Access Act (OZG).
image: https://transconnect.io/hubfs/TRANSCONNECT%20Logo.svg
layout: provider
modified: '2026-10-19'
name: SQL Projekt
nav: Providers
network: true
overview: 'SQL Projekt is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Integration, Low-Code, German, and Enterprise.


  SQL Projekt''s developer surface includes documentation, API reference, getting-started guide, engineering blog, support, and 7 more developer resources.'
random_paper: 20
score:
  band: emerging
  composite: 14.9
  coverage:
    artifact_dirs: 7
    catalog_earned: 32.0
    catalog_earned_first_party: 0.0
    catalog_gap: 83.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 0.0
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 45.2
    discoverability: 57.1
    operational_transparency: 5.3
  provenance:
    mcp: unknown
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 11.8
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Transconnect Online Domain Security
  slug: transconnect-online-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: transconnect-online
tags:
- Company
- Integration
- Low-Code
- German
- Enterprise
website: https://transconnect-online.de/
---
