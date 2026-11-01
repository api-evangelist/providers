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
  - sandbox
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
    idempotency: documented
    mcp_server: false
    openapi_examples: false
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 25.9
  scored_at: '2026-10-31'
api_count: 1
apis:
- description: The Klump REST API lets a merchant verify transactions, sync commerce product catalogs, create Klump Access hosted payment pages, and resend webhooks. A single base URL serves both sandbox and product
  name: Klump API
  slug: klump-api
artifact_total: 7
asyncapis:
- description: ''
  name: Klump Webhooks
  slug: klump-webhooks
common:
- group: commercial
  href: https://artifacts.apis.io/klump/plans/klump-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/klump-plans-pricing.yml
- group: company
  title: ''
  type: Website
  url: https://useklump.com
- group: start
  title: ''
  type: DeveloperPortal
  url: https://useklump.com/developers
- group: docs
  title: ''
  type: Documentation
  url: https://docs.useklump.com/docs
- group: docs
  title: ''
  type: APIReference
  url: https://docs.useklump.com/docs/api-keys-authorization
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.useklump.com/docs/getting-started
- group: operate
  title: ''
  type: Support
  url: https://useklump.com/contact
- group: company
  title: ''
  type: Blog
  url: https://useklump.com/blog
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/Klump-Inc
- group: commercial
  title: ''
  type: Pricing
  url: https://useklump.com/pricing
- group: start
  title: ''
  type: SignUp
  url: https://merchant.useklump.com/sign-up
- group: start
  title: ''
  type: Login
  url: https://merchant.useklump.com/sign-in
- group: commercial
  title: ''
  type: TermsOfService
  url: https://useklump.com/legal/terms-of-service
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://useklump.com/legal/privacy-policy
- group: auth
  href: https://artifacts.apis.io/klump/conformance/klump-conformance.yml
  title: ''
  type: Compliance
  url: conformance/klump-conformance.yml
- group: auth
  href: https://artifacts.apis.io/klump/authentication/klump-authentication.yml
  title: ''
  type: Authentication
  url: authentication/klump-authentication.yml
- group: build
  href: https://artifacts.apis.io/klump/packages/klump-packages.yml
  title: ''
  type: Packages
  url: packages/klump-packages.yml
- group: build
  href: https://artifacts.apis.io/klump/packages/klump-packages.yml
  title: ''
  type: SDKs
  url: packages/klump-packages.yml
- group: design
  href: https://artifacts.apis.io/klump/components/klump-components.yml
  title: ''
  type: Components
  url: components/klump-components.yml
- group: design
  href: https://artifacts.apis.io/klump/conventions/klump-conventions.yml
  title: ''
  type: Conventions
  url: conventions/klump-conventions.yml
- group: design
  href: https://artifacts.apis.io/klump/conventions/klump-conventions.yml
  title: ''
  type: Idempotency
  url: conventions/klump-conventions.yml
- group: design
  href: https://artifacts.apis.io/klump/errors/klump-error-codes.yml
  title: ''
  type: ErrorCatalog
  url: errors/klump-error-codes.yml
- group: design
  href: https://artifacts.apis.io/klump/lifecycle/klump-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/klump-lifecycle.yml
- group: start
  href: https://artifacts.apis.io/klump/sandbox/klump-sandbox.yml
  title: ''
  type: Sandbox
  url: sandbox/klump-sandbox.yml
- group: design
  href: https://artifacts.apis.io/klump/asyncapi/klump-webhooks.yml
  title: ''
  type: Webhooks
  url: asyncapi/klump-webhooks.yml
- group: design
  href: https://artifacts.apis.io/klump/conformance/klump-conformance.yml
  title: ''
  type: Conformance
  url: conformance/klump-conformance.yml
- group: agent
  href: https://artifacts.apis.io/klump/well-known/klump-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/klump-well-known.yml
- group: auth
  href: https://artifacts.apis.io/klump/security/klump-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/klump-domain-security.yml
- group: agent
  href: https://artifacts.apis.io/klump/mcp/klump-mcp.yml
  title: ''
  type: X-MCPServerCandidate
  url: mcp/klump-mcp.yml
- group: agent
  href: https://artifacts.apis.io/klump/llms/klump-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/klump-llms.txt
created: '2026-07-17'
description: Klump Technology Company Ltd is a Lagos, Nigeria based fintech whose flagship product, Klump BNPL (Buy Now, Pay Later), lets shoppers spread the cost of a purchase over monthly instalments at online and in-store merchant checkouts. Merchants integrate Klump either through the Klump.js client-side checkout widget, a framework component (React, Vue 2, Vue 3, Angular, React Native, Flutter), an e-commerce plugin (WooCommerce/WordPress, Magento 2, PrestaShop, OpenCart, WHMCS), a Laravel package, or directly against the Klump REST API at https://api.useklump.com. The API is secret-key authenticated via a klump-secret-key header, uses one base URL for both sandbox and production (the key and the merchant application state, TEST or LIVE, select the environment), and covers transaction verification, Klump Commerce product sync, Klump Access hosted payment pages, and webhook resend. Klump emits transaction lifecycle webhooks (initiated, successful, abandoned) signed with an X-Klump-Signature
  HMAC header and retried hourly for 72 hours. Klump is backed by Seedcamp and displays a PCI DSS Compliant badge.
finops:
- has_sources: true
  method: derived
  name: Klump Finops
  primary_unit: reducing balance
  service_category: ''
  slug: klump-finops
  template: false
image: https://useklump.com/images/meta.png
layout: provider
modified: '2026-07-19'
name: Klump
nav: Providers
network: true
overview: 'Klump is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Payments, Buy Now Pay Later, Fintech, and Lending.


  The Klump catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  Klump''s developer surface includes documentation, API reference, getting-started guide, support, engineering blog, pricing, signup flow, and 23 more developer resources.'
plans:
- name: Klump Plans Pricing
  plan_count: 2
  slug: klump-plans-pricing
- name: Klump Price Estimates
  plan_count: 0
  slug: klump-price-estimates
random_paper: 1
score:
  band: developing
  composite: 53.0
  coverage:
    artifact_dirs: 19
    catalog_earned: 48.0
    catalog_earned_first_party: 8.0
    catalog_gap: 67.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 5.8
  facets:
    access_clarity: 81.6
    contract_governance: 18.2
    contract_quality: 39.0
    developer_ergonomics: 71.4
    discoverability: 66.1
    operational_transparency: 13.2
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    countries:
    - nigeria
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
    regions:
    - africa
  previous_composite: 47.2
  provenance:
    conformance: first-party
    mcp: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Payments
    regime_id: payments
    score: 33.9
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  trend: rising
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
screenshot: https://apis.io/screenshots/klump/klump-2026-07-25T223950.png
security:
- kind: authentication
  name: Klump Authentication
  slug: klump-authentication
  summary_line: apiKey · 2 schemes
- kind: domain-security
  name: Klump Domain Security
  slug: klump-domain-security
  summary_line: TLSv1.3 · DMARC
slug: klump
tags:
- Company
- Payments
- Buy Now Pay Later
- Fintech
- Lending
- Checkout
- E-Commerce
- Nigeria
- Africa
- Instalments
- Consumer Credit
website: https://useklump.com
---
