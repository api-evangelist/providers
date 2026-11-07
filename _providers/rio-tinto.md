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
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: '0.2'
  score: 2.5
  scored_at: '2026-11-06'
api_count: 0
artifact_total: 10
common:
- group: other
  href: https://artifacts.apis.io/rio-tinto/hosts/rio-tinto-hosts.yml
  title: ''
  type: Hosts
  url: hosts/rio-tinto-hosts.yml
- group: other
  href: https://artifacts.apis.io/rio-tinto/vendors/rio-tinto-vendors.yml
  title: ''
  type: Vendors
  url: vendors/rio-tinto-vendors.yml
- group: company
  title: ''
  type: Blog
  url: https://www.riotinto.com/en/news
- group: company
  title: ''
  type: BlogRSS
  url: https://www.riotinto.com/en/news/feed/
- group: auth
  href: https://artifacts.apis.io/rio-tinto/security/rio-tinto-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/rio-tinto-domain-security.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/rio-tinto
- group: company
  title: ''
  type: Website
  url: https://www.riotinto.com/
- group: build
  title: ''
  type: GitHubOrg
  url: https://github.com/rio-tinto
- group: start
  title: ''
  type: SupplierPortal
  url: https://www.riotinto.com/en/about/suppliers/supplier-portals
- group: operate
  title: ''
  type: Support
  url: https://www.riotinto.com/en/utility/contact
- group: company
  title: ''
  type: Careers
  url: https://www.riotinto.com/en/careers
- group: company
  title: ''
  type: InvestorRelations
  url: https://www.riotinto.com/en/invest
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.riotinto.com/en/utility/terms-conditions
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.riotinto.com/en/utility/privacy-cookies
- group: design
  href: https://artifacts.apis.io/rio-tinto/vocabulary/rio-tinto-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/rio-tinto-vocabulary.yml
created: '2026-05-05'
description: Rio Tinto is a British-Australian multinational mining and metals corporation and one of the world's largest producers of iron ore, aluminum, copper, and diamonds. Rio Tinto does not publish a public developer API, but operates supplier portals (Supplier Master Data Management and a transactional platform) and a START traceability program. Its GitHub presence is limited to a small number of internal forks (ai-sentry, xpano).
features:
- description: Leading global producer of iron ore from Pilbara and other regions
  name: Iron Ore Production
- description: Integrated aluminum value chain from bauxite mining to smelting
  name: Aluminum and Bauxite
- description: Copper concentrates and diamond production for global markets
  name: Copper and Diamonds
- description: Lithium and other minerals critical to electrification
  name: Energy-Transition Minerals
- description: Product traceability program for responsibly sourced metals
  name: START Traceability
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/rio-tinto.png
layout: provider
modified: '2026-10-20'
name: Rio Tinto
nav: Providers
network: true
overview: 'Rio Tinto is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Mining, Metals, Resources, Critical Minerals, and Iron Ore.


  Rio Tinto''s developer surface includes engineering blog, support, and 13 more developer resources.'
plans:
- name: Rio Tinto Plans Pricing
  plan_count: 0
  slug: rio-tinto-plans-pricing
random_paper: 21
rate_limits:
- limit_count: 0
  name: Rio Tinto Rate Limits
  slug: rio-tinto-rate-limits
score:
  band: minimal
  composite: 10.1
  coverage:
    artifact_dirs: 15
    catalog_earned: 31.5
    catalog_earned_first_party: 0.0
    catalog_gap: 83.5
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -3.2
  facets:
    access_clarity: 10.5
    contract_governance: 13.6
    contract_quality: 0.0
    developer_ergonomics: 4.8
    discoverability: 48.2
    operational_transparency: 5.3
  previous_composite: 13.3
  provenance:
    mcp: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 14.7
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
screenshot: https://apis.io/screenshots/rio-tinto/rio-tinto-2026-06-20T193124.png
security:
- kind: domain-security
  name: Rio Tinto Domain Security
  slug: rio-tinto-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: rio-tinto
tags:
- Mining
- Metals
- Resources
- Critical Minerals
- Iron Ore
- Copper
- Aluminium
- Supply Chain
use_cases:
- description: Rio Tinto maintains supplier master data and transactional portals
  name: Supplier Onboarding
- description: START provides end-to-end traceability of materials from mine to product
  name: Responsible Sourcing
website: https://www.riotinto.com/
---
