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
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: '0.2'
  score: 2.5
  scored_at: '2026-10-31'
api_count: 1
apis:
- description: OpenWrt provides a Linux-based operating system for embedded devices such as routers.
  name: OpenWrt API
  slug: openwrt-api
artifact_total: 6
common:
- group: other
  href: https://artifacts.apis.io/openwrt/hosts/openwrt-hosts.yml
  title: ''
  type: Hosts
  url: hosts/openwrt-hosts.yml
- group: other
  href: https://artifacts.apis.io/openwrt/vendors/openwrt-vendors.yml
  title: ''
  type: Vendors
  url: vendors/openwrt-vendors.yml
- group: operate
  title: ''
  type: ChangeLog
  url: https://github.com/openwrt/openwrt/releases
- group: auth
  href: https://artifacts.apis.io/openwrt/security/openwrt-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/openwrt-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://openwrt.org/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://openwrt.org/developer
- group: docs
  title: ''
  type: Documentation
  url: https://openwrt.org/docs/start
- group: start
  title: ''
  type: GettingStarted
  url: https://openwrt.org/docs/start
- group: operate
  title: ''
  type: Support
  url: https://openwrt.org/support
- group: company
  title: ''
  type: Blog
  url: https://openwrt.org/blog
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/openwrt
- group: operate
  title: ''
  type: Roadmap
  url: https://openwrt.org/roadmap
- group: commercial
  title: ''
  type: Pricing
  url: https://openwrt.org/pricing
- group: commercial
  title: ''
  type: TermsOfService
  url: https://openwrt.org/tos
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://openwrt.org/privacy
- group: start
  title: ''
  type: SignUp
  url: https://openwrt.org/login
- group: build
  title: ''
  type: Postman
  url: https://www.postman.com/openwrt
coverage:
  checked: '2026-10-28'
  detail: No machine‑readable API specification (OpenAPI/GraphQL/AsyncAPI) was found on the provider’s documented developer portal.
  evidence:
  - status: 200
    url: https://dev.archive.openwrt.org/
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-10-28'
description: OpenWrt is an open-source project that provides a fully writable filesystem for embedded devices, primarily routers. It offers a Linux-based operating system with a package manager, allowing users to customize firmware, add features, and improve performance. The community maintains extensive documentation, guides, and a developer portal, supporting a wide range of hardware platforms. OpenWrt’s mission is to empower users with flexible, secure, and up-to-date networking solutions.
image: https://openwrt.org/_media/logo.png
layout: provider
modified: '2026-10-28'
name: OpenWrt
nav: Providers
network: true
overview: 'OpenWrt is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Open-Source, Firmware, Router, and Embedded.


  OpenWrt''s developer surface includes changelog, documentation, getting-started guide, support, engineering blog, pricing, signup flow, and 10 more developer resources.'
plans:
- name: Openwrt Plans Pricing
  plan_count: 0
  slug: openwrt-plans-pricing
random_paper: 15
rate_limits:
- limit_count: 0
  name: Openwrt Rate Limits
  slug: openwrt-rate-limits
scopes:
- name: Openwrt Scopes
  scope_count: 0
  slug: openwrt-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: thin
  composite: 27.9
  coverage:
    artifact_dirs: 20
    catalog_earned: 32.0
    catalog_earned_first_party: 0.0
    catalog_gap: 83.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 44.7
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 42.9
    discoverability: 57.1
    operational_transparency: 26.3
  provenance:
    conformance: unknown
    mcp: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 23.5
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: authentication
  name: Openwrt Authentication
  slug: openwrt-authentication
  summary_line: 0 schemes
- kind: domain-security
  name: Openwrt Domain Security
  slug: openwrt-domain-security
  summary_line: TLSv1.2 · HSTS · DMARC
slug: openwrt
tags:
- Company
- Open-Source
- Firmware
- Router
- Embedded
- Linux
- Networking
website: https://openwrt.org/
---
