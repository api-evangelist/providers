---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source:
  - authentication
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
    error_semantics: false
    event_surface_described: true
    idempotency: false
    mcp_server: false
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 19.8
  scored_at: '2026-09-04'
api_count: 1
apis:
- description: Merchant-integration API for SHEIN sellers and logistics partners — OpenAPI and Webhook capabilities covering product publishing, order fulfillment, logistics/shipping, and stock-preparation order man
  name: SHEIN Open Platform
  slug: shein-open-platform
artifact_total: 4
asyncapis:
- description: ''
  name: Shein Webhooks
  slug: shein-webhooks
common:
- group: company
  title: ''
  type: Website
  url: https://shein.com
- group: start
  title: ''
  type: DeveloperPortal
  url: https://open.sheincorp.com/
- group: docs
  title: ''
  type: Documentation
  url: https://open.sheincorp.com/en
- group: auth
  title: ''
  type: Authentication
  url: authentication/shein-authentication.yml
- group: design
  title: ''
  type: Webhooks
  url: asyncapi/shein-webhooks.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/shein-well-known.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/shein-domain-security.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/shein-llms.txt
- group: operate
  title: ''
  type: Support
  url: mailto:openapi@shein.com
- group: commercial
  title: ''
  type: TermsOfService
  url: https://open.sheincorp.com/contract
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://open.sheincorp.com/contract?contractType=PRIVACY_POLICY
- group: start
  title: ''
  type: SignUp
  url: https://open.sheincorp.com/
created: '2026-07-17'
description: 'SHEIN is a global online fast-fashion and lifestyle retailer. For third-party sellers and logistics partners it operates the SHEIN Open Platform (open.sheincorp.com), a merchant-integration platform exposing OpenAPI and Webhook capabilities for product management (publishing listings), SHEIN-fulfilled and seller-fulfilled order management, logistics and shipping, and stock-preparation order fulfillment. Integration follows an application-and-review model: a partner applies for an Open Platform account, creates an application, passes review, completes seller authorization, then integrates the API solutions. The production API is served from openapi.sheincorp.com and requires authenticated, seller-authorized access. Developer contact is openapi@shein.com.'
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/shein.png
layout: provider
modified: '2026-07-21'
name: SHEIN
nav: Providers
network: true
overview: 'SHEIN publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Consumer, E-Commerce, Retail, and Fashion.


  The SHEIN catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  SHEIN''s developer surface includes documentation, authentication, support, signup flow, and 8 more developer resources.'
random_paper: 10
score:
  band: thin
  composite: 33.0
  coverage:
    artifact_dirs: 6
    catalog_earned: 37.0
    catalog_earned_first_party: 0.0
    catalog_gap: 78.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 34.2
    commercial_clarity: 34.2
    contract_governance: 0.0
    contract_quality: 41.6
    developer_ergonomics: 35.7
    discoverability: 75.9
    governance: 0.0
    operational_transparency: 7.9
  previous_composite: 33.0
  schema_version: 0.18.3
  scored_at: '2026-09-04'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/shein/refs/heads/main/screenshots/shein-2026-09-02T155124.png
security:
- kind: authentication
  name: Shein Authentication
  slug: shein-authentication
  summary_line: seller-authorization · 0 schemes
- kind: domain-security
  name: Shein Domain Security
  slug: shein-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: shein
tags:
- Company
- Consumer
- E-Commerce
- Retail
- Fashion
- Marketplace
- Fulfillment
- Logistics
- Open Platform
- Sellers
website: https://shein.com
---
