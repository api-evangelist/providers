---
access_model:
  confidence: medium
  label: Contact Sales
  onboarding: unknown
  pricing: unknown
  public: false
  source:
  - https://fastship.co/fastship-for-business/
  - https://fastship.co/api
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
  scored_at: '2026-09-01'
api_count: 1
apis:
- description: 'The versioned REST API behind FastShip, Cloud Commerce''s cross-border e-commerce logistics platform. Discovered live at openapi.fastship.co: GET /api/v2 returns "Welcome to API Version 2.0" and POST /'
  name: FastShip Open API
  slug: fastship-open-api
artifact_total: 5
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/cloud-commerce-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://cloudcommerce.co
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/cloud-commerce-llms.txt
- group: commercial
  title: ''
  type: Plans
  url: plans/cloud-commerce-plans-pricing.yml
- group: build
  title: ''
  type: Packages
  url: packages/cloud-commerce-packages.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/cloud-commerce-rate-limits.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/cloud-commerce-conventions.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/cloud-commerce-lifecycle.yml
- group: operate
  title: ''
  type: StatusPage
  url: https://status.fastship.co/
- group: operate
  title: ''
  type: Support
  url: https://fastship.co/contactus/
- group: operate
  title: ''
  type: HelpCenter
  url: https://fastship.co/help/
- group: company
  title: ''
  type: Blog
  url: https://fastship.co/blog/
- group: start
  title: ''
  type: SignUp
  url: https://app.fastship.co/joinus
- group: start
  title: ''
  type: Login
  url: https://app.fastship.co/login
- group: commercial
  title: ''
  type: TermsOfService
  url: https://fastship.co/terms/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://fastship.co/privacy-policy/
coverage:
  checked: '2026-08-13'
  detail: 'FastShip''s API is live and answers anonymously at openapi.fastship.co/api/v2, but the only public route to it is a lead-capture form: fastship.co/api is a one-paragraph WordPress portfolio page titled "API & Widget", the documentation host docs.fastship.co resolves to 13.251.14.8 and then accepts no TCP connection, and the "FastShip For Business" page that markets API integration ends in a registration form with no reference, no spec and no pricing behind it.'
  evidence:
  - status: 200
    url: https://openapi.fastship.co/api/v2
  - status: 401
    url: https://openapi.fastship.co/api/v2/login
  - status: 200
    url: https://fastship.co/api
  - status: 0
    url: https://docs.fastship.co/
  - status: 404
    url: https://fastship.co/docs
  - status: 404
    url: https://openapi.fastship.co/openapi.json
  reason: sales-gate
  state: gated
created: '2026-07-17'
description: 'Cloud Commerce (CloudCommerce) is a Bangkok, Thailand-based venture tech builder helping small and medium enterprises across Southeast Asia sell globally. Backed by 500 Global (500 Startups) at the seed stage, it operates three commerce platforms: FastShip, a cross-border e-commerce logistics platform; CloudMall, an e-commerce distribution platform to build, run, and scale online marketplaces; and KOLLAB, an influencer-commerce platform connecting brands with over 100,000 KOLs across Instagram, TikTok, and Facebook. The company connects SME product data to global online marketplaces and logistics providers. FastShip runs a live versioned REST API at openapi.fastship.co and markets API integration to business accounts, but publishes no developer reference, no OpenAPI, and no SDKs: the documentation host docs.fastship.co accepts no connections and fastship.co/api is a one-paragraph marketing page. FastShip does serve a hand-authored llms.txt and a Pulsetic-hosted status page.'
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/cloud-commerce.png
layout: provider
modified: '2026-08-13'
name: Cloud Commerce
nav: Providers
network: true
overview: 'Cloud Commerce publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, E-Commerce, Logistics, Marketplace, and Influencer Marketing.


  Cloud Commerce''s developer surface includes support, engineering blog, signup flow, and 13 more developer resources.'
plans:
- name: Cloud Commerce Plans Pricing
  plan_count: 0
  slug: cloud-commerce-plans-pricing
random_paper: 16
rate_limits:
- limit_count: 1
  name: Cloud Commerce Rate Limits
  slug: cloud-commerce-rate-limits
score:
  band: emerging
  composite: 23.2
  coverage:
    artifact_dirs: 14
    catalog_gap: 70.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 34.2
    commercial_clarity: 34.2
    contract_governance: 18.2
    contract_quality: 0.0
    developer_ergonomics: 19.0
    discoverability: 75.9
    governance: 18.2
    operational_transparency: 21.1
  previous_composite: 23.2
  provenance:
    conformance: first-party
    mcp: derived
  schema_version: 0.17.2
  scored_at: '2026-09-01'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/cloud-commerce/refs/heads/main/screenshots/cloud-commerce-2026-07-25T205652.png
security:
- kind: authentication
  name: Cloud Commerce Authentication
  slug: cloud-commerce-authentication
  summary_line: 0 schemes
- kind: domain-security
  name: Cloud Commerce Domain Security
  slug: cloud-commerce-domain-security
  summary_line: TLSv1.3 · DMARC
slug: cloud-commerce
tags:
- Company
- E-Commerce
- Logistics
- Marketplace
- Influencer Marketing
- Cross-Border Commerce
- SME
- Southeast Asia
- Shipping
- Fulfillment
- Thailand
website: https://cloudcommerce.co
---
