---
access_model:
  confidence: high
  gated: none
  gated_source:
  - onboarding
  label: Paid · Self-serve signup
  onboarding: self-serve
  pricing: paid
  public: false
  source:
  - plans
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
    auth_clarity: negotiable
    consent_identity: false
    delegated_identity: documented
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: documented
    event_surface_described: true
    idempotency: documented
    mcp_server: false
    mcp_tool_quality: na
    openapi_examples: false
    operation_distinctiveness: distinct
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: derived
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 35.7
  scored_at: '2026-11-06'
agentic_access:
- acting_count: 7
  human_in_the_loop: 0
  name: Digits Com Agentic Access
  operation_count: 28
  slug: digits-com-agentic-access
  summary_line: 28 operations · 7 acting
api_count: 2
apis:
- description: Model Context Protocol server that lets AI clients like ChatGPT and Claude connect directly to Digits to query the ledger in natural language. Discovery is published as an MCP Server Card at /.well-kn
  name: Digits MCP Server
  slug: digits-com-mcp-server
- baseURL: https://connect.digits.com/v1
  baseurl_source: declared
  description: Ledger categories and dimensional axes (departments, locations, projects).
  name: Digits Chart of Accounts API
  slug: digits-com-chart-of-accounts-api
- baseURL: https://connect.digits.com/v1
  baseurl_source: declared
  description: Connected data sources feeding the ledger.
  name: Digits Connections API
  slug: digits-com-connections-api
- baseURL: https://connect.digits.com/v1
  baseurl_source: declared
  description: Balance Sheet, P&L, Cash Flow, Trial Balance, aging reports, and summaries.
  name: Digits Financial Statements API
  slug: digits-com-financial-statements-api
- baseURL: https://connect.digits.com/v1
  baseurl_source: declared
  description: Accounting-firm organizations, clients, entities, and employees.
  name: Digits Organizations API
  slug: digits-com-organizations-api
- baseURL: https://connect.digits.com/v1
  baseurl_source: declared
  description: Vendors, suppliers, customers, and other business relationships.
  name: Digits Parties API
  slug: digits-com-parties-api
- baseURL: https://connect.digits.com/v1
  baseurl_source: declared
  description: Push raw source data into the AGL for enrichment and categorization.
  name: Digits Sources API
  slug: digits-com-sources-api
- baseURL: https://connect.digits.com/v1
  baseurl_source: declared
  description: Read AI-categorized ledger transactions and journal entries.
  name: Digits Transactions API
  slug: digits-com-transactions-api
- baseURL: https://connect.digits.com/v1
  baseurl_source: declared
  description: Receive event notifications from Digits at a configured webhook endpoint; Digits POSTs a JSON event body and expects a 2xx acknowledgment (WebhookService.receiveWebhookEvent).
  name: Digits Webhooks API
  slug: digits-com-webhooks-api
- baseURL: https://connect.digits.com/v1
  baseurl_source: declared
  description: The Llms.txt API from Digits — 1 operation(s) for llms.txt.
  name: Digits Llms.txt API
  slug: digits-com-llms-txt-api
- baseURL: https://connect.digits.com/v1
  baseurl_source: declared
  description: The Sitemap.xml API from Digits — 1 operation(s) for sitemap.xml.
  name: Digits Sitemap.xml API
  slug: digits-com-sitemap-xml-api
- baseURL: https://connect.digits.com/v1
  baseurl_source: declared
  description: The .well Known API from Digits — 2 operation(s) for .well known.
  name: Digits .well Known API
  slug: digits-com-well-known-api
artifact_total: 39
asyncapis:
- description: ''
  name: Digits Com Webhooks
  slug: digits-com-webhooks
collections:
- collection_type: open
  name: Digits Connect Chart of Accounts API
  slug: open-digits-com-chart-of-accounts-api
- collection_type: open
  name: Digits Connect Chart of Accounts Connections API
  slug: open-digits-com-connections-api
- collection_type: open
  name: Digits Connect Chart of Accounts Financial Statements API
  slug: open-digits-com-financial-statements-api
- collection_type: open
  name: Digits Llms.txt API
  slug: open-digits-com-llms-txt-api
- collection_type: open
  name: Digits Connect Chart of Accounts Organizations API
  slug: open-digits-com-organizations-api
- collection_type: open
  name: Digits Connect Chart of Accounts Parties API
  slug: open-digits-com-parties-api
- collection_type: open
  name: Digits Llms.txt Sitemap.xml API
  slug: open-digits-com-sitemap-xml-api
- collection_type: open
  name: Digits Connect Chart of Accounts Sources API
  slug: open-digits-com-sources-api
