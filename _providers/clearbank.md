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
  band: agent-ready
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
    idempotency: documented
    mcp_server: false
    openapi_examples: partial
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 35.7
  scored_at: '2026-09-04'
agentic_access:
- acting_count: 29
  human_in_the_loop: 0
  name: Clearbank Agentic Access
  operation_count: 31
  slug: clearbank-agentic-access
  summary_line: 31 operations · 29 acting
api_count: 11
apis:
- baseURL: https://institution-api.clearbank.co.uk
  baseurl_source: declared
  description: The Accounts API from ClearBank — 2 operation(s) for accounts.
  name: ClearBank Accounts API
  slug: clearbank-accounts-api
- baseURL: https://institution-api.clearbank.co.uk
  baseurl_source: declared
  description: The CoP API from ClearBank — 1 operation(s) for cop.
  name: ClearBank Co P API
  slug: clearbank-cop-api
- baseURL: https://institution-api.clearbank.co.uk
  baseurl_source: declared
  description: The CreateFxQuoteEndpoint API from ClearBank — 1 operation(s) for createfxquoteendpoint.
  name: ClearBank Create Fx Quote Endpoint API
  slug: clearbank-createfxquoteendpoint-api
- baseURL: https://institution-api.clearbank.co.uk
  baseurl_source: declared
  description: The Customer API from ClearBank — 6 operation(s) for customer.
  name: ClearBank Customer API
  slug: clearbank-customer-api
- baseURL: https://institution-api.clearbank.co.uk
  baseurl_source: declared
  description: The Customer Due Diligence API from ClearBank — 1 operation(s) for customer due diligence.
  name: ClearBank Customer Due Diligence API
  slug: clearbank-customer-due-diligence-api
- baseURL: https://institution-api.clearbank.co.uk
  baseurl_source: declared
  description: The ExternalCrossBorderCustomerPaymentsV4 API from ClearBank — 1 operation(s) for externalcrossbordercustomerpaymentsv4.
  name: ClearBank External Cross Border Customer Payments V4 API
  slug: clearbank-externalcrossbordercustomerpaymentsv4-api
- baseURL: https://institution-api.clearbank.co.uk
  baseurl_source: declared
  description: The ExternalCustomerPaymentsV6 API from ClearBank — 1 operation(s) for externalcustomerpaymentsv6.
  name: ClearBank External Customer Payments V6 API
  slug: clearbank-externalcustomerpaymentsv6-api
- baseURL: https://institution-api.clearbank.co.uk
  baseurl_source: declared
  description: The ExternalInstitutionPaymentsV6 API from ClearBank — 1 operation(s) for externalinstitutionpaymentsv6.
  name: ClearBank External Institution Payments V6 API
  slug: clearbank-externalinstitutionpaymentsv6-api
- baseURL: https://institution-api.clearbank.co.uk
  baseurl_source: declared
  description: The ExternalReturnPaymentsV6 API from ClearBank — 1 operation(s) for externalreturnpaymentsv6.
  name: ClearBank External Return Payments V6 API
  slug: clearbank-externalreturnpaymentsv6-api
- baseURL: https://institution-api.clearbank.co.uk
  baseurl_source: declared
  description: The FpsPayments API from ClearBank — 2 operation(s) for fpspayments.
  name: ClearBank Fps Payments API
  slug: clearbank-fpspayments-api
- baseURL: https://institution-api.clearbank.co.uk
  baseurl_source: declared
  description: The Fx Orders API from ClearBank — 1 operation(s) for fx orders.
  name: ClearBank Fx Orders API
  slug: clearbank-fx-orders-api
- baseURL: https://institution-api.clearbank.co.uk
  baseurl_source: declared
  description: The Payments API from ClearBank — 3 operation(s) for payments.
  name: ClearBank Payments API
  slug: clearbank-payments-api
- baseURL: https://institution-api.clearbank.co.uk
  baseurl_source: declared
  description: The Retail API from ClearBank — 2 operation(s) for retail.
  name: ClearBank Retail API
  slug: clearbank-retail-api
- baseURL: https://institution-api.clearbank.co.uk
  baseurl_source: declared
  description: The SCT Payments API from ClearBank — 4 operation(s) for sct payments.
  name: ClearBank SCT Payments API
  slug: clearbank-sct-payments-api
