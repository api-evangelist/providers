---
access_model:
  confidence: medium
  label: Requires approval
  onboarding: approval
  pricing: unknown
  public: false
  source:
  - plans
  - authentication
  - rate-limits
  - security
  - sandbox
  trial: false
  try_now: false
api_count: 4
apis:
- baseURL: https://app.daloopa.com/api/v3
  baseurl_source: declared
  description: The Auth API from Daloopa — 10 operation(s) for auth.
  name: Daloopa Auth API
  slug: daloopa-auth-api
- baseURL: https://app.daloopa.com/api/v3
  baseurl_source: declared
  description: Company Data and Metadata
  name: Daloopa Companies API
  slug: daloopa-companies-api
- baseURL: https://app.daloopa.com/api/v3
  baseurl_source: declared
  description: The Consumption API from Daloopa — 6 operation(s) for consumption.
  name: Daloopa Consumption API
  slug: daloopa-consumption-api
- baseURL: https://app.daloopa.com/api/v3
  baseurl_source: declared
  description: The Daloopa MCP Service API from Daloopa — 1 operation(s) for daloopa mcp service.
  name: Daloopa Daloopa MCP Service API
  slug: daloopa-daloopa-mcp-service-api
- baseURL: https://app.daloopa.com/api/v3
  baseurl_source: declared
  description: The Data Warehouse API from Daloopa — 1 operation(s) for data warehouse.
  name: Daloopa Data Warehouse API
  slug: daloopa-data-warehouse-api
- baseURL: https://app.daloopa.com/api/v3
  baseurl_source: declared
  description: The Databricks API from Daloopa — 1 operation(s) for databricks.
  name: Daloopa Databricks API
  slug: daloopa-databricks-api
- baseURL: https://app.daloopa.com/api/v3
  baseurl_source: declared
  description: The Documents API from Daloopa — 5 operation(s) for documents.
  name: Daloopa Documents API
  slug: daloopa-documents-api
- baseURL: https://app.daloopa.com/api/v3
  baseurl_source: declared
  description: The Download API from Daloopa — 2 operation(s) for download.
  name: Daloopa Download API
  slug: daloopa-download-api
- baseURL: https://app.daloopa.com/api/v3
  baseurl_source: declared
  description: The Export API from Daloopa — 1 operation(s) for export.
  name: Daloopa Export API
  slug: daloopa-export-api
- baseURL: https://app.daloopa.com/api/v3
  baseurl_source: declared
  description: Financial Fundamentals Data
  name: Daloopa Fundamentals API
  slug: daloopa-fundamentals-api
- baseURL: https://app.daloopa.com/api/v3
  baseurl_source: declared
  description: The Health API from Daloopa — 1 operation(s) for health.
  name: Daloopa Health API
  slug: daloopa-health-api
- baseURL: https://app.daloopa.com/api/v3
  baseurl_source: declared
  description: The Industry Models API from Daloopa — 1 operation(s) for industry models.
  name: Daloopa Industry Models API
  slug: daloopa-industry-models-api
- baseURL: https://app.daloopa.com/api/v3
  baseurl_source: declared
  description: The Investing Skills API from Daloopa — 2 operation(s) for investing skills.
  name: Daloopa Investing Skills API
  slug: daloopa-investing-skills-api
- baseURL: https://app.daloopa.com/api/v3
  baseurl_source: declared
  description: The Market Data API from Daloopa — 2 operation(s) for market data.
  name: Daloopa Market Data API
  slug: daloopa-market-data-api
- baseURL: https://app.daloopa.com/api/v3
  baseurl_source: declared
  description: The Partnership API from Daloopa — 1 operation(s) for partnership.
  name: Daloopa Partnership API
  slug: daloopa-partnership-api
- baseURL: https://app.daloopa.com/api/v3
  baseurl_source: declared
  description: The Series API from Daloopa — 1 operation(s) for series.
  name: Daloopa Series API
  slug: daloopa-series-api
- baseURL: https://app.daloopa.com/api/v3
  baseurl_source: declared
  description: The Snowflake API from Daloopa — 1 operation(s) for snowflake.
  name: Daloopa Snowflake API
  slug: daloopa-snowflake-api
- baseURL: https://app.daloopa.com/api/v3
  baseurl_source: declared
  description: The Taxonomy API from Daloopa — 5 operation(s) for taxonomy.
  name: Daloopa Taxonomy API
  slug: daloopa-taxonomy-api
- baseURL: https://app.daloopa.com/api/v3
  baseurl_source: declared
  description: The Webhooks API from Daloopa — 6 operation(s) for webhooks.
  name: Daloopa Webhooks API
  slug: daloopa-webhooks-api
artifact_total: 29
asyncapis:
- description: ''
  name: Daloopa Webhooks
  slug: daloopa-webhooks
