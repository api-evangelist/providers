---
access_model:
  confidence: high
  label: Freemium · Self-serve signup
  onboarding: self-serve
  pricing: freemium
  public: false
  source:
  - plans
  - authentication
  trial: false
  try_now: true
agent_readiness:
  band: agent-ready
  band_gated_from: agent-native
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: negotiable
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: verified
    event_surface_described: true
    idempotency: false
    mcp_server: documented
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 38.8
  scored_at: '2026-09-10'
agentic_access:
- acting_count: 5
  human_in_the_loop: 0
  name: Fis Agentic Access
  operation_count: 8
  slug: fis-agentic-access
  summary_line: 8 operations · 5 acting
api_count: 2
apis:
- description: FIS (Fidelity National Information Services) provides core banking platforms including the Systematics suite. APIs bridge mainframe-based account processing, transaction management, and loan servicing
  name: FIS Core Banking API
  slug: fis-core-banking-api
- description: FIS wealth management APIs enable integration with portfolio management, account aggregation, trading, and advisory systems for wealth management platforms and financial advisors.
  name: FIS Wealth Management API
  slug: fis-wealth-management-api
- baseURL: https://api.fisglobal.com
  baseurl_source: declared
  description: Account information and balance inquiries
  name: FIS Global Accounts API
  slug: fis-accounts-api
- baseURL: https://api.fisglobal.com
  baseurl_source: declared
  description: ACH (Automated Clearing House) payment operations
  name: FIS Global ACH API
  slug: fis-ach-api
- baseURL: https://api.fisglobal.com
  baseurl_source: declared
  description: Initiate and manage payment transactions
  name: FIS Global Payments API
  slug: fis-payments-api
- baseURL: https://api.fisglobal.com
  baseurl_source: declared
  description: Transaction history and status
  name: FIS Global Transactions API
  slug: fis-transactions-api
- baseURL: https://api.fisglobal.com
  baseurl_source: declared
  description: Domestic and international wire transfer operations
  name: FIS Global Wire Transfers API
  slug: fis-wire-transfers-api
- baseURL: https://api.railz.ai
  baseurl_source: declared
  description: FIS Accounting Data as a Service (shipped as Railz before FIS acquired it) reads and writes a business's accounting, banking and commerce data through an authorised connection to that business's own s
  name: FIS Accounting Data as a Service
  slug: fis-accounting-data-as-a-service
- description: FIS Code Connect is the developer marketplace exposing FIS APIs across payments, banking, capital markets, and wealth management products. Access to most APIs requires a partner agreement and authenti
  name: FIS Code Connect API Marketplace
  slug: code-connect
artifact_total: 30
asyncapis:
- description: ''
  name: Fis Webhooks
  slug: fis-webhooks
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: FIS Payments Accounts API
  slug: open-fis-accounts-api
- collection_type: open
  name: FIS Payments Accounts ACH API
  slug: open-fis-ach-api
- collection_type: open
  name: FIS Accounts Payments API
  slug: open-fis-payments-api
- collection_type: open
  name: FIS Payments API
  slug: open-fis-payments
- collection_type: open
  name: FIS Payments Accounts Transactions API
  slug: open-fis-transactions-api
- collection_type: open
  name: FIS Payments Accounts Wire Transfers API
  slug: open-fis-wire-transfers-api
common:
- group: company
  title: ''
  type: InvestorRelations
  url: https://investor.fisglobal.com/
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/fis-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/fis-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/fis-authentication.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/FISGlobal
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/fis
- group: company
  title: ''
  type: Website
  url: https://www.fisglobal.com/
- group: agent
  title: ''
  type: WellKnown
  url: well-known/fis-well-known.yml
- group: auth
  title: ''
  type: SecurityTxt
  url: well-known/fis-security.txt
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/fis-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: Security
  url: https://www.fisglobal.com/en/responsible-disclosure
- group: auth
  title: ''
  type: TrustCenter
  url: security/fis-trust-center.yml
- group: build
  title: ''
  type: Packages
  url: packages/fis-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/fis-packages.yml
- group: design
  title: ''
  type: Components
  url: components/fis-components.yml
- group: start
  title: ''
  type: Sandbox
  url: sandbox/fis-sandbox.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/fis-lifecycle.yml
- group: operate
  title: ''
  type: StatusPage
  url: https://status.railz.ai
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/fis-changelog.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/fis-rate-limits.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/fis-plans-pricing.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/fis-problem-types.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/fis-conventions.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/fis-data-model.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/fis-conformance.yml
- group: design
  title: ''
  type: Webhooks
  url: asyncapi/fis-webhooks.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/fis-mcp.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/fis-llms.txt
