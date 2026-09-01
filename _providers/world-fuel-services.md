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
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    agentic_commerce: false
    auth_clarity: served
    consent_identity: false
    delegated_identity: served
    dry_run_mode: false
    dynamic_client_registration: true
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
  score: 17.6
  scored_at: '2026-09-01'
api_count: 0
artifact_total: 5
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/world-fuel-services-domain-security.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/world-fuel-services
- group: company
  title: ''
  type: Website
  url: https://www.world-kinect.com
- group: operate
  title: ''
  type: Support
  url: https://www.world-kinect.com/about-us/contact-world-kinect
- group: company
  title: ''
  type: Blog
  url: https://www.world-kinect.com/news-insights
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.world-kinect.com/your-privacy-center/privacy-policy
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.world-kinect.com/website-terms-and-conditions
- group: start
  title: ''
  type: Login
  url: https://myworld.wfscorp.com/
- group: agent
  title: ''
  type: WellKnown
  url: well-known/world-fuel-services-well-known.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/world-fuel-services-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/world-fuel-services-scopes.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/world-fuel-services-conformance.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/world-fuel-services-llms.txt
- group: commercial
  title: ''
  type: Plans
  url: plans/world-fuel-services-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/world-fuel-services-rate-limits.yml
coverage:
  checked: '2026-08-29'
  detail: Every World Kinect machine surface sits behind the myWorld customer portal, and portal access is granted only after a sales contact form — the company publishes no developer portal, no API reference and no contract, and the one anonymously readable machine-readable document on any host it controls is the Auth0 OIDC discovery metadata at auth.wfscorp.com.
  evidence:
  - status: 200
    url: https://auth.wfscorp.com/.well-known/openid-configuration
  - status: 200
    url: https://www.world-kinect.com/about-us/contact-us/portal-access-form
  - status: 404
    url: https://www.world-kinect.com/openapi.json
  - status: 200
    url: https://myworld.wfscorp.com/.well-known/agent-card.json
  - status: 0
    url: https://www.world-fuel-services.com
  reason: sales-gate
  state: gated
created: '2026-03-24'
description: 'World Fuel Services, which rebranded as World Kinect Corporation in 2023, is a Miami-based Fortune 100 global energy management company that supplies fuel, energy and related products and services across three segments — aviation, marine and land. It sells and distributes jet fuel, marine bunker fuel, diesel, gasoline, natural gas, power, lubricants and renewable fuels to airlines, business aviation operators, airports and FBOs, shipping fleets and ports, commercial and industrial customers, government and military accounts, and retail petroleum networks in more than 200 countries and territories. Its technology brands include the myWorld aviation portal and app, Trip View, AVCARD and EPIC fuel cards, the World Kinect Online energy portal, and the trip-support business acquired from Universal Weather and Aviation in 2024. Digital delivery is customer-portal-first: integrations such as fuel-price feeds into flight-planning platforms are arranged commercially rather than through
  a public developer program.'
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/world-fuel-services.png
layout: provider
modified: '2026-08-29'
name: World Fuel Services
nav: Providers
network: true
overview: 'World Fuel Services is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Fortune 100, Energy, Aviation Fuel, Marine Fuel, and Fuel Distribution.


  World Fuel Services'' developer surface includes support, engineering blog, authentication, and 12 more developer resources.'
plans:
- name: World Fuel Services Plans Pricing
  plan_count: 0
  slug: world-fuel-services-plans-pricing
press:
- date: '2026-05-25'
  title: World Kinect acquires Universal Weather's Trip Support ...
  url: https://www.linkedin.com/posts/world-fuel-services_aviation-tripsupport-worldkinect-activity-7369021536176857088-xjBn
- date: '2026-05-25'
  title: 0001628280-24-019007 | DEFR14A | iXBRL Viewer
  url: https://ir.world-kinect.com/node/17936/ixbrl-viewer
- date: '2026-05-25'
  title: 418133(1) World Fuel Services 2023 Proxy.indb
  url: https://www.sec.gov/Archives/edgar/data/789460/000130817923000840/int_courtesy-pdf.pdf
- date: '2026-05-25'
  title: World Energy and World Fuel Services extend partnership ...
  url: https://www.prnewswire.com/news-releases/world-energy-and-world-fuel-services-extend-partnership-with-a-six-year-up-to-27-million-gallon-purchasing-agreement-301822314.html
- date: '2026-05-25'
  title: World Fuel Services Corporation Names Sharda Cherwoo to the ...
  url: https://ir.world-kinect.com/news-releases/news-release-details/world-fuel-services-corporation-names-sharda-cherwoo-board
random_paper: 6
rate_limits:
- limit_count: 0
  name: World Fuel Services Rate Limits
  slug: world-fuel-services-rate-limits
scopes:
- name: World Fuel Services Scopes
  scope_count: 14
  slug: world-fuel-services-scopes
  summary_line: 14 scopes
score:
  band: emerging
  composite: 22.9
  coverage:
    artifact_dirs: 12
    catalog_gap: 88.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 27.6
    commercial_clarity: 27.6
    contract_governance: 18.2
    contract_quality: 0.0
    developer_ergonomics: 19.0
    discoverability: 57.4
    governance: 18.2
    operational_transparency: 0.0
  needs_work:
    note: Recorded so this provider's gaps can be attributed. Does not affect the composite above.
    owner: catalog
    reasons:
    - owner: catalog
      reason: never_enriched
  previous_composite: 22.9
  regulatory:
    applies: true
    matched_via: tags
    regime: Energy & Utilities
    regime_id: energy_utilities
    score: 56.8
  schema_version: 0.17.2
  scored_at: '2026-09-01'
  trend: flat
security:
- kind: authentication
  name: World Fuel Services Authentication
  slug: world-fuel-services-authentication
  summary_line: 1 scheme
- kind: domain-security
  name: World Fuel Services Domain Security
  slug: world-fuel-services-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: world-fuel-services
tags:
- Fortune 100
- Energy
- Aviation Fuel
- Marine Fuel
- Fuel Distribution
- Energy Management
- Sustainability
- Logistics
- Fuel Cards
website: https://www.world-kinect.com
---
