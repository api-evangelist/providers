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
    agent_skills: false
    agentic_access: derived
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
    rate_limit_signal: false
    reversibility_documented: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 37.7
  scored_at: '2026-10-17'
agentic_access:
- acting_count: 43
  human_in_the_loop: 0
  name: Finmid Agentic Access
  operation_count: 65
  slug: finmid-agentic-access
  summary_line: 65 operations · 43 acting
api_count: 2
apis:
- description: 'Embed B2B payment and financing into a platform: onboard buyers and sellers, create payment requests financed by a finmid loan, create payouts, upload documents, and track repayment. JSON over HTTPS, '
  name: finmid B2B Payments API
  slug: finmid-b2b-payments-api-2
- description: 'Offer pre-approved, customizable financing to businesses on a platform: real-time offer generation, an embeddable acceptance widget (iframe), business onboarding and KYB, fundings, and business paymen'
  name: finmid Capital API
  slug: finmid-capital-api-2
- baseURL: https://api.finmid.com
  baseurl_source: declared
  description: The Beta Endpoints API from Finmid — 1 operation(s) for beta endpoints.
  name: Finmid Beta Endpoints API
  slug: finmid-beta-endpoints-api
- baseURL: https://api.finmid.com
  baseurl_source: declared
  description: The Business API from Finmid — 6 operation(s) for business.
  name: Finmid Business API
  slug: finmid-business-api
- baseURL: https://api.finmid.com
  baseurl_source: declared
  description: The Buyer API from Finmid — 4 operation(s) for buyer.
  name: Finmid Buyer API
  slug: finmid-buyer-api
- baseURL: https://api.finmid.com
  baseurl_source: declared
  description: Endpoints for managing Capital Max applications.
  name: Finmid Capital Max API
  slug: finmid-capital-max-api
- baseURL: https://api.finmid.com
  baseurl_source: declared
  description: The CSP Financial Document API from Finmid — 4 operation(s) for csp financial document.
  name: Finmid CSP Financial Document API
  slug: finmid-csp-financial-document-api
- baseURL: https://api.finmid.com
  baseurl_source: declared
  description: The Document API from Finmid — 2 operation(s) for document.
  name: Finmid Document API
  slug: finmid-document-api
- baseURL: https://api.finmid.com
  baseurl_source: declared
  description: The Funding API from Finmid — 2 operation(s) for funding.
  name: Finmid Funding API
  slug: finmid-funding-api
- baseURL: https://api.finmid.com
  baseurl_source: declared
  description: Endpoints for managing Funding Applications.
  name: Finmid Funding Application API
  slug: finmid-funding-application-api
- baseURL: https://api.finmid.com
  baseurl_source: declared
  description: The Incoming Webhook API from Finmid — 2 operation(s) for incoming webhook.
  name: Finmid Incoming Webhook API
  slug: finmid-incoming-webhook-api
- baseURL: https://api.finmid.com
  baseurl_source: declared
  description: The Offer API from Finmid — 4 operation(s) for offer.
  name: Finmid Offer API
  slug: finmid-offer-api
- baseURL: https://api.finmid.com
  baseurl_source: declared
  description: The Offer Group API from Finmid — 3 operation(s) for offer group.
  name: Finmid Offer Group API
  slug: finmid-offer-group-api
- baseURL: https://api.finmid.com
  baseurl_source: declared
  description: The Onboarding API from Finmid — 1 operation(s) for onboarding.
  name: Finmid Onboarding API
  slug: finmid-onboarding-api
- baseURL: https://api.finmid.com
  baseurl_source: declared
  description: The Payment API from Finmid — 4 operation(s) for payment.
  name: Finmid Payment API
  slug: finmid-payment-api
- baseURL: https://api.finmid.com
  baseurl_source: declared
  description: The Payment Request API from Finmid — 6 operation(s) for payment request.
  name: Finmid Payment Request API
  slug: finmid-payment-request-api
- baseURL: https://api.finmid.com
  baseurl_source: declared
  description: The Sales statements API from Finmid — 1 operation(s) for sales statements.
  name: Finmid Sales statements API
  slug: finmid-sales-statements-api
- baseURL: https://api.finmid.com
  baseurl_source: declared
  description: The Seller API from Finmid — 4 operation(s) for seller.
  name: Finmid Seller API
  slug: finmid-seller-api
- baseURL: https://api.finmid.com
  baseurl_source: declared
  description: The Simulation API from Finmid — 17 operation(s) for simulation.
  name: Finmid Simulation API
  slug: finmid-simulation-api
- baseURL: https://api.finmid.com
  baseurl_source: declared
  description: The Tasks API from Finmid — 2 operation(s) for tasks.
  name: Finmid Tasks API
  slug: finmid-tasks-api
artifact_total: 25
asyncapis:
- description: ''
  name: Finmid Webhooks
  slug: finmid-webhooks
common:
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/finmid/refs/heads/main/agentic-access/finmid-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/finmid-agentic-access.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/finmid/refs/heads/main/rules/finmid-rules.yml
  title: ''
  type: Spectral
  url: rules/finmid-rules.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/finmid/refs/heads/main/vocabulary/finmid-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/finmid-vocabulary.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/finmid/refs/heads/main/errors/finmid-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/finmid-problem-types.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/finmid/refs/heads/main/hosts/finmid-hosts.yml
  title: ''
  type: Hosts
  url: hosts/finmid-hosts.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/finmid/refs/heads/main/vendors/finmid-vendors.yml
  title: ''
  type: Vendors
  url: vendors/finmid-vendors.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/finmid/refs/heads/main/security/finmid-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/finmid-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.finmid.com
