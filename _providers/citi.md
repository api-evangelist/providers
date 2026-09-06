---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source: []
  trial: false
  try_now: false
agent_readiness:
  band: agent-native
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: false
    agentic_commerce: false
    auth_clarity: negotiable
    consent_identity: false
    delegated_identity: documented
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: verified
    event_surface_described: true
    idempotency: verified
    mcp_server: false
    openapi_examples: verified
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: verified
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 49.8
  scored_at: '2026-09-05'
api_count: 118
apis:
- baseURL: https://tts.apib2b.citi.com/citiconnect/prod
  baseurl_source: declared
  description: OAuth 2.0 token issuance for every Citi institutional API. Four concurrent versions (V1-V4) of the authentication endpoint are published; each product API's own specification names the version it requ
  name: Citi API Authentication Services
  slug: citi-api-authentication-services
- baseURL: https://tts.apib2b.citi.com/citiconnect/prod/accountstatementservices
  baseurl_source: declared
  description: 'Real-time and intraday account information across Citi''s global network: balance inquiry, prior-day and intraday statements (ISO 20022 camt), account services, account statement blocks and filters, an'
  name: Citi Account Reporting APIs
  slug: citi-account-reporting-apis
- baseURL: https://tts.apib2b.citi.com/citiconnect/prod/paymentservices/v3
  baseurl_source: declared
  description: 'Payment initiation, status, cancellation, refund, enhanced inquiry, reconfirmation, bulk payments, instant/express payments and WorldLink cross-border payouts. Message bodies are ISO 20022 (pain.001, '
  name: Citi Outgoing Payments APIs
  slug: citi-outgoing-payments-apis
- baseURL: https://tts.apib2b.citi.com/citiconnect/prod
  baseurl_source: declared
  description: 'Collections and payment acceptance: online payment acceptance, direct debit and e-mandates, PayerID management, Brazil PIX dynamic and due-date collections, and instant direct debit. Citi publishes 10'
  name: Citi Payment Acceptance APIs
  slug: citi-payment-acceptance-apis
- baseURL: https://tts.apib2b.citi.com/tts/cards
  baseurl_source: declared
  description: Virtual Card Account lifecycle, mobile virtual cards, payment-intermediary VCA management, authorization notifications and webhooks, clearing exception reporting, purchase template details, mobile wal
  name: Citi Commercial Cards and Virtual Card Accounts APIs
  slug: citi-commercial-cards-and-virtual-card-accounts-apis
- baseURL: https://api.citivelocity.com/markets
  baseurl_source: declared
  description: Foreign exchange quoting, order placement, order cancellation and reporting over the CitiFX Gateway and Instant FX services, each published in matched synchronous and asynchronous variants, plus a FIX
  name: CitiFX Gateway and Instant FX APIs
  slug: citifx-gateway-and-instant-fx-apis
- baseURL: https://api.citivelocity.com/markets/dod
  baseurl_source: declared
  description: 'Custody and securities servicing: safekeeping accounts and positions, cash balances and transactions, securities transactions, custody penalties, tax reclaims, FX transactions, billing, and ETF order '
  name: Citi Custody and Securities Services APIs
  slug: citi-custody-and-securities-services-apis
- baseURL: https://b2b.api.icg.citi.com/citiconnect/prod/iis/api/funds/transferagency
  baseurl_source: declared
  description: Fund transfer agency data for investors, accounts, holdings and transactions, served through the CitiConnect institutional investor services gateway. Citi publishes 4 machine-readable specifications f
  name: Citi Funds Transfer Agency APIs
  slug: citi-funds-transfer-agency-apis
- baseURL: https://b2b.tts.icgservices.citi.com/citiconnect/openbanking/ukr/accountconsentservices/v1
  baseurl_source: declared
  description: 'Regulated open banking surfaces: Ukraine bank data sharing, Ukraine OAuth2 authentication and payment service initiation, and European commercial card account balance and statement transaction inquiry'
  name: Citi Open Banking APIs
  slug: citi-open-banking-apis
- baseURL: https://tts.apib2b.citi.com/citiconnect/prod
  baseurl_source: declared
  description: 'Trade finance over a lightweight message exchange interface: standby letters of credit, trade finance undertakings, amendment and cancellation, and receivables finance. Citi publishes 2 machine-readab'
  name: CitiConnect Trade Services APIs
  slug: citiconnect-trade-services-apis
- baseURL: https://b2b.api.icg.citi.com/citiconnect/prod/gatewayservices
  baseurl_source: declared
  description: 'Marketplace and gateway management for CitiConnect: onboarding, entitlement and configuration operations used to administer a client''s API estate. Citi publishes 1 machine-readable specification for t'
  name: Citi Gateway Services API
  slug: citi-gateway-services-api
- baseURL: https://tts.apib2b.citi.com/citiconnect/prod/selfservices/v1
  baseurl_source: declared
  description: 'Payment-adjacent services: beneficiary account validation and search, entity whitelisting, self-service integration operations, and Request to Pay. Citi publishes 4 machine-readable specifications for'
  name: Citi Additional Payment Services APIs
  slug: citi-additional-payment-services-apis
artifact_total: 20
asyncapis:
- description: ''
  name: Citi Webhooks
  slug: citi-webhooks
common:
- group: company
  title: ''
  type: Website
  url: https://www.citi.com
- group: start
  title: ''
  type: DeveloperPortal
  url: https://developer.citi.com/apis/marketplace
- group: start
  title: ''
  type: Portal
  url: https://partner.citi.com/developers
- group: docs
  title: ''
  type: Documentation
  url: https://developer.citi.com/apidocs/
