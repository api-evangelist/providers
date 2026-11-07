---
access_model:
  confidence: medium
  gated: none
  gated_source:
  - onboarding
  label: Freemium · Self-serve signup
  onboarding: self-serve
  pricing: freemium
  public: false
  source:
  - plans
  - authentication
  - security
  trial: false
  try_now: true
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
    dynamic_client_registration: true
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: documented
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
  score: 21.8
  scored_at: '2026-11-06'
api_count: 1
apis:
- description: API for Cinevva platform, documented at the developer guides.
  name: Cinevva API
  slug: cinevva-api
artifact_total: 4
common:
- group: commercial
  href: https://artifacts.apis.io/cinevva-com/plans/cinevva-com-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/cinevva-com-plans-pricing.yml
- group: auth
  href: https://artifacts.apis.io/cinevva-com/authentication/cinevva-com-authentication.yml
  title: ''
  type: Authentication
  url: authentication/cinevva-com-authentication.yml
- group: agent
  href: https://artifacts.apis.io/cinevva-com/llms/cinevva-com-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/cinevva-com-llms.txt
- group: agent
  href: https://artifacts.apis.io/cinevva-com/well-known/cinevva-com-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/cinevva-com-well-known.yml
- group: other
  href: https://artifacts.apis.io/cinevva-com/hosts/cinevva-com-hosts.yml
  title: ''
  type: Hosts
  url: hosts/cinevva-com-hosts.yml
- group: other
  href: https://artifacts.apis.io/cinevva-com/vendors/cinevva-com-vendors.yml
  title: ''
  type: Vendors
  url: vendors/cinevva-com-vendors.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://app.cinevva.com/legal/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://app.cinevva.com/legal/privacy
- group: commercial
  title: ''
  type: Pricing
  url: https://app.cinevva.com/plans
- group: company
  title: ''
  type: Newsroom
  url: https://app.cinevva.com/news/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://dev.cinevva.com/
- group: operate
  title: ''
  type: ChangeLog
  url: https://app.cinevva.com/blender-addon/changelog
- group: auth
  href: https://artifacts.apis.io/cinevva-com/security/cinevva-com-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/cinevva-com-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://cinevva.com/
- group: docs
  title: ''
  type: Documentation
  url: https://app.cinevva.com/
- group: start
  title: ''
  type: GettingStarted
  url: https://app.cinevva.com/tutorials/
- group: company
  title: ''
  type: Blog
  url: https://app.cinevva.com/blog/
coverage:
  checked: '2026-11-04'
  detail: Documentation pages exist but no OpenAPI, GraphQL schema, or other machine‑readable contract could be retrieved.
  evidence:
  - status: 200
    url: https://app.cinevva.com/guides/
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-11-03'
description: Cinevva is a platform that lets users create and play free browser games powered by AI. It offers AI‑driven tools to generate music, 3D models, sound effects, rig and animate characters, and then publish and share the games. The service focuses on making game creation accessible and collaborative, leveraging modern AI models for creative content.
image: https://app.cinevva.com/img/og-arcade.jpg
layout: provider
modified: '2026-11-03'
name: Cinevva
nav: Providers
network: true
overview: 'Cinevva is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Gaming, Artificial Intelligence, Browser, Platform, and Creative.


  Cinevva''s developer surface includes authentication, pricing, changelog, documentation, getting-started guide, engineering blog, and 11 more developer resources.'
plans:
- name: Cinevva Com Plans Pricing
  plan_count: 3
  slug: cinevva-com-plans-pricing
random_paper: 8
score:
  band: emerging
  composite: 21.9
  coverage:
    artifact_dirs: 9
    catalog_earned: 44.0
    catalog_earned_first_party: 12.0
    catalog_gap: 71.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 47.4
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 28.6
    discoverability: 58.0
    operational_transparency: 7.9
  provenance:
    mcp: unknown
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 14.5
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: authentication
  name: Cinevva Com Authentication
  slug: cinevva-com-authentication
  summary_line: 1 scheme
- kind: domain-security
  name: Cinevva Com Domain Security
  slug: cinevva-com-domain-security
  summary_line: TLSv1.3 · DMARC
slug: cinevva-com
tags:
- Gaming
- Artificial Intelligence
- Browser
- Platform
- Creative
website: https://cinevva.com/
---
