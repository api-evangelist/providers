---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source:
  - authentication
  - rate-limits
  - security
  trial: false
  try_now: false
agent_readiness:
  band: agent-aware
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
    error_semantics: documented
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
  score: 7.9
  scored_at: '2026-09-05'
api_count: 1
apis:
- description: The API behind the Leaf Logistics platform. api.leaflogistics.com runs Hasura GraphQL Engine v2.35.1 (community edition, pro-lite console) and exposes a GraphQL endpoint at /v1/graphql plus a Hasura R
  name: Leaf Logistics Platform API
  slug: leaf-logistics-platform-api
artifact_total: 5
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/leaf-logistics-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.leaflogistics.com/
- group: company
  title: ''
  type: Blog
  url: https://www.leaflogistics.com/blog/
- group: operate
  title: ''
  type: Support
  url: https://www.leaflogistics.com/contact/
- group: start
  title: ''
  type: SignUp
  url: https://www.leaflogistics.com/get-started/
- group: start
  title: ''
  type: Login
  url: https://app.leaflogistics.com/login
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.leaflogistics.com/terms-conditions/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.leaflogistics.com/privacy-policy/
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/leaflogistics/
- group: company
  title: ''
  type: Twitter
  url: https://twitter.com/leaflogistics
- group: learn
  title: ''
  type: YouTube
  url: https://www.youtube.com/channel/UClaxTC6MTjb9mfSKrXLwVKw
- group: company
  title: ''
  type: Press
  url: https://www.leaflogistics.com/press.html
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/leaf-logistics-llms.txt
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/leaf-logistics-problem-types.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/leaf-logistics-conformance.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/leaf-logistics-lifecycle.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/leaf-logistics-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/leaf-logistics-rate-limits.yml
- group: build
  title: ''
  type: Packages
  url: packages/leaf-logistics-packages.yml
coverage:
  checked: '2026-08-25'
  detail: Leaf runs a real Hasura GraphQL Engine v2.35.1 at api.leaflogistics.com, but /v1/graphql refuses anonymous introspection with "Missing 'Authorization' or 'Cookie' header in JWT authentication mode" and there is no developer site of any kind — /developers/, /api/ and /pricing/ do not exist and docs.leaflogistics.com does not resolve — so a "Get Started" contact form is the only route to the contract.
  evidence:
  - status: 200
    url: https://api.leaflogistics.com/v1/graphql
  - status: 403
    url: https://www.leaflogistics.com/developers/
  - status: 0
    url: https://docs.leaflogistics.com/
  - status: 200
    url: https://www.leaflogistics.com/get-started/
  reason: sales-gate
  state: gated
created: '2026-08-25'
description: 'Leaf Logistics Inc. is a New York-based freight coordination platform that lets shippers, carriers and brokers plan, schedule and move truckload freight months in advance instead of one load at a time. Leaf builds multi-shipper circuits and "Flex Fleets" — multi-shipper dedicated capacity — so participants get long-term contracted rates, guaranteed tender acceptance and fewer empty miles, which Leaf positions as both a cost and a Scope 3 emissions reduction. The platform is delivered as a hosted web application at app.leaflogistics.com backed by a Hasura GraphQL Engine API at api.leaflogistics.com. Leaf tells prospective shippers it will integrate with their existing TMS and carrier network "through email, phone, fax, EDI, API — whatever you prefer", but as of this profile it publishes no public developer portal, no API reference and no machine-readable contract: the GraphQL endpoint answers anonymously only with a JWT authentication error, so the schema is reachable only by
  onboarded customers.'
image: https://www.leaflogistics.com/wp-content/themes/leaflog/images/webclip.png
layout: provider
modified: '2026-08-25'
name: Leaf Logistics
nav: Providers
network: true
overview: 'Leaf Logistics publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Logistics, Freight, Transportation, Supply Chain, and Shipping.


  Leaf Logistics'' developer surface includes engineering blog, support, signup flow, YouTube channel, and 15 more developer resources.'
plans:
- name: Leaf Logistics Plans Pricing
  plan_count: 0
  slug: leaf-logistics-plans-pricing
random_paper: 2
rate_limits:
- limit_count: 0
  name: Leaf Logistics Rate Limits
  slug: leaf-logistics-rate-limits
score:
  band: emerging
  composite: 19.7
  coverage:
    artifact_dirs: 13
    catalog_earned: 37.0
    catalog_earned_first_party: 0.0
    catalog_gap: 78.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 34.2
    commercial_clarity: 34.2
    contract_governance: 18.2
    contract_quality: 0.0
    developer_ergonomics: 19.0
    discoverability: 68.5
    governance: 18.2
    operational_transparency: 0.0
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
    regions:
    - north-america
  previous_composite: 19.7
  provenance:
    conformance: first-party
  schema_version: 0.18.3
  scored_at: '2026-09-05'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/leaf-logistics/refs/heads/main/screenshots/leaf-logistics-2026-09-02T150228.png
security:
- kind: authentication
  name: Leaf Logistics Authentication
  slug: leaf-logistics-authentication
  summary_line: 2 schemes
- kind: domain-security
  name: Leaf Logistics Domain Security
  slug: leaf-logistics-domain-security
  summary_line: TLSv1.3 · DMARC
slug: leaf-logistics
tags:
- Logistics
- Freight
- Transportation
- Supply Chain
- Shipping
- Fleet Management
- Sustainability
- GraphQL
website: https://www.leaflogistics.com/
---
