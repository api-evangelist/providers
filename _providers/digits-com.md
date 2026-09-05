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
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 36.2
  scored_at: '2026-09-04'
agentic_access:
- acting_count: 8
  human_in_the_loop: 0
  name: Digits Com Agentic Access
  operation_count: 24
  slug: digits-com-agentic-access
  summary_line: 24 operations · 8 acting
api_count: 2
apis:
- baseURL: https://connect.digits.com/v1
  baseurl_source: declared
  description: Receive event notifications from Digits at a configured webhook endpoint; Digits POSTs a JSON event body and expects a 2xx acknowledgment (WebhookService.receiveWebhookEvent).
  name: Digits Webhooks API
  slug: digits-com-webhooks-api
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
  description: Event delivery to partner-configured endpoints.
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
artifact_total: 36
asyncapis:
- description: ''
  name: Digits Com Webhooks
  slug: digits-com-webhooks
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
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
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/digits-com-agentic-access.yml
- group: auth
  title: ''
  type: TrustCenter
  url: security/digits-com-trust-center.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/digits-com-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/digits-com-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/digits-com-authentication.yml
- group: auth
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
  title: ''
  type: Plans
  url: plans/digits-com-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/digits-com-rate-limits.yml
- group: commercial
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
  title: ''
  type: Overlay
  url: overlays/digits-com-overlay.yaml
- group: agent
  title: ''
  type: X-MCPServerCandidate
  url: mcp/digits-com-mcp.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/digits-com-llms.txt
- group: agent
  title: ''
  type: WellKnown
  url: well-known/digits-com-well-known.yml
- group: auth
  title: ''
  type: SecurityTxt
  url: well-known/digits-com-security.txt
- group: design
  title: ''
  type: Conventions
  url: conventions/digits-com-conventions.yml
- group: design
  title: ''
  type: Idempotency
  url: conventions/digits-com-conventions.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/digits-com-lifecycle.yml
- group: operate
  title: ''
  type: Deprecation
  url: lifecycle/digits-com-lifecycle.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/digits-com-conformance.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/digits-com-problem-types.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/digits-com-data-model.yml
- group: start
  title: ''
  type: Sandbox
  url: sandbox/digits-com-sandbox.yml
- group: design
  title: ''
  type: Webhooks
  url: asyncapi/digits-com-webhooks.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
created: '2026-07-01'
description: Digits is an AI-native accounting and bookkeeping platform for startups and their accountants, built around the Autonomous General Ledger (AGL) that auto-books the majority of transactions in real time. The Digits Connect API opens the AGL programmatically over REST with OAuth 2.0, letting partners send raw transaction, party, and dimension data for AI categorization and vendor enrichment, and read back ledger entries and financial statements. Digits also publishes an MCP server for AI agents (ChatGPT, Claude) to query the ledger.
finops:
- name: Digits Com Finops
  service_category: Business Applications
  slug: digits-com-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/digits-com.png
layout: provider
modified: '2026-08-08'
name: Digits
nav: Providers
network: true
overview: 'Digits publishes 12 APIs on the [APIs.io](https://apis.io/) network, including Webhooks API, Chart of Accounts API, Connections API, and 9 more. Tagged areas include Accounting, Bookkeeping, Finance, General Ledger, and Artificial Intelligence.


  The Digits catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  Digits'' developer surface includes authentication, documentation, engineering blog, API reference, getting-started guide, pricing, signup flow, and 33 more developer resources.'
plans:
- name: Digits Com Plans Pricing
  plan_count: 2
  slug: digits-com-plans-pricing
random_paper: 0
rate_limits:
- limit_count: 2
  name: Digits Com Rate Limits
  slug: digits-com-rate-limits
scopes:
- name: Digits Com Scopes
  scope_count: 2
  slug: digits-com-scopes
  summary_line: 2 scopes · authorizationCode
score:
  band: developing
  composite: 51.4
  coverage:
    artifact_dirs: 23
    catalog_earned: 56.0
    catalog_earned_first_party: 0.0
    catalog_gap: 59.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -0.8
  facets:
    access_clarity: 55.3
    commercial_clarity: 55.3
    contract_governance: 18.2
    contract_quality: 57.9
    developer_ergonomics: 48.2
    discoverability: 75.9
    governance: 18.2
    operational_transparency: 50.0
  previous_composite: 52.2
  provenance:
    agentic_access: derived
    conformance: first-party
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 11
    mcp: first-party
    skills: derived
  schema_version: 0.18.3
  scored_at: '2026-09-04'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/digits-com/refs/heads/main/screenshots/digits-com-2026-07-25T212036.png
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
