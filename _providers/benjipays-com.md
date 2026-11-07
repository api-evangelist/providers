---
access_model:
  confidence: high
  label: Paid
  onboarding: unknown
  pricing: paid
  public: false
  source:
  - plans
  - authentication
  - scopes
  - rate-limits
  - security
  trial: false
  try_now: false
agent_readiness:
  band: agent-native
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: served
    consent_identity: false
    delegated_identity: served
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: verified
    event_surface_described: false
    idempotency: verified
    mcp_server: documented
    mcp_tool_quality: na
    openapi_examples: verified
    operation_distinctiveness: distinct
    pagination_ratio: partial
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: true
  schema_version: '0.2'
  score: 50.1
  scored_at: '2026-11-06'
agentic_access:
- acting_count: 23
  human_in_the_loop: 0
  name: Benjipays Com Agentic Access
  operation_count: 57
  slug: benjipays-com-agentic-access
  summary_line: 57 operations · 23 acting
api_count: 2
apis:
- baseURL: https://api.benjipays.com
  baseurl_source: declared
  description: Live Xero chart accounts for deposit charges
  name: Benji Pays Accounting Accounts API
  slug: benjipays-com-accounting-accounts-api
- baseURL: https://api.benjipays.com
  baseurl_source: declared
  description: Auto-processing forecast for authenticated organizations
  name: Benji Pays Autoprocessing API
  slug: benjipays-com-autoprocessing-api
- baseURL: https://api.benjipays.com
  baseurl_source: declared
  description: Finalized billing data for invoicing (locked/completed months only)
  name: Benji Pays Billing API
  slug: benjipays-com-billing-api
- baseURL: https://api.benjipays.com
  baseurl_source: declared
  description: Accounting customers for authenticated organizations
  name: Benji Pays Customers API
  slug: benjipays-com-customers-api
- baseURL: https://api.benjipays.com
  baseurl_source: declared
  description: Sent emails for authenticated organizations
  name: Benji Pays Emails API
  slug: benjipays-com-emails-api
- baseURL: https://api.benjipays.com
  baseurl_source: declared
  description: Payment gateway discovery for authenticated organizations
  name: Benji Pays Gateways API
  slug: benjipays-com-gateways-api
- baseURL: https://api.benjipays.com
  baseurl_source: declared
  description: Accounting invoices for authenticated organizations
  name: Benji Pays Invoices API
  slug: benjipays-com-invoices-api
- baseURL: https://api.benjipays.com
  baseurl_source: declared
  description: Merchant-internal customer notes, categories, and statuses for authenticated organizations
  name: Benji Pays Notes API
  slug: benjipays-com-notes-api
- baseURL: https://api.benjipays.com
  baseurl_source: declared
  description: Profile (company details) for the authenticated organization
  name: Benji Pays Organization API
  slug: benjipays-com-organization-api
- baseURL: https://api.benjipays.com
  baseurl_source: declared
  description: Organization (end-customer) management under partners
  name: Benji Pays Organizations API
  slug: benjipays-com-organizations-api
- baseURL: https://api.benjipays.com
  baseurl_source: declared
  description: Partner account management (MSPs, accountants, ISOs)
  name: Benji Pays Partners API
  slug: benjipays-com-partners-api
- baseURL: https://api.benjipays.com
  baseurl_source: declared
  description: Unapplied (no-invoice) and applied (invoice-tied) payment links for authenticated organizations
  name: Benji Pays Payment Links API
  slug: benjipays-com-payment-links-api
- baseURL: https://api.benjipays.com
  baseurl_source: declared
  description: Customer payment-method-on-file requests for authenticated organizations
  name: Benji Pays Payment Method Requests API
  slug: benjipays-com-payment-method-requests-api
- baseURL: https://api.benjipays.com
  baseurl_source: declared
  description: Saved payment methods (profiles) for authenticated organizations
  name: Benji Pays Payment Methods API
  slug: benjipays-com-payment-methods-api
- baseURL: https://api.benjipays.com
  baseurl_source: declared
  description: Billing plan management for distributors
  name: Benji Pays Plans API
  slug: benjipays-com-plans-api
- baseURL: https://api.benjipays.com
  baseurl_source: declared
  description: The Settings API from Benji Pays — 1 operation(s) for settings.
  name: Benji Pays Settings API
  slug: benjipays-com-settings-api
- baseURL: https://api.benjipays.com
  baseurl_source: declared
  description: Payment transactions for authenticated organizations
  name: Benji Pays Transactions API
  slug: benjipays-com-transactions-api
- baseURL: https://api.benjipays.com
  baseurl_source: declared
  description: Usage and consumption reporting for billing (real-time calculation)
  name: Benji Pays Usage API
  slug: benjipays-com-usage-api
