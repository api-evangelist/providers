---
agent_readiness:
  band: agent-aware
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
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: true
  schema_version: '0.2'
  score: 5.4
  scored_at: '2026-10-31'
api_count: 1
apis:
- description: Provides access to HockeyTech site data via WordPress REST API.
  name: HockeyTech WP JSON API
  slug: hockeytech-wp-json-api
artifact_total: 6
common:
- group: other
  href: https://artifacts.apis.io/hockeytech/hosts/hockeytech-hosts.yml
  title: ''
  type: Hosts
  url: hosts/hockeytech-hosts.yml
- group: other
  href: https://artifacts.apis.io/hockeytech/vendors/hockeytech-vendors.yml
  title: ''
  type: Vendors
  url: vendors/hockeytech-vendors.yml
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.hockeytech.com/privacy-policy/
- group: start
  title: ''
  type: Login
  url: https://www.hockeytech.com/login/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/HockeyTech
- group: auth
  href: https://artifacts.apis.io/hockeytech/security/hockeytech-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/hockeytech-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://hockeytech.com/
coverage:
  checked: '2026-10-28'
  detail: No machine‑readable API specification (OpenAPI, AsyncAPI, GraphQL, etc.) is published despite the public WordPress JSON endpoint.
  evidence:
  - status: 200
    url: https://www.hockeytech.com/wp-json/
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-10-28'
description: HockeyTech is a provider of hockey-related technologies, analytics, and information services. It offers data feeds, live streaming, on-demand video, and statistical analysis tools for leagues, teams, and media partners. The company supplies APIs and web services that deliver structured sports data, player and game statistics, and media content, supporting integration with third‑party applications and platforms. Founded in 2005, HockeyTech serves professional and amateur hockey organizations worldwide, delivering real‑time scores, schedule data, and multimedia assets through its digital platform.
image: https://www.hockeytech.com/wp-content/uploads/2016/03/hockeytech-logo.png
layout: provider
modified: '2026-10-28'
name: HockeyTech league feed
nav: Providers
network: true
overview: HockeyTech league feed is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Sports, Data, Analytics, Streaming, and API.
plans:
- name: Hockeytech Plans Pricing
  plan_count: 0
  slug: hockeytech-plans-pricing
random_paper: 7
rate_limits:
- limit_count: 0
  name: Hockeytech Rate Limits
  slug: hockeytech-rate-limits
scopes:
- name: Hockeytech Scopes
  scope_count: 0
  slug: hockeytech-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: emerging
  composite: 12.7
  coverage:
    artifact_dirs: 19
    catalog_earned: 37.0
    catalog_earned_first_party: 0.0
    catalog_gap: 78.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 23.7
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 0.0
    discoverability: 66.1
    operational_transparency: 5.3
  provenance:
    conformance: unknown
    mcp: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 19.6
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: authentication
  name: Hockeytech Authentication
  slug: hockeytech-authentication
  summary_line: 0 schemes
- kind: domain-security
  name: Hockeytech Domain Security
  slug: hockeytech-domain-security
  summary_line: TLSv1.3 · DMARC
slug: hockeytech
tags:
- Sports
- Data
- Analytics
- Streaming
- API
website: https://hockeytech.com/
---
