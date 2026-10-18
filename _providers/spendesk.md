---
access_model:
  confidence: medium
  label: Paid
  onboarding: unknown
  pricing: paid
  public: false
  source:
  - plans
  trial: false
  try_now: false
agent_readiness:
  band: agent-native
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: negotiable
    consent_identity: false
    delegated_identity: documented
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: verified
    event_surface_described: derived
    idempotency: verified
    mcp_server: false
    openapi_examples: partial
    protected_resource_metadata: false
    rate_limit_signal: verified
    reversibility_documented: documented
    spec_presence: true
    well_known_catalog: true
  schema_version: '0.2'
  score: 47.8
  scored_at: '2026-10-17'
agentic_access:
- acting_count: 50
  human_in_the_loop: 0
  name: Spendesk Agentic Access
  operation_count: 106
  slug: spendesk-agentic-access
  summary_line: 106 operations · 50 acting
api_count: 1
apis:
- baseURL: https://api.spendesk.com
  baseurl_source: declared
  description: 'Experimental: generate purchase and bank journals from the company''s templates, download them, and check which entities are exported. Part of: [Exporting accounting data](/reference/exporting-accounti'
  name: Spendesk Accounting exports API
  slug: spendesk-accounting-exports-api
- baseURL: https://api.spendesk.com
  baseurl_source: declared
  description: Cost centers and analytical fields used to categorise spend. The `v1` endpoints read analytical fields and manage cost centers; the experimental `v2` endpoints also create, update and delete analytica
  name: Spendesk Analytical fields and cost centers API
  slug: spendesk-analytical-fields-and-cost-centers-api
- baseURL: https://api.spendesk.com
  baseurl_source: declared
  description: 'How to get an access token: Public API credentials (API keys) exchanged with HTTP Basic authentication, or OAuth 2.0 for partner apps — authorization code with PKCE, the token endpoint (code exchange '
  name: Spendesk Authentication API
  slug: spendesk-authentication-api
- baseURL: https://api.spendesk.com
  baseurl_source: declared
  description: 'Experimental: cards, their blocking history, and the order of a physical card.'
  name: Spendesk Cards API
  slug: spendesk-cards-api
- baseURL: https://api.spendesk.com
  baseurl_source: declared
  description: 'Experimental chart of accounts: read, create, update, bulk-sync and archive accounts, set their purpose, and assign suppliers and employees to their accounts. Part of: [Building an accounting integrat'
  name: Spendesk Chart of accounts API
  slug: spendesk-chart-of-accounts-api
- baseURL: https://api.spendesk.com
  baseurl_source: declared
  description: 'The companies (legal entities) of an organisation. Requires an organisation-level token (experimental). Part of: [Organisation-level access](/reference/organisation-level-access).'
  name: Spendesk Companies API
  slug: spendesk-companies-api
- baseURL: https://api.spendesk.com
  baseurl_source: declared
  description: 'Expense categories. `v1` reads them; the experimental `v2` endpoints manage expense category fields and their categories. Part of: [Building an accounting integration](/reference/building-an-accountin'
  name: Spendesk Expense categories API
  slug: spendesk-expense-categories-api
- baseURL: https://api.spendesk.com
  baseurl_source: declared
  description: 'Experimental: store and look up the IDs your ERP gives to Spendesk objects — suppliers, cost centers, expense categories, analytical fields and values, accounts — per provider. Part of: [Building an a'
  name: Spendesk External references API
  slug: spendesk-external-references-api
- baseURL: https://api.spendesk.com
  baseurl_source: declared
  description: 'Experimental supplier invoices and invoice intake: send invoices and credit notes to a company''s inbox by uploading their file, track the intakes, then list, summarise and retrieve the invoices.'
  name: Spendesk Invoices and intakes API
  slug: spendesk-invoices-and-intakes-api
- baseURL: https://api.spendesk.com
  baseurl_source: declared
  description: The Spendesk MCP server (Streamable HTTP transport), for AI assistants connected through OAuth 2.0.
  name: Spendesk MCP API
  slug: spendesk-mcp-api
- baseURL: https://api.spendesk.com
  baseurl_source: declared
  description: Payables — invoices, credit notes, card purchases and expense claims — with their attachments. Retrieve them in bulk through snapshots, search them, read one by ID; experimental endpoints let accounti
  name: Spendesk Payables API
  slug: spendesk-payables-api
- baseURL: https://api.spendesk.com
  baseurl_source: declared
  description: 'Experimental purchase orders: list, retrieve, create, cancel and close them, and download a purchase order''s document.'
  name: Spendesk Purchase orders API
  slug: spendesk-purchase-orders-api
- baseURL: https://api.spendesk.com
  baseurl_source: declared
  description: 'Experimental: spend requests, and successful and failed card transactions.'
  name: Spendesk Requests and transactions API
  slug: spendesk-requests-and-transactions-api