- baseURL: https://api.benjipays.com
  baseurl_source: declared
  description: Login accounts for authenticated organizations
  name: Benji Pays Users API
  slug: benjipays-com-users-api
- baseURL: https://api.benjipays.com
  baseurl_source: declared
  description: Authentication verification and testing endpoints
  name: Benji Pays Whoami API
  slug: benjipays-com-whoami-api
artifact_total: 42
common:
- group: agent
  href: https://artifacts.apis.io/benjipays-com/agentic-access/benjipays-com-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/benjipays-com-agentic-access.yml
- group: operate
  href: https://artifacts.apis.io/benjipays-com/rate-limits/benjipays-com-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/benjipays-com-rate-limits.yml
- group: commercial
  href: https://artifacts.apis.io/benjipays-com/plans/benjipays-com-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/benjipays-com-plans-pricing.yml
- group: design
  href: https://artifacts.apis.io/benjipays-com/rules/benjipays-com-rules.yml
  title: ''
  type: Spectral
  url: rules/benjipays-com-rules.yml
- group: design
  href: https://artifacts.apis.io/benjipays-com/json-ld/benjipays-com-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/benjipays-com-context.jsonld
- group: design
  href: https://artifacts.apis.io/benjipays-com/vocabulary/benjipays-com-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/benjipays-com-vocabulary.yml
- group: design
  href: https://artifacts.apis.io/benjipays-com/data-model/benjipays-com-data-model.yml
  title: ''
  type: DataModel
  url: data-model/benjipays-com-data-model.yml
- group: design
  href: https://artifacts.apis.io/benjipays-com/conventions/benjipays-com-conventions.yml
  title: ''
  type: Idempotency
  url: conventions/benjipays-com-conventions.yml
- group: design
  href: https://artifacts.apis.io/benjipays-com/conventions/benjipays-com-conventions.yml
  title: ''
  type: Conventions
  url: conventions/benjipays-com-conventions.yml
- group: auth
  title: ''
  type: Compliance
  url: https://benjipays.com/trust/
- group: auth
  href: https://artifacts.apis.io/benjipays-com/authentication/benjipays-com-authentication.yml
  title: ''
  type: Authentication
  url: authentication/benjipays-com-authentication.yml
- group: auth
  href: https://artifacts.apis.io/benjipays-com/scopes/benjipays-com-scopes.yml
  title: ''
  type: OAuthScopes
  url: scopes/benjipays-com-scopes.yml
- group: design
  href: https://artifacts.apis.io/benjipays-com/errors/benjipays-com-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/benjipays-com-problem-types.yml
- group: design
  href: https://artifacts.apis.io/benjipays-com/conformance/benjipays-com-conformance.yml
  title: ''
  type: Conformance
  url: conformance/benjipays-com-conformance.yml
- group: agent
  href: https://artifacts.apis.io/benjipays-com/llms/benjipays-com-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/benjipays-com-llms.txt
- group: build
  href: https://artifacts.apis.io/benjipays-com/mcp/benjipays-com-tool-crosswalk.yml
  title: ''
  type: ToolCrosswalk
  url: mcp/benjipays-com-tool-crosswalk.yml
- group: agent
  href: https://artifacts.apis.io/benjipays-com/mcp/benjipays-com-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/benjipays-com-mcp.yml
- group: agent
  href: https://artifacts.apis.io/benjipays-com/well-known/benjipays-com-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/benjipays-com-well-known.yml
- group: other
  href: https://artifacts.apis.io/benjipays-com/hosts/benjipays-com-hosts.yml
  title: ''
  type: Hosts
  url: hosts/benjipays-com-hosts.yml
- group: other
  href: https://artifacts.apis.io/benjipays-com/vendors/benjipays-com-vendors.yml
  title: ''
  type: Vendors
  url: vendors/benjipays-com-vendors.yml
- group: auth
  title: ''
  type: Security
  url: https://benjipays.com/security/
- group: company
  title: ''
  type: Newsroom
  url: https://benjipays.com/category/news/
- group: auth
  href: https://artifacts.apis.io/benjipays-com/security/benjipays-com-trust-center.yml
  title: ''
  type: TrustCenter
  url: security/benjipays-com-trust-center.yml
- group: auth
  href: https://artifacts.apis.io/benjipays-com/security/benjipays-com-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/benjipays-com-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://benjipays.com/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://developer.benjipays.com
- group: docs
  title: ''
  type: Documentation
  url: https://developer.benjipays.com/docs
- group: docs
  title: ''
  type: APIReference
  url: https://developer.benjipays.com/reference