- baseURL: https://institution-api.clearbank.co.uk
  baseurl_source: declared
  description: The SecondaryReferenceData API from ClearBank — 1 operation(s) for secondaryreferencedata.
  name: ClearBank Secondary Reference Data API
  slug: clearbank-secondaryreferencedata-api
artifact_total: 31
asyncapis:
- description: ''
  name: Clearbank Webhooks
  slug: clearbank-webhooks
collections:
- collection_type: open
  name: ClearBank CHAPS RTGS FI API V6
  slug: open-clearbank-chaps-v6
- collection_type: open
  name: ClearBank.CoP.Outbound.Api 1.0
  slug: open-clearbank-cop-outbound-v1
- collection_type: open
  name: ClearBank Cross-Border Sterling FI API V4
  slug: open-clearbank-cross-border-v4
- collection_type: open
  name: ClearBank Retail Customer V2 APIs
  slug: open-clearbank-customers_v2_retail
- collection_type: open
  name: FI Initiation API 3.0
  slug: open-clearbank-fps-initiate-payment-v3
- collection_type: open
  name: FX Orchestrator API
  slug: open-clearbank-fx-orchestrator-rfq
- collection_type: open
  name: Customer Due Diligence API
  slug: open-clearbank-know-your-customer-v1
- collection_type: open
  name: Accounts API
  slug: open-clearbank-mccy-accounts-v2
- collection_type: open
  name: Mccy Payment Orchestrator External Api V1
  slug: open-clearbank-mccy-payments-v1
- collection_type: open
  name: ClearBank.Sepa.Ct.Orchestrator.Api
  slug: open-clearbank-sepa-ct-v1
- collection_type: open
  name: ClearBank Financial Institutions API
  slug: open-clearbank-sterling-v4
common:
- group: other
  title: ''
  type: CapabilityMap
  url: capabilities/clearbank-capability-edges.yml
- group: agent
  title: ''
  type: X-MCPServerCandidate
  url: mcp/clearbank-mcp.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/clearbank-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/clearbank-domain-security.yml
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/clearbank-agentic-access.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/clearbank-authentication.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/clearbank-conventions.yml
- group: design
  title: ''
  type: Idempotency
  url: conventions/clearbank-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/clearbank-problem-types.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/clearbank-lifecycle.yml
- group: operate
  title: ''
  type: StatusPage
  url: https://clearbank.statuspage.io/
- group: operate
  title: ''
  type: Deprecation
  url: https://clearbank.github.io/uk/docs/api/support-life-cycle
- group: start
  title: ''
  type: Sandbox
  url: sandbox/clearbank-sandbox.yml
- group: design
  title: ''
  type: Webhooks
  url: asyncapi/clearbank-webhooks.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/clearbank-conformance.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/clearbank-data-model.yml
- group: build
  title: ''
  type: Packages
  url: packages/clearbank-packages.yml
- group: build
  title: ''
  type: Postman
  url: https://github.com/clearbank/fi-api-postman
- group: agent
  title: ''
  type: WellKnown
  url: well-known/clearbank-well-known.yml
- group: auth
  title: ''
  type: SecurityTxt
  url: well-known/clearbank-security.txt
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/clearbank-llms.txt
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: other
  title: ''
  type: Overlay
  url: overlays/clearbank-sterling-v4-overlay.yaml
- group: other
  title: ''
  type: Overlay
  url: overlays/clearbank-fps-initiate-payment-v3-overlay.yaml
- group: other
  title: ''
  type: Overlay
  url: overlays/clearbank-chaps-v6-overlay.yaml
- group: other
  title: ''
  type: Overlay
  url: overlays/clearbank-cross-border-v4-overlay.yaml
- group: other
  title: ''
  type: Overlay
  url: overlays/clearbank-mccy-accounts-v2-overlay.yaml
- group: other
  title: ''
  type: Overlay
  url: overlays/clearbank-mccy-payments-v1-overlay.yaml
- group: other
  title: ''
  type: Overlay
  url: overlays/clearbank-fx-orchestrator-rfq-overlay.yaml
- group: other
  title: ''
  type: Overlay
  url: overlays/clearbank-sepa-ct-v1-overlay.yaml
- group: other
  title: ''
  type: Overlay
  url: overlays/clearbank-cop-outbound-v1-overlay.yaml
- group: other
  title: ''
  type: Overlay
  url: overlays/clearbank-know-your-customer-v1-overlay.yaml
