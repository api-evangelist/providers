---
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
  scored_at: '2026-10-31'
api_count: 0
artifact_total: 4
common:
- group: commercial
  href: https://artifacts.apis.io/spark-shipping/plans/spark-shipping-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/spark-shipping-plans-pricing.yml
- group: other
  href: https://artifacts.apis.io/spark-shipping/hosts/spark-shipping-hosts.yml
  title: ''
  type: Hosts
  url: hosts/spark-shipping-hosts.yml
- group: other
  href: https://artifacts.apis.io/spark-shipping/vendors/spark-shipping-vendors.yml
  title: ''
  type: Vendors
  url: vendors/spark-shipping-vendors.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://sparkshipping.com/pages/terms_of_service
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.sparkshipping.com/pages/privacy_policy
- group: start
  title: ''
  type: DeveloperPortal
  url: https://portal.sparkshipping.com/
- group: auth
  href: https://artifacts.apis.io/spark-shipping/security/spark-shipping-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/spark-shipping-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://sparkshipping.com/
- group: company
  title: ''
  type: Blog
  url: https://www.sparkshipping.com/blog
- group: commercial
  title: ''
  type: Pricing
  url: https://www.sparkshipping.com/pricing
- group: company
  title: ''
  type: About
  url: https://www.sparkshipping.com/about_us
- group: operate
  title: ''
  type: Contact
  url: https://www.sparkshipping.com/contact-us
- group: operate
  title: ''
  type: FAQ
  url: https://www.sparkshipping.com/pages/faq
coverage:
  checked: '2026-10-27'
  detail: Provider documentation pages exist but no machine‑readable OpenAPI, AsyncAPI, GraphQL or other contract was found.
  evidence:
  - status: 200
    url: https://portal.sparkshipping.com/
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-10-27'
description: Spark Shipping provides an eCommerce dropshipping automation platform that enables merchants to import products with one click, synchronize inventory and pricing across multiple vendors, generate AI-powered product descriptions, and automate order routing and tracking updates. Their SaaS solution integrates with major marketplaces and shopping carts, offering tools for inventory management, price automation, and vendor integrations to streamline online retail operations.
image: https://www.sparkshipping.com/hubfs/Spark%20Shpping%20Dashboard%20v2.png
layout: provider
modified: '2026-10-27'
name: Spark Shipping
nav: Providers
network: true
overview: 'Spark Shipping is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, eCommerce, Dropshipping, Automation, and SaaS.


  Spark Shipping''s developer surface includes engineering blog, pricing, FAQ, and 10 more developer resources.'
plans:
- name: Spark Shipping Plans Pricing
  plan_count: 1
  slug: spark-shipping-plans-pricing
random_paper: 16
scopes:
- name: Spark Shipping Scopes
  scope_count: 0
  slug: spark-shipping-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: emerging
  composite: 19.0
  coverage:
    artifact_dirs: 20
    catalog_earned: 35.0
    catalog_earned_first_party: 8.0
    catalog_gap: 80.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 52.6
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 11.9
    discoverability: 48.2
    operational_transparency: 0.0
  provenance:
    conformance: unknown
    mcp: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 23.5
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: authentication
  name: Spark Shipping Authentication
  slug: spark-shipping-authentication
  summary_line: 0 schemes
- kind: domain-security
  name: Spark Shipping Domain Security
  slug: spark-shipping-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: spark-shipping
tags:
- Company
- eCommerce
- Dropshipping
- Automation
- SaaS
- Integration
website: https://sparkshipping.com/
---