- group: start
  title: ''
  type: GettingStarted
  url: https://developer.benjipays.com/docs/getting-started
- group: operate
  title: ''
  type: Support
  url: https://support.benjipays.com
- group: company
  title: ''
  type: Blog
  url: https://benjipays.com/category/blog/
- group: commercial
  title: ''
  type: Pricing
  url: https://benjipays.com/pricing/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://benjipays.com/terms-of-service/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://benjipays.com/privacy/
- group: operate
  title: ''
  type: StatusPage
  url: https://status.benjipays.com/
- group: operate
  title: ''
  type: Roadmap
  url: https://feedback.benjipays.com/roadmap
created: '2026-11-02'
description: Benji Pays connects QuickBooks Online, QuickBooks Desktop, Xero, and Business Central to Benji Payments and other gateways so invoice payments post to your books automatically. Not a general ledger. Benji Pays is invoice-to-cash software that sits between your accounting system and your payment rails, automating collections for managed service providers.
image: https://benjipays.com/wp-content/uploads/2026/10/benji-mark-512.png
json_schemas:
- name: BillingResponse
  property_count: 2
  slug: benjipays-com-billing-response
- name: CreatePartnerResponse
  property_count: 1
  slug: benjipays-com-create-partner-response
- name: CustomerNoteComment
  property_count: 11
  slug: benjipays-com-customer-note-comment
- name: CustomerNote
  property_count: 16
  slug: benjipays-com-customer-note
- name: CustomerNoteSummary
  property_count: 18
  slug: benjipays-com-customer-note-summary
- name: EchoResponse
  property_count: 3
  slug: benjipays-com-echo-response
- name: ListOrganizationsResponse
  property_count: 2
  slug: benjipays-com-list-organizations-response
- name: OrganizationProfileResponse
  property_count: 1
  slug: benjipays-com-organization-profile-response
- name: OrganizationSettingsResponse
  property_count: 1
  slug: benjipays-com-organization-settings-response
- name: PaymentMethodWithMandate
  property_count: 25
  slug: benjipays-com-payment-method-with-mandate
- name: UsageResponse
  property_count: 2
  slug: benjipays-com-usage-response
- name: WhoamiResponse
  property_count: 7
  slug: benjipays-com-whoami-response
jsonld:
- class_count: 74
  name: Benjipays Com Context
  property_count: 226
  slug: benjipays-com-context
layout: provider
mcp_servers:
- description: Remote MCP server at developer.benjipays.com.
  name: Benji Pays MCP Server
  slug: benjipays-com-mcp-yml
modified: '2026-11-02'
name: Benji Pays
nav: Providers
network: true
overview: 'Benji Pays publishes 20 API contracts indexed on the [APIs.io](https://apis.io/) network, including Accounting Accounts API, Autoprocessing API, Billing API, and 17 more. Tagged areas include Payments, Accounting, Integration, QuickBooks, and Xero.


  The Benji Pays catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  Benji Pays'' developer surface includes authentication, documentation, API reference, getting-started guide, support, engineering blog, pricing, and 29 more developer resources.'
plans:
- name: Benjipays Com Plans Pricing
  plan_count: 4
  slug: benjipays-com-plans-pricing
random_paper: 9
rate_limits:
- limit_count: 2
  name: Benjipays Com Rate Limits
  slug: benjipays-com-rate-limits
rules:
- authorship: generated
  effective_rule_count: 105
  extends:
  - spectral:oas
  name: Benji Pays API Rules
  rule_count: 64
  severity_counts:
    error: 46
    hint: 0
    info: 4
    warn: 14
  slug: benjipays-com-rules
scopes:
- name: Benjipays Com Scopes
  scope_count: 0
  slug: benjipays-com-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: developing
  composite: 52.7
  coverage:
    artifact_dirs: 28
    catalog_earned: 82.8
    catalog_earned_first_party: 20.0
    catalog_gap: 32.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 59.2
    contract_governance: 22.0
    contract_quality: 73.5
    developer_ergonomics: 34.5
    discoverability: 65.8
    operational_transparency: 36.8
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 100.0
      total: 20
    mcp: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Payments
    regime_id: payments
    score: 29.9
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: authentication
  name: Benjipays Com Authentication
  slug: benjipays-com-authentication
  summary_line: 2 schemes
- kind: domain-security
  name: Benjipays Com Domain Security
  slug: benjipays-com-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: trust-center
  name: Benjipays Com Trust Center
  slug: benjipays-com-trust-center
  summary_line: SOC 2, PCI DSS, GDPR
slug: benjipays-com
tags:
- Payments
- Accounting
- Integration
- QuickBooks
- Xero
website: https://benjipays.com/
---
