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
    mcp_server: false
    mcp_tool_quality: na
    openapi_examples: false
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: verified
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: '0.2'
  score: 14.4
  scored_at: '2026-11-06'
api_count: 0
artifact_total: 1
common:
- group: auth
  href: https://artifacts.apis.io/orion-law/well-known/orion-law-dev-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/orion-law-dev-security.txt
- group: agent
  href: https://artifacts.apis.io/orion-law/well-known/orion-law-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/orion-law-well-known.yml
- group: other
  href: https://artifacts.apis.io/orion-law/hosts/orion-law-hosts.yml
  title: ''
  type: Hosts
  url: hosts/orion-law-hosts.yml
- group: other
  href: https://artifacts.apis.io/orion-law/vendors/orion-law-vendors.yml
  title: ''
  type: Vendors
  url: vendors/orion-law-vendors.yml
- group: operate
  title: ''
  type: Support
  url: https://www.orionlaw.com/services/support/
- group: docs
  title: ''
  type: Documentation
  url: https://dev.orionlaw.com/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/orionlaw
- group: auth
  href: https://artifacts.apis.io/orion-law/security/orion-law-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/orion-law-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://orionlaw.com/
- group: company
  title: ''
  type: Blog
  url: https://www.orionlaw.com/blog/
- group: company
  title: ''
  type: About
  url: https://www.orionlaw.com/about/company/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.orionlaw.com/privacy-policy/
coverage:
  checked: '2026-10-29'
  detail: Developer portal at https://dev.orionlaw.com/ returns a JavaScript challenge and renders no machine‑readable spec.
  evidence:
  - status: 200
    url: https://dev.orionlaw.com/
  reason: js-rendered-docs
  state: unreadable
created: '2026-10-28'
description: Orion Law provides a comprehensive law firm management system that integrates financial, practice, case, document, and time management tools. Their platform delivers rapid ROI, increased profitability, and reliable performance for firms nationwide, supported by services such as data conversion, training, and support. The company emphasizes a complete legal management solution with a focus on scalability and customer success.
image: https://www.orionlaw.com/wp-content/uploads/2023/12/Financial-Management.webp
layout: provider
modified: '2026-10-28'
name: Orion Law
nav: Providers
network: true
overview: 'Orion Law is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Law, Software, Software-as-a-Service, Legal Tech, and Management.


  Orion Law''s developer surface includes support, documentation, engineering blog, and 9 more developer resources.'
random_paper: 8
score:
  band: minimal
  composite: 9.0
  coverage:
    artifact_dirs: 11
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -3.4
  facets:
    access_clarity: 5.3
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 8.3
    discoverability: 48.2
    operational_transparency: 13.2
  previous_composite: 12.4
  provenance:
    mcp: unknown
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 13.7
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
screenshot: https://apis.io/screenshots/orion-law/orion-law-2026-11-03T140735.png
security:
- kind: domain-security
  name: Orion Law Domain Security
  slug: orion-law-domain-security
  summary_line: TLSv1.3 · DNSSEC · DMARC
slug: orion-law
tags:
- Law
- Software
- Software-as-a-Service
- Legal Tech
- Management
website: https://orionlaw.com/
---