- group: start
  title: ''
  type: DeveloperPortal
  url: https://codeconnect.fisglobal.com/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.railz.ai/
- group: docs
  title: ''
  type: APIReference
  url: https://docs.railz.ai/reference
- group: start
  title: ''
  type: GettingStarted
  url: https://codeconnect.fisglobal.com/app/guides/gettingstarted
- group: start
  title: ''
  type: SignUp
  url: https://codeconnect.fisglobal.com/app/userregister
- group: operate
  title: ''
  type: Support
  url: https://codeconnect.fisglobal.com/app/guides/faqs
- group: commercial
  title: ''
  type: Pricing
  url: https://www.fisglobal.com/products/accounting-data-as-a-service
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.fisglobal.com/terms-of-use
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.fisglobal.com/privacy
- group: company
  title: ''
  type: Blog
  url: https://www.fisglobal.com/insights
created: '2026-04-28'
description: FIS (Fidelity National Information Services) is a global leader in financial technology providing APIs for core banking, payments, wealth management, and capital markets through the CodeConnect API marketplace. APIs connect financial institutions, fintechs, and enterprises to FIS banking and payment infrastructure.
finops:
- name: Fis Finops
  service_category: Financial Services Software
  slug: fis-finops
image: https://codeconnect.fisglobal.com/assets/FIS_codeConnect_logo_white.svg
json_schemas:
- name: FIS Payment
  property_count: 15
  slug: fis-payment
jsonld:
- class_count: 12
  name: Fis Context
  property_count: 10
  slug: fis-context
layout: provider
mcp_servers:
- description: ''
  name: FIS Global MCP Server
  slug: fis-global-mcp-server
modified: '2026-09-10'
name: FIS Global
nav: Providers
network: true
overview: 'FIS Global publishes 6 APIs on the [APIs.io](https://apis.io/) network, including Accounts API, ACH API, Payments API, and 3 more. Tagged areas include Banking, Core Banking, Financial-Services, Payments, and Fintech.


  The FIS Global catalog on APIs.io includes 1 event-driven AsyncAPI specification, 1 JSON-LD context, and 1 Spectral governance ruleset.


  FIS Global''s developer surface includes authentication, sandbox, changelog, documentation, API reference, getting-started guide, signup flow, and 32 more developer resources.'
plans:
- name: Fis Plans Pricing
  plan_count: 2
  slug: fis-plans-pricing
random_paper: 7
rate_limits:
- limit_count: 0
  name: Fis Rate Limits
  slug: fis-rate-limits
rules:
- effective_rule_count: 5
  extends: []
  name: FIS Global API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 3
  slug: fis-jsonschema-spectral-rules
scopes:
- name: Fis Scopes
  scope_count: 0
  slug: fis-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: strong
  composite: 65.8
  coverage:
    artifact_dirs: 29
    catalog_earned: 57.3
    catalog_earned_first_party: 8.0
    catalog_gap: 57.8
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 33.9
  facets:
    access_clarity: 81.6
    commercial_clarity: 81.6
    contract_governance: 14.4
    contract_quality: 70.3
    developer_ergonomics: 63.7
    discoverability: 59.3
    governance: 14.4
    operational_transparency: 52.6
  previous_composite: 31.9
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 0.0
      derived: 0
      marker_coverage: 0.0
      total: 5
    mcp: first-party
    skills: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Banking & Open Finance
    regime_id: banking_open_finance
    score: 67.1
  schema_version: 0.20.0
  scored_at: '2026-09-10'
  trend: rising
  upsert:
    applies: true
    score: 0.0
screenshot: https://raw.githubusercontent.com/api-evangelist/fis/refs/heads/main/screenshots/fis-2026-06-20T181251.png
security:
- kind: authentication
  name: Fis Authentication
  slug: fis-authentication
  summary_line: http/basic · 2 schemes
- kind: domain-security
  name: Fis Domain Security
  slug: fis-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Fis Vulnerability Disclosure
  slug: fis-vulnerability-disclosure
  summary_line: Bugcrowd · contact published
- kind: trust-center
  name: Fis Trust Center
  slug: fis-trust-center
  summary_line: trust center published
slug: fis
tags:
- Banking
- Core Banking
- Financial-Services
- Payments
- Fintech
website: https://www.fisglobal.com/
---
