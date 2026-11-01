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
- description: Kodi offers developer resources and documentation but does not publish a public API contract.
  name: Kodi Developer Resources
  slug: kodi-developer-resources
artifact_total: 6
common:
- group: other
  href: https://artifacts.apis.io/kodi/hosts/kodi-hosts.yml
  title: ''
  type: Hosts
  url: hosts/kodi-hosts.yml
- group: other
  href: https://artifacts.apis.io/kodi/vendors/kodi-vendors.yml
  title: ''
  type: Vendors
  url: vendors/kodi-vendors.yml
- group: other
  title: ''
  type: Leadership
  url: https://kodi.tv/about/team
- group: auth
  href: https://artifacts.apis.io/kodi/security/kodi-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/kodi-domain-security.yml
- group: auth
  href: https://artifacts.apis.io/kodi/security/kodi-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/kodi-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://kodi.tv/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://dev-kit.kodi.tv/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.kodi.tv/
- group: company
  title: ''
  type: Blog
  url: https://kodi.tv/blog
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/xbmc
- group: operate
  title: ''
  type: StatusPage
  url: https://status.kodi.tv/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://kodi.tv/about/terms-of-service
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://kodi.tv/about/privacy-policy
- group: start
  title: ''
  type: GettingStarted
  url: https://kodi.tv/download
coverage:
  checked: '2026-10-28'
  detail: Kodi provides developer documentation but does not publish any machine‑readable API specification.
  evidence:
  - status: 200
    url: https://kodi.tv/contribute/developers
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-10-28'
description: Kodi is an open-source home theater software project that provides a media center platform for playing videos, music, pictures, and games on a wide range of devices and operating systems. It supports a large catalog of community add-ons, offers a customizable 10-foot user interface for TVs, and enables streaming, live TV, and media library management. The project is maintained by the non-profit Kodi Foundation and a global volunteer community, emphasizing openness, extensibility, and cross‑platform compatibility.
image: https://avatars.githubusercontent.com/u/199122?v=4
layout: provider
modified: '2026-10-28'
name: Kodi
nav: Providers
network: true
overview: 'Kodi is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Media, Home-Theater, Open-Source, Entertainment, and Software.


  Kodi''s developer surface includes documentation, engineering blog, getting-started guide, and 11 more developer resources.'
plans:
- name: Kodi Plans Pricing
  plan_count: 0
  slug: kodi-plans-pricing
random_paper: 15
rate_limits:
- limit_count: 0
  name: Kodi Rate Limits
  slug: kodi-rate-limits
scopes:
- name: Kodi Scopes
  scope_count: 0
  slug: kodi-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: emerging
  composite: 20.8
  coverage:
    artifact_dirs: 20
    catalog_earned: 32.0
    catalog_earned_first_party: 0.0
    catalog_gap: 83.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 21.1
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 33.3
    discoverability: 58.9
    operational_transparency: 21.1
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
  name: Kodi Authentication
  slug: kodi-authentication
  summary_line: 0 schemes
- kind: domain-security
  name: Kodi Domain Security
  slug: kodi-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
slug: kodi
tags:
- Media
- Home-Theater
- Open-Source
- Entertainment
- Software
website: https://kodi.tv/
---
