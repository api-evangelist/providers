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
  band: agent-aware
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
    operation_distinctiveness: distinct
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 17.3
  scored_at: '2026-11-06'
api_count: 2
apis:
- description: API for Fleek subscription and rewards platform
  name: Fleek API
  slug: fleek-api
- baseURL: https://api.getfleek.app
  baseurl_source: declared
  description: 'getfleek-app API as documented publicly: 6 operations. Contract generated from the documentation by API Evangelist (2026-10-30); not the provider''s own document.'
  name: getfleek-app API
  slug: getfleek-app-api
artifact_total: 7
common:
- group: commercial
  href: https://artifacts.apis.io/getfleek-app/plans/getfleek-app-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/getfleek-app-plans-pricing.yml
- group: design
  href: https://artifacts.apis.io/getfleek-app/rules/getfleek-app-rules.yml
  title: ''
  type: Spectral
  url: rules/getfleek-app-rules.yml
- group: design
  href: https://artifacts.apis.io/getfleek-app/json-ld/getfleek-app-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/getfleek-app-context.jsonld
- group: design
  href: https://artifacts.apis.io/getfleek-app/vocabulary/getfleek-app-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/getfleek-app-vocabulary.yml
- group: design
  href: https://artifacts.apis.io/getfleek-app/data-model/getfleek-app-data-model.yml
  title: ''
  type: DataModel
  url: data-model/getfleek-app-data-model.yml
- group: design
  href: https://artifacts.apis.io/getfleek-app/conformance/getfleek-app-conformance.yml
  title: ''
  type: Conformance
  url: conformance/getfleek-app-conformance.yml
- group: agent
  href: https://artifacts.apis.io/getfleek-app/llms/getfleek-app-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/getfleek-app-llms.txt
- group: other
  href: https://artifacts.apis.io/getfleek-app/hosts/getfleek-app-hosts.yml
  title: ''
  type: Hosts
  url: hosts/getfleek-app-hosts.yml
- group: other
  href: https://artifacts.apis.io/getfleek-app/vendors/getfleek-app-vendors.yml
  title: ''
  type: Vendors
  url: vendors/getfleek-app-vendors.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://getfleek.app/terms-and-conditions
- group: start
  title: ''
  type: SignUp
  url: https://partners.getfleek.app/sign-up?utm_source=getfleek&utm_medium=website&utm_campaign=nav
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://getfleek.app/privacy-policy
- group: auth
  href: https://artifacts.apis.io/getfleek-app/security/getfleek-app-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/getfleek-app-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://getfleek.app/
- group: docs
  title: ''
  type: Documentation
  url: https://getfleek.app/developers
- group: company
  title: ''
  type: About
  url: https://getfleek.app/about
- group: company
  title: ''
  type: Blog
  url: https://getfleek.app/blog
- group: operate
  title: ''
  type: Contact
  url: https://getfleek.app/contact-us
created: '2026-10-30'
description: Fleek is a subscription and rewards platform that helps consumers discover, track, and manage recurring services across various categories. With over 6 million users and 1,500+ merchant partners, Fleek offers a unified dashboard to monitor renewals, cancel subscriptions, and earn rewards. The service is used by banks, fintechs, and enterprises to quickly launch subscription and rewards programs, providing a seamless integration for both consumers and businesses.
json_schemas:
- name: PostPartnerV3OrdersRequest
  property_count: 3
  slug: getfleek-app-post-partner-v3-orders-request
jsonld:
- class_count: 1
  name: Getfleek App Context
  property_count: 3
  slug: getfleek-app-context
layout: provider
modified: '2026-10-30'
name: getfleek-app
nav: Providers
network: true
overview: 'getfleek-app is listed with 2 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Subscription, Rewards, Fintech, Consumer App, and Platform.


  The getfleek-app catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  getfleek-app''s developer surface includes signup flow, documentation, engineering blog, and 15 more developer resources.'
plans:
- name: Getfleek App Plans Pricing
  plan_count: 4
  slug: getfleek-app-plans-pricing
random_paper: 5
rules:
- authorship: generated
  effective_rule_count: 51
  extends:
  - spectral:oas
  name: getfleek-app API Rules
  rule_count: 10
  severity_counts:
    error: 9
    hint: 0
    info: 1
    warn: 0
  slug: getfleek-app-rules
score:
  band: emerging
  composite: 23.4
  coverage:
    artifact_dirs: 19
    catalog_earned: 57.4
    catalog_earned_first_party: 12.0
    catalog_gap: 57.6
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -5.1
  facets:
    access_clarity: 48.7
    contract_governance: 19.7
    contract_quality: 19.0
    developer_ergonomics: 6.0
    discoverability: 60.7
    operational_transparency: 0.0
  previous_composite: 28.5
  provenance:
    conformance: derived
    contracts:
      callable: 100.0
      derived: 1
      marker_coverage: 100.0
      total: 1
    mcp: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 14.7
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: falling
  upsert:
    applies: true
    score: 0.0
screenshot: https://apis.io/screenshots/getfleek-app/getfleek-app-2026-11-03T132711.png
security:
- kind: domain-security
  name: Getfleek App Domain Security
  slug: getfleek-app-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
slug: getfleek-app
tags:
- Subscription
- Rewards
- Fintech
- Consumer App
- Platform
website: https://getfleek.app/
---
