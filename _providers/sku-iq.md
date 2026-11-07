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
  href: https://artifacts.apis.io/sku-iq/plans/sku-iq-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/sku-iq-plans-pricing.yml
- group: other
  href: https://artifacts.apis.io/sku-iq/hosts/sku-iq-hosts.yml
  title: ''
  type: Hosts
  url: hosts/sku-iq-hosts.yml
- group: other
  href: https://artifacts.apis.io/sku-iq/vendors/sku-iq-vendors.yml
  title: ''
  type: Vendors
  url: vendors/sku-iq-vendors.yml
- group: start
  title: ''
  type: SignUp
  url: https://app.skuiq.com/register
- group: auth
  href: https://artifacts.apis.io/sku-iq/security/sku-iq-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/sku-iq-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://skuiq.com/
- group: docs
  title: ''
  type: Documentation
  url: https://www.skuiq.com/solutions
- group: start
  title: ''
  type: GettingStarted
  url: https://www.skuiq.com/how-it-works
- group: commercial
  title: ''
  type: Pricing
  url: https://www.skuiq.com/pricing
- group: company
  title: ''
  type: Blog
  url: https://www.skuiq.com/blogs
- group: operate
  title: ''
  type: Support
  url: https://lp.skuiq.com/support
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.skuiq.com/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.skuiq.com/privacy-policy
created: '2026-10-27'
description: SKU IQ provides inventory synchronization solutions for small to medium businesses, connecting point‑of‑sale (POS) systems with eCommerce platforms. Their platform automates stock updates, prevents overselling, and consolidates order views across channels like Shopify, TikTok Shop, BigCommerce, and more. SKU IQ offers tiered pricing plans and a free trial, aiming to reduce manual data entry and operational errors for retailers.
layout: provider
modified: '2026-10-27'
name: SKU IQ
nav: Providers
network: true
overview: 'SKU IQ is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Inventory, Point-of-Sale, E-Commerce, Sync, and Retail.


  SKU IQ''s developer surface includes signup flow, documentation, getting-started guide, pricing, engineering blog, support, and 7 more developer resources.'
plans:
- name: Sku Iq Plans Pricing
  plan_count: 3
  slug: sku-iq-plans-pricing
random_paper: 2
score:
  band: emerging
  composite: 17.3
  coverage:
    artifact_dirs: 8
    catalog_earned: 37.0
    catalog_earned_first_party: 12.0
    catalog_gap: 78.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -7.9
  facets:
    access_clarity: 53.9
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 14.3
    discoverability: 44.6
    operational_transparency: 0.0
  needs_work:
    note: Recorded so this provider's gaps can be attributed. Does not affect the composite above.
    owner: catalog
    reasons:
    - owner: catalog
      reason: not_a_repo
  previous_composite: 25.2
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
screenshot: https://apis.io/screenshots/sku-iq/sku-iq-2026-11-03T143309.png
security:
- kind: domain-security
  name: Sku Iq Domain Security
  slug: sku-iq-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: sku-iq
tags:
- Inventory
- Point-of-Sale
- E-Commerce
- Sync
- Retail
- Automation
website: https://skuiq.com/
---
