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
    mcp_server: documented
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
  score: 3.1
  scored_at: '2026-11-06'
api_count: 1
apis:
- description: API for BoostedChat platform providing conversational automation.
  name: BoostedChat API
  slug: boostedchat-api
artifact_total: 3
common:
- group: commercial
  href: https://artifacts.apis.io/boostedchat-com/plans/boostedchat-com-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/boostedchat-com-plans-pricing.yml
- group: design
  href: https://artifacts.apis.io/boostedchat-com/conformance/boostedchat-com-conformance.yml
  title: ''
  type: Conformance
  url: conformance/boostedchat-com-conformance.yml
- group: other
  href: https://artifacts.apis.io/boostedchat-com/hosts/boostedchat-com-hosts.yml
  title: ''
  type: Hosts
  url: hosts/boostedchat-com-hosts.yml
- group: other
  href: https://artifacts.apis.io/boostedchat-com/vendors/boostedchat-com-vendors.yml
  title: ''
  type: Vendors
  url: vendors/boostedchat-com-vendors.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://boostedchat.com/tos
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://boostedchat.com/privacy
- group: commercial
  title: ''
  type: Pricing
  url: https://boostedchat.com/pricing
- group: docs
  title: ''
  type: Documentation
  url: https://boostedchat.com/docs
- group: auth
  href: https://artifacts.apis.io/boostedchat-com/security/boostedchat-com-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/boostedchat-com-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://boostedchat.com/
coverage:
  checked: '2026-11-02'
  detail: Documentation is available at https://boostedchat.com/docs but provides no machine‑readable OpenAPI, GraphQL, AsyncAPI or other contract.
  evidence:
  - status: 200
    url: https://boostedchat.com/docs
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-11-02'
description: BoostedChat provides AI‑powered conversational agents that engage leads instantly on WhatsApp, Messenger and Instagram. The platform offers proactive, personalized conversations that convert, with features like automated follow‑ups, scheduling, and multi‑channel support. It aims to make every customer feel like the only one, helping businesses increase engagement and sales through intelligent chat automation.
image: https://boostedchat.com/og-boosted-new.png
layout: provider
modified: '2026-11-02'
name: BoostedChat
nav: Providers
network: true
overview: 'BoostedChat is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Customer Engagement, Chatbots, Software-as-a-Service, Marketing, and E-Commerce.


  BoostedChat''s developer surface includes pricing, documentation, and 8 more developer resources.'
plans:
- name: Boostedchat Com Plans Pricing
  plan_count: 2
  slug: boostedchat-com-plans-pricing
random_paper: 20
score:
  band: emerging
  composite: 15.7
  coverage:
    artifact_dirs: 10
    catalog_earned: 40.0
    catalog_earned_first_party: 8.0
    catalog_gap: 75.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 36.8
    contract_governance: 18.2
    contract_quality: 0.0
    developer_ergonomics: 4.8
    discoverability: 57.1
    operational_transparency: 0.0
  provenance:
    conformance: first-party
    mcp: unknown
  regulatory:
    applies: true
    jurisdictions:
    - jurisdiction: EU
      standard: gdpr
    - jurisdiction: US
      standard: ccpa
    jurisdictions_satisfied: 2
    matched_via: residual_tags
    regime: AI & Biometrics
    regime_id: ai_biometrics
    score: 14.7
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Boostedchat Com Domain Security
  slug: boostedchat-com-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: boostedchat-com
tags:
- Customer Engagement
- Chatbots
- Software-as-a-Service
- Marketing
- E-Commerce
website: https://boostedchat.com/
---
