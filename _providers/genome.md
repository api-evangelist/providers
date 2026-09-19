---
access_model:
  confidence: high
  label: Per-transaction pricing, risk-classified; API access follows merchant account approval
  onboarding: unknown
  pricing: unknown
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
    agentic_access: derived
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
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 31.1
  scored_at: '2026-09-18'
agentic_access:
- acting_count: 2
  human_in_the_loop: 0
  name: Genome Agentic Access
  operation_count: 2
  slug: genome-agentic-access
  summary_line: 2 operations · 2 acting
api_count: 1
apis:
- description: The Genome merchant payments programme as a whole — hosted payment pages, host-to-host card processing, payouts, reporting and the PSD2 dedicated interface, all documented at developers.genome.eu.
  name: Genome
  slug: genome
- baseURL: https://api.genome.eu
  baseurl_source: declared
  description: Direct card processing. One endpoint dispatching eight transaction types — AUTH, AUTH3D, SALE, SALE3D, SETTLE, REFUND, VOID and CHECK — accepting form-encoded or JSON bodies.
  name: Genome Host-to-Host API
  slug: genome-host-to-host-api
- baseURL: https://api.genome.eu
  baseurl_source: declared
  description: Send funds to cardholders using full card data or a tokenized card. The synchronous response is pending; the final status arrives on the merchant callback. No reversal operation exists.
  name: Genome Payouts API
  slug: genome-payouts-api
- description: SEPA credit transfer payouts by IBAN, with a companion transaction-status surface. Amounts can be read including or excluding the SEPA payout fee. No OpenAPI is published for this surface.
  name: Genome SEPA Payout API
  slug: genome-sepa-payout-api
- description: Historical transaction and chargeback reporting over a required unix time window, paged by page and limit with a 1,000-record page ceiling. No OpenAPI is published for this surface.
  name: Genome Query on Demand API
  slug: genome-query-on-demand-api
- description: Check a SEPA beneficiary's name or identifier against the account before sending a payment. Returns the EPC VOP scheme outcomes — match, close match, no match, no applicable — with a suggested payee n
  name: Genome Verification of Payee API
  slug: genome-verification-of-payee-api
- description: Berlin Group NextGenPSD2 dedicated interface. Account Information Services, Payment Initiation Services for SEPA credit transfers, and Confirmation of Funds, secured with OAuth 2.0, Strong Customer Au
  name: Genome PSD2 API
  slug: genome-psd2-api
- description: Redirect checkout hosted by Genome, opened with an HS256 JWT signed with the SHA-256 digest of the payment page secret. Keeps card data out of merchant scope. Supports card and Pay by Bank.
  name: Genome Hosted Payment Page
  slug: genome-hosted-payment-page
artifact_total: 20
asyncapis:
- description: ''
  name: Genome Webhooks
  slug: genome-webhooks
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Genome Payments Host-to-Host API
  slug: open-genome-host-to-host-api
- collection_type: open
  name: Genome Payments Host-to-Host Payouts API
  slug: open-genome-payouts-api
- collection_type: open
  name: Genome Payments API
  slug: open-genome
common:
- group: company
  title: ''
  type: Website
  url: https://genome.eu/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://developers.genome.eu/
- group: docs
  title: ''
  type: Documentation
  url: https://developers.genome.eu/
- group: docs
  title: ''
  type: APIReference
  url: https://gateway.genome.eu/help/cc
- group: start
  title: ''
  type: GettingStarted
  url: https://developers.genome.eu/merchants/hosted-payment-page/
- group: operate
  title: ''
  type: Support
  url: https://support.genome.eu/hc/en-us/
- group: company
  title: ''
  type: Blog
  url: https://blog.genome.eu
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/genome-eu
- group: commercial
  title: ''
  type: Pricing
  url: https://genome.eu/low-risk-merchant-account-pricing/
- group: start
  title: ''
  type: SignUp
  url: https://my.genome.eu/signup
- group: commercial
  title: ''
  type: TermsOfService
  url: https://genome.eu/merchant-terms-of-use/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://genome.eu/privacy-notice/
- group: operate
  title: ''
  type: StatusPage
  url: https://status.genome.eu
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/genome-europe/
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/genome/refs/heads/main/authentication/genome-authentication.yml
  title: ''
  type: Authentication
  url: authentication/genome-authentication.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/genome/refs/heads/main/conventions/genome-conventions.yml
  title: ''
  type: Conventions
  url: conventions/genome-conventions.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/genome/refs/heads/main/conventions/genome-conventions.yml
  title: ''
  type: Idempotency
  url: conventions/genome-conventions.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/genome/refs/heads/main/errors/genome-error-codes.yml
  title: ''
  type: ErrorCatalog
  url: errors/genome-error-codes.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/genome/refs/heads/main/errors/genome-decline-codes.yml
  title: ''
  type: DeclineCodes
  url: errors/genome-decline-codes.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/genome/refs/heads/main/asyncapi/genome-webhooks.yml
  title: ''
  type: Webhooks
  url: asyncapi/genome-webhooks.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/genome/refs/heads/main/lifecycle/genome-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/genome-lifecycle.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/genome/refs/heads/main/conformance/genome-conformance.yml
  title: ''
  type: Conformance
  url: conformance/genome-conformance.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/genome/refs/heads/main/conformance/genome-conformance.yml
  title: ''
  type: Compliance
  url: conformance/genome-conformance.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/genome/refs/heads/main/security/genome-trust-center.yml
  title: ''
  type: TrustCenter
  url: security/genome-trust-center.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/genome/refs/heads/main/security/genome-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/genome-domain-security.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/genome/refs/heads/main/packages/genome-packages.yml
  title: ''
  type: Packages
  url: packages/genome-packages.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/genome/refs/heads/main/packages/genome-packages.yml
  title: ''
  type: SDKs
  url: packages/genome-packages.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/genome/refs/heads/main/components/genome-components.yml
  title: ''
  type: Components
  url: components/genome-components.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/genome/refs/heads/main/data-model/genome-data-model.yml
  title: ''
  type: DataModel
  url: data-model/genome-data-model.yml
