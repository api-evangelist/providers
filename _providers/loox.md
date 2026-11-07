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
    well_known_catalog: true
  schema_version: '0.2'
  score: 2.9
  scored_at: '2026-11-06'
api_count: 0
artifact_total: 2
common:
- group: commercial
  href: https://artifacts.apis.io/loox/plans/loox-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/loox-plans-pricing.yml
- group: agent
  href: https://artifacts.apis.io/loox/llms/loox-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/loox-llms.txt
- group: other
  href: https://artifacts.apis.io/loox/hosts/loox-hosts.yml
  title: ''
  type: Hosts
  url: hosts/loox-hosts.yml
- group: other
  href: https://artifacts.apis.io/loox/vendors/loox-vendors.yml
  title: ''
  type: Vendors
  url: vendors/loox-vendors.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://loox.app/legal/terms-of-service
- group: operate
  title: ''
  type: StatusPage
  url: https://status.loox.app/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://loox.app/legal/privacy-policy-merchants
- group: commercial
  title: ''
  type: Pricing
  url: https://loox.app/pricing
- group: company
  title: ''
  type: Blog
  url: https://loox.app/blog
- group: docs
  title: ''
  type: Documentation
  url: https://developers.loox.app/
- group: auth
  href: https://artifacts.apis.io/loox/security/loox-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/loox-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://loox.app/
coverage:
  checked: '2026-10-28'
  detail: The developer documentation at https://developers.loox.app/documentation/ returns HTML without any OpenAPI, AsyncAPI, GraphQL, gRPC, or WSDL specifications.
  evidence:
  - status: 200
    url: https://developers.loox.app/documentation/
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-10-28'
description: Loox provides a visual reviews platform for e‑commerce merchants, primarily on Shopify. It enables customers to submit photo‑rich reviews, share product experiences, and refer friends, helping over 130,000 brands grow through social proof marketing.
image: https://cdn.prod.website-files.com/5ffa9cb466ed902ac6f8fffc/685cf7adfc1cd1223994e244_new-og-image.jpg
layout: provider
modified: '2026-10-28'
name: Loox
nav: Providers
network: true
overview: 'Loox is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include E-Commerce, Reviews, Visual, Shopify, and Marketing.


  Loox''s developer surface includes pricing, engineering blog, documentation, and 9 more developer resources.'
plans:
- name: Loox Plans Pricing
  plan_count: 3
  slug: loox-plans-pricing
random_paper: 18
score:
  band: emerging
  composite: 16.5
  coverage:
    artifact_dirs: 10
    catalog_earned: 39.0
    catalog_earned_first_party: 12.0
    catalog_gap: 76.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -5.9
  facets:
    access_clarity: 47.4
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 6.0
    discoverability: 55.4
    operational_transparency: 7.9
  needs_work:
    note: Recorded so this provider's gaps can be attributed. Does not affect the composite above.
    owner: catalog
    reasons:
    - owner: catalog
      reason: not_a_repo
  previous_composite: 22.4
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
screenshot: https://apis.io/screenshots/loox/loox-2026-11-03T135049.png
security:
- kind: domain-security
  name: Loox Domain Security
  slug: loox-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: loox
tags:
- E-Commerce
- Reviews
- Visual
- Shopify
- Marketing
website: https://loox.app/
---
