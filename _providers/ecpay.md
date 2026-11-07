---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source:
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
    auth_clarity: false
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    mcp_tool_quality: na
    openapi_examples: false
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: '0.2'
  score: 0.0
  scored_at: '2026-11-06'
api_count: 1
apis:
- description: Developer portal providing API technical documentation overview for payment, logistics, e‑invoice and ticket services.
  name: ECPay Developers
  slug: ecpay-developers
artifact_total: 2
common:
- group: other
  href: https://artifacts.apis.io/ecpay/vendors/ecpay-vendors.yml
  title: ''
  type: Vendors
  url: vendors/ecpay-vendors.yml
- group: other
  href: https://artifacts.apis.io/ecpay/hosts/ecpay-hosts.yml
  title: ''
  type: Hosts
  url: hosts/ecpay-hosts.yml
- group: build
  href: https://artifacts.apis.io/ecpay/packages/ecpay-packages.yml
  title: ''
  type: SDKs
  url: packages/ecpay-packages.yml
- group: build
  href: https://artifacts.apis.io/ecpay/packages/ecpay-packages.yml
  title: ''
  type: Packages
  url: packages/ecpay-packages.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://support.ecpay.com.tw/terms-return/
- group: operate
  title: ''
  type: Support
  url: https://support.ecpay.com.tw/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.ecpay.com.tw/CreditCard/Privacy
- group: company
  title: ''
  type: Newsroom
  url: https://app.ecpay.com.tw/Home/News
- group: company
  title: ''
  type: Blog
  url: https://blog.ecpay.com.tw/
- group: docs
  title: ''
  type: Documentation
  url: https://developers.ecpay.com.tw/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/ECPay
- group: auth
  href: https://artifacts.apis.io/ecpay/security/ecpay-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/ecpay-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://ecpay.com.tw/
coverage:
  checked: '2026-10-27'
  detail: The developer portal provides only HTML documentation without a published OpenAPI, AsyncAPI, GraphQL, gRPC, or WSDL spec.
  evidence:
  - status: 200
    url: https://developers.ecpay.com.tw/
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-10-27'
description: ECPay (綠界科技) is a Taiwan‑based payment service provider offering a comprehensive suite of financial solutions, including credit‑card processing, ATM transfers, convenience‑store payments, electronic invoicing, logistics integration, and digital gift‑ticket services. It serves e‑commerce merchants, NGOs, and enterprises with APIs, SDKs, and AI‑enhanced tools to streamline checkout, recurring billing, and donation flows across multiple channels.
image: https://www.ecpay.com.tw/Content/themes/WebStyle20131201/images/service/ECPAY_470x246.jpg
layout: provider
modified: '2026-10-27'
name: ECPay
nav: Providers
network: true
overview: 'ECPay is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Payments, Fintech, Taiwan, and E-Commerce.


  ECPay''s developer surface includes support, engineering blog, documentation, and 10 more developer resources.'
random_paper: 2
score:
  band: minimal
  composite: 9.7
  coverage:
    artifact_dirs: 10
    catalog_earned: 32.0
    catalog_earned_first_party: 0.0
    catalog_gap: 83.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -4.8
  facets:
    access_clarity: 10.5
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 15.5
    discoverability: 58.0
    operational_transparency: 2.6
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    countries:
    - taiwan
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
    regions:
    - greater-china
  needs_work:
    note: Recorded so this provider's gaps can be attributed. Does not affect the composite above.
    owner: catalog
    reasons:
    - owner: catalog
      reason: not_a_repo
  previous_composite: 14.5
  provenance:
    mcp: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Payments
    regime_id: payments
    score: 8.9
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
screenshot: https://apis.io/screenshots/ecpay/ecpay-2026-11-03T131312.png
security:
- kind: domain-security
  name: Ecpay Domain Security
  slug: ecpay-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: ecpay
tags:
- Company
- Payments
- Fintech
- Taiwan
- E-Commerce
website: https://ecpay.com.tw/
---
