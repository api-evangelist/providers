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
    agent_skills: derived
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: verified
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
  score: 28.2
  scored_at: '2026-09-04'
agentic_access:
- acting_count: 34
  human_in_the_loop: 2
  name: Spare Agentic Access
  operation_count: 99
  slug: spare-agentic-access
  summary_line: 99 operations · 34 acting · 2 human-in-the-loop
api_count: 7
apis:
- baseURL: https://ob.tryspare.com/api/v1.0/authentication
  baseurl_source: declared
  description: The Account API from Spare — 4 operation(s) for account.
  name: Spare Account API
  slug: spare-account-api
- baseURL: https://ob.tryspare.com/api/v1.0/authentication
  baseurl_source: declared
  description: The AccountInformationReport API from Spare — 5 operation(s) for accountinformationreport.
  name: Spare AccountInformationReport API
  slug: spare-accountinformationreport-api
- baseURL: https://ob.tryspare.com/api/v1.0/authentication
  baseurl_source: declared
  description: The Balance API from Spare — 3 operation(s) for balance.
  name: Spare Balance API
  slug: spare-balance-api
- baseURL: https://ob.tryspare.com/api/v1.0/authentication
  baseurl_source: declared
  description: The Beneficiary API from Spare — 1 operation(s) for beneficiary.
  name: Spare Beneficiary API
  slug: spare-beneficiary-api
- baseURL: https://ob.tryspare.com/api/v1.0/authentication
  baseurl_source: declared
  description: The Cert API from Spare — 1 operation(s) for cert.
  name: Spare Cert API
  slug: spare-cert-api
- baseURL: https://ob.tryspare.com/api/v1.0/authentication
  baseurl_source: declared
  description: The Connection API from Spare — 4 operation(s) for connection.
  name: Spare Connection API
  slug: spare-connection-api
- baseURL: https://ob.tryspare.com/api/v1.0/authentication
  baseurl_source: declared
  description: The Consent API from Spare — 9 operation(s) for consent.
  name: Spare Consent API
  slug: spare-consent-api
- baseURL: https://ob.tryspare.com/api/v1.0/authentication
  baseurl_source: declared
  description: The Customer API from Spare — 5 operation(s) for customer.
  name: Spare Customer API
  slug: spare-customer-api
- baseURL: https://ob.tryspare.com/api/v1.0/authentication
  baseurl_source: declared
  description: The DirectDebit API from Spare — 1 operation(s) for directdebit.
  name: Spare DirectDebit API
  slug: spare-directdebit-api
- baseURL: https://ob.tryspare.com/api/v1.0/authentication
  baseurl_source: declared
  description: The Parties API from Spare — 1 operation(s) for parties.
  name: Spare Parties API
  slug: spare-parties-api
- baseURL: https://ob.tryspare.com/api/v1.0/authentication
  baseurl_source: declared
  description: The Payment API from Spare — 2 operation(s) for payment.
  name: Spare Payment API
  slug: spare-payment-api
- baseURL: https://ob.tryspare.com/api/v1.0/authentication
  baseurl_source: declared
  description: The Provider API from Spare — 2 operation(s) for provider.
  name: Spare Provider API
  slug: spare-provider-api
- baseURL: https://ob.tryspare.com/api/v1.0/authentication
  baseurl_source: declared
  description: The Request API from Spare — 11 operation(s) for request.
  name: Spare Request API
  slug: spare-request-api
- baseURL: https://ob.tryspare.com/api/v1.0/authentication
  baseurl_source: declared
  description: The RiskReport API from Spare — 6 operation(s) for riskreport.
  name: Spare RiskReport API
  slug: spare-riskreport-api
- baseURL: https://ob.tryspare.com/api/v1.0/authentication
  baseurl_source: declared
  description: The Statement API from Spare — 1 operation(s) for statement.
  name: Spare Statement API
  slug: spare-statement-api
- baseURL: https://ob.tryspare.com/api/v1.0/authentication
  baseurl_source: declared
  description: The Token API from Spare — 2 operation(s) for token.
  name: Spare Token API
  slug: spare-token-api
- baseURL: https://ob.tryspare.com/api/v1.0/authentication
  baseurl_source: declared
  description: The Transaction API from Spare — 5 operation(s) for transaction.
  name: Spare Transaction API
  slug: spare-transaction-api
artifact_total: 41
asyncapis:
- description: ''
  name: Spare Webhooks
  slug: spare-webhooks
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Information Account API
  slug: open-spare-account-api
- collection_type: open
  name: Information Account AccountInformationReport API
  slug: open-spare-accountinformationreport-api
- collection_type: open
  name: Information Account Balance API
  slug: open-spare-balance-api
- collection_type: open
  name: Information Account Beneficiary API
  slug: open-spare-beneficiary-api
- collection_type: open
  name: Information Account Cert API
  slug: open-spare-cert-api
- collection_type: open
  name: Information Account Connection API
  slug: open-spare-connection-api
- collection_type: open
  name: Information Account Consent API
  slug: open-spare-consent-api
- collection_type: open
  name: Information Account Customer API
  slug: open-spare-customer-api
- collection_type: open
  name: Information Account DirectDebit API
  slug: open-spare-directdebit-api
- collection_type: open
  name: Information Account Parties API
  slug: open-spare-parties-api
- collection_type: open
  name: Information Account Payment API
  slug: open-spare-payment-api
- collection_type: open
  name: Information Account Provider API
  slug: open-spare-provider-api