- baseURL: https://api.spendesk.com
  baseurl_source: declared
  description: 'Money movements on the Spendesk wallet: settlements (payments) and their export state, bank fees, wallet loads and the wallet summary. Part of: [What is Spend Data?](/reference/how-to-use-spend-data),'
  name: Spendesk Settlements and wallet API
  slug: spendesk-settlements-and-wallet-api
- baseURL: https://api.spendesk.com
  baseurl_source: declared
  description: The Spendesk Public API API from Spendesk — 0 operation(s) for spendesk public api.
  name: Spendesk Spendesk Public API
  slug: spendesk-spendesk-public-api-api
- baseURL: https://api.spendesk.com
  baseurl_source: declared
  description: 'Suppliers of a company: read them with `supplier:read`; create, update, archive and unarchive them with `experimental:supplier:manage`. Part of: [Building an accounting integration](/reference/buildin'
  name: Spendesk Suppliers API
  slug: spendesk-suppliers-api
- baseURL: https://api.spendesk.com
  baseurl_source: declared
  description: Members of a company (`user:read`).
  name: Spendesk Users API
  slug: spendesk-users-api
- baseURL: https://api.spendesk.com
  baseurl_source: declared
  description: 'Experimental webhook instances: subscribe an endpoint to payable and settlement events, and list, update or delete instances. Part of: [Using webhooks](/reference/using-webhooks), [Building an account'
  name: Spendesk Webhooks API
  slug: spendesk-webhooks-api
artifact_total: 35
asyncapis:
- description: ''
  name: Spendesk Webhooks
  slug: spendesk-webhooks
common:
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/spendesk/refs/heads/main/agentic-access/spendesk-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/spendesk-agentic-access.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/spendesk/refs/heads/main/rules/spendesk-rules.yml
  title: ''
  type: Spectral
  url: rules/spendesk-rules.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/spendesk/refs/heads/main/json-ld/spendesk-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/spendesk-context.jsonld
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/spendesk/refs/heads/main/vocabulary/spendesk-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/spendesk-vocabulary.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/spendesk/refs/heads/main/asyncapi/spendesk-webhooks.yml
  title: ''
  type: Webhooks
  url: asyncapi/spendesk-webhooks.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/spendesk/refs/heads/main/data-model/spendesk-data-model.yml
  title: ''
  type: DataModel
  url: data-model/spendesk-data-model.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/spendesk/refs/heads/main/conventions/spendesk-conventions.yml
  title: ''
  type: Idempotency
  url: conventions/spendesk-conventions.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/spendesk/refs/heads/main/conventions/spendesk-conventions.yml
  title: ''
  type: Conventions
  url: conventions/spendesk-conventions.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/spendesk/refs/heads/main/errors/spendesk-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/spendesk-problem-types.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/spendesk/refs/heads/main/conformance/spendesk-conformance.yml
  title: ''
  type: Conformance
  url: conformance/spendesk-conformance.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/spendesk/refs/heads/main/llms/spendesk-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/spendesk-llms.txt
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/spendesk/refs/heads/main/well-known/spendesk-status-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/spendesk-status-security.txt
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/spendesk/refs/heads/main/well-known/spendesk-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/spendesk-security.txt
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/spendesk/refs/heads/main/well-known/spendesk-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/spendesk-well-known.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/spendesk/refs/heads/main/hosts/spendesk-hosts.yml
  title: ''
  type: Hosts
  url: hosts/spendesk-hosts.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/spendesk/refs/heads/main/vendors/spendesk-vendors.yml
  title: ''
  type: Vendors
  url: vendors/spendesk-vendors.yml
- group: auth
  title: ''
  type: TrustCenter
  url: https://trust.spendesk.com/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.spendesk.com/legals/terms/
- group: auth
  title: ''
  type: Security
  url: https://www.spendesk.com/sl/security/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.spendesk.com/legals/privacy/
- group: company
  title: ''
  type: Newsroom
  url: https://www.spendesk.com/press/
- group: start
  title: ''
  type: Login
  url: https://app.spendesk.com/auth/login
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/spendesk/refs/heads/main/scopes/spendesk-scopes.yml
  title: ''
  type: OAuthScopes
  url: scopes/spendesk-scopes.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/spendesk/refs/heads/main/authentication/spendesk-authentication.yml
  title: ''
  type: Authentication
  url: authentication/spendesk-authentication.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/spendesk/refs/heads/main/security/spendesk-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/spendesk-vulnerability-disclosure.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/spendesk/refs/heads/main/security/spendesk-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/spendesk-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.spendesk.com/
- group: docs
  title: ''
  type: Documentation
  url: https://developer.spendesk.com/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/Spendesk
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/spendesk
- group: other
  title: ''
  type: X
  url: https://twitter.com/Spendesk
- group: company
  title: ''
  type: Blog
  url: https://www.spendesk.com/blog/
- group: commercial
  title: ''
  type: Pricing
  url: https://www.spendesk.com/pricing/
