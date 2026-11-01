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
artifact_total: 2
common:
- group: commercial
  href: https://artifacts.apis.io/cake-pos/plans/cake-pos-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/cake-pos-plans-pricing.yml
- group: other
  href: https://artifacts.apis.io/cake-pos/hosts/cake-pos-hosts.yml
  title: ''
  type: Hosts
  url: hosts/cake-pos-hosts.yml
- group: other
  href: https://artifacts.apis.io/cake-pos/vendors/cake-pos-vendors.yml
  title: ''
  type: Vendors
  url: vendors/cake-pos-vendors.yml
- group: auth
  href: https://artifacts.apis.io/cake-pos/security/cake-pos-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/cake-pos-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://trycake.com/
- group: docs
  title: ''
  type: Documentation
  url: https://trycake.com/
- group: commercial
  title: ''
  type: Pricing
  url: https://trycake.com/pricing
- group: operate
  title: ''
  type: Support
  url: https://trycake.com/cake-support
- group: company
  title: ''
  type: Blog
  url: https://trycake.com/blog
coverage:
  checked: '2026-10-27'
  detail: The provider's website does not expose any machine‑readable API specification or documentation.
  evidence:
  - status: 200
    url: https://trycake.com/
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-10-27'
description: CAKE POS provides a cloud‑based point‑of‑sale (POS) platform designed for restaurants and retail businesses. It offers tools for order management, payment processing, inventory tracking, employee scheduling, and analytics, all accessible via web and mobile interfaces. The service integrates with popular payment gateways and third‑party services, enabling seamless operations for small to medium‑size enterprises seeking modern, scalable POS solutions.
image: https://trycake.com/hubfs/NEW%20CAKE%20WEBSITE/primary-branding-hero.jpg
layout: provider
modified: '2026-10-27'
name: CAKE POS
nav: Providers
network: true
overview: 'CAKE POS is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, POS, Retail, Restaurants, and Cloud.


  CAKE POS''s developer surface includes documentation, pricing, support, engineering blog, and 5 more developer resources.'
plans:
- name: Cake Pos Plans Pricing
  plan_count: 3
  slug: cake-pos-plans-pricing
random_paper: 19
score:
  band: emerging
  composite: 15.2
  coverage:
    artifact_dirs: 6
    catalog_earned: 39.0
    catalog_earned_first_party: 12.0
    catalog_gap: 76.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 42.1
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 16.7
    discoverability: 48.2
    operational_transparency: 0.0
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 5.9
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Cake Pos Domain Security
  slug: cake-pos-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: cake-pos
tags:
- Company
- POS
- Retail
- Restaurants
- Cloud
website: https://trycake.com/
---
