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
  band: agent-native
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
    error_semantics: verified
    event_surface_described: true
    idempotency: verified
    mcp_server: verified
    openapi_examples: partial
    protected_resource_metadata: false
    rate_limit_signal: verified
    reversibility_documented: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 51.7
  scored_at: '2026-10-17'
agentic_access:
- acting_count: 237
  human_in_the_loop: 9
  name: Hihealth Agentic Access
  operation_count: 357
  slug: hihealth-agentic-access
  summary_line: 357 operations · 237 acting · 9 human-in-the-loop
api_count: 2
apis:
- description: The embedded credit-card API that powers hi.health. Partners issue and manage cards, cardholders, transactions, receipts, payments, statements and external transfers, with OAuth2 client-credentials au
  name: Pliant Cards-as-a-Service (CaaS) API
  slug: pliant-cards-as-a-service-caas-api
- description: The customer-facing Pro API for programmatic access to Pliant credit-card data and features (cards, cardholders, transactions, receipts, accounting, payments).
  name: Pliant Pro API
  slug: pliant-pro-api
- baseURL: https://partner-api.getpliant.com/api/
  baseurl_source: declared
  description: Create and revoke a shareable access link for a card. The person who opens the link does not need a Pliant account.
  name: hi.health Access Links API
  slug: hihealth-access-links-api
- baseURL: https://partner-api.getpliant.com/api/
  baseurl_source: declared
  description: This tag is for operations related to account entries
  name: hi.health Account Entries API
  slug: hihealth-account-entries-api
- baseURL: https://partner-api.getpliant.com/api/
  baseurl_source: declared
  description: This tag is for operations related to accounting projects
  name: hi.health Accounting Projects API
  slug: hihealth-accounting-projects-api
- baseURL: https://partner-api.getpliant.com/api/
  baseurl_source: declared
  description: This tag is for operations related to accounting teams
  name: hi.health Accounting Teams API
  slug: hihealth-accounting-teams-api
- baseURL: https://partner-api.getpliant.com/api/
  baseurl_source: declared
  description: This tag is for operations related to accounting transactions
  name: hi.health Accounting Transactions API
  slug: hihealth-accounting-transactions-api
- baseURL: https://partner-api.getpliant.com/api/
  baseurl_source: declared
  description: This tag is for operations related to beneficiaries
  name: hi.health Beneficiaries API
  slug: hihealth-beneficiaries-api
- baseURL: https://partner-api.getpliant.com/api/
  baseurl_source: declared
  description: This tag is for operations related to callbacks
  name: hi.health Callbacks API
  slug: hihealth-callbacks-api
- baseURL: https://partner-api.getpliant.com/api/
  baseurl_source: declared
  description: This tag is for operations related to card accounts
  name: hi.health Card Accounts API
  slug: hihealth-card-accounts-api
- baseURL: https://partner-api.getpliant.com/api/
  baseurl_source: declared
  description: This tag is for operations related to card controls
  name: hi.health Card Controls API
  slug: hihealth-card-controls-api
- baseURL: https://partner-api.getpliant.com/api/
  baseurl_source: declared
  description: This tag is for operations related to card copilots
  name: hi.health Card Copilots API
  slug: hihealth-card-copilots-api
- baseURL: https://partner-api.getpliant.com/api/
  baseurl_source: declared
  description: This tag is for operations related to card limit requests
  name: hi.health Card Limit Requests API
  slug: hihealth-card-limit-requests-api
- baseURL: https://partner-api.getpliant.com/api/
  baseurl_source: declared
  description: This tag is for operations related to card requests
  name: hi.health Card Requests API
  slug: hihealth-card-requests-api
- baseURL: https://partner-api.getpliant.com/api/
  baseurl_source: declared
  description: This tag is for operations related to card sensitive data
  name: hi.health Card Sensitive Data API
  slug: hihealth-card-sensitive-data-api
- baseURL: https://partner-api.getpliant.com/api/
  baseurl_source: declared
  description: This tag is for operations related to cardholders
  name: hi.health Cardholders API
  slug: hihealth-cardholders-api
- baseURL: https://partner-api.getpliant.com/api/
  baseurl_source: declared
  description: This tag is for operations related to cards
  name: hi.health Cards API
  slug: hihealth-cards-api
