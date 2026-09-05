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
- description: AI REST API returning product recommendations and performing actions in the Proton.ai distributor platform. Authenticated with a static API key in the request header. Documented as a public Postman co
  name: Proton API
  slug: proton-api
artifact_total: 4
common:
- group: auth
  title: ''
  type: TrustCenter
  url: security/proton-trust-center.yml
- group: company
  title: ''
  type: Website
  url: https://www.proton.ai/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://api.proton.ai/
- group: docs
  title: ''
  type: Documentation
  url: https://api.proton.ai/
- group: docs
  title: ''
  type: APIReference
  url: https://api.proton.ai/
- group: build
  title: ''
  type: Postman
  url: https://api.proton.ai/
- group: operate
  title: ''
  type: HelpCenter
  url: https://help.proton.ai/
- group: operate
  title: ''
  type: Support
  url: https://help.proton.ai/
- group: operate
  title: ''
  type: StatusPage
  url: https://status.proton.ai/
- group: company
  title: ''
  type: Blog
  url: https://www.proton.ai/blog
- group: auth
  title: ''
  type: Compliance
  url: https://www.proton.ai/security
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.proton.ai/terms-of-use
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.proton.ai/privacy-policy
- group: auth
  title: ''
  type: Authentication
  url: authentication/proton-authentication.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/proton-domain-security.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/proton-lifecycle.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/proton-well-known.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/proton-llms.txt
created: '2026-07-17'
description: Proton.ai is an AI-powered industry cloud platform for wholesale and B2B distributors. It connects and centralizes a distributor's customer, product, and transactional data across disparate systems, then applies deep-learning models to produce real-time product recommendations, automate CRM and e-commerce workflows, enrich product data, and streamline order and quote processing. Proton.ai exposes an AI REST API (documented via Postman at api.proton.ai) that returns product recommendations and performs actions inside the Proton platform, authenticated with a static API key supplied in the request header. The company is based in Boston and raised a $20M Series A led by Felicis Ventures. This profile was surfaced as a VC-portfolio lead and enriched by the API Evangelist pipeline.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/proton.png
layout: provider
modified: '2026-07-20'
name: Proton.ai
nav: Providers
network: true
overview: 'Proton.ai publishes 1 API on the [APIs.io](https://apis.io/) network: Proton API. Tagged areas include Company, Artificial Intelligence, Distribution, Wholesale, and B2B.


  Proton.ai''s developer surface includes documentation, API reference, support, engineering blog, authentication, and 13 more developer resources.'
random_paper: 2
score:
  band: thin
  composite: 27.0
  coverage:
    artifact_dirs: 7
    catalog_earned: 37.0
    catalog_earned_first_party: 0.0
    catalog_gap: 78.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 36.8
    commercial_clarity: 36.8
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 50.0
    discoverability: 75.9
    governance: 0.0
    operational_transparency: 15.8
  previous_composite: 27.0
  schema_version: 0.18.3
  scored_at: '2026-09-04'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/proton/refs/heads/main/screenshots/proton-2026-09-02T152230.png
security:
- kind: authentication
  name: Proton Authentication
  slug: proton-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Proton Domain Security
  slug: proton-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: trust-center
  name: Proton Trust Center
  slug: proton-trust-center
  summary_line: SOC 2, GDPR
slug: proton
tags:
- Company
- Artificial Intelligence
- Distribution
- Wholesale
- B2B
- Sales
- Recommendations
- CRM
- E-Commerce
website: https://www.proton.ai/
---