- collection_type: open
  name: Information Account Request API
  slug: open-spare-request-api
- collection_type: open
  name: Information Account RiskReport API
  slug: open-spare-riskreport-api
- collection_type: open
  name: Information Account Statement API
  slug: open-spare-statement-api
- collection_type: open
  name: Information Account Token API
  slug: open-spare-token-api
- collection_type: open
  name: Information Account Transaction API
  slug: open-spare-transaction-api
common:
- group: other
  title: ''
  type: CapabilityMap
  url: capabilities/spare-capability-edges.yml
- group: other
  title: ''
  type: Overlay
  url: overlays/spare-bahrain-ais-overlay.yaml
- group: auth
  title: ''
  type: TrustCenter
  url: security/spare-trust-center.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/spare-domain-security.yml
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/spare-agentic-access.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/spare-authentication.yml
- group: company
  title: ''
  type: Website
  url: https://tryspare.com
- group: start
  title: ''
  type: DeveloperPortal
  url: https://docs.tryspare.com/docs/welcome
- group: docs
  title: ''
  type: Documentation
  url: https://docs.tryspare.com/docs/welcome
- group: docs
  title: ''
  type: APIReference
  url: https://docs.tryspare.com/reference
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.tryspare.com/docs/auth-flow
- group: operate
  title: ''
  type: Support
  url: https://docs.tryspare.com/docs/support
- group: company
  title: ''
  type: Blog
  url: https://tryspare.com/blog
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/spare-technologies
- group: start
  title: ''
  type: SignUp
  url: https://dashboard.sandbox.tryspare.com/
- group: start
  title: ''
  type: Login
  url: https://dashboard.tryspare.com/
- group: build
  title: ''
  type: Postman
  url: https://documenter.getpostman.com/view/39844099/2sB2ixku9E
- group: commercial
  title: ''
  type: TermsOfService
  url: https://terms.tryspare.com/sa/en
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://terms.tryspare.com/sa/privacy/en
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/spare-llms.txt
- group: build
  title: ''
  type: Packages
  url: packages/spare-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/spare-packages.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/spare-scopes.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/spare-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/spare-error-codes.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/spare-lifecycle.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/spare-conformance.yml
- group: auth
  title: ''
  type: Compliance
  url: https://trust.tryspare.com/
- group: start
  title: ''
  type: Sandbox
  url: sandbox/spare-sandbox.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/spare-data-model.yml
- group: agent
  title: ''
  type: X-MCPServerCandidate
  url: mcp/spare-mcp.yml
- group: design
  title: ''
  type: Webhooks
  url: asyncapi/spare-webhooks.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
created: '2026-07-17'
description: Spare is a MENA-region open banking and open finance platform, licensed by the Central Bank of Bahrain as an Account Information Service Provider and Payment Initiation Service Provider (AISP/PISP) and permitted to test under the Saudi Central Bank (SAMA) regulatory sandbox. Spare exposes RESTful Account Information Services (AIS) — account details, balances, transactions, statements, beneficiaries, parties, direct debits, plus risk and affordability reports — and Payment Initiation Services (PIS) for domestic single, future-dated and standing-order payments, across separate Bahrain, KSA and UAE tenants hosted in-region for data-residency compliance. Developers authenticate with OAuth2 client credentials to obtain signed JWT bearer tokens, drive a customer to connection to consent to data flow, verify token and webhook signatures against a published JWKS, and integrate via official TypeScript, Java, .NET and PHP SDKs plus Postman collections.
image: https://files.readme.io/91c2031-small-Spare-logo-white3x.png
layout: provider
modified: '2026-07-21'
name: Spare
nav: Providers
network: true
overview: 'Spare publishes 17 APIs on the [APIs.io](https://apis.io/) network, including Account API, AccountInformationReport API, Balance API, and 14 more. Tagged areas include Open Banking, Open Finance, Account Information, Payment Initiation, and AISP.


  The Spare catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  Spare''s developer surface includes authentication, documentation, API reference, getting-started guide, support, engineering blog, signup flow, and 26 more developer resources.'
random_paper: 14
scopes:
- name: Spare Scopes
  scope_count: 0
  slug: spare-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: developing
  composite: 53.2
  coverage:
    artifact_dirs: 22
    catalog_earned: 40.0
    catalog_earned_first_party: 0.0
    catalog_gap: 75.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 43.4
    commercial_clarity: 43.4
    contract_governance: 4.5
    contract_quality: 58.3
    developer_ergonomics: 78.0
    discoverability: 81.5
    governance: 4.5
    operational_transparency: 10.5
  previous_composite: 53.2
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 17
    mcp: derived
    skills: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Banking & Open Finance
    regime_id: banking_open_finance
    score: 59.5
  schema_version: 0.18.3
  scored_at: '2026-09-04'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/spare/refs/heads/main/screenshots/spare-2026-08-17T082018.png
security:
- kind: authentication
  name: Spare Authentication
  slug: spare-authentication
  summary_line: oauth2/apiKey · 1 scheme
- kind: domain-security
  name: Spare Domain Security
  slug: spare-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
- kind: trust-center
  name: Spare Trust Center
  slug: spare-trust-center
  summary_line: SOC 2, ISO 27001
slug: spare
tags:
- Open Banking
- Open Finance
- Account Information
- Payment Initiation
- AISP
- PISP
- Consent
- Bank Data
- Transaction
- Balances
- Payments
- Fintech
- MENA
- Saudi Arabia
- Bahrain
- UAE
website: https://tryspare.com
---
