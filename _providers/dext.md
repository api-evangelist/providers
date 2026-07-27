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
    agent_skills: true
    agentic_access: false
    asyncapi_events: false
    auth_clarity: true
    consent_identity: false
    error_semantics: true
    idempotency: false
    mcp_server: true
    openapi_examples: false
    rate_limit_signal: true
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.1
  score: 57.7
  scored_at: '2026-07-27'
api_count: 1
apis:
- description: Practice client data-health metrics and activity statistics
  name: Dext Clients API
  slug: dext-clients-api
artifact_total: 7
common:
- group: auth
  title: ''
  type: TrustCenter
  url: security/dext-trust-center.yml
- group: company
  title: ''
  type: Website
  url: https://dext.com/
- group: docs
  title: ''
  type: Documentation
  url: https://help.dext.com/en/articles/272702-data-health-insights-api
- group: docs
  title: ''
  type: APIReference
  url: https://help.dext.com/en/articles/272702-data-health-insights-api
- group: start
  title: ''
  type: GettingStarted
  url: https://help.dext.com/en/articles/272702-data-health-insights-api
- group: operate
  title: ''
  type: HelpCenter
  url: https://help.dext.com/
- group: operate
  title: ''
  type: Support
  url: https://help.dext.com/
- group: company
  title: ''
  type: Blog
  url: https://dext.com/en/blog
- group: commercial
  title: ''
  type: Pricing
  url: https://dext.com/en/business/pricing
- group: commercial
  title: ''
  type: TermsOfService
  url: https://dext.com/us/terms-and-conditions
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://dext.com/us/privacy-policy
- group: start
  title: ''
  type: SignUp
  url: https://app.dext.com/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/dext
- group: operate
  title: ''
  type: StatusPage
  url: https://status.dext.com/
- group: auth
  title: ''
  type: Security
  url: https://dext.com/us/security
- group: auth
  title: ''
  type: Compliance
  url: https://dext.com/us/security
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/dext-llms.txt
- group: auth
  title: ''
  type: Authentication
  url: authentication/dext-authentication.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/dext-rate-limits.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/dext-conventions.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/dext-lifecycle.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/dext-problem-types.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/dext-conformance.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/dext-data-model.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/dext-mcp.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: docs
  title: ''
  type: OpenAPI
  url: openapi/dext-data-health-openapi.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/dext-domain-security.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/dext-vulnerability-disclosure.yml
created: '2026-07-17'
description: Dext is bookkeeping automation software for businesses, accountants and bookkeepers (formerly Receipt Bank / Dext Precision / Dext Commerce). It captures receipts, invoices and bank statements, extracts and validates the data with high accuracy, and publishes it into accounting software such as Xero, QuickBooks, Sage, Zoho and MYOB. Dext serves over 700,000 customers worldwide across the UK, US, Canada, Australia, France and South Africa. For accounting practices, Dext exposes a read-only Data Health & Insights REST API that returns client data-health metrics and rolling activity statistics, authenticated with practice-scoped bearer tokens and rate limited to 60 requests per minute.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/dext.png
layout: provider
mcp_servers:
- description: ''
  name: dext-mcp.yml
  slug: dext-mcpyml
modified: '2026-07-18'
name: Dext
nav: Providers
network: true
overview: 'Dext publishes 1 API on the [APIs.io](https://apis.io/) network: Clients API. Tagged areas include Company, Accounting, Bookkeeping, Receipts, and Expense Management.


  Dext''s developer surface includes documentation, API reference, getting-started guide, support, engineering blog, pricing, signup flow, and 22 more developer resources.'
random_paper: 29
rate_limits:
- limit_count: 0
  name: Dext Rate Limits
  slug: dext-rate-limits
score:
  band: developing
  composite: 51.8
  delta: 0.0
  facets:
    commercial_clarity: 60.5
    contract_quality: 58.4
    developer_ergonomics: 58.7
    discoverability: 92.5
    governance: 0.0
    operational_transparency: 31.6
  previous_composite: 51.8
  schema_version: 0.5
  scored_at: '2026-07-27'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/dext/refs/heads/main/screenshots/dext-2026-07-25T211838.png
security:
- kind: authentication
  name: Dext Authentication
  slug: dext-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Dext Domain Security
  slug: dext-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Dext Vulnerability Disclosure
  slug: dext-vulnerability-disclosure
  summary_line: contact published
- kind: trust-center
  name: Dext Trust Center
  slug: dext-trust-center
  summary_line: ISO 27001, PCI DSS, GDPR
slug: dext
tags:
- Company
- Accounting
- Bookkeeping
- Receipts
- Expense Management
- Financial Automation
- Data Health
- OCR
website: https://dext.com/
---