- group: operate
  title: ''
  type: StatusPage
  url: https://status.spendesk.com/
- group: commercial
  href: https://raw.githubusercontent.com/api-evangelist/spendesk/refs/heads/main/plans/spendesk-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/spendesk-plans-pricing.yml
- group: operate
  href: https://raw.githubusercontent.com/api-evangelist/spendesk/refs/heads/main/rate-limits/spendesk-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/spendesk-rate-limits.yml
- group: commercial
  href: https://raw.githubusercontent.com/api-evangelist/spendesk/refs/heads/main/finops/spendesk-finops.yml
  title: ''
  type: FinOps
  url: finops/spendesk-finops.yml
- group: company
  href: https://raw.githubusercontent.com/api-evangelist/spendesk/refs/heads/main/blogs/blogs.json
  title: ''
  type: BlogFeed
  url: blogs/blogs.json
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/spendesk/refs/heads/main/json-ld/spendesk-context.jsonld
  title: ''
  type: JSONLDContext
  url: json-ld/spendesk-context.jsonld
created: '2026-06-12'
description: Spendesk is an AI-powered spend management and procurement platform serving over 200,000 users across Europe. Its public REST API enables partners and customers to integrate programmatic card issuance, transaction retrieval, expense claims processing, vendor and invoice management, and accounting exports into their own tools and workflows. Authentication is supported via API keys (for customers) and OAuth2 (for partners building native integrations). API access requires a Premium or Enterprise subscription plan, and the developer portal at developer.spendesk.com provides reference documentation, changelogs, a Postman collection, and webhook administration.
finops:
- has_sources: false
  method: generated
  name: Spendesk Finops
  primary_unit: ''
  service_category: ''
  slug: spendesk-finops
  template: true
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/spendesk.png
json_schemas:
- name: intake
  property_count: 26
  slug: spendesk-intake
- name: intakeSummary
  property_count: 23
  slug: spendesk-intake-summary
- name: invoice
  property_count: 37
  slug: spendesk-invoice
- name: payable
  property_count: 34
  slug: spendesk-payable
- name: searchPayable
  property_count: 0
  slug: spendesk-search-payable
- name: supplier
  property_count: 19
  slug: spendesk-supplier
jsonld:
- class_count: 9
  name: Spendesk Context
  property_count: 10
  slug: spendesk-context
layout: provider
modified: '2026-06-12'
name: Spendesk
nav: Providers
network: true
overview: 'Spendesk publishes 18 API contracts indexed on the [APIs.io](https://apis.io/) network, including Accounting exports API, Analytical fields and cost centers API, Authentication API, and 15 more. Tagged areas include Spend Management, Corporate Cards, Expense Management, Invoices, and Procurement.


  The Spendesk catalog on APIs.io includes 1 event-driven AsyncAPI specification, 1 JSON-LD context, and 1 Spectral governance ruleset.


  Spendesk''s developer surface includes authentication, documentation, engineering blog, pricing, and 35 more developer resources.'
plans:
- name: Spendesk Plans Pricing
  plan_count: 3
  slug: spendesk-plans-pricing
random_paper: 3
rate_limits:
- limit_count: 3
  name: Spendesk Rate Limits
  slug: spendesk-rate-limits
rules:
- authorship: generated
  effective_rule_count: 61
  extends:
  - spectral:oas
  name: Spendesk API Rules
  rule_count: 20
  severity_counts:
    error: 11
    hint: 0
    info: 2
    warn: 7
  slug: spendesk-rules
scopes:
- name: Spendesk Scopes
  scope_count: 39
  slug: spendesk-scopes
  summary_line: 39 scopes · clientCredentials/authorizationCode
score:
  band: strong
  composite: 59.6
  coverage:
    artifact_dirs: 26
    catalog_earned: 68.8
    catalog_earned_first_party: 0.0
    catalog_gap: 46.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 29.1
  facets:
    access_clarity: 60.5
    contract_governance: 22.0
    contract_quality: 73.1
    developer_ergonomics: 17.9
    discoverability: 75.0
    operational_transparency: 52.6
  previous_composite: 30.5
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
    score: 41.1
  schema_version: 0.24.0
  scored_at: '2026-10-17'
  trend: rising
  upsert:
    applies: true
    score: 61.1
screenshot: https://raw.githubusercontent.com/api-evangelist/spendesk/refs/heads/main/screenshots/spendesk-2026-06-20T194306.png
security:
- kind: authentication
  name: Spendesk Authentication
  slug: spendesk-authentication
  summary_line: oauth2 · 1 scheme
- kind: domain-security
  name: Spendesk Domain Security
  slug: spendesk-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Spendesk Vulnerability Disclosure
  slug: spendesk-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: spendesk
tags:
- Spend Management
- Corporate Cards
- Expense Management
- Invoices
- Procurement
- Fintech
- Accounting
- Payments
website: https://www.spendesk.com/
---
