---
access_model:
  confidence: medium
  label: Freemium
  onboarding: unknown
  pricing: freemium
  public: false
  source:
  - plans
  trial: false
  try_now: false
agent_readiness:
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: false
    agentic_commerce: false
    auth_clarity: negotiable
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: verified
    event_surface_described: derived
    idempotency: false
    mcp_server: false
    openapi_examples: partial
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 32.8
  scored_at: '2026-09-17'
api_count: 15
apis:
- baseURL: https://sandbox-api.novopayment.com/accounts/v1
  baseurl_source: declared
  description: NovoPayment offers the Accounts API to provide a customized, scalable, light and portable set of functionalities. These functionalities can be used by financial institutions for supporting banking act
  name: NovoPayment Accounts API
  slug: accounts
- baseURL: https://sandbox-api.novopayment.com/aliasdirectory/v1
  baseurl_source: declared
  description: The Alias Directory API enables a set of operations to store and manage users' information safely for sending funds between them. One of the main advantages of using NovoPayment's Alias Directory is t
  name: NovoPayment Alias Directory API
  slug: alias-directory
- baseURL: https://sandbox-api.novopayment.com/api/v1.3
  baseurl_source: declared
  description: Card Issuing, Switching, and Transaction Processing groups together the activities surrounding creating card programs, issuing cards to customers, managing those cards, and processing the transactions
  name: NovoPayment Cards API
  slug: cards
- baseURL: https://sandbox-api.novopayment.com/kyc/v1
  baseurl_source: declared
  description: The Compliance API allows you to validate the identity of the person who is registering in the system, with facial, document, and address verification among others. It is easy to implement and is appl
  name: NovoPayment Compliance API
  slug: compliance
- baseURL: https://sandbox-api.novopayment.com/customers/v1
  baseurl_source: declared
  description: The Customers API allows to handle the different type of customers that can be served by NovoPayment’s platform. This includes individuals, commercial and merchant customers. For most of the operation
  name: NovoPayment Customers API
  slug: customers
- baseURL: https://cert-api.novopayment.com
  baseurl_source: declared
  description: 'NovoPayment, as a Token Service Provider, has a collection of APIs that enables Issuers to participate in the Tokenization ecosystem; we are responsible for the interaction between the Issuer and the '
  name: NovoPayment Issuer Tokenization API
  slug: issuer-tokenization
- baseURL: https://[URLIssuer]/v2
  baseurl_source: declared
  description: Introduction NovoPayment, as a Token Service Provider, has a collection of APIs that enables Issuers to participate in the Tokenization ecosystem; we are responsible for the interaction between the Is
  name: NovoPayment MasterCard Tokenization API
  slug: mastercard-issuer-tokenization
- baseURL: https://sandbox-api.novopayment.com/api/v1/mpqr
  baseurl_source: declared
  description: 'Merchant Presented QR is a Service that includes payment or transactions process with tokens. A Registered Merchant on the service can expose a QR in the store, and the users of an Issuer´s Tokenized '
  name: NovoPayment Merchant Presented QR
  slug: merchant-presented-qr
- baseURL: https://sandbox-api.novopayment.com/oauth2/v1
  baseurl_source: declared
  description: '"The OAuth 2.0 authorization framework allows a third-party application to gain limited access to an HTTP service, either on behalf of the resource owner by orchestrating an approval interaction betwe'
  name: NovoPayment Security OAuth2 API
  slug: oauth2-data-encryption
- baseURL: https://sandbox-api.novopayment.com/onboarding/v1
  baseurl_source: declared
  description: The Onboarding API, groups together a pool of operations for the creation of a request for a digital bank account. Below operations are available for onboarding API Validate Identity Document. This op
  name: NovoPayment Onboarding API
  slug: onboarding
- baseURL: https://sandbox-api.novopayment.com/operations/v1
  baseurl_source: declared
  description: The transaction operations API can be used to generate the transactional operations that can be configured in an existing account or card program. Below operations are available for Transaction Operat
  name: NovoPayment Operations API
  slug: operations
