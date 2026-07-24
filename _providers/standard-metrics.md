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
    agent_skills: true
    agentic_access: true
    asyncapi_events: false
    auth_clarity: true
    consent_identity: false
    error_semantics: true
    idempotency: false
    mcp_server: true
    openapi_examples: false
    rate_limit_signal: true
    spec_presence: true
    well_known_catalog: true
  schema_version: 0.1
  score: 76.0
  scored_at: '2026-07-23'
agentic_access:
- acting_count: 19
  human_in_the_loop: 1
  name: Standard Metrics Agentic Access
  operation_count: 34
  slug: standard-metrics-agentic-access
  summary_line: 34 operations · 19 acting · 1 human-in-the-loop
api_count: 14
apis:
- description: The budgets API from Standard Metrics — 1 operation(s) for budgets.
  name: Standard Metrics budgets API
  slug: standard-metrics-budgets-api
- description: The cap_table API from Standard Metrics — 10 operation(s) for cap_table.
  name: Standard Metrics cap_table API
  slug: standard-metrics-cap-table-api
- description: The companies API from Standard Metrics — 3 operation(s) for companies.
  name: Standard Metrics companies API
  slug: standard-metrics-companies-api
- description: The custom-columns API from Standard Metrics — 3 operation(s) for custom-columns.
  name: Standard Metrics custom-columns API
  slug: standard-metrics-custom-columns-api
- description: The documents API from Standard Metrics — 2 operation(s) for documents.
  name: Standard Metrics documents API
  slug: standard-metrics-documents-api
- description: The firm-details API from Standard Metrics — 1 operation(s) for firm-details.
  name: Standard Metrics firm-details API
  slug: standard-metrics-firm-details-api
- description: The funds API from Standard Metrics — 1 operation(s) for funds.
  name: Standard Metrics funds API
  slug: standard-metrics-funds-api
- description: The information-reports API from Standard Metrics — 1 operation(s) for information-reports.
  name: Standard Metrics information-reports API
  slug: standard-metrics-information-reports-api
- description: The information-requests API from Standard Metrics — 1 operation(s) for information-requests.
  name: Standard Metrics information-requests API
  slug: standard-metrics-information-requests-api
- description: The metrics API from Standard Metrics — 3 operation(s) for metrics.
  name: Standard Metrics metrics API
  slug: standard-metrics-metrics-api
- description: The notes API from Standard Metrics — 1 operation(s) for notes.
  name: Standard Metrics notes API
  slug: standard-metrics-notes-api
- description: The O API from Standard Metrics — 1 operation(s) for o.
  name: Standard Metrics O API
  slug: standard-metrics-o-api
- description: The users API from Standard Metrics — 1 operation(s) for users.
  name: Standard Metrics users API
  slug: standard-metrics-users-api
- description: The whoami API from Standard Metrics — 1 operation(s) for whoami.
  name: Standard Metrics whoami API
  slug: standard-metrics-whoami-api
artifact_total: 21
common:
- group: company
  title: ''
  type: Website
  url: https://standardmetrics.io
- group: start
  title: ''
  type: DeveloperPortal
  url: https://docs.standardmetrics.io
- group: docs
  title: ''
  type: Documentation
  url: https://docs.standardmetrics.io/introduction
- group: docs
  title: ''
  type: APIReference
  url: https://docs.standardmetrics.io/api-reference/setting-up
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.standardmetrics.io/guides/initialsetup
- group: company
  title: ''
  type: Blog
  url: https://standardmetrics.io/blog-posts/
- group: operate
  title: ''
  type: Support
  url: https://standardmetrics.io/faq/
- group: start
  title: ''
  type: SignUp
  url: https://standardmetrics.io/request-a-demo/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://standardmetrics.io/terms-of-service/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://standardmetrics.io/privacy-policy/
- group: operate
  title: ''
  type: ChangeLog
  url: https://docs.standardmetrics.io/changelog
- group: auth
  title: ''
  type: Authentication
  url: authentication/standard-metrics-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/standard-metrics-scopes.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/standard-metrics-mcp.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/standard-metrics-llms.txt
- group: agent
  title: ''
  type: WellKnown
  url: well-known/standard-metrics-well-known.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/standard-metrics-problem-types.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/standard-metrics-lifecycle.yml
- group: operate
  title: ''
  type: Deprecation
  url: lifecycle/standard-metrics-lifecycle.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/standard-metrics-conventions.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/standard-metrics-rate-limits.yml
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/standard-metrics-changelog.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/standard-metrics-conformance.yml
- group: auth
  title: ''
  type: Compliance
  url: https://standardmetrics.io/security/
- group: design
  title: ''
  type: DataModel
  url: data-model/standard-metrics-data-model.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/standard-metrics-agentic-access.yml
- group: auth
  title: ''
  type: TrustCenter
  url: security/standard-metrics-trust-center.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/standard-metrics-domain-security.yml
created: '2026-07-17'
description: Standard Metrics is an AI-driven portfolio management platform for venture capital and private equity firms. It centralizes portfolio company performance data, financial metrics, documents, cap-table and investment data, and notes so investors can streamline portfolio reviews, audits, and LP reporting while reducing the reporting burden on portfolio companies. Standard Metrics exposes a REST API (OAuth2 client-credentials, Bearer tokens) covering companies, metrics, budgets, documents, funds, information requests, notes, users, and a beta Investment Data API for cap-table financing events, securities, share classes, and transactions. It also publishes two official remote MCP servers that connect Claude, ChatGPT, and other LLM clients directly to firm data.
image: https://standardmetrics.io/wp-content/uploads/2024/07/Standard-Metrics-Thumbnail.jpg
layout: provider
mcp_servers:
- description: ''
  name: standard-metrics-mcp.yml
  slug: standard-metrics-mcpyml
modified: '2026-07-21'
name: Standard Metrics
nav: Providers
network: true
overview: 'Standard Metrics publishes 14 APIs on the [APIs.io](https://apis.io/) network, including budgets API, cap_table API, companies API, and 11 more. Tagged areas include Company, Venture Capital, Private Equity, Portfolio Management, and Financial Data.


  Standard Metrics'' developer surface includes documentation, API reference, getting-started guide, engineering blog, support, signup flow, changelog, and 22 more developer resources.'
random_paper: 21
rate_limits:
- limit_count: 2
  name: Standard Metrics Rate Limits
  slug: standard-metrics-rate-limits
scopes:
- name: Standard Metrics Scopes
  scope_count: 3
  slug: standard-metrics-scopes
  summary_line: 3 scopes
score:
  band: developing
  composite: 51.8
  delta: 0.0
  facets:
    commercial_clarity: 50.0
    contract_quality: 50.0
    developer_ergonomics: 67.4
    discoverability: 100.0
    governance: 0.0
    operational_transparency: 44.7
  previous_composite: 51.8
  schema_version: 0.5
  scored_at: '2026-07-23'
  trend: flat
security:
- kind: authentication
  name: Standard Metrics Authentication
  slug: standard-metrics-authentication
  summary_line: oauth2/http · 3 schemes
- kind: domain-security
  name: Standard Metrics Domain Security
  slug: standard-metrics-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
- kind: trust-center
  name: Standard Metrics Trust Center
  slug: standard-metrics-trust-center
  summary_line: SOC 2, GDPR
slug: standard-metrics
tags:
- Company
- Venture Capital
- Private Equity
- Portfolio Management
- Financial Data
- Investment Data
- Cap Table
- Metrics
- Reporting
- MCP
website: https://standardmetrics.io
---
