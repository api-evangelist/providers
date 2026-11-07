---
access_model:
  confidence: low
  gated: none
  gated_source:
  - onboarding
  label: Paid · Open access
  onboarding: open
  pricing: paid
  public: true
  source:
  - plans
  - security
  trial: false
  try_now: false
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
  score: 18.7
  scored_at: '2026-11-06'
api_count: 1
apis:
- description: AdLiftr provides a REST API for managing media buying campaigns, but the developer portal requires authentication and does not expose public documentation.
  name: AdLiftr API
  slug: adliftr-api
artifact_total: 3
common:
- group: commercial
  href: https://artifacts.apis.io/adliftr-com/plans/adliftr-com-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/adliftr-com-plans-pricing.yml
- group: agent
  href: https://artifacts.apis.io/adliftr-com/llms/adliftr-com-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/adliftr-com-llms.txt
- group: agent
  href: https://artifacts.apis.io/adliftr-com/well-known/adliftr-com-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/adliftr-com-well-known.yml
- group: other
  href: https://artifacts.apis.io/adliftr-com/hosts/adliftr-com-hosts.yml
  title: ''
  type: Hosts
  url: hosts/adliftr-com-hosts.yml
- group: other
  href: https://artifacts.apis.io/adliftr-com/vendors/adliftr-com-vendors.yml
  title: ''
  type: Vendors
  url: vendors/adliftr-com-vendors.yml
- group: auth
  href: https://artifacts.apis.io/adliftr-com/security/adliftr-com-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/adliftr-com-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://adliftr.com/
- group: company
  title: ''
  type: Blog
  url: https://adliftr.com/blog
- group: start
  title: ''
  type: DeveloperPortal
  url: https://developers.adliftr.com/
- group: start
  title: ''
  type: Login
  url: https://app.adliftr.com/auth/login
- group: start
  title: ''
  type: SignUp
  url: https://app.adliftr.com/auth/sign-up
- group: commercial
  title: ''
  type: Pricing
  url: https://adliftr.com/pricing
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://adliftr.com/privacy
- group: commercial
  title: ''
  type: TermsOfService
  url: https://adliftr.com/terms
- group: docs
  title: ''
  type: Documentation
  url: https://developers.adliftr.com/
- group: docs
  title: ''
  type: APIReference
  url: https://developers.adliftr.com/
- group: start
  title: ''
  type: GettingStarted
  url: https://developers.adliftr.com/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/AdLiftr
coverage:
  checked: '2026-10-31'
  detail: Developer portal redirects to a login page, preventing public access to API documentation.
  evidence:
  - status: 200
    url: https://developers.adliftr.com/
  reason: auth-required
  state: gated
created: '2026-10-31'
description: AdLiftr is a media buying platform that lets performance marketers, DTC brands, and agencies bulk launch ads to Meta, TikTok, Google Ads, and Snapchat in minutes. Connect once, upload your creatives, and launch batches without Ads Manager repetition — from the dashboard, the REST API, or your AI assistant via MCP. 7-day free trial, no credit card required.
image: https://adliftr.com/og-image.png
layout: provider
modified: '2026-10-31'
name: AdLiftr
nav: Providers
network: true
overview: 'AdLiftr is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Media Buying, Performance Marketing, Advertising, and MCP.


  AdLiftr''s developer surface includes engineering blog, signup flow, pricing, documentation, API reference, getting-started guide, and 12 more developer resources.'
plans:
- name: Adliftr Com Plans Pricing
  plan_count: 3
  slug: adliftr-com-plans-pricing
random_paper: 2
score:
  band: emerging
  composite: 20.1
  coverage:
    artifact_dirs: 9
    catalog_earned: 39.0
    catalog_earned_first_party: 12.0
    catalog_gap: 76.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -10.3
  facets:
    access_clarity: 53.9
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 20.2
    discoverability: 48.2
    operational_transparency: 2.6
  previous_composite: 30.4
  provenance:
    mcp: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 15.7
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: falling
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Adliftr Com Domain Security
  slug: adliftr-com-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: adliftr-com
tags:
- Media Buying
- Performance Marketing
- Advertising
- MCP
website: https://adliftr.com/
---