- collection_type: open
  name: Digits Connect Chart of Accounts Transactions API
  slug: open-digits-com-transactions-api
- collection_type: open
  name: Digits Connect Chart of Accounts Webhooks API
  slug: open-digits-com-webhooks-api
- collection_type: open
  name: Digits Llms.txt .well Known API
  slug: open-digits-com-well-known-api
- collection_type: open
  name: Digits Connect API
  slug: open-digits-com
common:
- group: other
  href: https://artifacts.apis.io/digits-com/capabilities/digits-com-capability-edges.yml
  title: ''
  type: CapabilityMap
  url: capabilities/digits-com-capability-edges.yml
- group: agent
  href: https://artifacts.apis.io/digits-com/agentic-access/digits-com-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/digits-com-agentic-access.yml
- group: auth
  href: https://artifacts.apis.io/digits-com/security/digits-com-trust-center.yml
  title: ''
  type: TrustCenter
  url: security/digits-com-trust-center.yml
- group: auth
  href: https://artifacts.apis.io/digits-com/security/digits-com-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/digits-com-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/digits-com/security/digits-com-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/digits-com-domain-security.yml
- group: auth
  href: https://artifacts.apis.io/digits-com/authentication/digits-com-authentication.yml
  title: ''
  type: Authentication
  url: authentication/digits-com-authentication.yml
- group: auth
  href: https://artifacts.apis.io/digits-com/scopes/digits-com-scopes.yml
  title: ''
  type: OAuthScopes
  url: scopes/digits-com-scopes.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/digits
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/digits-financial
- group: company
  title: ''
  type: Website
  url: https://digits.com
- group: docs
  title: ''
  type: Documentation
  url: https://developer.digits.com
- group: commercial
  href: https://artifacts.apis.io/digits-com/plans/digits-com-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/digits-com-plans-pricing.yml
- group: operate
  href: https://artifacts.apis.io/digits-com/rate-limits/digits-com-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/digits-com-rate-limits.yml
- group: commercial
  href: https://artifacts.apis.io/digits-com/finops/digits-com-finops.yml
  title: ''
  type: FinOps
  url: finops/digits-com-finops.yml
- group: company
  title: ''
  type: Blog
  url: https://digits.com/blog/rss.xml
- group: start
  title: ''
  type: DeveloperPortal
  url: https://developer.digits.com
- group: docs
  title: ''
  type: APIReference
  url: https://developer.digits.com/reference/companyservice_get
- group: start
  title: ''
  type: GettingStarted
  url: https://developer.digits.com/docs/app-creation
- group: commercial
  title: ''
  type: Pricing
  url: https://digits.com/pricing
- group: start
  title: ''
  type: SignUp
  url: https://my.digits.com
- group: start
  title: ''
  type: Login
  url: https://my.digits.com
- group: commercial
  title: ''
  type: TermsOfService
  url: https://my.digits.com/legal/terms-of-service
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://my.digits.com/legal/privacy-policy
- group: operate
  title: ''
  type: Support
  url: https://help.digits.com
- group: auth
  title: ''
  type: Security
  url: https://digits.com/security/
- group: auth
  title: ''
  type: Compliance
  url: https://trust.digits.com
- group: other
  href: https://artifacts.apis.io/digits-com/overlays/digits-com-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/digits-com-overlay.yaml
- group: agent
  href: https://artifacts.apis.io/digits-com/mcp/digits-com-mcp.yml
  title: ''
  type: X-MCPServerCandidate
  url: mcp/digits-com-mcp.yml
- group: agent
  href: https://artifacts.apis.io/digits-com/llms/digits-com-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/digits-com-llms.txt
- group: agent
  href: https://artifacts.apis.io/digits-com/well-known/digits-com-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/digits-com-well-known.yml
- group: auth
  href: https://artifacts.apis.io/digits-com/well-known/digits-com-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/digits-com-security.txt
- group: design
  href: https://artifacts.apis.io/digits-com/conventions/digits-com-conventions.yml
  title: ''
  type: Conventions
  url: conventions/digits-com-conventions.yml
- group: design
  href: https://artifacts.apis.io/digits-com/conventions/digits-com-conventions.yml
  title: ''
  type: Idempotency
  url: conventions/digits-com-conventions.yml
- group: design
  href: https://artifacts.apis.io/digits-com/lifecycle/digits-com-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/digits-com-lifecycle.yml
- group: operate
  href: https://artifacts.apis.io/digits-com/lifecycle/digits-com-lifecycle.yml
  title: ''
  type: Deprecation
  url: lifecycle/digits-com-lifecycle.yml
