---
access_model:
  confidence: medium
  label: Freemium
  onboarding: unknown
  pricing: freemium
  public: false
  source:
  - plans
  - authentication
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
    mcp_server: documented
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
  score: 21.8
  scored_at: '2026-11-06'
api_count: 1
apis:
- description: AdAce Ads API provides advertising management endpoints.
  name: AdAce Ads API
  slug: adace-ads-api
artifact_total: 4
common:
- group: commercial
  href: https://artifacts.apis.io/adace-website/plans/adace-website-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/adace-website-plans-pricing.yml
- group: auth
  href: https://artifacts.apis.io/adace-website/authentication/adace-website-authentication.yml
  title: ''
  type: Authentication
  url: authentication/adace-website-authentication.yml
- group: design
  href: https://artifacts.apis.io/adace-website/conformance/adace-website-conformance.yml
  title: ''
  type: Conformance
  url: conformance/adace-website-conformance.yml
- group: agent
  href: https://artifacts.apis.io/adace-website/llms/adace-website-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/adace-website-llms.txt
- group: auth
  href: https://artifacts.apis.io/adace-website/well-known/adace-website-ads-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/adace-website-ads-security.txt
- group: agent
  href: https://artifacts.apis.io/adace-website/well-known/adace-website-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/adace-website-well-known.yml
- group: other
  href: https://artifacts.apis.io/adace-website/hosts/adace-website-hosts.yml
  title: ''
  type: Hosts
  url: hosts/adace-website-hosts.yml
- group: other
  href: https://artifacts.apis.io/adace-website/vendors/adace-website-vendors.yml
  title: ''
  type: Vendors
  url: vendors/adace-website-vendors.yml
- group: auth
  title: ''
  type: TrustCenter
  url: https://ads.adace.website/en/trust
- group: commercial
  title: ''
  type: TermsOfService
  url: https://ads.adace.website/en/terms
- group: operate
  title: ''
  type: Support
  url: https://ads.adace.website/en/support
- group: auth
  title: ''
  type: Security
  url: https://ads.adace.website/en/blog/security
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://ads.adace.website/en/privacy
- group: company
  title: ''
  type: Newsroom
  url: https://ads.adace.website/en/press
- group: operate
  title: ''
  type: ChangeLog
  url: https://ads.adace.website/en/whats-new
- group: auth
  href: https://artifacts.apis.io/adace-website/security/adace-website-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/adace-website-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://adace.website/
- group: start
  title: ''
  type: GettingStarted
  url: https://adace.website/about.html
- group: company
  title: ''
  type: Blog
  url: https://adace.website/blog
- group: commercial
  title: ''
  type: Pricing
  url: https://adace.website/payment/
- group: operate
  title: ''
  type: Contact
  url: https://adace.website/contacts.html
coverage:
  detail: the company serves an API surface but requires credentials before any description of it can be read
  evidence:
  - status: null
    url: https://ads.adace.website/openapi.json
  - status: 401
    url: https://ads.adace.website/mcp
  - status: 200
    url: https://adace.website/
  reason: partner-login
  state: gated
created: '2026-10-31'
description: AdAce is a full‑cycle advertising agency specializing in lead generation across Google, Meta, TikTok, and LinkedIn. They offer turnkey solutions including ad campaign management, website development, analytics, and recruitment software, serving over 100 clients since 2023 with measurable results such as 6,700+ leads per campaign and cost‑per‑lead as low as $0.61.
image: https://adace.website/assets/img/og.png
layout: provider
modified: '2026-10-31'
name: AdAce
nav: Providers
network: true
overview: 'AdAce is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Advertising, Lead Generation, Marketing, Software-as-a-Service, and Agency.


  AdAce''s developer surface includes authentication, support, changelog, getting-started guide, engineering blog, pricing, and 15 more developer resources.'
plans:
- name: Adace Website Plans Pricing
  plan_count: 8
  slug: adace-website-plans-pricing
random_paper: 22
score:
  band: emerging
  composite: 24.7
  coverage:
    artifact_dirs: 11
    catalog_earned: 49.0
    catalog_earned_first_party: 12.0
    catalog_gap: 66.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -8.6
  facets:
    access_clarity: 51.3
    contract_governance: 4.5
    contract_quality: 0.0
    developer_ergonomics: 21.4
    discoverability: 67.0
    operational_transparency: 13.2
  previous_composite: 33.3
  provenance:
    conformance: derived
    mcp: unknown
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 23.0
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: falling
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: authentication
  name: Adace Website Authentication
  slug: adace-website-authentication
  summary_line: 1 scheme
- kind: domain-security
  name: Adace Website Domain Security
  slug: adace-website-domain-security
  summary_line: TLSv1.3
slug: adace-website
tags:
- Advertising
- Lead Generation
- Marketing
- Software-as-a-Service
- Agency
website: https://adace.website/
---
