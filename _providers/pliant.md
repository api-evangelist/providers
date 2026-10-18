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
  band: agent-ready
  band_gated_from: agent-native
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
    mcp_server: verified
    openapi_examples: partial
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 41.1
  scored_at: '2026-10-17'
agentic_access:
- acting_count: 88
  human_in_the_loop: 2
  name: Pliant Agentic Access
  operation_count: 131
  slug: pliant-agentic-access
  summary_line: 131 operations · 88 acting · 2 human-in-the-loop
api_count: 1
apis:
- baseURL: https://partner-api.getpliant.com/api/
  baseurl_source: declared
  description: This tag is for operations related to account entries
  name: Pliant Account Entries API
  slug: pliant-account-entries-api
- baseURL: https://partner-api.getpliant.com/api/
  baseurl_source: declared
  description: This tag is for operations related to accounting projects
  name: Pliant Accounting Projects API
  slug: pliant-accounting-projects-api
- baseURL: https://partner-api.getpliant.com/api/
  baseurl_source: declared
  description: This tag is for operations related to accounting teams
  name: Pliant Accounting Teams API
  slug: pliant-accounting-teams-api
- baseURL: https://partner-api.getpliant.com/api/
  baseurl_source: declared
  description: This tag is for operations related to accounting transactions
  name: Pliant Accounting Transactions API
  slug: pliant-accounting-transactions-api
- baseURL: https://partner-api.getpliant.com/api/
  baseurl_source: declared
  description: This tag is for operations related to callbacks
  name: Pliant Callbacks API
  slug: pliant-callbacks-api
- baseURL: https://partner-api.getpliant.com/api/
  baseurl_source: declared
  description: This tag is for operations related to card accounts
  name: Pliant Card Accounts API
  slug: pliant-card-accounts-api
- baseURL: https://partner-api.getpliant.com/api/
  baseurl_source: declared
  description: This tag is for operations related to card controls
  name: Pliant Card Controls API
  slug: pliant-card-controls-api
- baseURL: https://partner-api.getpliant.com/api/
  baseurl_source: declared
  description: This tag is for operations related to card copilots
  name: Pliant Card Copilots API
  slug: pliant-card-copilots-api
- baseURL: https://partner-api.getpliant.com/api/
  baseurl_source: declared
  description: This tag is for operations related to card sensitive data
  name: Pliant Card Sensitive Data API
  slug: pliant-card-sensitive-data-api
- baseURL: https://partner-api.getpliant.com/api/
  baseurl_source: declared
  description: This tag is for operations related to cardholders
  name: Pliant Cardholders API
  slug: pliant-cardholders-api
- baseURL: https://partner-api.getpliant.com/api/
  baseurl_source: declared
  description: This tag is for operations related to cards
  name: Pliant Cards API
  slug: pliant-cards-api
- baseURL: https://partner-api.getpliant.com/api/
  baseurl_source: declared
  description: This tag is for operations related to custom fields
  name: Pliant Custom Fields API
  slug: pliant-custom-fields-api
- baseURL: https://partner-api.getpliant.com/api/
  baseurl_source: declared
  description: This tag is for operations related to organizations
  name: Pliant Organizations API
  slug: pliant-organizations-api
- baseURL: https://partner-api.getpliant.com/api/
  baseurl_source: declared
  description: This tag is for operations related to payments
  name: Pliant Payments API
  slug: pliant-payments-api
- baseURL: https://partner-api.getpliant.com/api/
  baseurl_source: declared
  description: This tag is for operations related to receipt automatching
  name: Pliant Receipt Automatching API
  slug: pliant-receipt-automatching-api
- baseURL: https://partner-api.getpliant.com/api/
  baseurl_source: declared
  description: This tag is for operations related to receipts
  name: Pliant Receipts API
  slug: pliant-receipts-api
- baseURL: https://partner-api.getpliant.com/api/
  baseurl_source: declared
  description: This tag is for operations related to statements
  name: Pliant Statements API
  slug: pliant-statements-api
- baseURL: https://partner-api.getpliant.com/api/
  baseurl_source: declared
  description: This tag is for operations related to test data generation
  name: Pliant Test Data Generator (Sandbox-only) API
  slug: pliant-test-data-generator-sandbox-only-api
