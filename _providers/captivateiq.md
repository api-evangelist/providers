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
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: false
    agentic_commerce: false
    auth_clarity: served
    consent_identity: false
    delegated_identity: served
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: documented
    event_surface_described: false
    idempotency: false
    mcp_server: documented
    openapi_examples: partial
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 36.0
  scored_at: '2026-08-26'
api_count: 16
apis:
- description: The Attribute Worksheets API from CaptivateIQ — 5 operation(s) for attribute worksheets.
  name: CaptivateIQ Attribute Worksheets API
  slug: captivateiq-attribute-worksheets-api
- description: The Audit Logs API from CaptivateIQ — 1 operation(s) for audit logs.
  name: CaptivateIQ Audit Logs API
  slug: captivateiq-audit-logs-api
- description: The Commission Plans API from CaptivateIQ — 5 operation(s) for commission plans.
  name: CaptivateIQ Commission Plans API
  slug: captivateiq-commission-plans-api
- description: The Dashboards API from CaptivateIQ — 2 operation(s) for dashboards.
  name: CaptivateIQ Dashboards API
  slug: captivateiq-dashboards-api
- description: The Data Workbooks API from CaptivateIQ — 2 operation(s) for data workbooks.
  name: CaptivateIQ Data Workbooks API
  slug: captivateiq-data-workbooks-api
- description: The Data Worksheets API from CaptivateIQ — 8 operation(s) for data worksheets.
  name: CaptivateIQ Data Worksheets API
  slug: captivateiq-data-worksheets-api
- description: The Employee Assumptions API from CaptivateIQ — 3 operation(s) for employee assumptions.
  name: CaptivateIQ Employee Assumptions API
  slug: captivateiq-employee-assumptions-api
- description: The Employees API from CaptivateIQ — 4 operation(s) for employees.
  name: CaptivateIQ Employees API
  slug: captivateiq-employees-api
- description: The Hierarchies API from CaptivateIQ — 6 operation(s) for hierarchies.
  name: CaptivateIQ Hierarchies API
  slug: captivateiq-hierarchies-api
- description: The Jobs API from CaptivateIQ — 4 operation(s) for jobs.
  name: CaptivateIQ Jobs API
  slug: captivateiq-jobs-api
- description: The Metadata API from CaptivateIQ — 1 operation(s) for metadata.
  name: CaptivateIQ Metadata API
  slug: captivateiq-metadata-api
- description: The Payouts API from CaptivateIQ — 8 operation(s) for payouts.
  name: CaptivateIQ Payouts API
  slug: captivateiq-payouts-api
- description: The Report Models API from CaptivateIQ — 5 operation(s) for report models.
  name: CaptivateIQ Report Models API
  slug: captivateiq-report-models-api
- description: The Transformation Worksheets API from CaptivateIQ — 3 operation(s) for transformation worksheets.
  name: CaptivateIQ Transformation Worksheets API
  slug: captivateiq-transformation-worksheets-api
- description: The Uploads API from CaptivateIQ — 3 operation(s) for uploads.
  name: CaptivateIQ Uploads API
  slug: captivateiq-uploads-api
- description: The Users API from CaptivateIQ — 2 operation(s) for users.
  name: CaptivateIQ Users API
  slug: captivateiq-users-api
artifact_total: 41
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: CaptivateIQ Attribute Worksheets API
  slug: open-captivateiq-attribute-worksheets-api
- collection_type: open
  name: CaptivateIQ Attribute Worksheets Audit Logs API
  slug: open-captivateiq-audit-logs-api
- collection_type: open
  name: CaptivateIQ Attribute Worksheets Commission Plans API
  slug: open-captivateiq-commission-plans-api
- collection_type: open
  name: CaptivateIQ Attribute Worksheets Dashboards API
  slug: open-captivateiq-dashboards-api
- collection_type: open
  name: CaptivateIQ Attribute Worksheets Data Workbooks API
  slug: open-captivateiq-data-workbooks-api
- collection_type: open
  name: CaptivateIQ Attribute Worksheets Data Worksheets API
  slug: open-captivateiq-data-worksheets-api
- collection_type: open
  name: CaptivateIQ Attribute Worksheets Employee Assumptions API
  slug: open-captivateiq-employee-assumptions-api
- collection_type: open
  name: CaptivateIQ Attribute Worksheets Employees API
  slug: open-captivateiq-employees-api
- collection_type: open
  name: CaptivateIQ Attribute Worksheets Hierarchies API
  slug: open-captivateiq-hierarchies-api
- collection_type: open
  name: CaptivateIQ Attribute Worksheets Jobs API
  slug: open-captivateiq-jobs-api
- collection_type: open
  name: CaptivateIQ Attribute Worksheets Metadata API
  slug: open-captivateiq-metadata-api
- collection_type: open
  name: CaptivateIQ Attribute Worksheets Payouts API
  slug: open-captivateiq-payouts-api
- collection_type: open
  name: CaptivateIQ Attribute Worksheets Report Models API
  slug: open-captivateiq-report-models-api
- collection_type: open
  name: CaptivateIQ Attribute Worksheets Transformation Worksheets API
  slug: open-captivateiq-transformation-worksheets-api
- collection_type: open
  name: CaptivateIQ Attribute Worksheets Uploads API
  slug: open-captivateiq-uploads-api
- collection_type: open
  name: CaptivateIQ Attribute Worksheets Users API
  slug: open-captivateiq-users-api
common:
- group: agent
  title: ''
  type: MCPServer
  url: mcp/captivateiq-mcp.yml
- group: other
  title: ''
  type: Overlay
  url: overlays/captivateiq-openapi-overlay.yaml