- group: start
  title: ''
  type: DeveloperPortal
  url: https://docs.finmid.com
- group: docs
  title: ''
  type: Documentation
  url: https://docs.finmid.com
- group: docs
  title: ''
  type: APIReference
  url: https://docs.finmid.com/reference/api-introduction
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.finmid.com/docs/finmid-products
- group: company
  title: ''
  type: Blog
  url: https://finmid.com/blog/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/finmid
- group: start
  title: ''
  type: SignUp
  url: https://platform.finmid.com
- group: start
  title: ''
  type: Login
  url: https://platform.finmid.com
- group: operate
  title: ''
  type: Support
  url: mailto:support@finmid.com
- group: commercial
  title: ''
  type: TermsOfService
  url: https://finmid.com/legal/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://finmid.com/privacy/
- group: operate
  title: ''
  type: StatusPage
  url: https://finmid.statuspage.io
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/finmid/refs/heads/main/lifecycle/finmid-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/finmid-lifecycle.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/finmid/refs/heads/main/llms/finmid-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/finmid-llms.txt
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/finmid/refs/heads/main/authentication/finmid-authentication.yml
  title: ''
  type: Authentication
  url: authentication/finmid-authentication.yml
- group: start
  href: https://raw.githubusercontent.com/api-evangelist/finmid/refs/heads/main/sandbox/finmid-sandbox.yml
  title: ''
  type: Sandbox
  url: sandbox/finmid-sandbox.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/finmid/refs/heads/main/errors/finmid-error-codes.yml
  title: ''
  type: ErrorCatalog
  url: errors/finmid-error-codes.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/finmid/refs/heads/main/asyncapi/finmid-webhooks.yml
  title: ''
  type: Webhooks
  url: asyncapi/finmid-webhooks.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/finmid/refs/heads/main/conventions/finmid-conventions.yml
  title: ''
  type: Conventions
  url: conventions/finmid-conventions.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/finmid/refs/heads/main/components/finmid-components.yml
  title: ''
  type: Components
  url: components/finmid-components.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/finmid/refs/heads/main/conformance/finmid-conformance.yml
  title: ''
  type: Conformance
  url: conformance/finmid-conformance.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/finmid/refs/heads/main/mcp/finmid-mcp.yml
  title: ''
  type: X-MCPServerCandidate
  url: mcp/finmid-mcp.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/finmid/refs/heads/main/data-model/finmid-data-model.yml
  title: ''
  type: DataModel
  url: data-model/finmid-data-model.yml
created: '2026-07-17'
description: 'finmid is a Berlin-based embedded lending and B2B payments infrastructure provider that lets software platforms and marketplaces offer financing — cash advances, term loans, and business loans — to their customers across 30+ European markets without becoming a lender or handling the regulatory complexity themselves. finmid exposes two REST APIs: the B2B Payments API (buyer/seller onboarding, payment requests, payouts, and repayment) and the Capital API (pre-approved offer generation, an embeddable acceptance widget, business onboarding/KYB, fundings, and payments). Both APIs are JSON over HTTPS, authenticated with an environment-scoped X-API-Key header, with a separate sandbox environment, HMAC-signed webhooks for asynchronous events, and HTTP Message Signatures (RFC 9421, Ed25519) for platform-provided capital payout execution.'
image: https://finmid.com/icon-192x192.png
layout: provider
modified: '2026-07-19'
name: Finmid
nav: Providers
network: true
overview: 'Finmid publishes 20 API contracts indexed on the [APIs.io](https://apis.io/) network, including Beta Endpoints API, Business API, Buyer API, and 17 more. Tagged areas include Company, Embedded Finance, Embedded Lending, B2B Payments, and Fintech.


  The Finmid catalog on APIs.io includes 1 event-driven AsyncAPI specification and 1 Spectral governance ruleset.


  Finmid''s developer surface includes documentation, API reference, getting-started guide, engineering blog, signup flow, support, authentication, and 24 more developer resources.'
random_paper: 15
rules:
- authorship: generated
  effective_rule_count: 55
  extends:
  - spectral:oas
  name: Finmid API Rules
  rule_count: 14
  severity_counts:
    error: 10
    hint: 0
    info: 1
    warn: 3
  slug: finmid-rules
score:
  band: developing
  composite: 44.2
  coverage:
    artifact_dirs: 23
    catalog_earned: 42.8
    catalog_earned_first_party: 0.0
    catalog_gap: 72.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 9.3
  facets:
    access_clarity: 21.1
    contract_governance: 22.0
    contract_quality: 57.3
    developer_ergonomics: 48.8
    discoverability: 73.2
    operational_transparency: 22.4
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    countries:
    - germany
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
    regions:
    - dach
    - europe
  previous_composite: 34.9
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 100.0
      total: 18
    mcp: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Payments
    regime_id: payments
    score: 25.9
  schema_version: 0.24.0
  scored_at: '2026-10-17'
  trend: rising
  upsert:
    applies: true
    score: 27.8
screenshot: https://raw.githubusercontent.com/api-evangelist/finmid/refs/heads/main/screenshots/finmid-2026-07-25T214532.png
security:
- kind: authentication
  name: Finmid Authentication
  slug: finmid-authentication
  summary_line: apiKey/httpMessageSignatures · 2 schemes
- kind: domain-security
  name: Finmid Domain Security
  slug: finmid-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: finmid
tags:
- Company
- Embedded Finance
- Embedded Lending
- B2B Payments
- Fintech
- Lending
- Capital
- Financing
- Payments
- Marketplace
website: https://www.finmid.com
---
