---
access_model:
  confidence: low
  label: Paid
  onboarding: unknown
  pricing: paid
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
  href: https://artifacts.apis.io/belly/plans/belly-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/belly-plans-pricing.yml
- group: other
  href: https://artifacts.apis.io/belly/hosts/belly-hosts.yml
  title: ''
  type: Hosts
  url: hosts/belly-hosts.yml
- group: other
  href: https://artifacts.apis.io/belly/vendors/belly-vendors.yml
  title: ''
  type: Vendors
  url: vendors/belly-vendors.yml
- group: build
  href: https://artifacts.apis.io/belly/packages/belly-packages.yml
  title: ''
  type: SDKs
  url: packages/belly-packages.yml
- group: build
  href: https://artifacts.apis.io/belly/packages/belly-packages.yml
  title: ''
  type: Packages
  url: packages/belly-packages.yml
- group: start
  title: ''
  type: SignUp
  url: https://www.bellycard.com/get-sub/sign-up/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.bellycard.com/privacy/
- group: commercial
  title: ''
  type: Pricing
  url: https://www.bellycard.com/business/pricing/
- group: other
  title: ''
  type: Leadership
  url: https://www.bellycard.com/about/team/
- group: company
  title: ''
  type: Blog
  url: https://www.bellycard.com/resources/category/blog
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/bellycard
- group: auth
  href: https://artifacts.apis.io/belly/security/belly-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/belly-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.bellycard.com
- group: operate
  title: ''
  type: Support
  url: https://www.bellycard.com/support
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.bellycard.com/terms-policy
coverage:
  detail: the company publishes no developer documentation host and no machine-readable contract on its own domain
  evidence:
  - status: 403
    url: https://api.bellycard.com/mcp
  - status: 403
    url: https://www.bellycard.com/mcp
  - status: null
    url: https://www.bellycard.com
  reason: no-developer-program
  state: none
created: '2026-10-25'
description: Belly provides a customer loyalty and marketing automation platform for small and medium businesses. Founded in 2011, Belly offers a customizable loyalty program that integrates with point-of-sale systems, delivers analytics, and helps businesses engage customers through rewards, campaigns, and personalized experiences. The service is used by retailers, restaurants, and other consumer‑facing brands to build lasting relationships and gather actionable insights.
layout: provider
modified: '2026-10-25'
name: Belly
nav: Providers
network: true
overview: 'Belly is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Loyalty, Marketing, Small Business, Retail, and Software-as-a-Service.


  Belly''s developer surface includes signup flow, pricing, engineering blog, support, and 11 more developer resources.'
plans:
- name: Belly Plans Pricing
  plan_count: 3
  slug: belly-plans-pricing
random_paper: 8
score:
  band: emerging
  composite: 17.0
  coverage:
    artifact_dirs: 11
    catalog_earned: 37.0
    catalog_earned_first_party: 12.0
    catalog_gap: 78.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -6.2
  facets:
    access_clarity: 53.9
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 10.7
    discoverability: 45.5
    operational_transparency: 2.6
  previous_composite: 23.2
  provenance:
    conformance: unknown
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 9.8
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: falling
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
screenshot: https://apis.io/screenshots/belly/belly-2026-11-03T121648.png
security:
- kind: domain-security
  name: Belly Domain Security
  slug: belly-domain-security
  summary_line: TLSv1.3
slug: belly
tags:
- Loyalty
- Marketing
- Small Business
- Retail
- Software-as-a-Service
- Company
website: https://www.bellycard.com
---
