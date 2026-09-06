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
  scored_at: '2026-09-05'
api_count: 0
artifact_total: 2
common:
- group: company
  title: ''
  type: Website
  url: https://storehub.com
- group: docs
  title: ''
  type: Documentation
  url: https://care.storehub.com/en/
- group: operate
  title: ''
  type: Support
  url: https://www.storehub.com/my/contact
- group: commercial
  title: ''
  type: Pricing
  url: https://www.storehub.com/my/pricing
- group: company
  title: ''
  type: Blog
  url: https://www.storehub.com/my/blog
- group: start
  title: ''
  type: SignUp
  url: https://www.storehub.com/my/request-a-demo
- group: start
  title: ''
  type: Login
  url: https://redirect.storehubhq.com/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.storehub.com/my/terms-conditions
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.storehub.com/my/privacy-policy
- group: auth
  title: ''
  type: Authentication
  url: authentication/storehub-authentication.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/storehub-domain-security.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/storehub-llms.txt
created: '2026-07-17'
description: StoreHub is Southeast Asia's leading all-in-one cloud-based point-of-sale (POS) and business-management platform. Founded in 2013 and headquartered in Malaysia, it powers over 18,000 restaurants, retailers, and service-based businesses across Malaysia, the Philippines, and Thailand. The platform bundles POS, inventory management, multi-location management, employee management, reporting and analytics, QR Order & Pay, e-invoicing (LHDN/BIR compliant), loyalty and cashback, SMS marketing (Engage), Beep Delivery online ordering, a branded webstore, and marketplace and food-delivery integrations. StoreHub exposes a private, partner-gated REST API for custom integrations (dedicated API access is an Enterprise-tier feature); credentials are issued by Customer Care on request and there is no public OpenAPI specification or self-serve developer portal.
image: https://framerusercontent.com/images/inCzE8S5A4pU0LnQwXwR2NnU3I4.png
layout: provider
modified: '2026-07-21'
name: StoreHub
nav: Providers
network: true
overview: 'StoreHub is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Point-of-Sale, Retail, Restaurant, and Inventory Management.


  StoreHub''s developer surface includes documentation, support, pricing, engineering blog, signup flow, authentication, and 6 more developer resources.'
random_paper: 15
score:
  band: emerging
  composite: 20.2
  coverage:
    artifact_dirs: 6
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
    developer_ergonomics: 28.6
    discoverability: 57.4
    governance: 0.0
    operational_transparency: 0.0
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
    regions:
    - southeast-asia
  previous_composite: 20.2
  regulatory:
    applies: true
    matched_via: tags
    regime: Payments
    regime_id: payments
    score: 31.3
  schema_version: 0.18.3
  scored_at: '2026-09-05'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/storehub/refs/heads/main/screenshots/storehub-2026-09-02T160928.png
security:
- kind: authentication
  name: Storehub Authentication
  slug: storehub-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Storehub Domain Security
  slug: storehub-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: storehub
tags:
- Company
- Point-of-Sale
- Retail
- Restaurant
- Inventory Management
- Payments
- E-Commerce
- Loyalty
- Southeast Asia
- Small Business
website: https://storehub.com
---