- baseURL: https://sandbox-api.novopayment.com/paymentauthorizer/v1
  baseurl_source: declared
  description: The Payment Authorizer API enables the authorization process of a transaction from a payment gateway. In addition, this API can retrieve the details of a transaction and execute the reversal and refun
  name: NovoPayment Payment Authorizer API
  slug: payment-authorizer
- baseURL: https://sandbox-api.novopayment.com/profiles/v1
  baseurl_source: declared
  description: Below operations are available for Profile API Get Customer Configuration Parameters This operation allows to consult the different configurations of a customer. Customer Configuration Update This ope
  name: NovoPayment Profile API
  slug: profile
- baseURL: https://sandbox-api.novopayment.com/pushprovisioning/v1
  baseurl_source: declared
  description: Use Cases If you are a Bank that wants to give your customers the possibility to seamless register their debit and credit cards in payment platforms such as Apple Pay, Samsung Pay and Google Pay, as e
  name: NovoPayment Push Provisioning API
  slug: push-provisioning
- baseURL: https://sandbox-api.novopayment.com/realtimepayments/v1
  baseurl_source: declared
  description: The Real-time payments API leverage the newest technologies to pull/push payments amongst VISA or MasterCard branded products such as debit, prepaid, and credit cards to manage transactions between in
  name: NovoPayment Real-Time Payments API
  slug: real-time-payments
artifact_total: 22
asyncapis:
- description: ''
  name: Novopayment Webhooks
  slug: novopayment-webhooks
common:
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/novopayment/refs/heads/main/scopes/novopayment-scopes.yml
  title: ''
  type: OAuthScopes
  url: scopes/novopayment-scopes.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/novopayment/refs/heads/main/authentication/novopayment-authentication.yml
  title: ''
  type: Authentication
  url: authentication/novopayment-authentication.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/novopayment/refs/heads/main/security/novopayment-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/novopayment-domain-security.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/novopayment
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/novopayment_2/
- group: company
  title: ''
  type: Website
  url: https://novopayment.com/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://developer.novopayment.com/
- group: docs
  title: ''
  type: Documentation
  url: https://developer.novopayment.com/api
- group: docs
  title: ''
  type: APIReference
  url: https://developer.novopayment.com/api
- group: start
  title: ''
  type: GettingStarted
  url: https://developer.novopayment.com/guides/quick-start
- group: start
  title: ''
  type: SignUp
  url: https://developer.novopayment.com/user/register
- group: start
  title: ''
  type: Login
  url: https://developer.novopayment.com/user
- group: operate
  title: ''
  type: Support
  url: https://novopayment.com/contact/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://developer.novopayment.com/terms-and-conditions-use
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://developer.novopayment.com/privacy-policy
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/novopayment/refs/heads/main/packages/novopayment-packages.yml
  title: ''
  type: Packages
  url: packages/novopayment-packages.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/novopayment/refs/heads/main/packages/novopayment-packages.yml
  title: ''
  type: SDKs
  url: packages/novopayment-packages.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/novopayment/refs/heads/main/llms/novopayment-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/novopayment-llms.txt
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/novopayment/refs/heads/main/mcp/novopayment-mcp.yml
  title: ''
  type: X-MCPServerCandidate
  url: mcp/novopayment-mcp.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/novopayment/refs/heads/main/conformance/novopayment-conformance.yml
  title: ''
  type: Conformance
  url: conformance/novopayment-conformance.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/novopayment/refs/heads/main/conformance/novopayment-conformance.yml
  title: ''
  type: Compliance
  url: conformance/novopayment-conformance.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/novopayment/refs/heads/main/errors/novopayment-error-codes.yml
  title: ''
  type: ErrorCatalog
  url: errors/novopayment-error-codes.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/novopayment/refs/heads/main/errors/novopayment-decline-codes.yml
  title: ''
  type: DeclineCodes
  url: errors/novopayment-decline-codes.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/novopayment/refs/heads/main/lifecycle/novopayment-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/novopayment-lifecycle.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/novopayment/refs/heads/main/conventions/novopayment-conventions.yml
  title: ''
  type: Conventions
  url: conventions/novopayment-conventions.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/novopayment/refs/heads/main/data-model/novopayment-data-model.yml
  title: ''
  type: DataModel
  url: data-model/novopayment-data-model.yml