- group: other
  title: ''
  type: Overlay
  url: overlays/clearbank-customers_v2_retail-overlay.yaml
- group: company
  title: ''
  type: Website
  url: https://www.clear.bank/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://clearbank.github.io/
- group: docs
  title: ''
  type: Documentation
  url: https://clearbank.github.io/uk/docs/api/
- group: start
  title: ''
  type: GettingStarted
  url: https://clearbank.github.io/uk/docs/api/getting-started/
- group: docs
  title: ''
  type: APIReference
  url: https://clear.bank/explore-our-api
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/clearbank
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/clearbank
- group: company
  title: ''
  type: Blog
  url: https://clear.bank/newsroom
- group: auth
  title: ''
  type: Security
  url: https://clear.bank/security
- group: commercial
  title: ''
  type: TermsOfService
  url: https://clear.bank/legal/terms-and-conditions
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://clear.bank/data-protection-and-privacy
created: '2026-07-23'
description: ClearBank is a UK clearing and Banking-as-a-Service bank, founded in 2015 by Nick Ogden (founder of WorldPay) and Charles McManus and granted a banking licence in December 2016 as the first new UK clearing bank in more than 250 years. ClearBank Limited is authorised by the Prudential Regulation Authority and regulated by the Financial Conduct Authority and the Prudential Regulation Authority (FRN 754568), with a European subsidiary, ClearBank Europe N.V., authorised by the European Central Bank. It is privately owned, backed by Apax Partners and PPF Group. Built cloud-native on Microsoft Azure, ClearBank is a direct participant in the UK payment schemes (Faster Payments, CHAPS, Bacs) and offers Agency Banking, Embedded Banking, and Transaction Banking to banks, fintechs, and corporates through a single proprietary JSON REST API. Unlike the CMA9 retail banks, ClearBank is not a mandated Open Banking ASPSP and does not publish the OBIE Open Data (ATMs/Branches/Products) or OBIE
  Read/Write (AISP/PISP/CBPII) APIs; its public developer surface is the token-authenticated, RSA-signed ClearBank Financial Institutions API covering GBP accounts and payments, multi-currency accounts, FX, SEPA, cross-border payments, Confirmation of Payee, customer due diligence (KYC), and embedded/retail banking, with a full simulation environment for onboarding.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/apis-json-logo.jpg
layout: provider
modified: '2026-07-23'
name: ClearBank
nav: Providers
network: true
overview: 'ClearBank publishes 15 APIs on the [APIs.io](https://apis.io/) network, including Accounts API, Co P API, Create Fx Quote Endpoint API, and 12 more. Tagged areas include Financial-Services, Banking, Banking as a Service, Embedded Banking, and Payments.


  The ClearBank catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  ClearBank''s developer surface includes authentication, sandbox, documentation, getting-started guide, API reference, engineering blog, and 38 more developer resources.'
random_paper: 7
score:
  band: developing
  composite: 45.1
  coverage:
    artifact_dirs: 21
    catalog_earned: 40.0
    catalog_earned_first_party: 0.0
    catalog_gap: 75.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 21.1
    commercial_clarity: 21.1
    contract_governance: 4.5
    contract_quality: 48.5
    developer_ergonomics: 61.3
    discoverability: 81.5
    governance: 4.5
    operational_transparency: 44.7
  previous_composite: 45.1
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 0.0
      derived: 0
      marker_coverage: 0.0
      total: 15
    mcp: derived
    skills: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Banking & Open Finance
    regime_id: banking_open_finance
    score: 44.3
  schema_version: 0.18.3
  scored_at: '2026-09-04'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/clearbank/refs/heads/main/screenshots/clearbank-2026-07-25T205542.png
security:
- kind: authentication
  name: Clearbank Authentication
  slug: clearbank-authentication
  summary_line: http/custom-signature · 3 schemes
- kind: domain-security
  name: Clearbank Domain Security
  slug: clearbank-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
- kind: vulnerability-disclosure
  name: Clearbank Vulnerability Disclosure
  slug: clearbank-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: clearbank
tags:
- Financial-Services
- Banking
- Banking as a Service
- Embedded Banking
- Payments
- Clearing
- Faster Payments
- CHAPS
- Multi-Currency
- Foreign Exchange
- Open Banking
- United Kingdom
- Fintech
website: https://www.clear.bank/
---
