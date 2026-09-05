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
    idempotency: false
    mcp_server: false
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 23.6
  scored_at: '2026-09-04'
api_count: 5
apis:
- description: Collect payments from customers in Africa via card, bank transfer, USSD, M-Pesa, mobile money and the Klasha wallet, including charge validation, refunds and exchange rates.
  name: Klasha Payments API
  slug: payments-api
- description: Send money locally to bank accounts and mobile money wallets across Africa and to China, with bank-code lookup, account resolution, wallet balances and Triple-DES encrypted transfer payloads.
  name: Klasha Payout API
  slug: payout-api
- description: Generate a quote and swap funds between merchant wallets using internal Klasha foreign-exchange rates, then fetch the resulting swap by reference or quote token.
  name: Klasha Swap API
  slug: swap-api
- description: Create virtual accounts on demand in NGN and GHS, receive customer funds through them, requery accounts, poll collection status and pull balances and statements.
  name: Klasha Virtual Account API
  slug: virtual-accounts-api
- description: Generate payment links for merchants and sub-merchants to collect payments without a code integration, from the dashboard or over the API.
  name: Klasha Payment Link API
  slug: payment-link-api
artifact_total: 9
asyncapis:
- description: ''
  name: Klasha Webhooks
  slug: klasha-webhooks
common:
- group: auth
  title: ''
  type: TrustCenter
  url: security/klasha-trust-center.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/klasha-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.klasha.com
- group: start
  title: ''
  type: DeveloperPortal
  url: https://developers.klasha.com/
- group: docs
  title: ''
  type: Documentation
  url: https://developers.klasha.com/
- group: docs
  title: ''
  type: APIReference
  url: https://developers.klasha.com/accepting-payments/payments-api
- group: start
  title: ''
  type: GettingStarted
  url: https://developers.klasha.com/integrating-klasha/getting-started
- group: operate
  title: ''
  type: Support
  url: https://support.klasha.com/
- group: start
  title: ''
  type: SignUp
  url: https://dashboard.klasha.com/signup
- group: start
  title: ''
  type: Login
  url: https://dashboard.klasha.com/auth/login
- group: company
  title: ''
  type: Blog
  url: https://www.klasha.com/blog
- group: operate
  title: ''
  type: Community
  url: https://join.slack.com/t/klashadev/shared_invite/zt-xnnmdpo0-5Dx6gNuj9b9oiQIuKvqYgw
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.klasha.com/legal#terms-and-conditions
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.klasha.com/legal#privacy-policy
- group: auth
  title: ''
  type: Security
  url: https://www.klasha.com/legal#information-security-policy
- group: auth
  title: ''
  type: Compliance
  url: https://www.klasha.com/compliance
- group: operate
  title: ''
  type: StatusPage
  url: https://status.klasha.com/
- group: build
  title: ''
  type: Postman
  url: https://www.postman.com/klasha-hq
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/klasha-apps
- group: auth
  title: ''
  type: Authentication
  url: authentication/klasha-authentication.yml
- group: build
  title: ''
  type: Packages
  url: packages/klasha-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/klasha-packages.yml
- group: design
  title: ''
  type: Components
  url: components/klasha-components.yml
- group: start
  title: ''
  type: Sandbox
  url: sandbox/klasha-sandbox.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/klasha-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/klasha-problem-types.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/klasha-lifecycle.yml
- group: design
  title: ''
  type: Webhooks
  url: asyncapi/klasha-webhooks.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/klasha-data-model.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/klasha-conformance.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/klasha-llms.txt
- group: agent
  title: ''
  type: X-MCPServerCandidate
  url: mcp/klasha-mcp.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
created: '2026-07-17'
description: Klasha is a cross-border payments company for emerging markets that lets international businesses sell into Africa and accept payments online in local African currencies. The Klasha platform covers payment collection (cards, bank transfer, USSD, M-Pesa and mobile money, Klasha wallet), payouts to bank accounts and mobile money wallets across Africa and to China, currency swap between merchant wallets at internal Klasha rates, virtual account creation for bank-account collection, payment links, and an embeddable JavaScript checkout. Developers integrate through the documented REST APIs at developers.klasha.com, the Klasha Inline JavaScript library, first-party web and mobile SDKs (Angular, React, Vue 2/3, iOS, Android, Flutter, Ionic, React Native), or ready-made e-commerce plugins for WooCommerce, Magento 2, BigCommerce, OpenCart, Ecwid, Wix and Weebly.
image: https://klasha.com/icon.svg
layout: provider
modified: '2026-07-19'
name: Klasha
nav: Providers
network: true
overview: 'Klasha publishes 5 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Payments, Cross-Border Payments, Africa, and Emerging Markets.


  The Klasha catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  Klasha''s developer surface includes documentation, API reference, getting-started guide, support, signup flow, engineering blog, authentication, and 26 more developer resources.'
random_paper: 19
score:
  band: strong
  composite: 54.3
  coverage:
    artifact_dirs: 17
    catalog_earned: 40.0
    catalog_earned_first_party: 0.0
    catalog_gap: 75.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 43.4
    commercial_clarity: 43.4
    contract_governance: 18.2
    contract_quality: 41.6
    developer_ergonomics: 73.2
    discoverability: 81.5
    governance: 18.2
    operational_transparency: 36.8
  previous_composite: 54.3
  provenance:
    conformance: first-party
    mcp: derived
    skills: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Payments
    regime_id: payments
    score: 68.8
  schema_version: 0.18.3
  scored_at: '2026-09-04'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/klasha/refs/heads/main/screenshots/klasha-2026-07-25T223937.png
security:
- kind: authentication
  name: Klasha Authentication
  slug: klasha-authentication
  summary_line: apiKey/http · 2 schemes
- kind: domain-security
  name: Klasha Domain Security
  slug: klasha-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: trust-center
  name: Klasha Trust Center
  slug: klasha-trust-center
  summary_line: ISO 27001, PCI DSS
slug: klasha
tags:
- Company
- Payments
- Cross-Border Payments
- Africa
- Emerging Markets
- Mobile Money
- Payouts
- Foreign Exchange
- Virtual Accounts
- Checkout
- Financial-Services
website: https://www.klasha.com
---