- baseURL: https://partner-api.getpliant.com/api/
  baseurl_source: declared
  description: This tag is for operations related to cashback
  name: hi.health Cashback API
  slug: hihealth-cashback-api
- baseURL: https://partner-api.getpliant.com/api/
  baseurl_source: declared
  description: This tag is for operations related to custom fields
  name: hi.health Custom Fields API
  slug: hihealth-custom-fields-api
- baseURL: https://partner-api.getpliant.com/api/
  baseurl_source: declared
  description: This tag is for operations related to external transfers
  name: hi.health External Transfers API
  slug: hihealth-external-transfers-api
- baseURL: https://partner-api.getpliant.com/api/
  baseurl_source: declared
  description: This tag is for operations related to identity verification
  name: hi.health Identity Verification API
  slug: hihealth-identity-verification-api
- baseURL: https://partner-api.getpliant.com/api/
  baseurl_source: declared
  description: This tag is for miscellaneous operations
  name: hi.health Misc API
  slug: hihealth-misc-api
- baseURL: https://partner-api.getpliant.com/api/
  baseurl_source: declared
  description: This tag is for operations related to mobile wallet tokenization
  name: hi.health Mobile Wallet Tokenization API
  slug: hihealth-mobile-wallet-tokenization-api
- baseURL: https://partner-api.getpliant.com/api/
  baseurl_source: declared
  description: This tag is for operations related to onboarding submissions, including submission lifecycle management, validation, callbacks, and reference data
  name: hi.health Onboarding Submissions API
  slug: hihealth-onboarding-submissions-api
- baseURL: https://partner-api.getpliant.com/api/
  baseurl_source: declared
  description: This tag is for operations related to organizations
  name: hi.health Organizations API
  slug: hihealth-organizations-api
- baseURL: https://partner-api.getpliant.com/api/
  baseurl_source: declared
  description: This tag is for operations related to payments
  name: hi.health Payments API
  slug: hihealth-payments-api
- baseURL: https://partner-api.getpliant.com/api/
  baseurl_source: declared
  description: This tag is for operations related to receipt automatching
  name: hi.health Receipt Automatching API
  slug: hihealth-receipt-automatching-api
- baseURL: https://partner-api.getpliant.com/api/
  baseurl_source: declared
  description: This tag is for operations related to receipts
  name: hi.health Receipts API
  slug: hihealth-receipts-api
- baseURL: https://partner-api.getpliant.com/api/
  baseurl_source: declared
  description: This tag is for operations related to statements
  name: hi.health Statements API
  slug: hihealth-statements-api
- baseURL: https://partner-api.getpliant.com/api/
  baseurl_source: declared
  description: This tag is for operations related to test data generation
  name: hi.health Test Data Generator (Sandbox-only) API
  slug: hihealth-test-data-generator-sandbox-only-api
- baseURL: https://partner-api.getpliant.com/api/
  baseurl_source: declared
  description: This tag is for operations related to transactions
  name: hi.health Transactions API
  slug: hihealth-transactions-api
- baseURL: https://partner-api.getpliant.com/api/
  baseurl_source: declared
  description: This tag is for operations related to Verification of Payee (VoP) — name-check service mandatory under the SEPA Instant Payments Regulation
  name: hi.health Verification of Payee API
  slug: hihealth-verification-of-payee-api
artifact_total: 48
asyncapis:
- description: ''
  name: Hihealth Webhooks
  slug: hihealth-webhooks
common:
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/hihealth/refs/heads/main/agentic-access/hihealth-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/hihealth-agentic-access.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/hihealth/refs/heads/main/rules/hihealth-rules.yml
  title: ''
  type: Spectral
  url: rules/hihealth-rules.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/hihealth/refs/heads/main/json-ld/hihealth-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/hihealth-context.jsonld
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/hihealth/refs/heads/main/vocabulary/hihealth-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/hihealth-vocabulary.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/hihealth/refs/heads/main/data-model/hihealth-data-model.yml
  title: ''
  type: DataModel
  url: data-model/hihealth-data-model.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/hihealth/refs/heads/main/conventions/hihealth-conventions.yml
  title: ''
  type: Idempotency
  url: conventions/hihealth-conventions.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/hihealth/refs/heads/main/hosts/hihealth-hosts.yml
  title: ''
  type: Hosts
  url: hosts/hihealth-hosts.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/hihealth/refs/heads/main/vendors/hihealth-vendors.yml
  title: ''
  type: Vendors
  url: vendors/hihealth-vendors.yml
