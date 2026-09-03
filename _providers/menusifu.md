---
access_model:
  confidence: medium
  label: Freemium · Requires approval
  onboarding: approval
  pricing: freemium
  public: false
  source:
  - plans
  - rate-limits
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
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 2.5
  scored_at: '2026-09-02'
api_count: 0
artifact_total: 3
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/menusifu-domain-security.yml
- group: build
  title: ''
  type: Packages
  url: packages/menusifu-packages.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/menusifu-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/menusifu-rate-limits.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/menusifu-llms.txt
- group: company
  title: ''
  type: Website
  url: https://www.menusifu.com/
- group: commercial
  title: ''
  type: Pricing
  url: https://www.menusifu.com/pricing
- group: company
  title: ''
  type: Blog
  url: https://www.menusifu.com/blog
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.menusifu.com/privacy-policy
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.menusifu.com/master-services-agreement
- group: start
  title: ''
  type: SignUp
  url: https://www.menusifu.com/restaurant-pos-demo
- group: other
  title: ''
  type: CaseStudies
  url: https://www.menusifu.com/customer-stories
- group: company
  title: ''
  type: Careers
  url: https://www.menusifu.com/career
coverage:
  checked: '2026-08-25'
  detail: 'MenuSifu ships restaurant POS software only as an end-user product: its 286-URL sitemap contains no developer, API or integration-reference page, and its production backend api.menusifu.com answers every anonymous path — /openapi.json, /swagger.json, /v2/api-docs, /graphql and every /.well-known/* — with HTTP 401 "Full authentication is required to access this resource".'
  evidence:
  - status: 401
    url: https://api.menusifu.com/openapi.json
  - status: 401
    url: https://api.menusifu.com/v2/api-docs
  - status: 401
    url: https://api.menusifu.com/graphql
  - status: 404
    url: https://www.menusifu.com/llms.txt
  - status: 404
    url: https://www.menusifu.com/.well-known/agent-card.json
  - status: 200
    url: https://www.menusifu.com/sitemap.xml
  reason: no-developer-program
  state: none
created: '2026-08-25'
description: 'MenuSifu is a U.S. restaurant technology company founded in 2014 that builds an all-in-one point-of-sale and restaurant operations platform, used by more than 15,000 active restaurants and supported from offices in New York, Los Angeles, Houston, Orlando, Silicon Valley and Chicago. The platform spans POS terminals and handhelds, self-service kiosks, kitchen display and kitchen-automation systems, electronic menus and order-status screens, online ordering, scan-to-order, waitlist and reservations, loyalty, coupons and SMS marketing, and analytics and reporting, with direct order integrations into DoorDash, Uber Eats, Grubhub, Fantuan and HungryPanda. It is sold alongside an ecosystem of sibling brands — USEZPAY (payment processing), MealKeyway (marketing), EZ Capital (restaurant financing), WeFood and ShowTop. MenuSifu markets no public developer program: it publishes no API reference, no OpenAPI or other machine-readable contract, and no SDKs, and its production host api.menusifu.com
  rejects every anonymous request.'
image: https://cdn.prod.website-files.com/69366fbc0f086e839c80b396/69787c18dfed54b6493f243e_menusifu.webp
layout: provider
modified: '2026-08-25'
name: MenuSifu
nav: Providers
network: true
overview: 'MenuSifu is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Point-of-Sale, Restaurant, Restaurant Technology, and Hospitality.


  MenuSifu''s developer surface includes pricing, engineering blog, signup flow, and 10 more developer resources.'
plans:
- name: Menusifu Plans Pricing
  plan_count: 4
  slug: menusifu-plans-pricing
random_paper: 15
rate_limits:
- limit_count: 0
  name: Menusifu Rate Limits
  slug: menusifu-rate-limits
score:
  band: emerging
  composite: 19.2
  coverage:
    artifact_dirs: 8
    catalog_gap: 76.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 76.3
    commercial_clarity: 76.3
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 2.4
    discoverability: 50.0
    governance: 0.0
    operational_transparency: 0.0
  previous_composite: 19.2
  regulatory:
    applies: true
    matched_via: tags
    regime: Payments
    regime_id: payments
    score: 21.9
  schema_version: 0.18.0
  scored_at: '2026-09-02'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/menusifu/refs/heads/main/screenshots/menusifu-2026-09-02T150520.png
security:
- kind: domain-security
  name: Menusifu Domain Security
  slug: menusifu-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: menusifu
tags:
- Company
- Point-of-Sale
- Restaurant
- Restaurant Technology
- Hospitality
- Payments
- Online Ordering
- Loyalty
- Kitchen Display Systems
- Hardware
website: https://www.menusifu.com/
---
