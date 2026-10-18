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
  href: https://raw.githubusercontent.com/api-evangelist/teletrac-navman/refs/heads/main/hosts/teletrac-navman-hosts.yml
  title: ''
  type: Hosts
  url: hosts/teletrac-navman-hosts.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/teletrac-navman/refs/heads/main/vendors/teletrac-navman-vendors.yml
  title: ''
  type: Vendors
  url: vendors/teletrac-navman-vendors.yml
- group: operate
  title: ''
  type: Support
  url: https://support.teletracnavman.com/support/home
- group: operate
  title: ''
  type: StatusPage
  url: https://status.teletracnavman.com/client-setup
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.teletracnavman.com/privacy-notice
- group: company
  title: ''
  type: Newsroom
  url: https://www.teletracnavman.com/company/press
- group: other
  title: ''
  type: Leadership
  url: https://www.teletracnavman.com/company/leadership
- group: company
  title: ''
  type: Blog
  url: https://www.teletracnavman.com/resources/blog
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/teletrac-navman/refs/heads/main/security/teletrac-navman-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/teletrac-navman-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.teletracnavman.com
coverage:
  detail: the company publishes no developer documentation host and no machine-readable contract on its own domain
  evidence:
  - status: 403
    url: https://www.teletracnavman.com/mcp
  - status: 401
    url: https://support.teletracnavman.com/mcp
  - status: 200
    url: https://www.teletracnavman.com
  reason: no-developer-program
  state: none
created: '2026-10-13'
description: Teletrac Navman provides GPS fleet tracking and telematics solutions for businesses worldwide. Their platform offers real‑time vehicle location, driver safety monitoring, compliance tools, and analytics to improve fleet efficiency and reduce operational costs. The company serves a broad range of industries, including transportation, construction, and public sector, delivering integrated hardware and software for comprehensive fleet management.
layout: provider
modified: '2026-10-13'
name: Teletrac Navman
nav: Providers
network: true
overview: 'Teletrac Navman is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Fleet Management, Telematics, GPS Tracking, Driver Safety, and Compliance.


  Teletrac Navman''s developer surface includes support, engineering blog, and 8 more developer resources.'
random_paper: 20
score:
  band: minimal
  composite: 9.6
  coverage:
    artifact_dirs: 5
    catalog_earned: 25.0
    catalog_earned_first_party: 0.0
    catalog_gap: 90.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 10.5
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 7.1
    discoverability: 48.2
    operational_transparency: 15.8
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 9.8
  schema_version: 0.24.0
  scored_at: '2026-10-17'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Teletrac Navman Domain Security
  slug: teletrac-navman-domain-security
  summary_line: TLSv1.3 · DMARC
slug: teletrac-navman
tags:
- Fleet Management
- Telematics
- GPS Tracking
- Driver Safety
- Compliance
- Company
website: https://www.teletracnavman.com
---