collections:
- collection_type: open
  name: Daloopa API
  slug: open-daloopa-api
- collection_type: open
  name: Daloopa MCP Service
  slug: open-daloopa-mcp-service
common:
- group: other
  title: ''
  type: Overlay
  url: overlays/daloopa-api-security-overlay.yaml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/daloopa-mcp.yml
- group: agent
  title: ''
  type: MCPServer
  url: https://mcp.daloopa.com/server/mcp
- group: company
  title: ''
  type: Website
  url: https://daloopa.com/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://docs.daloopa.com/docs/overview
- group: docs
  title: ''
  type: Documentation
  url: https://docs.daloopa.com/docs/overview
- group: docs
  title: ''
  type: APIReference
  url: https://docs.daloopa.com/reference/companies_list_v3
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.daloopa.com/docs/api-authentication
- group: operate
  title: ''
  type: Support
  url: https://docs.daloopa.com/docs/contact-us
- group: company
  title: ''
  type: Blog
  url: https://daloopa.com/blog
- group: company
  title: ''
  type: BlogRSS
  url: https://daloopa.com/blog/feed
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/daloopa
- group: start
  title: ''
  type: SignUp
  url: https://daloopa.com/demo
- group: commercial
  title: ''
  type: TermsOfService
  url: https://daloopa.com/terms-of-use
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://daloopa.com/privacy-policy
- group: operate
  title: ''
  type: StatusPage
  url: https://status.daloopa.com/
- group: operate
  title: ''
  type: Deprecation
  url: lifecycle/daloopa-lifecycle.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/daloopa-lifecycle.yml
- group: agent
  title: ''
  type: LLMSTxt
  url: llms/daloopa-llms.txt
- group: agent
  title: ''
  type: LLMSTxt
  url: https://docs.daloopa.com/llms.txt
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: build
  title: ''
  type: Packages
  url: packages/daloopa-packages.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/daloopa-conformance.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/daloopa-domain-security.yml
- group: auth
  title: ''
  type: TrustCenter
  url: security/daloopa-trust-center.yml
- group: auth
  title: ''
  type: TrustCenter
  url: https://trust.daloopa.com/
- group: commercial
  title: ''
  type: Plans
  url: plans/daloopa-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/daloopa-rate-limits.yml
- group: design
  title: ''
  type: Components
  url: components/daloopa-components.yml
created: '2026-08-11'
description: Daloopa is an AI-powered fundamental financial data platform for institutional investors, providing analyst-verified, source-linked financial data extracted from SEC filings, earnings transcripts, investor presentations and press releases. Coverage spans 6,000+ global public companies with roughly 14 years of history, and every datapoint is hyperlinked back to the exact location in the original source document for auditability. The company sells to hedge funds, mutual funds, investment banks, equity research and private equity teams, and delivers the same dataset across a REST API, a hosted remote MCP server, an Excel add-in, prebuilt Data Sheets, the Scout AI modeling agent, and native cloud-warehouse shares via Snowflake, Databricks and AWS S3.
image: https://avatars.githubusercontent.com/u/42851514?v=4
layout: provider
mcp_servers:
- description: ''
  name: Daloopa MCP Server
  slug: daloopa-mcp-server
- description: ''
  name: Daloopa MCP Server
  slug: daloopa-mcp-server-2
modified: '2026-08-11'
name: Daloopa
nav: Providers
network: true
overview: 'Daloopa publishes 19 APIs on the [APIs.io](https://apis.io/) network, including Auth API, Companies API, Consumption API, and 16 more. Tagged areas include Financial Data, Fundamental Data, Market Data, Investment Research, and Equity Research.


  The Daloopa catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  Daloopa''s developer surface includes documentation, API reference, getting-started guide, support, engineering blog, signup flow, and 23 more developer resources.'
plans:
- name: Daloopa Plans Pricing
  plan_count: 0
  slug: daloopa-plans-pricing
random_paper: 1
rate_limits:
- limit_count: 1
  name: Daloopa Rate Limits
  slug: daloopa-rate-limits
screenshot: https://raw.githubusercontent.com/api-evangelist/daloopa/refs/heads/main/screenshots/daloopa-2026-08-17T080848.png
security:
- kind: authentication
  name: Daloopa Authentication
  slug: daloopa-authentication
  summary_line: http/oauth2/apiKey · 4 schemes
- kind: domain-security
  name: Daloopa Domain Security
  slug: daloopa-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: trust-center
  name: Daloopa Trust Center
  slug: daloopa-trust-center
  summary_line: trust center published
slug: daloopa
tags:
- Financial Data
- Fundamental Data
- Market Data
- Investment Research
- Equity Research
- SEC Filings
- Earnings
- Fintech
- MCP
- agent-native
- Agent Skills
- Webhook
- Data Warehouse
website: https://daloopa.com/
---