- group: start
  href: https://raw.githubusercontent.com/api-evangelist/novopayment/refs/heads/main/sandbox/novopayment-sandbox.yml
  title: ''
  type: Sandbox
  url: sandbox/novopayment-sandbox.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/novopayment/refs/heads/main/asyncapi/novopayment-webhooks.yml
  title: ''
  type: Webhooks
  url: asyncapi/novopayment-webhooks.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/novopayment/refs/heads/main/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: commercial
  href: https://raw.githubusercontent.com/api-evangelist/novopayment/refs/heads/main/plans/novopayment-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/novopayment-plans-pricing.yml
- group: operate
  href: https://raw.githubusercontent.com/api-evangelist/novopayment/refs/heads/main/rate-limits/novopayment-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/novopayment-rate-limits.yml
- group: commercial
  href: https://raw.githubusercontent.com/api-evangelist/novopayment/refs/heads/main/finops/novopayment-finops.yml
  title: ''
  type: FinOps
  url: finops/novopayment-finops.yml
created: '2025-02-17'
description: NovoPayment is a Miami-headquartered banking-as-a-service and embedded-finance platform serving banks, fintechs, retailers and payment companies across the Americas. Its developer hub publishes an OAuth2-secured REST API suite spanning six product families — Card Solutions, Digital Banking, Digital Acquiring, Digital Wallets, Payments and Tokenization — covering card issuing and processing, digital account opening, KYC and compliance checks, customer and profile management, alias directories, real-time P2P payments, merchant-presented QR acceptance, payment authorization, and Visa/Mastercard token service provisioning including push provisioning to Apple Pay, Google Pay and Samsung Pay. Access runs through a self-service sandbox, with UAT and production promoted by request after project review.
finops:
- name: Novopayment Finops
  service_category: API
  slug: novopayment-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/novopayment.png
layout: provider
modified: '2026-09-17'
name: NovoPayment
nav: Providers
network: true
overview: 'NovoPayment publishes 15 APIs on the [APIs.io](https://apis.io/) network, including Accounts API, Alias Directory API, Cards API, and 12 more. Tagged areas include Payments, Banking as a Service, Embedded Finance, Card Issuing, and Digital Wallet.


  The NovoPayment catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  NovoPayment''s developer surface includes authentication, documentation, API reference, getting-started guide, signup flow, support, sandbox, and 25 more developer resources.'
plans:
- name: Novopayment Plans Pricing
  plan_count: 0
  slug: novopayment-plans-pricing
random_paper: 6
rate_limits:
- limit_count: 0
  name: Novopayment Rate Limits
  slug: novopayment-rate-limits
scopes:
- name: Novopayment Scopes
  scope_count: 0
  slug: novopayment-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: strong
  composite: 58.9
  coverage:
    artifact_dirs: 23
    catalog_earned: 43.0
    catalog_earned_first_party: 0.0
    catalog_gap: 72.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 48.4
  facets:
    access_clarity: 50.0
    contract_governance: 18.2
    contract_quality: 57.7
    developer_ergonomics: 70.8
    discoverability: 81.5
    operational_transparency: 10.5
  previous_composite: 10.5
  provenance:
    conformance: first-party
    contracts:
      callable: 93.3
      derived: 0
      marker_coverage: 0.0
      total: 15
    mcp: derived
    skills: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Payments
    regime_id: payments
    score: 68.8
  schema_version: 0.22.0
  scored_at: '2026-09-17'
  trend: rising
  upsert:
    applies: true
    score: 38.9
screenshot: https://raw.githubusercontent.com/api-evangelist/novopayment/refs/heads/main/screenshots/novopayment-2026-06-20T190444.png
security:
- kind: authentication
  name: Novopayment Authentication
  slug: novopayment-authentication
  summary_line: oauth2 · 1 scheme
- kind: domain-security
  name: Novopayment Domain Security
  slug: novopayment-domain-security
  summary_line: TLSv1.3 · DMARC
slug: novopayment
tags:
- Payments
- Banking as a Service
- Embedded Finance
- Card Issuing
- Digital Wallet
- Tokenization
- Real-Time Payments
- Onboarding
- KYC
- Latin America
- Fintech
- Digital Banking
website: https://novopayment.com/
---
