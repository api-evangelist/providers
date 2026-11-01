---
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
  score: 13.9
  scored_at: '2026-10-31'
api_count: 1
apis:
- description: Meal‑planning API (no public contract discovered)
  name: noshup-ca API
  slug: noshup-ca-api
artifact_total: 3
common:
- group: commercial
  href: https://artifacts.apis.io/noshup-ca/plans/noshup-ca-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/noshup-ca-plans-pricing.yml
- group: agent
  href: https://artifacts.apis.io/noshup-ca/llms/noshup-ca-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/noshup-ca-llms.txt
- group: agent
  href: https://artifacts.apis.io/noshup-ca/well-known/noshup-ca-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/noshup-ca-well-known.yml
- group: other
  href: https://artifacts.apis.io/noshup-ca/hosts/noshup-ca-hosts.yml
  title: ''
  type: Hosts
  url: hosts/noshup-ca-hosts.yml
- group: other
  href: https://artifacts.apis.io/noshup-ca/vendors/noshup-ca-vendors.yml
  title: ''
  type: Vendors
  url: vendors/noshup-ca-vendors.yml
- group: start
  title: ''
  type: Login
  url: https://noshup.ca/login
- group: operate
  title: ''
  type: ChangeLog
  url: https://noshup.ca/blog/releases
- group: auth
  href: https://artifacts.apis.io/noshup-ca/security/noshup-ca-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/noshup-ca-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://noshup.ca/
- group: commercial
  title: ''
  type: Pricing
  url: https://noshup.ca/pricing
- group: company
  title: ''
  type: Blog
  url: https://noshup.ca/blog
- group: commercial
  title: ''
  type: TermsOfService
  url: https://noshup.ca/legal/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://noshup.ca/legal/privacy
- group: operate
  title: ''
  type: Support
  url: https://noshup.ca/contact
coverage:
  checked: '2026-10-30'
  detail: No OpenAPI, AsyncAPI, GraphQL, gRPC, or WSDL spec found despite public documentation pages.
  evidence:
  - status: 200
    url: https://noshup.ca/
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-10-30'
description: NoshUp is a Canadian meal‑planning and recipe management platform that helps households create weekly meal plans, generate grocery lists, and match items to flyer deals from major Canadian retailers such as FreshCo, Costco, and Walmart. Users can import existing recipes, customize dietary preferences, and track spending, while the service integrates with AI assistants for conversational planning. The platform offers free and paid tiers, supports multiple diets, and aims to reduce food waste and grocery costs for families across Canada.
image: https://noshup.ca/og-image.png
layout: provider
modified: '2026-10-30'
name: noshup-ca
nav: Providers
network: true
overview: 'noshup-ca is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Meal Planning, Recipes, Grocery, Canadian, and AI Integration.


  noshup-ca''s developer surface includes changelog, pricing, engineering blog, support, and 10 more developer resources.'
plans:
- name: Noshup Ca Plans Pricing
  plan_count: 3
  slug: noshup-ca-plans-pricing
random_paper: 22
score:
  band: emerging
  composite: 25.1
  coverage:
    artifact_dirs: 9
    catalog_earned: 44.0
    catalog_earned_first_party: 12.0
    catalog_gap: 71.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 76.3
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 7.1
    discoverability: 57.1
    operational_transparency: 15.8
  provenance:
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
  name: Noshup Ca Domain Security
  slug: noshup-ca-domain-security
  summary_line: TLSv1.3 · DMARC
slug: noshup-ca
tags:
- Meal Planning
- Recipes
- Grocery
- Canadian
- AI Integration
website: https://noshup.ca/
---
