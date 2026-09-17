---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source:
  - authentication
  - rate-limits
  - security
  - sandbox
  trial: false
  try_now: false
agent_readiness:
  band: agent-native
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
    event_surface_described: true
    idempotency: verified
    mcp_server: false
    openapi_examples: verified
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 39.3
  scored_at: '2026-09-16'
api_count: 1
apis:
- description: The dedicated PSD2 Third Party Provider (TPP) interface for The Bank of London, implementing the UK Open Banking Read/Write API v3.1 (AIS, PIS, PIIS, plus dynamic client registration and OpenID Connec
  name: Bank of London PSD2 / Open Banking UK API
  slug: bank-of-london-psd2-open-banking-uk-api
- baseURL: https://api.bankoflondon.com/
  baseurl_source: declared
  description: The Accounts API from The Bank of London — 3 operation(s) for accounts.
  name: The Bank of London Accounts API
  slug: the-bank-of-london-accounts-api
- baseURL: https://api.bankoflondon.com/
  baseurl_source: declared
  description: The Confirmation of Payee API from The Bank of London — 1 operation(s) for confirmation of payee.
  name: The Bank of London Confirmation of Payee API
  slug: the-bank-of-london-confirmation-of-payee-api
- baseURL: https://api.bankoflondon.com/
  baseurl_source: declared
  description: The Customer Management API from The Bank of London — 4 operation(s) for customer management.
  name: The Bank of London Customer Management API
  slug: the-bank-of-london-customer-management-api
- baseURL: https://api.bankoflondon.com/
  baseurl_source: declared
  description: The Mandates (Direct Debits) API from The Bank of London — 3 operation(s) for mandates (direct debits).
  name: The Bank of London Mandates (Direct Debits) API
  slug: the-bank-of-london-mandates-direct-debits-api
- baseURL: https://api.bankoflondon.com/
  baseurl_source: declared
  description: The Payments V2 API from The Bank of London — 9 operation(s) for payments v2.
  name: The Bank of London Payments V2 API
  slug: the-bank-of-london-payments-v2-api
- baseURL: https://api.bankoflondon.com/
  baseurl_source: declared
  description: The Standing Orders API from The Bank of London — 5 operation(s) for standing orders.
  name: The Bank of London Standing Orders API
  slug: the-bank-of-london-standing-orders-api
- baseURL: https://api.bankoflondon.com/
  baseurl_source: declared
  description: The Statements API from The Bank of London — 2 operation(s) for statements.
  name: The Bank of London Statements API
  slug: the-bank-of-london-statements-api
- baseURL: https://api.bankoflondon.com/
  baseurl_source: declared
  description: The Transactions API from The Bank of London — 4 operation(s) for transactions.
  name: The Bank of London Transactions API
  slug: the-bank-of-london-transactions-api
- baseURL: https://api.bankoflondon.com/
  baseurl_source: declared
  description: The Virtual Account Management API from The Bank of London — 7 operation(s) for virtual account management.
  name: The Bank of London Virtual Account Management API
  slug: the-bank-of-london-virtual-account-management-api
- baseURL: https://api.bankoflondon.com/
  baseurl_source: declared
  description: The Webhook Management API from The Bank of London — 4 operation(s) for webhook management.
  name: The Bank of London Webhook Management API
  slug: the-bank-of-london-webhook-management-api
artifact_total: 16
asyncapis:
- description: ''
  name: The Bank Of London Webhooks
  slug: the-bank-of-london-webhooks
common:
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/the-bank-of-london/refs/heads/main/overlays/the-bank-of-london-api-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/the-bank-of-london-api-overlay.yaml
- group: company
  title: ''
  type: Website
  url: https://www.bankoflondon.com/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://developer.bankoflondon.com/
- group: docs
  title: ''
  type: Documentation
  url: https://developer.bankoflondon.com/docs/guides/getting-started-guide
- group: docs
  title: ''
  type: APIReference
  url: https://developer.bankoflondon.com/apis/the-bank-of-london-api
- group: start
  title: ''
  type: GettingStarted
  url: https://developer.bankoflondon.com/docs/guides/getting-started-guide
- group: start
  title: ''
  type: SignUp
  url: https://developer.bankoflondon.com/register
- group: start
  title: ''
  type: Login
  url: https://developer.bankoflondon.com/login
- group: operate
  title: ''
  type: Support
  url: https://www.bankoflondon.com/contact-us
- group: operate
  title: ''
  type: HelpCenter
  url: https://www.bankoflondon.com/faqs
- group: company
  title: ''
  type: Blog
  url: https://www.bankoflondon.com/newsroom
- group: commercial
  title: ''
  type: Pricing
  url: https://www.bankoflondon.com/regulated-financial-services
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.bankoflondon.com/legals/terms-of-use
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.bankoflondon.com/legals/privacy-policy
- group: operate
  title: ''
  type: StatusPage
  url: https://status.bankoflondon.com/
- group: commercial
  href: https://raw.githubusercontent.com/api-evangelist/the-bank-of-london/refs/heads/main/plans/the-bank-of-london-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/the-bank-of-london-plans-pricing.yml
- group: operate
  href: https://raw.githubusercontent.com/api-evangelist/the-bank-of-london/refs/heads/main/rate-limits/the-bank-of-london-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/the-bank-of-london-rate-limits.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/the-bank-of-london/refs/heads/main/authentication/the-bank-of-london-authentication.yml
  title: ''
  type: Authentication
  url: authentication/the-bank-of-london-authentication.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/the-bank-of-london/refs/heads/main/conventions/the-bank-of-london-conventions.yml
  title: ''
  type: Conventions
  url: conventions/the-bank-of-london-conventions.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/the-bank-of-london/refs/heads/main/conventions/the-bank-of-london-conventions.yml
  title: ''
  type: Idempotency
  url: conventions/the-bank-of-london-conventions.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/the-bank-of-london/refs/heads/main/lifecycle/the-bank-of-london-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/the-bank-of-london-lifecycle.yml
- group: operate
  href: https://raw.githubusercontent.com/api-evangelist/the-bank-of-london/refs/heads/main/lifecycle/the-bank-of-london-lifecycle.yml
  title: ''
  type: Deprecation
  url: lifecycle/the-bank-of-london-lifecycle.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/the-bank-of-london/refs/heads/main/errors/the-bank-of-london-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/the-bank-of-london-problem-types.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/the-bank-of-london/refs/heads/main/conformance/the-bank-of-london-conformance.yml
  title: ''
  type: Conformance
  url: conformance/the-bank-of-london-conformance.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/the-bank-of-london/refs/heads/main/conformance/the-bank-of-london-conformance.yml
  title: ''
  type: Compliance
  url: conformance/the-bank-of-london-conformance.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/the-bank-of-london/refs/heads/main/data-model/the-bank-of-london-data-model.yml
  title: ''
  type: DataModel
  url: data-model/the-bank-of-london-data-model.yml
- group: start
  href: https://raw.githubusercontent.com/api-evangelist/the-bank-of-london/refs/heads/main/sandbox/the-bank-of-london-sandbox.yml
  title: ''
  type: Sandbox
  url: sandbox/the-bank-of-london-sandbox.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/the-bank-of-london/refs/heads/main/asyncapi/the-bank-of-london-webhooks.yml
  title: ''
  type: Webhooks
  url: asyncapi/the-bank-of-london-webhooks.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/the-bank-of-london/refs/heads/main/packages/the-bank-of-london-packages.yml
  title: ''
  type: Packages
  url: packages/the-bank-of-london-packages.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/the-bank-of-london/refs/heads/main/llms/the-bank-of-london-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/the-bank-of-london-llms.txt
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/the-bank-of-london/refs/heads/main/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/the-bank-of-london/refs/heads/main/security/the-bank-of-london-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/the-bank-of-london-domain-security.yml
created: '2026-08-30'
description: The Bank of London (TBOL) is a UK principal clearing bank and Banking-as-a-Service provider, authorised by the Bank of England's Prudential Regulation Authority and regulated by the FCA and PRA (FRN 930379). Operating a "safer by design" model in which client deposits are never loaned, invested or leveraged, it offers clearing, payments and settlement, agency banking, embedded banking (BaaS) and commercial and corporate banking to banks, non-bank financial institutions, virtual-asset service providers, digital platforms, financial intermediaries and corporates. Its Developer Studio at developer.bankoflondon.com publishes a public OpenAPI 3.0.3 contract for the Bank of London API v2 covering accounts, customer onboarding, virtual account management, Confirmation of Payee, Faster Payments, Bacs, CHAPS, agency and cross-border payments, standing orders, direct-debit mandates, transactions, statements and webhooks, backed by a free open sandbox that requires no NDA. A separate PSD2
  / Open Banking UK v3.1 TPP interface is operated on the bank's behalf by Salt Edge Priora under provider code `tbol`.
image: https://cdn.prod.website-files.com/67ac63e504ea6d324d5e5a44/67ac8464295e3d604352cb63_256x256%20Webclip%20image.png
layout: provider
modified: '2026-08-30'
name: The Bank of London
nav: Providers
network: true
overview: 'The Bank of London publishes 10 APIs on the [APIs.io](https://apis.io/) network, including Accounts API, Confirmation of Payee API, Customer Management API, and 7 more. Tagged areas include Company, Banking, Clearing Bank, Payments, and Banking as a Service.


  The The Bank of London catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  The Bank of London''s developer surface includes documentation, API reference, getting-started guide, signup flow, support, engineering blog, pricing, and 25 more developer resources.'
plans:
- name: The Bank Of London Plans Pricing
  plan_count: 0
  slug: the-bank-of-london-plans-pricing
random_paper: 15
rate_limits:
- limit_count: 1
  name: The Bank Of London Rate Limits
  slug: the-bank-of-london-rate-limits
score:
  band: strong
  composite: 54.5
  coverage:
    artifact_dirs: 20
    catalog_earned: 45.0
    catalog_earned_first_party: 8.0
    catalog_gap: 70.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 2.3
  facets:
    access_clarity: 52.6
    contract_governance: 0.0
    contract_quality: 61.0
    developer_ergonomics: 66.1
    discoverability: 68.5
    operational_transparency: 52.6
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    countries:
    - united-kingdom
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
    regions:
    - europe
    - united-kingdom-ireland
  previous_composite: 52.2
  provenance:
    conformance: first-party
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 10
    mcp: derived
    skills: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Banking & Open Finance
    regime_id: banking_open_finance
    score: 48.1
  schema_version: 0.22.0
  scored_at: '2026-09-16'
  trend: flat
  upsert:
    applies: true
    score: 0.0
screenshot: https://raw.githubusercontent.com/api-evangelist/the-bank-of-london/refs/heads/main/screenshots/the-bank-of-london-2026-09-02T163320.png
security:
- kind: authentication
  name: The Bank Of London Authentication
  slug: the-bank-of-london-authentication
  summary_line: 1 scheme
- kind: domain-security
  name: The Bank Of London Domain Security
  slug: the-bank-of-london-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: the-bank-of-london
tags:
- Company
- Banking
- Clearing Bank
- Payments
- Banking as a Service
- Embedded Finance
- Open Banking
- PSD2
- Faster Payments
- Financial-Services
- United Kingdom
- Virtual Accounts
website: https://www.bankoflondon.com/
---
