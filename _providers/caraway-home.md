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
    agentic_commerce: platform
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
    protected_resource_metadata: verified
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: '0.2'
  score: 4.5
  scored_at: '2026-11-06'
api_count: 1
apis:
- description: API for Caraway Home e-commerce platform
  name: Caraway Home API
  slug: caraway-home-api
artifact_total: 2
common:
- group: agent
  href: https://artifacts.apis.io/caraway-home/llms/caraway-home-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/caraway-home-llms.txt
- group: agent
  href: https://artifacts.apis.io/caraway-home/well-known/caraway-home-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/caraway-home-well-known.yml
- group: other
  href: https://artifacts.apis.io/caraway-home/hosts/caraway-home-hosts.yml
  title: ''
  type: Hosts
  url: hosts/caraway-home-hosts.yml
- group: other
  href: https://artifacts.apis.io/caraway-home/vendors/caraway-home-vendors.yml
  title: ''
  type: Vendors
  url: vendors/caraway-home-vendors.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://carawayhome.com/pages/terms-and-conditions
- group: operate
  title: ''
  type: Support
  url: https://support.carawayhome.com/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://carawayhome.com/pages/privacy-policy
- group: company
  title: ''
  type: Blog
  url: https://carawayhome.com/blog
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/carawayhome
- group: auth
  href: https://artifacts.apis.io/caraway-home/security/caraway-home-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/caraway-home-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://carawayhome.com
coverage:
  checked: '2026-10-07'
  detail: No OpenAPI, AsyncAPI, GraphQL, or other machine‑readable contract was discovered despite probing known hosts.
  evidence:
  - status: 404
    url: https://carawayhome.com/api/mcp
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-10-06'
description: Caraway Home creates non‑stick ceramic cookware, bakeware, and home goods with a focus on sustainability and PFAS‑free materials. Their e‑commerce platform offers free shipping, a 30‑day trial, and a health‑conscious kitchen experience. The online store features a wide selection of durable pots, pans, and accessories designed with modern aesthetics, backed by over 180,000 five‑star reviews and a commitment to quality and environmental responsibility.
layout: provider
modified: '2026-10-06'
name: Caraway Home
nav: Providers
network: true
overview: 'Caraway Home is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Cookware, Home Goods, Sustainable, and E-Commerce.


  Caraway Home''s developer surface includes support, engineering blog, and 9 more developer resources.'
random_paper: 14
score:
  band: minimal
  composite: 8.4
  coverage:
    artifact_dirs: 9
    catalog_earned: 30.0
    catalog_earned_first_party: 0.0
    catalog_gap: 85.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -3.8
  facets:
    access_clarity: 10.5
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 3.6
    discoverability: 60.7
    operational_transparency: 2.6
  previous_composite: 12.2
  provenance:
    mcp: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 9.8
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
screenshot: https://apis.io/screenshots/caraway-home/caraway-home-2026-11-03T123253.png
security:
- kind: domain-security
  name: Caraway Home Domain Security
  slug: caraway-home-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: caraway-home
tags:
- Company
- Cookware
- Home Goods
- Sustainable
- E-Commerce
website: https://carawayhome.com
---
