---
agent_readiness:
  band: agent-ready
  band_gated_from: agent-native
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
    error_semantics: verified
    event_surface_described: false
    idempotency: false
    mcp_server: documented
    openapi_examples: partial
    operation_distinctiveness: distinct
    pagination_ratio: partial
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: true
  schema_version: '0.2'
  score: 43.8
  scored_at: '2026-10-31'
api_count: 1
apis:
- baseURL: https://api.bettermenu.live
  baseurl_source: declared
  description: The Conversions API from BetterMenu — 1 operation(s) for conversions.
  name: BetterMenu Conversions API
  slug: bettermenu-conversions-api
- baseURL: https://api.bettermenu.live
  baseurl_source: declared
  description: Account entitlement and plan status.
  name: BetterMenu Entitlements API
  slug: bettermenu-entitlements-api
- baseURL: https://api.bettermenu.live
  baseurl_source: declared
  description: Organization-level capabilities spanning multiple resource types (e.g. search).
  name: BetterMenu Org API
  slug: bettermenu-org-api
- baseURL: https://api.bettermenu.live
  baseurl_source: declared
  description: 'Recipe authoring: create and manage recipes, servings, ingredient resolution, nutrition computation and analysis, labels, and version history.'
  name: BetterMenu Studio API
  slug: bettermenu-studio-api
artifact_total: 6
common:
- group: commercial
  href: https://artifacts.apis.io/bettermenu/plans/bettermenu-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/bettermenu-plans-pricing.yml
- group: design
  href: https://artifacts.apis.io/bettermenu/data-model/bettermenu-data-model.yml
  title: ''
  type: DataModel
  url: data-model/bettermenu-data-model.yml
- group: design
  href: https://artifacts.apis.io/bettermenu/errors/bettermenu-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/bettermenu-problem-types.yml
- group: agent
  href: https://artifacts.apis.io/bettermenu/llms/bettermenu-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/bettermenu-llms.txt
- group: auth
  href: https://artifacts.apis.io/bettermenu/well-known/bettermenu-www-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/bettermenu-www-security.txt
- group: agent
  href: https://artifacts.apis.io/bettermenu/well-known/bettermenu-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/bettermenu-well-known.yml
- group: other
  href: https://artifacts.apis.io/bettermenu/hosts/bettermenu-hosts.yml
  title: ''
  type: Hosts
  url: hosts/bettermenu-hosts.yml
- group: other
  href: https://artifacts.apis.io/bettermenu/vendors/bettermenu-vendors.yml
  title: ''
  type: Vendors
  url: vendors/bettermenu-vendors.yml
- group: operate
  title: ''
  type: ChangeLog
  url: https://bettermenu.live/changelog/
- group: auth
  href: https://artifacts.apis.io/bettermenu/security/bettermenu-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/bettermenu-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://bettermenu.live/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.bettermenu.live/docs/api
- group: docs
  title: ''
  type: APIReference
  url: https://docs.bettermenu.live/docs/api
- group: commercial
  title: ''
  type: Pricing
  url: https://bettermenu.live/pricing/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://bettermenu.live/terms/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://bettermenu.live/privacy/
- group: operate
  title: ''
  type: Support
  url: https://bettermenu.live/support/
- group: company
  title: ''
  type: Blog
  url: https://bettermenu.live/blog/
coverage:
  checked: '2026-10-21'
  detail: The provider's documentation at https://docs.bettermenu.live/docs/api is HTML with no machine‑readable OpenAPI/AsyncAPI/GraphQL spec.
  evidence:
  - status: 200
    url: https://docs.bettermenu.live/docs/api
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-10-21'
description: BetterMenu provides a cloud‑based recipe formulation platform for food manufacturers, enabling rapid product development with built‑in FDA‑compliant nutrition labeling. Users can input ingredient lists and instantly generate nutrition facts panels, streamline formulation, and accelerate time‑to‑market while ensuring regulatory compliance. The service offers a web‑based interface, pricing plans, and integrates FDA guidelines to help bring food products to market faster.
image: https://bettermenu.live/images/og-image.png
layout: provider
modified: '2026-10-21'
name: BetterMenu
nav: Providers
network: true
overview: 'BetterMenu publishes 4 API contracts indexed on the [APIs.io](https://apis.io/) network, including Conversions API, Entitlements API, Org API, and 1 more. Tagged areas include FoodTech, RecipeFormulation, FDACompliance, SaaS, and Cloud.


  BetterMenu''s developer surface includes changelog, documentation, API reference, pricing, support, engineering blog, and 12 more developer resources.'
plans:
- name: Bettermenu Plans Pricing
  plan_count: 1
  slug: bettermenu-plans-pricing
random_paper: 3
score:
  band: thin
  composite: 34.3
  coverage:
    artifact_dirs: 13
    catalog_earned: 45.0
    catalog_earned_first_party: 8.0
    catalog_gap: 70.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 52.6
    contract_governance: 0.0
    contract_quality: 33.3
    developer_ergonomics: 23.8
    discoverability: 66.1
    operational_transparency: 26.3
  provenance:
    contracts:
      callable: 0.0
      derived: 1
      marker_coverage: 25.0
      total: 4
    mcp: unknown
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
- kind: domain-security
  name: Bettermenu Domain Security
  slug: bettermenu-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: bettermenu
tags:
- FoodTech
- RecipeFormulation
- FDACompliance
- SaaS
- Cloud
website: https://bettermenu.live/
---
