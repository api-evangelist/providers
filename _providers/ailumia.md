---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source: []
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
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: '0.2'
  score: 0.0
  scored_at: '2026-10-17'
api_count: 0
artifact_total: 2
common:
- group: commercial
  title: ''
  type: Pricing
  url: https://ailumia.com/pricing/
- group: commercial
  href: https://raw.githubusercontent.com/api-evangelist/ailumia/refs/heads/main/plans/ailumia-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/ailumia-plans-pricing.yml
- group: company
  title: ''
  type: Blog
  url: https://ailumia.com/blog/
- group: company
  title: ''
  type: BlogRSS
  url: https://ailumia.com/feed/
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/ailumia/refs/heads/main/security/ailumia-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/ailumia-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://ailumia.com
created: '2026-07-17'
description: Ailumia is an AI-driven retail operations platform that helps brands and sellers grow on the world's most valuable marketplaces, with a focus on Amazon. The platform applies artificial intelligence across the retail workflow to manage marketplace sales, inventory, supply chain, and finances, giving operators data-driven guidance and automation to navigate the challenges of modern e-commerce. Founded in 2019 and headquartered in Taipei, Taiwan, Ailumia is backed by 500 Global. This API Evangelist profile was surfaced from the 500 Global portfolio; enrichment probing found a Cloudflare-fronted WordPress marketing presence but no public developer, API, or documentation surface.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/ailumia.png
layout: provider
modified: '2026-10-06'
name: Ailumia
nav: Providers
network: true
overview: 'Ailumia is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, E-Commerce, Retail, Marketplace, and Amazon.


  Ailumia''s developer surface includes pricing, engineering blog, and 4 more developer resources.'
plans:
- name: Ailumia Plans Pricing
  plan_count: 6
  slug: ailumia-plans-pricing
random_paper: 12
score:
  band: emerging
  composite: 12.3
  coverage:
    artifact_dirs: 6
    catalog_earned: 39.0
    catalog_earned_first_party: 12.0
    catalog_gap: 76.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 9.0
  facets:
    access_clarity: 42.1
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 2.4
    discoverability: 48.2
    operational_transparency: 0.0
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    countries:
    - taiwan
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
    regions:
    - greater-china
  previous_composite: 3.3
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 5.5
  schema_version: 0.24.0
  scored_at: '2026-10-17'
  trend: rising
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
screenshot: https://raw.githubusercontent.com/api-evangelist/ailumia/refs/heads/main/screenshots/ailumia-2026-07-25T195353.png
security:
- kind: domain-security
  name: Ailumia Domain Security
  slug: ailumia-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
slug: ailumia
tags:
- Company
- E-Commerce
- Retail
- Marketplace
- Amazon
- Inventory
- Supply Chain
- Artificial Intelligence
- Analytics
website: https://ailumia.com
---
