---
access_model:
  confidence: medium
  label: Free · Requires approval
  onboarding: approval
  pricing: free
  public: false
  source:
  - plans
  trial: false
  try_now: false
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: derived
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
    openapi_examples: verified
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 26.8
  scored_at: '2026-09-05'
api_count: 1
apis:
- description: The Cardtonic Gift Card Developer API enables merchants and platforms to integrate gift card services into their websites, mobile apps, and point-of-sale systems. The API exposes a catalog of more tha
  name: Cardtonic Gift Card Developer API
  slug: gift-card-developer-api
- description: Cardtonic Virtual Dollar Cards are user-facing USD-denominated cards that let African customers pay merchants that accept Visa/Mastercard globally. The product is currently consumed through the Cardto
  name: Cardtonic Virtual Dollar Card
  slug: virtual-dollar-card
- description: Cardtonic Bill Payments cover airtime top-ups, mobile data, electricity, TV subscriptions, and betting wallets across more than 100 countries, consumed through the Cardtonic app and dashboard. Partner
  name: Cardtonic Bill Payments
  slug: bill-payments
- baseURL: https://api.cardtonic.com/v1
  baseurl_source: declared
  description: The Cardtonic Business API is the account, credential and compliance layer of Cardtonic's developer program, and the only Cardtonic surface with a published machine-readable contract. It covers busine
  name: Cardtonic Business API
  slug: business-api
artifact_total: 11
collections:
- collection_type: open
  name: API Collection
  slug: open-cardtonic
common:
- group: company
  title: ''
  type: Website
  url: https://cardtonic.com/
- group: other
  title: ''
  type: Developer
  url: https://cardtonic.com/developer
- group: start
  title: ''
  type: DeveloperPortal
  url: https://cardtonic.com/developer
- group: docs
  title: ''
  type: Documentation
  url: https://docs.cardtonic.com
- group: docs
  title: ''
  type: APIReference
  url: https://docs.cardtonic.com
- group: other
  title: ''
  type: Dashboard
  url: https://dashboard.cardtonic.com/
- group: start
  title: ''
  type: Login
  url: https://dashboard.cardtonic.com/signin
- group: start
  title: ''
  type: SignUp
  url: https://dashboard.cardtonic.com/signup
- group: company
  title: ''
  type: About
  url: https://thetonictech.com/about-us
- group: company
  title: ''
  type: Blog
  url: https://cardtonic.com/read
- group: operate
  title: ''
  type: HelpCenter
  url: https://help.cardtonic.com/en/
- group: operate
  title: ''
  type: Support
  url: https://help.cardtonic.com/en/
- group: operate
  title: ''
  type: Contact
  url: https://cardtonic.com/contact-us
- group: operate
  title: ''
  type: StatusPage
  url: https://status.cardtonic.com/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://cardtonic.com/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://cardtonic.com/privacy
- group: other
  title: ''
  type: X
  url: https://x.com/cardtonic
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/thetonictech
- group: company
  title: ''
  type: Instagram
  url: https://www.instagram.com/cardtonic
- group: agent
  title: ''
  type: LlmsText
  url: https://cardtonic.com/llms.txt
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/cardtonic-llms.txt
- group: design
  title: ''
  type: Conformance
  url: conformance/cardtonic-conformance.yml
- group: auth
  title: ''
  type: Compliance
  url: conformance/cardtonic-conformance.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/cardtonic-lifecycle.yml
- group: build
  title: ''
  type: Packages
  url: packages/cardtonic-packages.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/cardtonic-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/cardtonic-rate-limits.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/cardtonic-domain-security.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/cardtonic-finops.yml
created: '2025-02-08'
description: Cardtonic is an Africa-focused fintech platform, operated by The Tonic Technologies, that lets users trade gift cards (sell unused cards for cash and buy over 14,000 local and international gift cards), issue virtual dollar cards, pay bills (airtime, data, electricity, TV, betting), purchase eSIMs in 140+ countries, and shop for gadgets through its Just Gadgets storefront. Cardtonic supports Naira and Cedi settlement for users in Nigeria and Ghana, carries a PCI DSS certification badge, and is registered with the Nigeria Data Protection Commission (NDPC) as a Data Controller of Major Importance under the Nigeria Data Protection Act 2023. For businesses, Cardtonic advertises a Gift Card Developer API (waitlist-only, no published contract) and separately publishes a real OpenAPI 3.0.1 contract for its Business API - business signup, login, 2FA, BVN and corporate KYC, and API-key issuance - through an Apidog-hosted documentation site at docs.cardtonic.com, against the base https://api.cardtonic.com/v1.
finops:
- name: Cardtonic Finops
  service_category: Fintech / Gift Cards
  slug: cardtonic-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/cardtonic.png
layout: provider
mcp_servers:
- description: A CANDIDATE tool list derived from Cardtonic's published OpenAPI operations. Cardtonic ships no MCP server of any kind. Nothing below is offered by the provider; each entry inherits its input schema f
  name: Cardtonic MCP Server
  slug: cardtonic-mcp-server
modified: '2026-09-05'
name: Cardtonic
nav: Providers
network: true
overview: 'Cardtonic publishes 1 API on the [APIs.io](https://apis.io/) network: Business API. Tagged areas include Africa, Bill Payments, eSIM, Finance, and Fintech.


  Cardtonic''s developer surface includes documentation, API reference, signup flow, engineering blog, support, and 24 more developer resources.'
plans:
- name: Cardtonic Plans Pricing
  plan_count: 1
  slug: cardtonic-plans-pricing
random_paper: 6
rate_limits:
- limit_count: 1
  name: Cardtonic Rate Limits
  slug: cardtonic-rate-limits
score:
  band: developing
  composite: 54.0
  coverage:
    artifact_dirs: 21
    catalog_earned: 51.0
    catalog_earned_first_party: 16.0
    catalog_gap: 64.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 30.9
  facets:
    access_clarity: 71.1
    commercial_clarity: 71.1
    contract_governance: 18.2
    contract_quality: 43.5
    developer_ergonomics: 54.2
    discoverability: 66.7
    governance: 18.2
    operational_transparency: 28.9
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
    regions:
    - africa
  previous_composite: 23.1
  provenance:
    conformance: first-party
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 100.0
      total: 1
    mcp: derived
    skills: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Payments
    regime_id: payments
    score: 68.8
  schema_version: 0.18.3
  scored_at: '2026-09-05'
  trend: rising
screenshot: https://raw.githubusercontent.com/api-evangelist/cardtonic/refs/heads/main/screenshots/cardtonic-2026-06-20T173956.png
security:
- kind: authentication
  name: Cardtonic Authentication
  slug: cardtonic-authentication
  summary_line: 3 schemes
- kind: domain-security
  name: Cardtonic Domain Security
  slug: cardtonic-domain-security
  summary_line: TLSv1.3 · DMARC
slug: cardtonic
tags:
- Africa
- Bill Payments
- eSIM
- Finance
- Fintech
- Gift Cards
- Ghana
- Nigeria
- Payments
- Virtual Dollar Cards
website: https://cardtonic.com/
---
