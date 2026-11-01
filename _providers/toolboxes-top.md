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
- description: Subtitle Toolkit API documented at the guides page. Provides endpoints for subtitle conversion and manipulation, but no machine‑readable contract is published.
  name: Toolboxes.top API
  slug: toolboxes-top-api
artifact_total: 2
common:
- group: agent
  href: https://artifacts.apis.io/toolboxes-top/llms/toolboxes-top-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/toolboxes-top-llms.txt
- group: other
  href: https://artifacts.apis.io/toolboxes-top/hosts/toolboxes-top-hosts.yml
  title: ''
  type: Hosts
  url: hosts/toolboxes-top-hosts.yml
- group: other
  href: https://artifacts.apis.io/toolboxes-top/vendors/toolboxes-top-vendors.yml
  title: ''
  type: Vendors
  url: vendors/toolboxes-top-vendors.yml
- group: auth
  href: https://artifacts.apis.io/toolboxes-top/security/toolboxes-top-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/toolboxes-top-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://toolboxes.top/
- group: docs
  title: ''
  type: Documentation
  url: https://toolboxes.top/guides/
- group: company
  title: ''
  type: About
  url: https://toolboxes.top/about
- group: operate
  title: ''
  type: Contact
  url: https://toolboxes.top/contact
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://toolboxes.top/privacy
coverage:
  checked: '2026-10-30'
  detail: Guides page documents subtitle tools but provides no OpenAPI, AsyncAPI, GraphQL, gRPC, or WSDL contract.
  evidence:
  - status: 200
    url: https://toolboxes.top/guides/
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-10-30'
description: Toolboxes.top provides a suite of free, browser‑based subtitle tools that run entirely client‑side. Users can convert, clean, shift, merge, and analyze subtitle files (SRT, VTT, ASS, etc.) without uploading data, creating accounts, or exposing content. The platform emphasizes privacy, offline capability after load, and no file‑size limits, making it suitable for developers, content creators, and anyone needing quick subtitle manipulation directly in the browser.
layout: provider
modified: '2026-10-30'
name: toolboxes-top
nav: Providers
network: true
overview: 'toolboxes-top is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Subtitle Tools, Browser Based, Open Source, and Free.


  toolboxes-top''s developer surface includes documentation and 8 more developer resources.'
random_paper: 7
score:
  band: minimal
  composite: 8.6
  coverage:
    artifact_dirs: 8
    catalog_earned: 30.0
    catalog_earned_first_party: 0.0
    catalog_gap: 85.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 10.5
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 9.5
    discoverability: 53.6
    operational_transparency: 0.0
  provenance:
    mcp: unknown
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 9.8
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Toolboxes Top Domain Security
  slug: toolboxes-top-domain-security
  summary_line: TLSv1.3
slug: toolboxes-top
tags:
- Company
- Subtitle Tools
- Browser Based
- Open Source
- Free
website: https://toolboxes.top/
---
