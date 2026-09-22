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
  trial: false
  try_now: false
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: false
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: verified
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 22.1
  scored_at: '2026-09-21'
api_count: 1
apis:
- baseURL: https://www.buxfer.com/api
  baseurl_source: declared
  description: List accounts and balances.
  name: Buxfer Accounts API
  slug: buxfer-accounts-api
- baseURL: https://www.buxfer.com/api
  baseurl_source: declared
  description: Obtain an ephemeral API token.
  name: Buxfer Authentication API
  slug: buxfer-authentication-api
- baseURL: https://www.buxfer.com/api
  baseurl_source: declared
  description: Tags, budgets, reminders.
  name: Buxfer Organization API
  slug: buxfer-organization-api
- baseURL: https://www.buxfer.com/api
  baseurl_source: declared
  description: Groups, contacts and loans for shared expenses.
  name: Buxfer Social API
  slug: buxfer-social-api
- baseURL: https://www.buxfer.com/api
  baseurl_source: declared
  description: Create, edit, delete, list and import transactions.
  name: Buxfer Transactions API
  slug: buxfer-transactions-api
artifact_total: 14
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Buxfer Accounts API
  slug: open-buxfer-accounts-api
- collection_type: open
  name: Buxfer Accounts Authentication API
  slug: open-buxfer-authentication-api
- collection_type: open
  name: Buxfer Accounts Organization API
  slug: open-buxfer-organization-api
- collection_type: open
  name: Buxfer Accounts Social API
  slug: open-buxfer-social-api
- collection_type: open
  name: Buxfer Accounts Transactions API
  slug: open-buxfer-transactions-api
common:
- group: company
  title: ''
  type: Website
  url: https://www.buxfer.com/
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/buxfer/refs/heads/main/overlays/buxfer-openapi-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/buxfer-openapi-overlay.yaml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/buxfer/refs/heads/main/security/buxfer-trust-center.yml
  title: ''
  type: TrustCenter
  url: security/buxfer-trust-center.yml
- group: auth
  title: ''
  type: Compliance
  url: https://www.buxfer.com/help/security
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/buxfer/refs/heads/main/well-known/buxfer-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/buxfer-well-known.yml
- group: start
  title: ''
  type: DeveloperPortal
  url: https://www.buxfer.com/help/api
- group: docs
  title: ''
  type: Documentation
  url: https://www.buxfer.com/help/api
- group: docs
  title: ''
  type: APIReference
  url: https://www.buxfer.com/help/api
- group: operate
  title: ''
  type: Support
  url: https://www.buxfer.com/help/
- group: company
  title: ''
  type: Blog
  url: https://blog.buxfer.com
- group: commercial
  title: ''
  type: Pricing
  url: https://www.buxfer.com/pricing/
- group: start
  title: ''
  type: SignUp
  url: https://www.buxfer.com/signup/
- group: start
  title: ''
  type: Login
  url: https://www.buxfer.com/login/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.buxfer.com/terms/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.buxfer.com/privacy/
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/buxfer/refs/heads/main/authentication/buxfer-authentication.yml
  title: ''
  type: Authentication
  url: authentication/buxfer-authentication.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/buxfer/refs/heads/main/conventions/buxfer-conventions.yml
  title: ''
  type: Conventions
  url: conventions/buxfer-conventions.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/buxfer/refs/heads/main/data-model/buxfer-data-model.yml
  title: ''
  type: DataModel
  url: data-model/buxfer-data-model.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/buxfer/refs/heads/main/errors/buxfer-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/buxfer-problem-types.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/buxfer/refs/heads/main/conformance/buxfer-conformance.yml
  title: ''
  type: Conformance
  url: conformance/buxfer-conformance.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/buxfer/refs/heads/main/lifecycle/buxfer-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/buxfer-lifecycle.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/buxfer/refs/heads/main/mcp/buxfer-mcp.yml
  title: ''
  type: X-MCPServerCandidate
  url: mcp/buxfer-mcp.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/buxfer/refs/heads/main/llms/buxfer-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/buxfer-llms.txt
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/buxfer/refs/heads/main/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/buxfer/refs/heads/main/security/buxfer-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/buxfer-domain-security.yml
created: '2026-07-17'
description: Buxfer is a personal finance and money management platform that consolidates bank, investment and retirement accounts in one place. It connects to 20,000+ banks across 70+ countries, tracks assets in 100+ currencies, and provides budgeting with real-time alerts, expense forecasting, net-worth projection, automatic transaction tagging with custom rules, investment and retirement planning, shared-expense groups, and encrypted cloud backups to Dropbox, Google Drive or OneDrive. Buxfer exposes a JSON HTTP API for reading accounts, transactions, tags, budgets, reminders, groups, contacts and loans, and for creating, editing and deleting transactions and uploading statements. Authentication uses a login call that returns an ephemeral token passed on every subsequent request. Buxfer is a Y Combinator company.
image: https://www.buxfer.com/favicon.ico
layout: provider
modified: '2026-07-18'
name: Buxfer
nav: Providers
network: true
overview: 'Buxfer publishes 5 APIs on the [APIs.io](https://apis.io/) network, including Accounts API, Authentication API, Organization API, and 2 more. Tagged areas include Company, Personal Finance, Money Management, Budgeting, and Banking.


  Buxfer''s developer surface includes documentation, API reference, support, engineering blog, pricing, signup flow, authentication, and 18 more developer resources.'
random_paper: 14
score:
  band: thin
  composite: 33.3
  coverage:
    artifact_dirs: 17
    catalog_earned: 37.0
    catalog_earned_first_party: 0.0
    catalog_gap: 78.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 60.5
    contract_governance: 4.5
    contract_quality: 13.5
    developer_ergonomics: 47.0
    discoverability: 75.9
    operational_transparency: 0.0
  previous_composite: 33.3
  provenance:
    conformance: derived
    contracts:
      callable: 100.0
      derived: 5
      marker_coverage: 100.0
      total: 5
    mcp: derived
    skills: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Banking & Open Finance
    regime_id: banking_open_finance
    score: 38.0
  schema_version: 0.22.0
  scored_at: '2026-09-21'
  trend: flat
  upsert:
    applies: true
    score: 0.0
screenshot: https://raw.githubusercontent.com/api-evangelist/buxfer/refs/heads/main/screenshots/buxfer-2026-07-25T204124.png
security:
- kind: authentication
  name: Buxfer Authentication
  slug: buxfer-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Buxfer Domain Security
  slug: buxfer-domain-security
  summary_line: TLSv1.2 · HSTS
- kind: trust-center
  name: Buxfer Trust Center
  slug: buxfer-trust-center
  summary_line: ISO 27001, PCI DSS
slug: buxfer
tags:
- Company
- Personal Finance
- Money Management
- Budgeting
- Banking
- Fintech
- Financial Data
- Transaction
- Investment
- Expense Tracking
website: https://www.buxfer.com/
---
