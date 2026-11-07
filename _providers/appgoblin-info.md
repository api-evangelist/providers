---
access_model:
  confidence: low
  label: Freemium
  onboarding: unknown
  pricing: freemium
  public: false
  source:
  - plans
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
api_count: 0
artifact_total: 2
common:
- group: commercial
  href: https://artifacts.apis.io/appgoblin-info/plans/appgoblin-info-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/appgoblin-info-plans-pricing.yml
- group: agent
  href: https://artifacts.apis.io/appgoblin-info/well-known/appgoblin-info-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/appgoblin-info-well-known.yml
- group: other
  href: https://artifacts.apis.io/appgoblin-info/hosts/appgoblin-info-hosts.yml
  title: ''
  type: Hosts
  url: hosts/appgoblin-info-hosts.yml
- group: other
  href: https://artifacts.apis.io/appgoblin-info/vendors/appgoblin-info-vendors.yml
  title: ''
  type: Vendors
  url: vendors/appgoblin-info-vendors.yml
- group: start
  title: ''
  type: SignUp
  url: https://appgoblin.info/auth/signup
- group: build
  title: ''
  type: SDKs
  url: https://appgoblin.info/sdks
- group: auth
  href: https://artifacts.apis.io/appgoblin-info/security/appgoblin-info-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/appgoblin-info-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://appgoblin.info/
- group: docs
  title: ''
  type: Documentation
  url: https://appgoblin.info/api-docs
- group: commercial
  title: ''
  type: Pricing
  url: https://appgoblin.info/pricing
- group: company
  title: ''
  type: Blog
  url: https://appgoblin.info/blog
- group: operate
  title: ''
  type: Contact
  url: https://appgoblin.info/contact
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://appgoblin.info/privacy_policy.html
coverage:
  checked: '2026-11-01'
  detail: The public API documentation page provides HTML only and no OpenAPI, AsyncAPI, GraphQL, gRPC, or WSDL contracts were discovered after exhaustive probing.
  evidence:
  - status: 200
    url: https://appgoblin.info/api-docs
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-11-01'
description: AppGoblin provides free and paid mobile app marketing tools, offering B2B intelligence on app rankings, SDK usage, ad creatives, and growth trends. Their platform lets users track install estimates, monitor keyword performance, analyze SDK stacks across millions of Android and iOS apps, and access detailed reports on ad networks and product analytics. Targeted at app marketers, ASO teams, and competitor researchers, AppGoblin delivers real‑time insights, data exports, and customizable dashboards to inform acquisition strategies and market analysis.
image: https://appgoblin.info/previews/appgoblin_companies_smaller.png
layout: provider
modified: '2026-11-01'
name: AppGoblin
nav: Providers
network: true
overview: 'AppGoblin is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Mobile, Marketing, Analytics, B2B, and Intelligence.


  AppGoblin''s developer surface includes signup flow, documentation, pricing, engineering blog, and 9 more developer resources.'
plans:
- name: Appgoblin Info Plans Pricing
  plan_count: 3
  slug: appgoblin-info-plans-pricing
random_paper: 13
score:
  band: emerging
  composite: 16.1
  coverage:
    artifact_dirs: 8
    catalog_earned: 39.0
    catalog_earned_first_party: 12.0
    catalog_gap: 76.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -4.9
  facets:
    access_clarity: 48.7
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 13.1
    discoverability: 48.2
    operational_transparency: 0.0
  previous_composite: 21.0
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 7.8
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Appgoblin Info Domain Security
  slug: appgoblin-info-domain-security
  summary_line: TLSv1.3 · DMARC
slug: appgoblin-info
tags:
- Mobile
- Marketing
- Analytics
- B2B
- Intelligence
website: https://appgoblin.info/
---
