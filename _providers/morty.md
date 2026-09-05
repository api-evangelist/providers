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
api_count: 0
artifact_total: 2
common:
- group: company
  title: ''
  type: Website
  url: https://morty.com/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://platform.morty.com/
- group: docs
  title: ''
  type: Documentation
  url: https://platform.morty.com/docs/
- group: operate
  title: ''
  type: Support
  url: https://platform.morty.com/faq/
- group: start
  title: ''
  type: SignUp
  url: https://platform.morty.com/join/
- group: commercial
  title: ''
  type: Pricing
  url: https://www.morty.com/pricing
- group: company
  title: ''
  type: Blog
  url: https://www.morty.com/blog
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.morty.com/legal/privacy
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.morty.com/legal/tos
- group: design
  title: ''
  type: Components
  url: components/morty-components.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/morty-authentication.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/morty-domain-security.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/morty-llms.txt
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/morty-changelog.yml
created: '2026-07-17'
description: 'Morty is a digital mortgage platform and modular, embeddable mortgage infrastructure company (a Techstars-backed fintech). It gives loan officers, brokers, realtors, and fintech partners an all-in-one, compliance-ready stack to launch and scale a mortgage business without building from scratch: a Loan Origination System (LOS), Point-of-Sale (POS), a real-time Product & Pricing Engine (PPE), a lender network (25+ lenders), processing and fulfillment, and Rosey AI automation. Partners can embed mortgage into their own product via Morty''s embeddable widgets and "real-time pricing, eligibility, and overlays via API," with an API key provisioned through a partnership (Contact Sales). Morty publishes no public OpenAPI, developer portal, or /.well-known API surface today — the API is partner-gated.'
image: https://morty-cms.s3.us-east-2.amazonaws.com/public/Morty_Logo_Square.png
layout: provider
modified: '2026-07-20'
name: Morty
nav: Providers
network: true
overview: 'Morty is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Mortgage, Lending, Fintech, and Mortgage Infrastructure.


  Morty''s developer surface includes documentation, support, signup flow, pricing, engineering blog, authentication, changelog, and 7 more developer resources.'
random_paper: 4
score:
  band: emerging
  composite: 24.4
  coverage:
    artifact_dirs: 8
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 44.7
    commercial_clarity: 44.7
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 38.1
    discoverability: 57.4
    governance: 0.0
    operational_transparency: 15.8
  previous_composite: 24.4
  schema_version: 0.18.3
  scored_at: '2026-09-04'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/morty/refs/heads/main/screenshots/morty-2026-08-07T184313.png
security:
- kind: authentication
  name: Morty Authentication
  slug: morty-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Morty Domain Security
  slug: morty-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: morty
tags:
- Company
- Mortgage
- Lending
- Fintech
- Mortgage Infrastructure
- Loan Origination
- Pricing Engine
- Embedded Finance
website: https://morty.com/
---
