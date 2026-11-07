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
  href: https://artifacts.apis.io/stuck/plans/stuck-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/stuck-plans-pricing.yml
- group: company
  title: ''
  type: Website
  url: https://stucktheapp.com
- group: start
  title: ''
  type: SignUp
  url: https://app.stucktheapp.com
- group: start
  title: ''
  type: Login
  url: https://app.stucktheapp.com
- group: company
  title: ''
  type: Blog
  url: https://stucktheapp.com/blogs
- group: commercial
  title: ''
  type: Pricing
  url: https://stucktheapp.com/#pricing
- group: operate
  title: ''
  type: Support
  url: mailto:stuck@stucktheapp.com
- group: auth
  href: https://artifacts.apis.io/stuck/security/stuck-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/stuck-domain-security.yml
created: '2026-07-17'
description: STUCK? is a content creation, translation, and localization platform based in Jeddah, Saudi Arabia that pairs AI efficiency with human expertise. Customers can request work fully AI-powered, fully human-expert-led, or as a hybrid (AI drafting with human review) across translation, content writing, video subtitling, editing, and dialect localization. The platform matches requesters to vetted experts in under ten minutes, supports direct chat and document upload, and runs a quality-assurance review step. Pricing spans pay-as-you-go, monthly and annual subscriptions, and custom enterprise plans. Stuck is a portfolio company of 500 Global and was added to the API Evangelist network as a company profile; it publishes a web/app product but no public developer API at this time.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/stuck.png
layout: provider
modified: '2026-07-21'
name: Stuck
nav: Providers
network: true
overview: 'Stuck is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Translation, Localization, Content, and Artificial Intelligence.


  Stuck''s developer surface includes signup flow, engineering blog, pricing, support, and 4 more developer resources.'
plans:
- name: Stuck Plans Pricing
  plan_count: 4
  slug: stuck-plans-pricing
random_paper: 2
score:
  band: emerging
  composite: 12.2
  coverage:
    artifact_dirs: 6
    catalog_earned: 39.0
    catalog_earned_first_party: 12.0
    catalog_gap: 76.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 36.8
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 7.1
    discoverability: 48.2
    operational_transparency: 0.0
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    countries:
    - saudi-arabia
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
    regions:
    - mena
    - middle-east
  previous_composite: 12.2
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 5.5
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
screenshot: https://apis.io/screenshots/stuck/stuck-2026-09-02T161029.png
security:
- kind: domain-security
  name: Stuck Domain Security
  slug: stuck-domain-security
  summary_line: TLSv1.3 · DMARC
slug: stuck
tags:
- Company
- Translation
- Localization
- Content
- Artificial Intelligence
- Software-as-a-Service
website: https://stucktheapp.com
---
