---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source:
  - security
  trial: false
  try_now: false
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
    mcp_tool_quality: na
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
  scored_at: '2026-11-06'
api_count: 1
apis:
- description: API for Judo platform, documented at the developer portal.
  name: Judo API
  slug: judo-api
artifact_total: 2
common:
- group: other
  href: https://artifacts.apis.io/judo-app/hosts/judo-app-hosts.yml
  title: ''
  type: Hosts
  url: hosts/judo-app-hosts.yml
- group: other
  href: https://artifacts.apis.io/judo-app/vendors/judo-app-vendors.yml
  title: ''
  type: Vendors
  url: vendors/judo-app-vendors.yml
- group: build
  href: https://artifacts.apis.io/judo-app/packages/judo-app-packages.yml
  title: ''
  type: SDKs
  url: packages/judo-app-packages.yml
- group: build
  href: https://artifacts.apis.io/judo-app/packages/judo-app-packages.yml
  title: ''
  type: Packages
  url: packages/judo-app-packages.yml
- group: start
  title: ''
  type: GettingStarted
  url: https://developer.judo.app/docs/getting-started/export-to-xcode
- group: docs
  title: ''
  type: Documentation
  url: https://developer.judo.app/
- group: auth
  href: https://artifacts.apis.io/judo-app/security/judo-app-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/judo-app-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://developer.judo.app
coverage:
  checked: '2026-10-25'
  detail: Developer portal pages are rendered via JavaScript, preventing machine‑readable spec discovery.
  evidence:
  - status: 200
    url: https://developer.judo.app
  reason: js-rendered-docs
  state: unreadable
created: '2026-10-25'
description: Rover, operating under the brand Judo, provides a no‑code platform for building SwiftUI applications. The service offers SDKs, a visual editor, and server‑driven UI components that let developers create iOS apps without writing code. Documentation and developer resources are hosted at developer.judo.app, with guides covering getting started, SDK integration, customization, and advanced features. The company targets mobile developers seeking rapid prototyping and production‑grade app delivery.
layout: provider
modified: '2026-10-25'
name: Rover
nav: Providers
network: true
overview: 'Rover is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, No-Code, SwiftUI, Mobile, and Developer Tools.


  Rover''s developer surface includes getting-started guide, documentation, and 6 more developer resources.'
random_paper: 8
score:
  band: minimal
  composite: 7.6
  coverage:
    artifact_dirs: 7
    catalog_earned: 30.0
    catalog_earned_first_party: 0.0
    catalog_gap: 85.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -2.1
  facets:
    access_clarity: 0.0
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 17.9
    discoverability: 53.6
    operational_transparency: 0.0
  previous_composite: 9.7
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 5.9
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
screenshot: https://apis.io/screenshots/judo-app/judo-app-2026-11-03T134236.png
security:
- kind: domain-security
  name: Judo App Domain Security
  slug: judo-app-domain-security
  summary_line: DMARC
slug: judo-app
tags:
- Company
- No-Code
- SwiftUI
- Mobile
- Developer Tools
website: https://developer.judo.app
---
