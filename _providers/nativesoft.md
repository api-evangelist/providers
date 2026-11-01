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
  score: 3.1
  scored_at: '2026-10-31'
api_count: 1
apis:
- description: NativeRest provides a native desktop client for interacting with REST APIs; documentation at https://nativesoft.com/docs
  name: NativeRest API
  slug: nativerest-api
artifact_total: 3
common:
- group: commercial
  href: https://artifacts.apis.io/nativesoft/plans/nativesoft-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/nativesoft-plans-pricing.yml
- group: other
  href: https://artifacts.apis.io/nativesoft/hosts/nativesoft-hosts.yml
  title: ''
  type: Hosts
  url: hosts/nativesoft-hosts.yml
- group: auth
  href: https://artifacts.apis.io/nativesoft/security/nativesoft-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/nativesoft-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://nativesoft.com/
- group: docs
  title: ''
  type: Documentation
  url: https://nativesoft.com/docs
- group: company
  title: ''
  type: Blog
  url: https://nativesoft.com/blog
- group: commercial
  title: ''
  type: Pricing
  url: https://nativesoft.com/pricing
- group: start
  title: ''
  type: GettingStarted
  url: https://nativesoft.com/docs#getting-started
- group: operate
  title: ''
  type: Support
  url: mailto:support@nativesoft.com
- group: start
  title: ''
  type: DeveloperPortal
  url: https://nativesoft.com/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/nativesoftcom
coverage:
  checked: '2026-10-21'
  detail: Documentation is served as HTML pages without a machine‑readable OpenAPI spec.
  evidence:
  - status: 404
    url: https://nativesoft.com/openapi.json
  reason: js-rendered-docs
  state: unreadable
created: '2026-10-21'
description: NativeSoft develops high-performance native desktop applications for interacting with REST APIs across Windows, macOS, and Linux platforms. Their flagship product, NativeRest, offers a lightweight, memory-efficient alternative to Electron-based clients, featuring offline mode, built-in proxy support, and extensive testing utilities. The company focuses on delivering fast, secure, and user-friendly tools for developers and API consumers, emphasizing native performance and cross‑platform consistency.
layout: provider
modified: '2026-10-21'
name: NativeSoft
nav: Providers
network: true
overview: 'NativeSoft is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Software, Desktop, REST, and Cross-Platform.


  NativeSoft''s developer surface includes documentation, engineering blog, pricing, getting-started guide, support, and 6 more developer resources.'
plans:
- name: Nativesoft Plans Pricing
  plan_count: 3
  slug: nativesoft-plans-pricing
random_paper: 11
score:
  band: emerging
  composite: 20.7
  coverage:
    artifact_dirs: 9
    catalog_earned: 42.0
    catalog_earned_first_party: 12.0
    catalog_gap: 73.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 42.1
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 38.1
    discoverability: 53.6
    operational_transparency: 5.3
  provenance:
    mcp: unknown
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 5.9
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Nativesoft Domain Security
  slug: nativesoft-domain-security
  summary_line: TLSv1.3 · DMARC
slug: nativesoft
tags:
- Company
- Software
- Desktop
- REST
- Cross-Platform
website: https://nativesoft.com/
---
