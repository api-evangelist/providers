---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source:
  - plans
  trial: false
  try_now: false
agent_readiness:
  band: human-only
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
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: derived
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: '0.2'
  score: 3.1
  scored_at: '2026-10-17'
api_count: 0
artifact_total: 16
common:
- group: commercial
  href: https://raw.githubusercontent.com/api-evangelist/aeropostale/refs/heads/main/plans/aeropostale-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/aeropostale-plans-pricing.yml
- group: operate
  href: https://raw.githubusercontent.com/api-evangelist/aeropostale/refs/heads/main/rate-limits/aeropostale-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/aeropostale-rate-limits.yml
- group: commercial
  href: https://raw.githubusercontent.com/api-evangelist/aeropostale/refs/heads/main/finops/aeropostale-finops.yml
  title: ''
  type: FinOps
  url: finops/aeropostale-finops.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/aeropostale/refs/heads/main/security/aeropostale-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/aeropostale-domain-security.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/aeropostale
- group: company
  title: ''
  type: Website
  url: https://www.aeropostale.com/
- group: start
  title: ''
  type: Login
  url: https://www.aeropostale.com/account/login
- group: auth
  title: ''
  type: Authentication
  url: ''
- group: auth
  title: ''
  type: Compliance
  url: ''
created: '2026-05-05'
description: An American specialty retailer offering on-trend apparel, accessories, and personal care products targeted at teens and young adults. Operates stores across the United States and internationally through franchise partnerships.
features:
- description: Direct-to-consumer e-commerce storefront for apparel, accessories, and personal-care products.
  name: Online Storefront
- description: Aéropostale loyalty / rewards program for U.S. customers offering points on purchases and member-only offers.
  name: Tarjeta Aéropostale Rewards
- description: Locate U.S. and international Aéropostale stores including franchise locations.
  name: Store Locator
- description: Co-branded retail credit card with reward acceleration on Aéropostale purchases.
  name: Aero Credit Card
finops:
- has_sources: true
  method: generated
  name: Aeropostale Finops
  primary_unit: ''
  service_category: Retail / Fashion
  slug: aeropostale-finops
  template: false
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/aeropostale.png
integrations:
- description: Authentic Brands Group owns the Aéropostale brand; the operational retail business is run by partners such as SPARC Group / Simon Property Group.
  name: Authentic Brands Group
- description: SPARC Group operates Aéropostale's U.S. retail and e-commerce business under license from Authentic Brands Group.
  name: SPARC Group
- description: Rakuten Advertising affiliate network distribution.
  name: Rakuten Advertising
- description: Commission Junction (CJ) affiliate program partner.
  name: CJ Affiliate
layout: provider
modified: '2026-05-16'
name: Aéropostale
nav: Providers
network: true
overview: 'Aéropostale is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Retail, Fashion, and Teen Apparel.


  Aéropostale''s developer surface includes authentication and 6 more developer resources.'
plans:
- name: Aeropostale Plans Pricing
  plan_count: 1
  slug: aeropostale-plans-pricing
random_paper: 17
rate_limits:
- limit_count: 1
  name: Aeropostale Rate Limits
  slug: aeropostale-rate-limits
score:
  band: emerging
  composite: 11.2
  coverage:
    artifact_dirs: 7
    catalog_earned: 26.0
    catalog_earned_first_party: 0.0
    catalog_gap: 89.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -6.0
  facets:
    access_clarity: 19.7
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 11.9
    discoverability: 39.3
    operational_transparency: 5.3
  previous_composite: 17.2
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 16.7
  schema_version: 0.24.0
  scored_at: '2026-10-17'
  trend: falling
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
screenshot: https://raw.githubusercontent.com/api-evangelist/aeropostale/refs/heads/main/screenshots/aeropostale-2026-06-20T165520.png
security:
- kind: domain-security
  name: Aeropostale Domain Security
  slug: aeropostale-domain-security
  summary_line: TLSv1.3 · DMARC
slug: aeropostale
tags:
- Retail
- Fashion
- Teen Apparel
use_cases:
- description: Specialty apparel retail targeted at teens and young adults via stores and e-commerce.
  name: Teen Apparel Retail
- description: Branded brick-and-mortar retail operating primarily in U.S. shopping malls.
  name: Mall-Based Retail
- description: International market distribution through franchise partner agreements.
  name: International Franchise Distribution
- description: Loyalty-driven customer engagement through the rewards program and email marketing.
  name: Loyalty Engagement
website: https://www.aeropostale.com/
---
