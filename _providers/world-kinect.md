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
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 2.5
  scored_at: '2026-09-04'
api_count: 0
artifact_total: 3
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/world-kinect-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.world-kinect.com
- group: company
  title: ''
  type: About
  url: https://www.world-kinect.com/about-us
- group: operate
  title: ''
  type: Support
  url: https://www.world-kinect.com/about-us/contact-world-kinect
- group: start
  title: ''
  type: Login
  url: https://www.world-kinect.com/fuel-lubricants/world-kinect-customer-portals
- group: company
  title: ''
  type: Blog
  url: https://www.world-kinect.com/news-insights
- group: company
  title: ''
  type: BlogRSS
  url: https://www.world-kinect.com/rss.xml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.world-kinect.com/website-terms-and-conditions
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.world-kinect.com/your-privacy-center
- group: company
  title: ''
  type: Careers
  url: https://www.world-kinect.com/careers
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/world-kinect
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/world-kinect-llms.txt
- group: commercial
  title: ''
  type: Plans
  url: plans/world-kinect-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/world-kinect-rate-limits.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/world-kinect-conformance.yml
coverage:
  checked: '2026-09-04'
  detail: World Kinect's fuel-price and AVCARD API is real and reaches operators through third-party flight-operations platforms, but it has no public reference — the only route in is the Portal Access request form, and every myWorld portal host answers HTTP 200 with an Angular SPA shell for /api-docs, /openapi.json and every /.well-known/ path.
  evidence:
  - status: 200
    url: https://www.world-kinect.com/about-us/contact-us/portal-access-form
  - status: 200
    url: https://myworld.air.wfscorp.com/api-docs
  - status: 404
    url: https://www.world-kinect.com/llms.txt
  - status: 200
    url: https://www.world-kinect.com/sitemap.xml
  reason: customer-only-docs
  state: gated
created: '2026-03-21'
description: 'World Kinect Corporation (NYSE: WKC), formerly World Fuel Services, is a Fortune 500 energy, commodities and services company headquartered in Doral, Florida. It supplies and manages aviation, marine and land fuel, lubricants, natural gas, power, water and carbon-management services for airlines, business aviation operators, shipping lines, commercial fleets, fuel retailers and industrial customers in more than 200 countries. Its digital surface is a family of authenticated customer portals — myWorld for aviation, land, marine and carbon management, World Kinect Online for energy services, and the Flyers Energy and Quick Fuel Vantage/Advantage portals — plus a fuel-price and AVCARD integration that reaches operators through third-party flight-operations platforms. World Kinect publishes no public developer portal, API reference or machine-readable API contract.'
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/world-kinect.png
layout: provider
modified: '2026-09-04'
name: World Kinect
nav: Providers
network: true
overview: 'World Kinect is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Fortune 500, Energy, Fuel, Aviation, and Marine.


  World Kinect''s developer surface includes support, engineering blog, and 13 more developer resources.'
plans:
- name: World Kinect Plans Pricing
  plan_count: 0
  slug: world-kinect-plans-pricing
random_paper: 17
rate_limits:
- limit_count: 0
  name: World Kinect Rate Limits
  slug: world-kinect-rate-limits
score:
  band: emerging
  composite: 14.2
  coverage:
    artifact_dirs: 8
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 11.3
  facets:
    access_clarity: 34.2
    commercial_clarity: 34.2
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 7.1
    discoverability: 50.0
    governance: 0.0
    operational_transparency: 0.0
  needs_work:
    note: Recorded so this provider's gaps can be attributed. Does not affect the composite above.
    owner: catalog
    reasons:
    - owner: catalog
      reason: no_resolvable_host
    - owner: catalog
      reason: never_enriched
  previous_composite: 2.9
  provenance:
    conformance: first-party
  regulatory:
    applies: true
    matched_via: tags
    regime: Energy & Utilities
    regime_id: energy_utilities
    score: 25.7
  schema_version: 0.18.3
  scored_at: '2026-09-04'
  trend: rising
screenshot: https://raw.githubusercontent.com/api-evangelist/world-kinect/refs/heads/main/screenshots/world-kinect-2026-06-20T201623.png
security:
- kind: domain-security
  name: World Kinect Domain Security
  slug: world-kinect-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: world-kinect
tags:
- Fortune 500
- Energy
- Fuel
- Aviation
- Marine
- Transportation
- Sustainability
- Commodities
- Logistics
website: https://www.world-kinect.com
---
