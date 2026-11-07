---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source:
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
api_count: 1
apis:
- description: Prose provides a personalized haircare and skincare platform; API details are not publicly documented.
  name: Prose API
  slug: prose-api
artifact_total: 2
common:
- group: other
  href: https://artifacts.apis.io/prosehair-com/hosts/prosehair-com-hosts.yml
  title: ''
  type: Hosts
  url: hosts/prosehair-com-hosts.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://prose.com/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://prose.com/privacy
- group: auth
  href: https://artifacts.apis.io/prosehair-com/security/prosehair-com-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/prosehair-com-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.prosehair.com
created: '2026-10-25'
description: Prose provides personalized haircare and skincare products through a custom formulation platform. Customers complete a free consultation to receive formulas tailored to their hair type, skin concerns, and lifestyle. The service combines a digital questionnaire with proprietary algorithms to create bespoke products, shipped directly to consumers. Prose emphasizes science‑backed ingredients, sustainability, and a subscription model for ongoing product delivery.
layout: provider
modified: '2026-10-25'
name: Prose
nav: Providers
network: true
overview: Prose is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Hair Care, Skincare, Personalization, and Subscription.
random_paper: 17
score:
  band: minimal
  composite: 6.7
  coverage:
    artifact_dirs: 7
    catalog_earned: 30.0
    catalog_earned_first_party: 0.0
    catalog_gap: 85.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -2.7
  facets:
    access_clarity: 10.5
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 0.0
    discoverability: 53.6
    operational_transparency: 0.0
  needs_work:
    note: Recorded so this provider's gaps can be attributed. Does not affect the composite above.
    owner: catalog
    reasons:
    - owner: catalog
      reason: not_a_repo
  previous_composite: 9.4
  provenance:
    mcp: unknown
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 9.8
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
screenshot: https://apis.io/screenshots/prosehair-com/prosehair-com-2026-11-03T141641.png
security:
- kind: domain-security
  name: Prosehair Com Domain Security
  slug: prosehair-com-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: prosehair-com
tags:
- Company
- Hair Care
- Skincare
- Personalization
- Subscription
website: https://www.prosehair.com
---
