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
  band: agent-ready
  band_gated_from: agent-native
  dimensions:
    agent_card: conformant
    agent_skills: unknown
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: served
    consent_identity: false
    delegated_identity: served
    dry_run_mode: false
    dynamic_client_registration: true
    error_semantics: documented
    event_surface_described: false
    idempotency: false
    mcp_server: documented
    mcp_tool_quality: na
    openapi_examples: partial
    operation_distinctiveness: distinct
    pagination_ratio: false
    protected_resource_metadata: verified
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: true
  schema_version: '0.2'
  score: 55.6
  scored_at: '2026-11-06'
agentic_access:
- acting_count: 39
  human_in_the_loop: 0
  name: Ai2Fin Com Agentic Access
  operation_count: 71
  slug: ai2fin-com-agentic-access
  summary_line: 71 operations · 39 acting
api_count: 1
apis:
- baseURL: https://api.ai2fin.com
  baseurl_source: declared
  description: AI-driven categorization and tax analysis endpoints
  name: AI2Fin AI Analysis API
  slug: ai2fin-com-ai-analysis-api
- baseURL: https://api.ai2fin.com
  baseurl_source: declared
  description: Chat conversations, messaging, and assistant file handling
  name: AI2Fin AI Assistant API
  slug: ai2fin-com-ai-assistant-api
- baseURL: https://api.ai2fin.com
  baseurl_source: declared
  description: AI-powered categorization and tax analysis
  name: AI2Fin AI Services API
  slug: ai2fin-com-ai-services-api
- baseURL: https://api.ai2fin.com
  baseurl_source: declared
  description: Financial analytics and tax report generation
  name: AI2Fin Analytics & Reports API
  slug: ai2fin-com-analytics-reports-api
- baseURL: https://api.ai2fin.com
  baseurl_source: declared
  description: User authentication and authorization
  name: AI2Fin Authentication API
  slug: ai2fin-com-authentication-api
- baseURL: https://api.ai2fin.com
  baseurl_source: declared
  description: Custom rules engine for automated workflows
  name: AI2Fin Automation API
  slug: ai2fin-com-automation-api
- baseURL: https://api.ai2fin.com
  baseurl_source: declared
  description: First-party endpoints for managing your own transactions and CSV imports. These return your own account data in your own authenticated session; they are not a third-party integration surface. Data syn
  name: AI2Fin Bank Transactions API
  slug: ai2fin-com-bank-transactions-api
- baseURL: https://api.ai2fin.com
  baseurl_source: declared
  description: Bill management with pattern recognition and auto-linking
  name: AI2Fin Bills & Recurring Payments API
  slug: ai2fin-com-bills-recurring-payments-api
- baseURL: https://api.ai2fin.com
  baseurl_source: declared
  description: Transaction and expense category management
  name: AI2Fin Categories API
  slug: ai2fin-com-categories-api
- baseURL: https://api.ai2fin.com
  baseurl_source: declared
  description: Expense tracking with tax deduction support
  name: AI2Fin Expenses API
  slug: ai2fin-com-expenses-api
- baseURL: https://api.ai2fin.com
  baseurl_source: declared
  description: Global GST/VAT rate lookup and calculations
  name: AI2Fin GST & Tax API
  slug: ai2fin-com-gst-tax-api
- baseURL: https://api.ai2fin.com
  baseurl_source: declared
  description: 'Model Context Protocol endpoints for AI integrations. Finance MCP server with 65+ tools for expense tracking, tax deductions, bill management, and financial analysis. Supports OAuth (JWT) and API key '
  name: AI2Fin MCP Server API
  slug: ai2fin-com-mcp-server-api
- baseURL: https://api.ai2fin.com
  baseurl_source: declared
  description: Receipt ingestion, AI analysis, and linkage APIs
  name: AI2Fin Receipts & Attachments API
  slug: ai2fin-com-receipts-attachments-api
- baseURL: https://api.ai2fin.com
  baseurl_source: declared
  description: AI-powered unified search across all entities
  name: AI2Fin Search API
  slug: ai2fin-com-search-api
- baseURL: https://api.ai2fin.com
  baseurl_source: declared
  description: Category sets, multi-category assignments, and transaction history (Elite+ only)
  name: AI2Fin Smart Categories API
  slug: ai2fin-com-smart-categories-api
- baseURL: https://api.ai2fin.com
  baseurl_source: declared
  description: Subscription and quota management
  name: AI2Fin Subscription API
  slug: ai2fin-com-subscription-api
- baseURL: https://api.ai2fin.com
  baseurl_source: declared
  description: Vehicle registration and business trip tracking
  name: AI2Fin Travel & Vehicles API
  slug: ai2fin-com-travel-vehicles-api