- baseURL: https://partner-api.getpliant.com/api/
  baseurl_source: declared
  description: This tag is for operations related to transactions
  name: Pliant Transactions API
  slug: pliant-transactions-api
artifact_total: 26
asyncapis:
- description: ''
  name: Pliant Callbacks Webhooks
  slug: pliant-callbacks-webhooks
common:
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/pliant/refs/heads/main/agentic-access/pliant-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/pliant-agentic-access.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/pliant/refs/heads/main/rules/pliant-rules.yml
  title: ''
  type: Spectral
  url: rules/pliant-rules.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/pliant/refs/heads/main/vocabulary/pliant-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/pliant-vocabulary.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/pliant/refs/heads/main/errors/pliant-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/pliant-problem-types.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/pliant/refs/heads/main/hosts/pliant-hosts.yml
  title: ''
  type: Hosts
  url: hosts/pliant-hosts.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/pliant/refs/heads/main/vendors/pliant-vendors.yml
  title: ''
  type: Vendors
  url: vendors/pliant-vendors.yml
- group: company
  title: ''
  type: Newsroom
  url: https://www.getpliant.com/en-us/press
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/pliant/refs/heads/main/security/pliant-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/pliant-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: Security
  url: https://www.getpliant.com/.well-known/security.txt
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/pliant/refs/heads/main/well-known/pliant-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/pliant-security.txt
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/pliant/refs/heads/main/well-known/pliant-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/pliant-well-known.yml
- group: start
  title: ''
  type: DeveloperPortal
  url: https://customer-api.getpliant.com
- group: docs
  title: ''
  type: Documentation
  url: https://customer-api.getpliant.com/docs/introduction
- group: docs
  title: ''
  type: APIReference
  url: https://customer-api.getpliant.com/reference/list-organizations
- group: start
  title: ''
  type: GettingStarted
  url: https://customer-api.getpliant.com/docs/introduction
- group: company
  title: ''
  type: Website
  url: https://www.getpliant.com/en-us
- group: company
  title: ''
  type: Blog
  url: https://www.getpliant.com/en-us/blog
- group: commercial
  title: ''
  type: Pricing
  url: https://www.getpliant.com/en-us/pricing
- group: operate
  title: ''
  type: Support
  url: https://help.getpliant.com/en/
- group: operate
  title: ''
  type: HelpCenter
  url: https://help.getpliant.com/en/
- group: start
  title: ''
  type: SignUp
  url: https://www.getpliant.com/en-us/book-demo
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.getpliant.com/en-us/privacy-policy
- group: operate
  title: ''
  type: StatusPage
  url: https://customer-api.getpliant.com/page/status
- group: operate
  title: ''
  type: Deprecation
  url: https://customer-api.getpliant.com/docs/versioning
- group: operate
  title: ''
  type: ChangeLog
  url: https://customer-api.getpliant.com/changelog
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/pliant/refs/heads/main/mcp/pliant-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/pliant-mcp.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/pliant/refs/heads/main/authentication/pliant-authentication.yml
  title: ''
  type: Authentication
  url: authentication/pliant-authentication.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/pliant/refs/heads/main/asyncapi/pliant-callbacks-webhooks.yml
  title: ''
  type: Webhooks
  url: asyncapi/pliant-callbacks-webhooks.yml
