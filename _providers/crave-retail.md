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
  schema_version: 0.2
  score: 0.0
  scored_at: '2026-09-04'
api_count: 0
artifact_total: 1
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/crave-retail-domain-security.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/crave-retail-llms.txt
- group: company
  title: ''
  type: Website
  url: https://craveretail.com/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://craveretail.com/privacy.html
- group: commercial
  title: ''
  type: TermsOfService
  url: https://craveretail.com/terms.html
created: '2026-07-17'
description: Crave Retail, Inc. builds in-store retail technology that connects shoppers, store associates, and product data across physical touchpoints. Its platform spans Crave Engage (customer-facing digital shopping assistants in fitting rooms, on the sales floor, and on mobile), Crave Assist (store-associate tools for floor visibility, service routing, and item lookup), and Smart Fitting Rooms, the RFID-based connected fitting-room product it started with. Crave reports 3,000+ live touchpoints, 27M+ shopper sessions, and operations across 10+ countries. The company is Techstars-backed. As of this enrichment pass it publishes a marketing and legal web presence but no public developer API, OpenAPI specification, SDKs, or documentation.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/crave-retail.png
layout: provider
modified: '2026-07-18'
name: Crave Retail
nav: Providers
network: true
overview: Crave Retail is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Retail, Retail Technology, In-Store, and Smart Fitting Rooms.
random_paper: 18
score:
  band: minimal
  composite: 10.0
  coverage:
    artifact_dirs: 3
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
    contract_quality: 0.0
    developer_ergonomics: 0.0
    discoverability: 57.4
    governance: 0.0
    operational_transparency: 0.0
  previous_composite: 10.0
  schema_version: 0.18.3
  scored_at: '2026-09-04'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/crave-retail/refs/heads/main/screenshots/crave-retail-2026-07-25T210649.png
security:
- kind: domain-security
  name: Crave Retail Domain Security
  slug: crave-retail-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: crave-retail
tags:
- Company
- Retail
- Retail Technology
- In-Store
- Smart Fitting Rooms
- RFID
- Shopping
- E-Commerce
website: https://craveretail.com/
---
