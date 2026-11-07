---
access_model:
  confidence: medium
  gated: none
  gated_source:
  - onboarding
  label: Free · Open access
  onboarding: open
  pricing: free
  public: true
  source:
  - plans
  - authentication
  - security
  trial: false
  try_now: true
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
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: '0.2'
  score: 17.6
  scored_at: '2026-11-06'
api_count: 1
apis:
- description: Programmatic API for Adflipr email marketing automation.
  name: Adflipr API
  slug: adflipr-api
artifact_total: 6
common:
- group: commercial
  href: https://artifacts.apis.io/adflipr-com/plans/adflipr-com-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/adflipr-com-plans-pricing.yml
- group: agent
  href: https://artifacts.apis.io/adflipr-com/llms/adflipr-com-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/adflipr-com-llms.txt
- group: agent
  href: https://artifacts.apis.io/adflipr-com/well-known/adflipr-com-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/adflipr-com-well-known.yml
- group: other
  href: https://artifacts.apis.io/adflipr-com/hosts/adflipr-com-hosts.yml
  title: ''
  type: Hosts
  url: hosts/adflipr-com-hosts.yml
- group: other
  href: https://artifacts.apis.io/adflipr-com/vendors/adflipr-com-vendors.yml
  title: ''
  type: Vendors
  url: vendors/adflipr-com-vendors.yml
- group: start
  title: ''
  type: Login
  url: https://adflipr.com/app/login
- group: operate
  title: ''
  type: ChangeLog
  url: https://adflipr.com/whats-new/
- group: start
  title: ''
  type: GettingStarted
  url: https://adflipr.com/docs/help-docs/getting-started/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/adflipr
- group: auth
  href: https://artifacts.apis.io/adflipr-com/security/adflipr-com-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/adflipr-com-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://adflipr.com/
- group: docs
  title: ''
  type: Documentation
  url: https://adflipr.com/docs/
- group: docs
  title: ''
  type: APIReference
  url: https://adflipr.com/docs/
- group: operate
  title: ''
  type: Support
  url: https://adflipr.com/contact-us/
- group: company
  title: ''
  type: Blog
  url: https://adflipr.com/blog/
- group: commercial
  title: ''
  type: Pricing
  url: https://adflipr.com/pricing/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://adflipr.com/terms-conditions/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://adflipr.com/privacy-policy/
coverage:
  checked: '2026-10-31'
  detail: API base URL https://adflipr.com/api/v1 returns 401 Unauthorized, indicating authentication required.
  evidence:
  - status: 401
    url: https://adflipr.com/api/v1/openapi.json
  reason: auth-required
  state: gated
created: '2026-10-31'
description: Adflipr is an all-in-one email marketing automation platform for eCommerce. It automates campaigns, recovers abandoned carts, and grows revenue with Shopify and WooCommerce integrations. Learn how Adflipr transforms eCommerce marketing automation, its mission and vision to empower businesses to automate marketing with ease and efficiency.
image: https://adflipr.com/wp-content/uploads/2024/07/adflipr_black_logo.svg
layout: provider
modified: '2026-10-31'
name: Adflipr
nav: Providers
network: true
overview: 'Adflipr is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Email Marketing, Automation, E-Commerce, Software-as-a-Service, and Marketing.


  Adflipr''s developer surface includes changelog, getting-started guide, documentation, API reference, support, engineering blog, pricing, and 11 more developer resources.'
plans:
- name: Adflipr Com Plans Pricing
  plan_count: 1
  slug: adflipr-com-plans-pricing
random_paper: 22
rate_limits:
- limit_count: 0
  name: Adflipr Com Rate Limits
  slug: adflipr-com-rate-limits
scopes:
- name: Adflipr Com Scopes
  scope_count: 0
  slug: adflipr-com-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: emerging
  composite: 21.8
  coverage:
    artifact_dirs: 20
    catalog_earned: 45.0
    catalog_earned_first_party: 8.0
    catalog_gap: 70.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -10.0
  facets:
    access_clarity: 43.4
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 17.9
    discoverability: 66.1
    operational_transparency: 10.5
  previous_composite: 31.8
  provenance:
    conformance: unknown
    mcp: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 25.5
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: falling
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: authentication
  name: Adflipr Com Authentication
  slug: adflipr-com-authentication
  summary_line: 0 schemes
- kind: domain-security
  name: Adflipr Com Domain Security
  slug: adflipr-com-domain-security
  summary_line: TLSv1.3 · DMARC
slug: adflipr-com
tags:
- Email Marketing
- Automation
- E-Commerce
- Software-as-a-Service
- Marketing
website: https://adflipr.com/
---
