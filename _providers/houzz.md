---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source:
  - authentication
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
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 2.5
  scored_at: '2026-09-04'
api_count: 1
apis:
- description: Official Houzz commerce API for third-party marketplace partners. Lets sellers and vendors sync product catalog/listings, update inventory levels and pricing, and retrieve and manage orders. Access is
  name: Houzz Seller & Vendor Commerce API
  slug: houzz-seller-vendor-commerce-api
artifact_total: 3
common:
- group: company
  title: ''
  type: Website
  url: https://houzz.com
- group: docs
  title: ''
  type: APIReference
  url: https://help.houzz.com/s/topic/0TO44000000UgcMGAS/houzz-seller-api?language=en_US
- group: operate
  title: ''
  type: Support
  url: https://help.houzz.com
- group: company
  title: ''
  type: Blog
  url: https://www.houzz.com/magazine
- group: commercial
  title: ''
  type: Pricing
  url: https://www.houzz.com/houzz-pro/pricing
- group: start
  title: ''
  type: SignUp
  url: https://www.houzz.com/signup
- group: start
  title: ''
  type: Login
  url: https://www.houzz.com/signin
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.houzz.com/termsOfUse
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.houzz.com/privacyPolicy
- group: auth
  title: ''
  type: Authentication
  url: authentication/houzz-authentication.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/houzz-domain-security.yml
created: '2026-07-17'
description: 'Houzz is a home renovation and design platform that connects homeowners with home professionals, products, and design inspiration, and operates Houzz Pro, an all-in-one business management SaaS for contractors and design professionals (3D floor plans, takeoffs, estimates, invoices, scheduling, CRM, and marketing). For commerce, Houzz runs a marketplace and exposes an official Seller/Vendor Commerce API (opened to third-party partners in 2016) that lets merchants sync product listings, inventory, pricing, and orders. API access is gated: sellers enable it under Settings > API in the Houzz dashboard or request it via sellerapi@houzz.com, then authenticate integrations with an App ID, Token, and User Name. Houzz does not publish a general-purpose public developer portal, OpenAPI spec, or first-party SDKs; integration is handled through the Seller/Vendor programs and Houzz Pro''s pre-built integrations (QuickBooks, Zapier, Gmail, Google Calendar/Drive, Gusto).'
image: https://st.hzcdn.com/static/apple-touch-icon-precomposed.png
layout: provider
modified: '2026-07-19'
name: Houzz
nav: Providers
network: true
overview: 'Houzz publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, E-Commerce, Marketplace, Home Improvement, and Interior Design.


  Houzz''s developer surface includes API reference, support, engineering blog, pricing, signup flow, authentication, and 5 more developer resources.'
random_paper: 9
score:
  band: emerging
  composite: 21.0
  coverage:
    artifact_dirs: 4
    catalog_earned: 37.0
    catalog_earned_first_party: 0.0
    catalog_gap: 78.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 44.7
    commercial_clarity: 44.7
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 26.2
    discoverability: 68.5
    governance: 0.0
    operational_transparency: 0.0
  previous_composite: 21.0
  schema_version: 0.18.3
  scored_at: '2026-09-04'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/houzz/refs/heads/main/screenshots/houzz-2026-07-25T221720.png
security:
- kind: authentication
  name: Houzz Authentication
  slug: houzz-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Houzz Domain Security
  slug: houzz-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: houzz
tags:
- Company
- E-Commerce
- Marketplace
- Home Improvement
- Interior Design
- Home Renovation
- Furniture
- Software-as-a-Service
website: https://houzz.com
---