- group: design
  href: https://artifacts.apis.io/digits-com/conformance/digits-com-conformance.yml
  title: ''
  type: Conformance
  url: conformance/digits-com-conformance.yml
- group: design
  href: https://artifacts.apis.io/digits-com/errors/digits-com-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/digits-com-problem-types.yml
- group: design
  href: https://artifacts.apis.io/digits-com/data-model/digits-com-data-model.yml
  title: ''
  type: DataModel
  url: data-model/digits-com-data-model.yml
- group: start
  href: https://artifacts.apis.io/digits-com/sandbox/digits-com-sandbox.yml
  title: ''
  type: Sandbox
  url: sandbox/digits-com-sandbox.yml
- group: design
  href: https://artifacts.apis.io/digits-com/asyncapi/digits-com-webhooks.yml
  title: ''
  type: Webhooks
  url: asyncapi/digits-com-webhooks.yml
- group: agent
  href: https://artifacts.apis.io/digits-com/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
created: '2026-07-01'
description: Digits is an AI-native accounting and bookkeeping platform for startups and their accountants, built around the Autonomous General Ledger (AGL) that auto-books the majority of transactions in real time. The Digits Connect API opens the AGL programmatically over REST with OAuth 2.0, letting partners send raw transaction, party, and dimension data for AI categorization and vendor enrichment, and read back ledger entries and financial statements. Digits also publishes an MCP server for AI agents (ChatGPT, Claude) to query the ledger.
finops:
- has_sources: true
  method: derived
  name: Digits Com Finops
  primary_unit: subscription
  service_category: ''
  slug: digits-com-finops
  template: false
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/digits-com.png
layout: provider
modified: '2026-08-08'
name: Digits
nav: Providers
network: true
overview: 'Digits publishes 12 API contracts indexed on the [APIs.io](https://apis.io/) network, including Chart of Accounts API, Connections API, Financial Statements API, and 9 more. Tagged areas include Accounting, Bookkeeping, Finance, General Ledger, and Artificial Intelligence.


  The Digits catalog on APIs.io includes 1 event-driven AsyncAPI specification and 1 Spectral governance ruleset.


  Digits'' developer surface includes authentication, documentation, engineering blog, API reference, getting-started guide, pricing, signup flow, and 34 more developer resources.'
plans:
- name: Digits Com Plans Pricing
  plan_count: 3
  slug: digits-com-plans-pricing
- name: Digits Com Price Estimates
  plan_count: 0
  slug: digits-com-price-estimates
random_paper: 0
rate_limits:
- limit_count: 2
  name: Digits Com Rate Limits
  slug: digits-com-rate-limits
rules:
- authorship: generated
  effective_rule_count: 103
  extends:
  - spectral:oas
  name: Digits API Rules
  rule_count: 62
  severity_counts:
    error: 57
    hint: 0
    info: 2
    warn: 3
  slug: digits-com-rules
scopes:
- name: Digits Com Scopes
  scope_count: 2
  slug: digits-com-scopes
  summary_line: 2 scopes · authorizationCode
score:
  band: strong
  composite: 59.9
  coverage:
    artifact_dirs: 30
    catalog_earned: 53.5
    catalog_earned_first_party: 12.0
    catalog_gap: 61.5
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 4.2
  facets:
    access_clarity: 65.8
    contract_governance: 31.8
    contract_quality: 54.3
    developer_ergonomics: 67.3
    discoverability: 64.3
    operational_transparency: 34.2
  previous_composite: 55.7
  provenance:
    agentic_access: derived
    conformance: first-party
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 27.3
      total: 11
    mcp: first-party
    skills: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 34.5
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: true
    score: 27.8
screenshot: https://apis.io/screenshots/digits-com/digits-com-2026-07-25T212036.png
security:
- kind: authentication
  name: Digits Com Authentication
  slug: digits-com-authentication
  summary_line: oauth2 · 1 scheme
- kind: domain-security
  name: Digits Com Domain Security
  slug: digits-com-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
- kind: vulnerability-disclosure
  name: Digits Com Vulnerability Disclosure
  slug: digits-com-vulnerability-disclosure
  summary_line: security.txt · contact published
- kind: trust-center
  name: Digits Com Trust Center
  slug: digits-com-trust-center
  summary_line: SOC 2
skill_count: 3
skills:
- name: Run the Digits bill-pay workflow
  slug: digits-com-bill-pay-workflow
- name: Read Digits financial statements
  slug: digits-com-read-financial-statements
- name: Sync source transactions into Digits
  slug: digits-com-sync-source-transactions
slug: digits-com
tags:
- Accounting
- Bookkeeping
- Finance
- General Ledger
- Artificial Intelligence
- Fintech
website: https://digits.com
---