- group: start
  href: https://raw.githubusercontent.com/api-evangelist/genome/refs/heads/main/sandbox/genome-sandbox.yml
  title: ''
  type: Sandbox
  url: sandbox/genome-sandbox.yml
- group: commercial
  href: https://raw.githubusercontent.com/api-evangelist/genome/refs/heads/main/plans/genome-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/genome-plans-pricing.yml
- group: operate
  href: https://raw.githubusercontent.com/api-evangelist/genome/refs/heads/main/rate-limits/genome-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/genome-rate-limits.yml
- group: commercial
  href: https://raw.githubusercontent.com/api-evangelist/genome/refs/heads/main/finops/genome-finops.yml
  title: ''
  type: FinOps
  url: finops/genome-finops.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/genome/refs/heads/main/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/genome/refs/heads/main/llms/genome-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/genome-llms.txt
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/genome/refs/heads/main/agentic-access/genome-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/genome-agentic-access.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/genome/refs/heads/main/mcp/genome-mcp.yml
  title: ''
  type: X-MCPServerCandidate
  url: mcp/genome-mcp.yml
created: '2025-03-01'
description: 'Genome, operated by UAB "Maneuver LT" of Vilnius, is an Electronic Money Institution licensed and supervised by the Bank of Lithuania. It runs multi-currency personal and business accounts, issues Visa cards, and sells a merchant payments stack that is documented as six public API surfaces: the Host-to-Host API for direct card processing (AUTH, AUTH3D, SALE, SALE3D, SETTLE, REFUND, VOID and CHECK), the Payout API for sending funds to cardholders, the SEPA Payout API, the Query on Demand reporting API, a Verification of Payee API returning the EPC scheme''s match outcomes, and a Berlin Group NextGenPSD2 dedicated interface offered free of charge to registered AISPs and PISPs. Batch transfers are submitted as ISO 20022 pain.001.001.03. Outcomes are carried in a proprietary 137-code response envelope rather than HTTP status codes, and Genome publishes no OpenAPI, AsyncAPI, MCP server or /.well-known/ document on any of its hosts.'
finops:
- name: Genome Finops
  service_category: API
  slug: genome-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/genome.png
layout: provider
modified: '2026-09-12'
name: Genome
nav: Providers
network: true
overview: 'Genome publishes 2 APIs on the [APIs.io](https://apis.io/) network: Host-to-Host API and Payouts API. Tagged areas include Finance, Payments, Banking, Open Banking, and PSD2.


  The Genome catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  Genome''s developer surface includes documentation, API reference, getting-started guide, support, engineering blog, pricing, signup flow, and 30 more developer resources.'
plans:
- name: Genome Plans Pricing
  plan_count: 3
  slug: genome-plans-pricing
random_paper: 19
rate_limits:
- limit_count: 0
  name: Genome Rate Limits
  slug: genome-rate-limits
score:
  band: strong
  composite: 57.5
  coverage:
    artifact_dirs: 25
    catalog_earned: 52.0
    catalog_earned_first_party: 12.0
    catalog_gap: 63.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 86.8
    contract_governance: 0.0
    contract_quality: 59.7
    developer_ergonomics: 73.2
    discoverability: 68.5
    operational_transparency: 26.3
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
    regions:
    - europe
  previous_composite: 57.5
  provenance:
    agentic_access: derived
    conformance: first-party
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 2
    mcp: derived
    skills: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Banking & Open Finance
    regime_id: banking_open_finance
    score: 38.0
  schema_version: 0.22.0
  scored_at: '2026-09-18'
  trend: flat
  upsert:
    applies: true
    score: 0.0
screenshot: https://raw.githubusercontent.com/api-evangelist/genome/refs/heads/main/screenshots/genome-2026-06-20T181737.png
security:
- kind: authentication
  name: Genome Authentication
  slug: genome-authentication
  summary_line: 7 schemes
- kind: domain-security
  name: Genome Domain Security
  slug: genome-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: trust-center
  name: Genome Trust Center
  slug: genome-trust-center
  summary_line: ISO/IEC 27001:2022, ISO/IEC 27701:2019, PCI DSS
slug: genome
tags:
- Finance
- Payments
- Banking
- Open Banking
- PSD2
- SEPA
- Card Processing
- Payouts
- Electronic Money Institution
- Europe
website: https://genome.eu/
---
