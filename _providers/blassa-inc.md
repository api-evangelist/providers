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
api_count: 0
artifact_total: 3
asyncapis:
- description: ''
  name: Blassa Inc Webhooks
  slug: blassa-inc-webhooks
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/blassa-inc-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://blassa.io
- group: start
  title: ''
  type: DeveloperPortal
  url: https://blassa.readme.io/
- group: docs
  title: ''
  type: Documentation
  url: https://blassa.readme.io/
- group: docs
  title: ''
  type: APIReference
  url: https://blassa.readme.io/reference/about-blassa
- group: start
  title: ''
  type: SignUp
  url: https://business.blassa.io
- group: commercial
  title: ''
  type: Pricing
  url: https://blassa.io/pricing
- group: company
  title: ''
  type: Blog
  url: https://blassa.io/blog
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://blassa.io/privacy
- group: auth
  title: ''
  type: Authentication
  url: authentication/blassa-inc-authentication.yml
- group: design
  title: ''
  type: Webhooks
  url: asyncapi/blassa-inc-webhooks.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/blassa-inc-well-known.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/blassa-inc-llms.txt
created: '2026-07-17'
description: Blassa is an AI-powered location intelligence and geocoding platform built for the informal addressing systems common across the Middle East and Africa (MEA), where up to 40% of deliveries fail on the first attempt. The Blassa API turns ambiguous location descriptions and photos into precise coordinates and structured, verified addresses, offering forward and reverse geocoding, multi-language address autocomplete (Arabic, French, and local languages), address validation with deliverability scoring, and photo-to-location conversion. It targets logistics, e-commerce, and last-mile delivery companies looking to cut failed deliveries and improve checkout conversion. Founded in 2021 and backed by 500 Global and the Sanabil Accelerator, Blassa exposes its capabilities through a credit-metered REST API with free, Pro, and Enterprise plans, an API-key auth model, webhook support, and a hosted developer portal.
image: https://storage.googleapis.com/gpt-engineer-file-uploads/7t37Ke0rqPPrjfKJWKCzuL6xo1r2/social-images/social-1770386874845-Logo.png
layout: provider
modified: '2026-07-18'
name: Blassa Inc.
nav: Providers
network: true
overview: 'Blassa Inc. is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Location Intelligence, Geocoding, Address Verification, and Maps.


  The Blassa Inc. catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  Blassa Inc.''s developer surface includes documentation, API reference, signup flow, pricing, engineering blog, authentication, and 7 more developer resources.'
random_paper: 2
score:
  band: thin
  composite: 26.9
  coverage:
    artifact_dirs: 7
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 21.1
    commercial_clarity: 21.1
    contract_governance: 0.0
    contract_quality: 41.6
    developer_ergonomics: 27.4
    discoverability: 57.4
    governance: 0.0
    operational_transparency: 7.9
  previous_composite: 26.9
  schema_version: 0.18.3
  scored_at: '2026-09-04'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/blassa-inc/refs/heads/main/screenshots/blassa-inc-2026-07-25T203300.png
security:
- kind: authentication
  name: Blassa Inc Authentication
  slug: blassa-inc-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Blassa Inc Domain Security
  slug: blassa-inc-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: blassa-inc
tags:
- Company
- Location Intelligence
- Geocoding
- Address Verification
- Maps
- Logistics
- Last Mile Delivery
- E-Commerce
- Middle East
- Africa
website: https://blassa.io
---
