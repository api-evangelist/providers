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
  score: 22.7
  scored_at: '2026-09-05'
api_count: 1
apis:
- baseURL: https://api.tiendanube.com/2025-03/
  baseurl_source: declared
  description: 'REST API for building public apps and integrations on the Nuvemshop / Tiendanube e-commerce platform: products, orders, customers, categories, coupons, discounts, transactions, shipping, locations, me'
  name: Nuvemshop Tiendanube API
  slug: nuvemshop-tiendanube-api
artifact_total: 7
asyncapis:
- description: Webhook event surface for the Nuvemshop/Tiendanube platform. Apps register a Webhook resource (event + url) and receive HTTP POST callbacks signed with HMAC-SHA256 in the x-linkedstore-hmac-sha256 hea
  name: Nuvemshop Tiendanube Webhook Events
  slug: nuvemshop-tiendanube-events-asyncapi
- description: ''
  name: Nuvemshop Tiendanube Webhooks
  slug: nuvemshop-tiendanube-webhooks
common:
- group: company
  title: ''
  type: Website
  url: https://www.nuvemshop.com.br/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://dev.tiendanube.com/
- group: docs
  title: ''
  type: Documentation
  url: https://tiendanube.github.io/api-documentation/
- group: docs
  title: ''
  type: APIReference
  url: https://tiendanube.github.io/api-documentation/intro
- group: start
  title: ''
  type: GettingStarted
  url: https://dev.tiendanube.com/docs/getting-started
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/TiendaNube
- group: operate
  title: ''
  type: Support
  url: https://atendimento.nuvemshop.com.br/
- group: company
  title: ''
  type: Blog
  url: https://www.nuvemshop.com.br/blog
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.nuvemshop.com.br/termos-de-uso
- group: operate
  title: ''
  type: StatusPage
  url: https://status.nuvemshop.com.br/
- group: build
  title: ''
  type: SDKs
  url: packages/nuvemshop-tiendanube-packages.yml
- group: build
  title: ''
  type: Packages
  url: packages/nuvemshop-tiendanube-packages.yml
- group: build
  title: ''
  type: CLI
  url: cli/nuvemshop-tiendanube-cli.yml
- group: design
  title: ''
  type: Components
  url: components/nuvemshop-tiendanube-components.yml
- group: auth
  title: ''
  type: SecurityTxt
  url: well-known/nuvemshop-tiendanube-security.txt
- group: agent
  title: ''
  type: WellKnown
  url: well-known/nuvemshop-tiendanube-well-known.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/nuvemshop-tiendanube-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: Security
  url: security/nuvemshop-tiendanube-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/nuvemshop-tiendanube-domain-security.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/nuvemshop-tiendanube-llms.txt
created: '2026-07-17'
description: Nuvemshop (Tiendanube in Spanish-speaking markets) is the leading e-commerce platform in Latin America, powering online stores for merchants across Brazil, Argentina, Mexico, Chile, Colombia and beyond. Its REST API lets partners and developers build public apps and integrations that manage products, variants, images, categories, orders, draft orders, abandoned checkouts, customers, coupons, discounts, transactions, payment providers, shipping carriers, locations, metafields, scripts and store data. Apps authenticate with a restricted OAuth 2 authorization-code flow (non-expiring bearer tokens), respect a leaky-bucket rate limit, and subscribe to a rich catalog of webhooks (order, product, customer, category, fulfillment, subscription and data-protection events) verified with HMAC-SHA256. The platform also ships an official CLI, the nube-sdk JavaScript packages, and the Nimbus design system.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/nuvemshop-tiendanube.png
layout: provider
modified: '2026-07-20'
name: Nuvemshop Tiendanube
nav: Providers
network: true
overview: 'Nuvemshop Tiendanube publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, E-Commerce, Retail, Online Stores, and Payments.


  The Nuvemshop Tiendanube catalog on APIs.io includes 2 event-driven AsyncAPI specifications.


  Nuvemshop Tiendanube''s developer surface includes documentation, API reference, getting-started guide, support, engineering blog, CLI, and 14 more developer resources.'
random_paper: 18
scopes:
- name: Nuvemshop Tiendanube Scopes
  scope_count: 12
  slug: nuvemshop-tiendanube-scopes
  summary_line: 12 scopes · authorizationCode
score:
  band: developing
  composite: 41.9
  coverage:
    artifact_dirs: 17
    catalog_earned: 37.0
    catalog_earned_first_party: 0.0
    catalog_gap: 78.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 10.5
    commercial_clarity: 10.5
    contract_governance: 4.5
    contract_quality: 42.7
    developer_ergonomics: 61.9
    discoverability: 75.9
    governance: 4.5
    operational_transparency: 36.8
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
    regions:
    - latin-america
  previous_composite: 41.9
  provenance:
    conformance: derived
    mcp: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Payments
    regime_id: payments
    score: 57.8
  schema_version: 0.18.3
  scored_at: '2026-09-05'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/nuvemshop-tiendanube/refs/heads/main/screenshots/nuvemshop-tiendanube-2026-08-07T185801.png
security:
- kind: authentication
  name: Nuvemshop Tiendanube Authentication
  slug: nuvemshop-tiendanube-authentication
  summary_line: oauth2 · 1 scheme
- kind: domain-security
  name: Nuvemshop Tiendanube Domain Security
  slug: nuvemshop-tiendanube-domain-security
  summary_line: TLSv1.3 · DMARC
- kind: vulnerability-disclosure
  name: Nuvemshop Tiendanube Vulnerability Disclosure
  slug: nuvemshop-tiendanube-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: nuvemshop-tiendanube
tags:
- Company
- E-Commerce
- Retail
- Online Stores
- Payments
- Shipping
- Webhook
- Authentication
- Latin America
- Storefront
- Apps Platform
website: https://www.nuvemshop.com.br/
---