artifact_total: 34
common:
- group: agent
  href: https://artifacts.apis.io/ai2fin-com/agentic-access/ai2fin-com-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/ai2fin-com-agentic-access.yml
- group: design
  href: https://artifacts.apis.io/ai2fin-com/rules/ai2fin-com-rules.yml
  title: ''
  type: Spectral
  url: rules/ai2fin-com-rules.yml
- group: design
  href: https://artifacts.apis.io/ai2fin-com/json-ld/ai2fin-com-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/ai2fin-com-context.jsonld
- group: design
  href: https://artifacts.apis.io/ai2fin-com/vocabulary/ai2fin-com-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/ai2fin-com-vocabulary.yml
- group: agent
  href: https://artifacts.apis.io/ai2fin-com/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: design
  href: https://artifacts.apis.io/ai2fin-com/data-model/ai2fin-com-data-model.yml
  title: ''
  type: DataModel
  url: data-model/ai2fin-com-data-model.yml
- group: design
  href: https://artifacts.apis.io/ai2fin-com/conventions/ai2fin-com-conventions.yml
  title: ''
  type: Conventions
  url: conventions/ai2fin-com-conventions.yml
- group: auth
  title: ''
  type: Compliance
  url: https://ai2fin.com/security
- group: auth
  href: https://artifacts.apis.io/ai2fin-com/authentication/ai2fin-com-authentication.yml
  title: ''
  type: Authentication
  url: authentication/ai2fin-com-authentication.yml
- group: design
  href: https://artifacts.apis.io/ai2fin-com/errors/ai2fin-com-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/ai2fin-com-problem-types.yml
- group: design
  href: https://artifacts.apis.io/ai2fin-com/conformance/ai2fin-com-conformance.yml
  title: ''
  type: Conformance
  url: conformance/ai2fin-com-conformance.yml
- group: agent
  href: https://artifacts.apis.io/ai2fin-com/llms/ai2fin-com-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/ai2fin-com-llms.txt
- group: other
  href: https://artifacts.apis.io/ai2fin-com/a2a/ai2fin-com-a2a.yml
  title: ''
  type: AgentCard
  url: a2a/ai2fin-com-a2a.yml
- group: build
  href: https://artifacts.apis.io/ai2fin-com/mcp/ai2fin-com-tool-crosswalk.yml
  title: ''
  type: ToolCrosswalk
  url: mcp/ai2fin-com-tool-crosswalk.yml
- group: agent
  href: https://artifacts.apis.io/ai2fin-com/mcp/ai2fin-com-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/ai2fin-com-mcp.yml
- group: auth
  href: https://artifacts.apis.io/ai2fin-com/well-known/ai2fin-com-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/ai2fin-com-security.txt
- group: auth
  href: https://artifacts.apis.io/ai2fin-com/well-known/ai2fin-com-docs-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/ai2fin-com-docs-security.txt
- group: auth
  href: https://artifacts.apis.io/ai2fin-com/well-known/ai2fin-com-app-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/ai2fin-com-app-security.txt
- group: auth
  href: https://artifacts.apis.io/ai2fin-com/well-known/ai2fin-com-api-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/ai2fin-com-api-security.txt
- group: agent
  href: https://artifacts.apis.io/ai2fin-com/well-known/ai2fin-com-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/ai2fin-com-well-known.yml
- group: other
  href: https://artifacts.apis.io/ai2fin-com/hosts/ai2fin-com-hosts.yml
  title: ''
  type: Hosts
  url: hosts/ai2fin-com-hosts.yml
- group: other
  href: https://artifacts.apis.io/ai2fin-com/vendors/ai2fin-com-vendors.yml
  title: ''
  type: Vendors
  url: vendors/ai2fin-com-vendors.yml
- group: auth
  title: ''
  type: Security
  url: https://ai2fin.com/security
- group: company
  title: ''
  type: Newsroom
  url: https://ai2fin.com/press
- group: auth
  href: https://artifacts.apis.io/ai2fin-com/security/ai2fin-com-trust-center.yml
  title: ''
  type: TrustCenter
  url: security/ai2fin-com-trust-center.yml
- group: auth
  href: https://artifacts.apis.io/ai2fin-com/security/ai2fin-com-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/ai2fin-com-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/ai2fin-com/security/ai2fin-com-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/ai2fin-com-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://ai2fin.com/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://ai2fin.com/developers
- group: docs
  title: ''
  type: Documentation
  url: https://docs.ai2fin.com
