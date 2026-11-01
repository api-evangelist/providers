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
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: '0.2'
  score: 0.0
  scored_at: '2026-10-31'
api_count: 1
apis:
- description: Zen Cart provides a RESTful API for managing store data, though no machine‑readable specification is published.
  name: Zen Cart API
  slug: zen-cart-api
artifact_total: 2
common:
- group: agent
  href: https://artifacts.apis.io/zen-cart/llms/zen-cart-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/zen-cart-llms.txt
- group: other
  href: https://artifacts.apis.io/zen-cart/hosts/zen-cart-hosts.yml
  title: ''
  type: Hosts
  url: hosts/zen-cart-hosts.yml
- group: other
  href: https://artifacts.apis.io/zen-cart/vendors/zen-cart-vendors.yml
  title: ''
  type: Vendors
  url: vendors/zen-cart-vendors.yml
- group: build
  href: https://artifacts.apis.io/zen-cart/packages/zen-cart-packages.yml
  title: ''
  type: SDKs
  url: packages/zen-cart-packages.yml
- group: build
  href: https://artifacts.apis.io/zen-cart/packages/zen-cart-packages.yml
  title: ''
  type: Packages
  url: packages/zen-cart-packages.yml
- group: auth
  href: https://artifacts.apis.io/zen-cart/security/zen-cart-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/zen-cart-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://zen-cart.com/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.zen-cart.com/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://zen-cart.com/
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.zen-cart.com/user/first_steps/
- group: operate
  title: ''
  type: Support
  url: https://zen-cart.com/forums
- group: company
  title: ''
  type: Blog
  url: https://zen-cart.com/newsletter
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/zencart
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://zen-cart.com/privacy
coverage:
  checked: '2026-10-27'
  detail: Documentation pages are rendered via JavaScript, preventing machine‑readable spec discovery.
  evidence:
  - status: 200
    url: https://docs.zen-cart.com/
  reason: js-rendered-docs
  state: unreadable
created: '2026-10-27'
description: Zen Cart is an open‑source e‑commerce platform that enables merchants to build and manage online stores. It offers a flexible, modular architecture with a wide range of extensions, themes, and payment integrations, supporting both small businesses and larger enterprises. The community‑driven project provides extensive documentation, developer guides, and support forums, allowing developers to customize and extend functionality through plugins and custom code.
layout: provider
modified: '2026-10-27'
name: Zen Cart
nav: Providers
network: true
overview: 'Zen Cart is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include e-commerce, open-source, php, shopping-cart, and community.


  Zen Cart''s developer surface includes documentation, getting-started guide, support, engineering blog, and 10 more developer resources.'
random_paper: 12
score:
  band: emerging
  composite: 16.4
  coverage:
    artifact_dirs: 9
    catalog_earned: 30.0
    catalog_earned_first_party: 0.0
    catalog_gap: 85.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 10.5
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 45.2
    discoverability: 53.6
    operational_transparency: 5.3
  provenance:
    mcp: derived
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
  name: Zen Cart Domain Security
  slug: zen-cart-domain-security
  summary_line: TLSv1.3 · DMARC
slug: zen-cart
tags:
- e-commerce
- open-source
- php
- shopping-cart
- community
- platform
website: https://zen-cart.com/
---