- group: docs
  title: ''
  type: APIReference
  url: https://developer.citi.com/apidocs/
- group: start
  title: ''
  type: GettingStarted
  url: https://developer.citi.com/apidocs/authentication/authentication-only-guide
- group: start
  title: ''
  type: SignUp
  url: https://partner.citi.com/user/register
- group: start
  title: ''
  type: Login
  url: https://partner.citi.com/user/login
- group: operate
  title: ''
  type: Support
  url: https://partner.citi.com/contact-us
- group: commercial
  title: ''
  type: TermsOfService
  url: https://partner.citi.com/legal/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://partner.citi.com/legal/privacy-policy
- group: company
  title: ''
  type: Blog
  url: https://www.citigroup.com/global/news
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/citi
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/citi
- group: start
  title: ''
  type: Sandbox
  url: sandbox/citi-sandbox.yml
- group: docs
  title: ''
  type: Documentation
  url: https://www.citigroup.com/global/insights/citiconnect-api-portal
- group: auth
  title: ''
  type: Authentication
  url: authentication/citi-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/citi-scopes.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/citi-conventions.yml
- group: design
  title: ''
  type: Idempotency
  url: conventions/citi-conventions.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/citi-conformance.yml
- group: auth
  title: ''
  type: Compliance
  url: conformance/citi-conformance.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/citi-problem-types.yml
- group: build
  title: ''
  type: DeclineCodes
  url: errors/citi-decline-codes.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/citi-lifecycle.yml
- group: operate
  title: ''
  type: Deprecation
  url: lifecycle/citi-lifecycle.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/citi-data-model.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/citi-rate-limits.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/citi-plans-pricing.yml
- group: build
  title: ''
  type: Packages
  url: packages/citi-packages.yml
- group: design
  title: ''
  type: Webhooks
  url: asyncapi/citi-webhooks.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/citi-llms.txt
- group: agent
  title: ''
  type: MCPServer
  url: mcp/citi-mcp.yml
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/citi-changelog.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/citi-domain-security.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/citi-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: Security
  url: https://www.citi.com/reporting-vulnerability
created: '2026-03-21'
description: 'Citi is the consumer and institutional brand of Citigroup, serving over 200 million customers across 160 countries. Citi runs one of the largest published API estates in banking: 118 machine-readable OpenAPI and Swagger contracts covering 297 operations are served from developer.citi.com across payment initiation and status, payment acceptance and collections, account reporting and statements, commercial cards and virtual card accounts, CitiFX Gateway and Instant FX, custody and securities services, funds transfer agency, trade services, open banking and gateway services. The payment estate is ISO 20022 native: pain.001, pacs.008, pacs.009 and camt.056 message types are declared inside the contracts themselves, in matched JSON and XML encodings. Authentication is OAuth 2.0 client-credentials over mutual TLS with message-level PKI signing. A sandbox estate is declared in the contracts; production access is relationship-managed through Citi sales.'
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/citi.png
layout: provider
mcp_servers:
- description: ''
  name: Citi MCP Server
  slug: citi-mcp-server
modified: '2026-09-05'
name: Citi
nav: Providers
network: true
overview: 'Citi publishes 12 APIs on the [APIs.io](https://apis.io/) network, including API Authentication Services, Account Reporting APIs, Outgoing Payments APIs, and 9 more. Tagged areas include Banking, Financial-Services, Open Banking, Payments, and Treasury.


  The Citi catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  Citi''s developer surface includes developer portal, documentation, API reference, getting-started guide, signup flow, support, engineering blog, and 31 more developer resources.'
plans:
- name: Citi Plans Pricing
  plan_count: 0
  slug: citi-plans-pricing
random_paper: 5
rate_limits:
- limit_count: 0
  name: Citi Rate Limits
  slug: citi-rate-limits
scopes:
- name: Citi Scopes
  scope_count: 24
  slug: citi-scopes
  summary_line: 24 scopes · clientCredentials/authorizationCode
score:
  band: strong
  composite: 60.1
  coverage:
    artifact_dirs: 21
    catalog_earned: 40.0
    catalog_earned_first_party: 0.0
    catalog_gap: 75.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 56.4
  facets:
    access_clarity: 42.1
    commercial_clarity: 42.1
    contract_governance: 4.5
    contract_quality: 66.5
    developer_ergonomics: 66.1
    discoverability: 74.1
    governance: 4.5
    operational_transparency: 44.7
  previous_composite: 3.7
  provenance:
    conformance: derived
    contracts:
      callable: 91.3
      derived: 0
      marker_coverage: 0.0
      total: 118
    mcp: derived
    skills: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Banking & Open Finance
    regime_id: banking_open_finance
    score: 84.8
  schema_version: 0.18.3
  scored_at: '2026-09-05'
  trend: rising
screenshot: https://raw.githubusercontent.com/api-evangelist/citi/refs/heads/main/screenshots/citi-2026-06-20T174409.png
security:
- kind: authentication
  name: Citi Authentication
  slug: citi-authentication
  summary_line: apiKey/http/oauth2/unknown · 10 schemes
- kind: domain-security
  name: Citi Domain Security
  slug: citi-domain-security
  summary_line: TLSv1.2 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Citi Vulnerability Disclosure
  slug: citi-vulnerability-disclosure
  summary_line: Bugcrowd
slug: citi
tags:
- Banking
- Financial-Services
- Open Banking
- Payments
- Treasury
- ISO 20022
- Commercial Cards
- Foreign Exchange
- Custody
- Trade Finance
- Corporate Banking
- API Gateway
website: https://www.citi.com
---
