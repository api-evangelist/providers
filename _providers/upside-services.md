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
artifact_total: 2
common:
- group: auth
  title: ''
  type: TrustCenter
  url: security/upside-services-trust-center.yml
- group: auth
  title: ''
  type: Compliance
  url: https://trust.upside.com/
- group: auth
  title: ''
  type: DomainSecurity
  url: security/upside-services-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.upside.com/
- group: company
  title: ''
  type: About
  url: https://www.upside.com/about
- group: company
  title: ''
  type: Blog
  url: https://www.upside.com/blog
- group: operate
  title: ''
  type: PressReleases
  url: https://www.upside.com/newsroom
- group: company
  title: ''
  type: Careers
  url: https://www.upside.com/careers
- group: operate
  title: ''
  type: Support
  url: https://support.upside.com/hc/en-us
- group: start
  title: ''
  type: Login
  url: https://dashboard.upside.com/login
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.upside.com/data-and-security/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.upside.com/data-and-security/privacy-policy
- group: company
  title: ''
  type: Partners
  url: https://www.upside.com/partnerships/tech-integration
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/upside-services-llms.txt
- group: agent
  title: ''
  type: WellKnownProbe
  url: well-known/upside-services-well-known.yml
created: '2026-07-17'
description: Upside (Upside Services, Inc.) is a retail technology company whose platform delivers personalized cash-back offers on gas, groceries, and dining to more than five million consumers through the Upside app and embedded partner experiences. Merchants across fuel and convenience, grocery, and restaurants pay only for measured incremental profit, verified against control groups. Upside operates an enterprise partner API used by companies like Fiserv, GasBuddy, Lyft, Uber, and Marqeta to embed offers, but publishes no public developer portal, API documentation, or SDKs - API access is arranged through its partnerships team. Backed by DCVC (first invested 2016).
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/upside-services.png
layout: provider
modified: '2026-07-21'
name: Upside Services
nav: Providers
network: true
overview: 'Upside Services is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Cashback, Retail, Fuel, and Grocery.


  Upside Services'' developer surface includes engineering blog, support, and 13 more developer resources.'
random_paper: 9
score:
  band: emerging
  composite: 17.2
  coverage:
    artifact_dirs: 5
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 50.0
    commercial_clarity: 50.0
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 7.1
    discoverability: 57.4
    governance: 0.0
    operational_transparency: 0.0
  previous_composite: 17.2
  schema_version: 0.18.3
  scored_at: '2026-09-04'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/upside-services/refs/heads/main/screenshots/upside-services-2026-09-02T165100.png
security:
- kind: domain-security
  name: Upside Services Domain Security
  slug: upside-services-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: trust-center
  name: Upside Services Trust Center
  slug: upside-services-trust-center
  summary_line: SOC 2, ISO 27001, PCI DSS
slug: upside-services
tags:
- Company
- Cashback
- Retail
- Fuel
- Grocery
- Restaurant
- Loyalty
- Consumer Incentives
website: https://www.upside.com/
---