- group: docs
  title: ''
  type: APIReference
  url: https://docs.ai2fin.com
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.ai2fin.com
- group: operate
  title: ''
  type: Support
  url: https://ai2fin.com/contact
- group: company
  title: ''
  type: Blog
  url: https://ai2fin.com/blog
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/ai2fin
- group: commercial
  title: ''
  type: Pricing
  url: https://ai2fin.com/pricing
- group: commercial
  title: ''
  type: TermsOfService
  url: https://ai2fin.com/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://ai2fin.com/privacy
coverage:
  detail: the company serves an API surface but requires credentials before any description of it can be read
  evidence:
  - status: null
    url: https://docs.ai2fin.com/mcp
  - status: 401
    url: https://api.ai2fin.com/mcp
  - status: 401
    url: https://app.ai2fin.com/api/mcp
  - status: 200
    url: https://ai2fin.com/
  reason: partner-login
  state: gated
created: '2026-11-01'
description: Track and categorise transactions, find tax deductions and estimate what you owe with 2Fin. Intelligent money tools in every country. Start free today. 2Fin is a tax and money app for employees, sole traders and people who are both, available in every country — plus freelancers, students, property investors and small businesses.
image: https://ai2fin.com/logo.png
json_schemas:
- name: BankTransaction
  property_count: 13
  slug: ai2fin-com-bank-transaction
- name: BillPatternInput
  property_count: 7
  slug: ai2fin-com-bill-pattern-input
- name: CategorySet
  property_count: 12
  slug: ai2fin-com-category-set
- name: CustomRuleInput
  property_count: 7
  slug: ai2fin-com-custom-rule-input
- name: TransactionCategory
  property_count: 11
  slug: ai2fin-com-transaction-category
- name: TransactionFieldHistory
  property_count: 11
  slug: ai2fin-com-transaction-field-history
jsonld:
- class_count: 29
  name: Ai2Fin Com Context
  property_count: 114
  slug: ai2fin-com-context
layout: provider
mcp_servers:
- description: Remote MCP server at api.ai2fin.com.
  name: AI2Fin MCP Server
  slug: ai2fin-com-mcp-yml
modified: '2026-11-01'
name: AI2Fin
nav: Providers
network: true
overview: 'AI2Fin publishes 17 API contracts indexed on the [APIs.io](https://apis.io/) network, including AI Analysis API, AI Assistant API, AI Services API, and 14 more. Tagged areas include Finance, Tax, Personal Finance, Software-as-a-Service, and Employee Benefits.


  The AI2Fin catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  AI2Fin''s developer surface includes authentication, documentation, API reference, getting-started guide, support, engineering blog, pricing, and 31 more developer resources.'
plans:
- name: Ai2Fin Com Plans Pricing
  plan_count: 0
  slug: ai2fin-com-plans-pricing
random_paper: 21
rate_limits:
- limit_count: 0
  name: Ai2Fin Com Rate Limits
  slug: ai2fin-com-rate-limits
rules:
- authorship: generated
  effective_rule_count: 52
  extends:
  - spectral:oas
  name: AI2Fin API Rules
  rule_count: 11
  severity_counts:
    error: 9
    hint: 0
    info: 1
    warn: 1
  slug: ai2fin-com-rules
scopes:
- name: Ai2Fin Com Scopes
  scope_count: 0
  slug: ai2fin-com-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: developing
  composite: 42.7
  coverage:
    artifact_dirs: 30
    catalog_earned: 62.8
    catalog_earned_first_party: 0.0
    catalog_gap: 52.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -10.6
  facets:
    access_clarity: 27.6
    contract_governance: 22.0
    contract_quality: 60.8
    developer_ergonomics: 41.0
    discoverability: 65.8
    operational_transparency: 7.9
  previous_composite: 53.3
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 17
    mcp: first-party
    skills: unknown
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 38.7
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: falling
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: authentication
  name: Ai2Fin Com Authentication
  slug: ai2fin-com-authentication
  summary_line: 2 schemes
- kind: domain-security
  name: Ai2Fin Com Domain Security
  slug: ai2fin-com-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
- kind: vulnerability-disclosure
  name: Ai2Fin Com Vulnerability Disclosure
  slug: ai2fin-com-vulnerability-disclosure
  summary_line: security.txt · contact published
- kind: trust-center
  name: Ai2Fin Com Trust Center
  slug: ai2fin-com-trust-center
  summary_line: SOC 2, ISO 27001, PCI DSS, GDPR
slug: ai2fin-com
tags:
- Finance
- Tax
- Personal Finance
- Software-as-a-Service
- Employee Benefits
website: https://ai2fin.com/
---