- group: company
  title: ''
  type: Website
  url: https://www.captivateiq.com/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://developers.captivateiq.com/
- group: docs
  title: ''
  type: Documentation
  url: https://developers.captivateiq.com/docs/getting-started-with-captivateiq
- group: docs
  title: ''
  type: APIReference
  url: https://developers.captivateiq.com/reference
- group: start
  title: ''
  type: GettingStarted
  url: https://developers.captivateiq.com/docs/getting-started-with-captivateiq
- group: operate
  title: ''
  type: ChangeLog
  url: https://developers.captivateiq.com/changelog
- group: company
  title: ''
  type: Blog
  url: https://www.captivateiq.com/blog
- group: commercial
  title: ''
  type: Pricing
  url: https://www.captivateiq.com/pricing
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.captivateiq.com/privacy-policy
- group: commercial
  title: ''
  type: TermsOfService
  url: https://developers.captivateiq.com/page/terms-and-conditions
- group: operate
  title: ''
  type: Support
  url: mailto:support@captivateiq.com
- group: start
  title: ''
  type: Login
  url: https://app.captivateiq.com/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/captivateiq
- group: operate
  title: ''
  type: StatusPage
  url: https://status.captivateiq.com/
- group: auth
  title: ''
  type: Compliance
  url: https://www.captivateiq.com/security-policy
- group: auth
  title: ''
  type: Security
  url: https://www.captivateiq.com/security-policy
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/captivateiq-llms.txt
- group: build
  title: ''
  type: Packages
  url: packages/captivateiq-packages.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/captivateiq-well-known.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/captivateiq-lifecycle.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/captivateiq-conformance.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/captivateiq-domain-security.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/captivateiq-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: TrustCenter
  url: security/captivateiq-trust-center.yml
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/captivateiq-changelog.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/captivateiq-rate-limits.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/captivateiq-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/captivateiq-scopes.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/captivateiq-plans-pricing.yml
- group: build
  title: ''
  type: ToolCrosswalk
  url: mcp/captivateiq-tool-crosswalk.yml
created: '2026-07-17'
description: CaptivateIQ is a sales performance and commission management platform that automates the calculation, administration, and reporting of sales commissions and incentive compensation. Its ICM (Incentive Compensation Management) and SPM (Sales Performance Management) products let revenue, finance, and sales-ops teams design complex commission plans, model quotas and territories, and pay reps accurately and on time. CaptivateIQ exposes a public REST API (ciq/v1) for managing employees, users, hierarchies, data workbooks and worksheets, employee assumptions, commission plans, period groups, payouts, report models, transformation worksheets, uploads, dashboards, and audit logs. The API uses token-based authentication (Authorization header with a "Token" prefix), limit/offset pagination, and per-tier rate limiting, and is documented on a public developer portal with guides, recipes, a changelog, and an llms.txt index. CaptivateIQ also serves a live remote MCP endpoint on its developer-docs
  host and an RFC 8414 OAuth authorization-server metadata document on its app host, and publicly announced a customer-facing CaptivateIQ MCP Server (limited beta, May 2026) for connecting live compensation and planning data to AI tools.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/captivateiq.png
layout: provider
mcp_servers:
- description: ''
  name: CaptivateIQ MCP Server
  slug: captivateiq-mcp-server
modified: '2026-08-13'
name: CaptivateIQ
nav: Providers
network: true
overview: 'CaptivateIQ publishes 16 APIs on the [APIs.io](https://apis.io/) network, including Attribute Worksheets API, Audit Logs API, Commission Plans API, and 13 more. Tagged areas include Company, Cloud Saas, Sales Commissions, Incentive Compensation Management, and Sales Performance Management.


  CaptivateIQ''s developer surface includes documentation, API reference, getting-started guide, changelog, engineering blog, pricing, support, and 26 more developer resources.'
plans:
- name: Captivateiq Plans Pricing
  plan_count: 0
  slug: captivateiq-plans-pricing
random_paper: 3
rate_limits:
- limit_count: 2
  name: Captivateiq Rate Limits
  slug: captivateiq-rate-limits
scopes:
- name: Captivateiq Scopes
  scope_count: 0
  slug: captivateiq-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: developing
  composite: 51.0
  delta: 0.0
  facets:
    access_clarity: 48.7
    commercial_clarity: 48.7
    contract_governance: 30.3
    contract_quality: 51.6
    developer_ergonomics: 39.9
    discoverability: 92.6
    governance: 30.3
    operational_transparency: 57.9
  previous_composite: 51.0
  provenance:
    conformance: first-party
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 100.0
      total: 16
    mcp: first-party
    skills: derived
  schema_version: 0.15.0
  scored_at: '2026-08-26'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/captivateiq/refs/heads/main/screenshots/captivateiq-2026-07-25T204452.png
security:
- kind: authentication
  name: Captivateiq Authentication
  slug: captivateiq-authentication
  summary_line: apiKey/oauth2 · 2 schemes
- kind: domain-security
  name: Captivateiq Domain Security
  slug: captivateiq-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
- kind: vulnerability-disclosure
  name: Captivateiq Vulnerability Disclosure
  slug: captivateiq-vulnerability-disclosure
  summary_line: contact published
- kind: trust-center
  name: Captivateiq Trust Center
  slug: captivateiq-trust-center
  summary_line: ISO 27001, SOC 1, SOC 2, SOX, GDPR
slug: captivateiq
tags:
- Company
- Cloud Saas
- Sales Commissions
- Incentive Compensation Management
- Sales Performance Management
- Revenue Operations
- Finance
- Payouts
- Commission Plans
- Sales Compensation
website: https://www.captivateiq.com/
---