- group: start
  href: https://raw.githubusercontent.com/api-evangelist/pliant/refs/heads/main/sandbox/pliant-sandbox.yml
  title: ''
  type: Sandbox
  url: sandbox/pliant-sandbox.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/pliant/refs/heads/main/conventions/pliant-conventions.yml
  title: ''
  type: Conventions
  url: conventions/pliant-conventions.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/pliant/refs/heads/main/errors/pliant-error-codes.yml
  title: ''
  type: ErrorCatalog
  url: errors/pliant-error-codes.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/pliant/refs/heads/main/lifecycle/pliant-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/pliant-lifecycle.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/pliant/refs/heads/main/data-model/pliant-data-model.yml
  title: ''
  type: DataModel
  url: data-model/pliant-data-model.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/pliant/refs/heads/main/conformance/pliant-conformance.yml
  title: ''
  type: Conformance
  url: conformance/pliant-conformance.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/pliant/refs/heads/main/conformance/pliant-conformance.yml
  title: ''
  type: Compliance
  url: conformance/pliant-conformance.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/pliant/refs/heads/main/components/pliant-components.yml
  title: ''
  type: Components
  url: components/pliant-components.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/pliant/refs/heads/main/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/pliant/refs/heads/main/llms/pliant-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/pliant-llms.txt
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/pliant/refs/heads/main/security/pliant-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/pliant-domain-security.yml
created: '2026-07-17'
description: Pliant is a Berlin-based financial technology company offering a business credit card and spend-management platform, plus Cards-as-a-Service (CaaS) and Banking-as-a-Service (BaaS) infrastructure for banks and platforms. Its Pro API lets customers programmatically issue physical, virtual, single-use and specialized cards (travel, fleet, benefits, insurance-claim), apply card controls and advanced limits, retrieve transactions and accounting data, manage receipts, projects, teams and statements, and subscribe to real-time callbacks. Pliant is PCI DSS certified, ISO/IEC 27001:2022 certified and holds an EU e-money license, with customers including BMW, Decathlon, Deutsche Telekom and Commerzbank.
image: https://a.storyblok.com/f/169635/1200x630/92b10eaf7c/pliant-og-image.png
layout: provider
mcp_servers:
- description: 'Pliant publishes an official hosted/remote MCP server for the Pro API (Customer). It exposes direct API access to Pliant Pro API functionality, documentation search, real-time data from the connected '
  name: Pliant MCP Server
  slug: pliant-customer-api
modified: '2026-07-20'
name: Pliant
nav: Providers
network: true
overview: 'Pliant publishes 19 API contracts indexed on the [APIs.io](https://apis.io/) network, including Account Entries API, Accounting Projects API, Accounting Teams API, and 16 more. Tagged areas include Company, Payments, Corporate Cards, Card Issuing, and Spend Management.


  The Pliant catalog on APIs.io includes 1 event-driven AsyncAPI specification and 1 Spectral governance ruleset.


  Pliant''s developer surface includes documentation, API reference, getting-started guide, engineering blog, pricing, support, signup flow, and 32 more developer resources.'
random_paper: 10
rules:
- authorship: generated
  effective_rule_count: 57
  extends:
  - spectral:oas
  name: Pliant API Rules
  rule_count: 16
  severity_counts:
    error: 11
    hint: 0
    info: 1
    warn: 4
  slug: pliant-rules
score:
  band: strong
  composite: 56.3
  coverage:
    artifact_dirs: 25
    catalog_earned: 42.8
    catalog_earned_first_party: 0.0
    catalog_gap: 72.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 12.4
  facets:
    access_clarity: 42.1
    contract_governance: 35.6
    contract_quality: 57.8
    developer_ergonomics: 47.0
    discoverability: 76.7
    operational_transparency: 32.9
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    countries:
    - germany
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
    regions:
    - dach
    - europe
  previous_composite: 43.9
  provenance:
    agentic_access: derived
    conformance: first-party
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 100.0
      total: 19
    mcp: first-party
    skills: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Payments
    regime_id: payments
    score: 35.7
  schema_version: 0.24.0
  scored_at: '2026-10-17'
  trend: rising
  upsert:
    applies: true
    score: 61.1
screenshot: https://raw.githubusercontent.com/api-evangelist/pliant/refs/heads/main/screenshots/pliant-2026-08-17T081307.png
security:
- kind: authentication
  name: Pliant Authentication
  slug: pliant-authentication
  summary_line: oauth2 · 1 scheme
- kind: domain-security
  name: Pliant Domain Security
  slug: pliant-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Pliant Vulnerability Disclosure
  slug: pliant-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: pliant
tags:
- Company
- Payments
- Corporate Cards
- Card Issuing
- Spend Management
- Expense Management
- Fintech
- Cards-as-a-Service
- Banking as a Service
- Travel
- Accounting
website: https://www.getpliant.com/en-us
---
