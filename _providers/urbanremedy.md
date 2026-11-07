---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source:
  - authentication
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
    auth_clarity: bearer
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
  score: 2.5
  scored_at: '2026-11-06'
api_count: 1
apis:
- description: 'The public WordPress REST API (wp-json) of the Urban Remedy website at urbanremedy.com: the route index of the site''s content management system, catalogued as one site surface rather than as separate '
  name: Urban Remedy Website (WordPress REST)
  slug: urbanremedy-com-website-wordpress-rest
artifact_total: 3
common:
- group: company
  title: ''
  type: Website
  url: https://urbanremedy.com
- group: company
  title: ''
  type: Blog
  url: https://urbanremedy.com/blog/
- group: operate
  title: ''
  type: Support
  url: https://urbanremedy.com/contact/
- group: start
  title: ''
  type: SignUp
  url: https://urbanremedy.com/my-account/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://urbanremedy.com/terms/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://urbanremedy.com/privacy/
- group: auth
  href: https://artifacts.apis.io/urbanremedy/authentication/urbanremedy-authentication.yml
  title: ''
  type: Authentication
  url: authentication/urbanremedy-authentication.yml
- group: agent
  href: https://artifacts.apis.io/urbanremedy/well-known/urbanremedy-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/urbanremedy-well-known.yml
- group: agent
  href: https://artifacts.apis.io/urbanremedy/llms/urbanremedy-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/urbanremedy-llms.txt
- group: auth
  href: https://artifacts.apis.io/urbanremedy/security/urbanremedy-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/urbanremedy-domain-security.yml
created: '2026-07-17'
description: Urban Remedy is a certified B Corp organic food company founded by Neka Pasquale on the belief that food is healing. It makes fresh, organic, plant-based, ready-to-eat meals, cold pressed juices, juice cleanses, and snacks with fresh, locally sourced ingredients, delivered nationwide and sold through its own retail stores and kiosks. The company runs on WordPress + WooCommerce, exposing a live public storefront REST surface at /wp-json/ alongside its e-commerce site.
image: https://urbanremedy.com/wp-content/uploads/cropped-UR-favicon-192x192.png
layout: provider
modified: '2026-07-25'
name: Urban Remedy
nav: Providers
network: true
overview: 'Urban Remedy is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Food, Organic, Plant-Based, and Juice.


  Urban Remedy''s developer surface includes engineering blog, support, signup flow, authentication, and 6 more developer resources.'
random_paper: 6
score:
  band: emerging
  composite: 18.0
  coverage:
    artifact_dirs: 9
    catalog_earned: 32.0
    catalog_earned_first_party: 0.0
    catalog_gap: 83.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -0.9
  facets:
    access_clarity: 34.2
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 23.8
    discoverability: 57.1
    operational_transparency: 0.0
  previous_composite: 18.9
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 19.6
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
screenshot: https://apis.io/screenshots/urbanremedy/urbanremedy-2026-09-02T165208.png
security:
- kind: authentication
  name: Urbanremedy Authentication
  slug: urbanremedy-authentication
  summary_line: none/apiKey · 2 schemes
- kind: domain-security
  name: Urbanremedy Domain Security
  slug: urbanremedy-domain-security
  summary_line: TLSv1.3 · DMARC
slug: urbanremedy
tags:
- Company
- Food
- Organic
- Plant-Based
- Juice
- Wellness
- E-Commerce
- Retail
website: https://urbanremedy.com
---