- group: company
  title: ''
  type: Newsroom
  url: https://www.getpliant.com/en/press
- group: company
  title: ''
  type: Blog
  url: https://getpliant.com/en/blog
- group: commercial
  title: ''
  type: Pricing
  url: https://getpliant.com/en/pricing
- group: start
  title: ''
  type: SignUp
  url: https://app.getpliant.com/?language=en
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://getpliant.com/en/privacy-policy
- group: commercial
  title: ''
  type: TermsOfService
  url: https://getpliant.com/en/imprint
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/getpliant
- group: company
  title: ''
  type: Website
  url: https://www.getpliant.com/en/industry/insurance-payments/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://partner.getpliant.com/
- group: docs
  title: ''
  type: Documentation
  url: https://partner.getpliant.com/
- group: docs
  title: ''
  type: APIReference
  url: https://partner.getpliant.com/reference
- group: start
  title: ''
  type: GettingStarted
  url: https://partner.getpliant.com/docs/introduction.md
- group: operate
  title: ''
  type: Support
  url: https://help.getpliant.com/
- group: operate
  title: ''
  type: StatusPage
  url: https://help.getpliant.com/
- group: operate
  title: ''
  type: Deprecation
  url: https://partner.getpliant.com/docs/versioning.md
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/hihealth/refs/heads/main/authentication/hihealth-authentication.yml
  title: ''
  type: Authentication
  url: authentication/hihealth-authentication.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/hihealth/refs/heads/main/scopes/hihealth-scopes.yml
  title: ''
  type: OAuthScopes
  url: scopes/hihealth-scopes.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/hihealth/refs/heads/main/conventions/hihealth-conventions.yml
  title: ''
  type: Conventions
  url: conventions/hihealth-conventions.yml
- group: operate
  href: https://raw.githubusercontent.com/api-evangelist/hihealth/refs/heads/main/rate-limits/hihealth-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/hihealth-rate-limits.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/hihealth/refs/heads/main/errors/hihealth-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/hihealth-problem-types.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/hihealth/refs/heads/main/lifecycle/hihealth-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/hihealth-lifecycle.yml
- group: start
  href: https://raw.githubusercontent.com/api-evangelist/hihealth/refs/heads/main/sandbox/hihealth-sandbox.yml
  title: ''
  type: Sandbox
  url: sandbox/hihealth-sandbox.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/hihealth/refs/heads/main/asyncapi/hihealth-webhooks.yml
  title: ''
  type: Webhooks
  url: asyncapi/hihealth-webhooks.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/hihealth/refs/heads/main/mcp/hihealth-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/hihealth-mcp.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/hihealth/refs/heads/main/llms/hihealth-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/hihealth-llms.txt
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/hihealth/refs/heads/main/well-known/hihealth-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/hihealth-well-known.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/hihealth/refs/heads/main/well-known/hihealth-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/hihealth-security.txt
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/hihealth/refs/heads/main/security/hihealth-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/hihealth-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: Security
  url: https://www.getpliant.com/.well-known/security.txt
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/hihealth/refs/heads/main/security/hihealth-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/hihealth-domain-security.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/hihealth/refs/heads/main/conformance/hihealth-conformance.yml
  title: ''
  type: Conformance
  url: conformance/hihealth-conformance.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/hihealth/refs/heads/main/conformance/hihealth-conformance.yml
  title: ''
  type: Compliance
  url: conformance/hihealth-conformance.yml
- group: operate
  href: https://raw.githubusercontent.com/api-evangelist/hihealth/refs/heads/main/changelog/hihealth-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/hihealth-changelog.yml
