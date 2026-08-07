---
access_model:
  confidence: medium
  label: Self-serve signup
  onboarding: self-serve
  pricing: unknown
  public: false
  source:
  - authentication
  trial: false
  try_now: false
agent_readiness:
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    auth_clarity: true
    consent_identity: true
    dry_run_mode: false
    error_semantics: false
    event_surface_described: true
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: false
    spec_presence: true
    well_known_catalog: true
  schema_version: 0.2
  score: 36.9
  scored_at: '2026-08-06'
api_count: 1
apis:
- description: 'RealGifts full REST API for embedding a gift shop, reward store, and wishlist into a platform: browse a 1M+ gift catalog, create and send gifts, handle privacy-preserving recipient redemption, and tra'
  name: RealGifts API
  slug: realgifts-api
artifact_total: 5
asyncapis:
- description: ''
  name: Real Gift Services Webhooks
  slug: real-gift-services-webhooks
common:
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/real-gift-services-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: Security
  url: security/real-gift-services-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/real-gift-services-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.getrealgifts.com
- group: start
  title: ''
  type: DeveloperPortal
  url: https://www.getrealgifts.com/#developers
- group: docs
  title: ''
  type: Documentation
  url: https://www.getrealgifts.com/documentation
- group: docs
  title: ''
  type: APIReference
  url: https://www.getrealgifts.com/documentation
- group: commercial
  title: ''
  type: Pricing
  url: https://www.getrealgifts.com/pricing
- group: start
  title: ''
  type: SignUp
  url: https://www.getrealgifts.com/signup
- group: start
  title: ''
  type: Login
  url: https://www.getrealgifts.com/login
- group: operate
  title: ''
  type: Support
  url: https://www.getrealgifts.com/contact
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.getrealgifts.com/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.getrealgifts.com/privacy
- group: commercial
  title: ''
  type: License
  url: https://www.getrealgifts.com/license
- group: auth
  title: ''
  type: Authentication
  url: authentication/real-gift-services-authentication.yml
- group: build
  title: ''
  type: Packages
  url: packages/real-gift-services-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/real-gift-services-packages.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/real-gift-services-conventions.yml
- group: design
  title: ''
  type: Components
  url: components/real-gift-services-components.yml
- group: design
  title: ''
  type: Webhooks
  url: asyncapi/real-gift-services-webhooks.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/real-gift-services-well-known.yml
- group: auth
  title: ''
  type: SecurityTxt
  url: well-known/real-gift-services-security.txt
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/real-gift-services-llms.txt
created: '2026-07-17'
description: RealGifts (Real Gift Services) is a Gifting-as-a-Service (GaaS) and G-Commerce platform, operating since 2008, that lets platforms and apps embed a turnkey gift shop, reward store, and wishlist experience in minutes. Its curated catalog spans more than one million gifts across hundreds of brands, sold through drop-in widgets, badges, and buttons or a full REST API with webhooks and SDKs for JavaScript, Node.js, PHP, Python, Ruby, Perl, iOS, and Android. Platforms integrate once, white-label the storefront, checkout, and email, and earn commissions on every order while RealGifts handles payments, shipping, redemption, multi-currency display, international delivery, and recipient-privacy-preserving gift claiming. RealGifts was an fbFund recipient, was built for the Facebook Gift Shop, and has been featured in TIME and Fast Company.
image: https://www.getrealgifts.com/images/brand/realgifts-og-image.png
layout: provider
modified: '2026-07-20'
name: Real Gift Services
nav: Providers
network: true
overview: 'Real Gift Services publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Gifting, Gift Cards, Rewards, and Loyalty.


  The Real Gift Services catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  Real Gift Services'' developer surface includes documentation, API reference, pricing, signup flow, support, authentication, and 17 more developer resources.'
random_paper: 109
score:
  band: developing
  composite: 42.1
  delta: 0.0
  facets:
    commercial_clarity: 44.7
    contract_quality: 51.6
    developer_ergonomics: 45.7
    discoverability: 87.0
    governance: 0.0
    operational_transparency: 18.4
  previous_composite: 42.1
  schema_version: 0.9.1
  scored_at: '2026-08-06'
  trend: flat
security:
- kind: authentication
  name: Real Gift Services Authentication
  slug: real-gift-services-authentication
  summary_line: 1 scheme
- kind: domain-security
  name: Real Gift Services Domain Security
  slug: real-gift-services-domain-security
  summary_line: TLSv1.3 · DNSSEC · DMARC
- kind: vulnerability-disclosure
  name: Real Gift Services Vulnerability Disclosure
  slug: real-gift-services-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: real-gift-services
tags:
- Company
- Gifting
- Gift Cards
- Rewards
- Loyalty
- E-Commerce
- Commerce
- Embedded Commerce
- API
- SDKs
- Webhooks
website: https://www.getrealgifts.com
---