created: '2026-07-17'
description: 'hi.health is a cashless, real-time claims and payments platform for the insurance industry, now operated as "hi.health by Pliant" after joining Pliant. It replaces legacy reimbursement models with instantly issued virtual and physical cards whose spend is programmatically controlled per policy, merchant, currency and country. Members pay nothing upfront: eligible claims are settled in real time at the point of care across health, home, travel, corporate and auto insurance lines, and structured transaction data is streamed back to insurers for dashboards, reconciliation and fraud prevention. The developer surface is Pliant''s PCI-DSS-certified Cards-as-a-Service (CaaS) and Pro API: OAuth2 client-credentials access, asynchronous callback/webhook events, and a full sandbox, which partners embed to issue and manage cards, cardholders, transactions, receipts, payments and external transfers.'
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/hihealth.png
json_schemas:
- name: CardDetailBatch
  property_count: 47
  slug: hihealth-card-detail-batch
- name: CardDetail
  property_count: 40
  slug: hihealth-card-detail
- name: OrganizationCreate
  property_count: 12
  slug: hihealth-organization-create
- name: OrganizationDetail
  property_count: 32
  slug: hihealth-organization-detail
- name: TransactionDetailBatch
  property_count: 37
  slug: hihealth-transaction-detail-batch
- name: TransactionDetail
  property_count: 35
  slug: hihealth-transaction-detail
jsonld:
- class_count: 120
  name: Hihealth Context
  property_count: 321
  slug: hihealth-context
layout: provider
mcp_servers:
- description: Remote MCP server at partner.getpliant.com.
  name: hi.health MCP Server
  slug: hihealth-mcp-yml
modified: '2026-07-19'
name: hi.health
nav: Providers
network: true
overview: 'hi.health publishes 32 API contracts indexed on the [APIs.io](https://apis.io/) network, including Access Links API, Account Entries API, Accounting Projects API, and 29 more. Tagged areas include Company, Insurance, Payments, Cards, and Fintech.


  The hi.health catalog on APIs.io includes 1 event-driven AsyncAPI specification, 1 JSON-LD context, and 1 Spectral governance ruleset.


  hi.health''s developer surface includes engineering blog, pricing, signup flow, documentation, API reference, getting-started guide, support, and 34 more developer resources.'
random_paper: 3
rate_limits:
- limit_count: 1
  name: Hihealth Rate Limits
  slug: hihealth-rate-limits
rules:
- authorship: generated
  effective_rule_count: 57
  extends:
  - spectral:oas
  name: hi.health API Rules
  rule_count: 16
  severity_counts:
    error: 12
    hint: 0
    info: 1
    warn: 3
  slug: hihealth-rules
scopes:
- name: Hihealth Scopes
  scope_count: 3
  slug: hihealth-scopes
  summary_line: 3 scopes
score:
  band: strong
  composite: 65.3
  coverage:
    artifact_dirs: 27
    catalog_earned: 70.8
    catalog_earned_first_party: 8.0
    catalog_gap: 44.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 16.6
  facets:
    access_clarity: 39.5
    contract_governance: 35.6
    contract_quality: 72.0
    developer_ergonomics: 39.3
    discoverability: 76.7
    operational_transparency: 69.7
  previous_composite: 48.7
  provenance:
    agentic_access: derived
    conformance: first-party
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 100.0
      total: 30
    mcp: first-party
  regulatory:
    applies: true
    matched_via: tags
    regime: Insurance
    regime_id: insurance
    score: 50.9
  schema_version: 0.24.0
  scored_at: '2026-10-17'
  trend: rising
  upsert:
    applies: true
    score: 61.1
screenshot: https://raw.githubusercontent.com/api-evangelist/hihealth/refs/heads/main/screenshots/hihealth-2026-07-25T221215.png
security:
- kind: authentication
  name: Hihealth Authentication
  slug: hihealth-authentication
  summary_line: oauth2 · 1 scheme
- kind: domain-security
  name: Hihealth Domain Security
  slug: hihealth-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Hihealth Vulnerability Disclosure
  slug: hihealth-vulnerability-disclosure
  summary_line: Hackerone · security.txt · contact published
slug: hihealth
tags:
- Company
- Insurance
- Payments
- Cards
- Fintech
- Health
- Cards-as-a-Service
- Embedded Finance
- Reimbursement
- Claims
website: https://www.getpliant.com/en/industry/insurance-payments/
---
