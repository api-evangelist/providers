---
api_count: 3
apis:
- baseURL: https://otpm-api.aibidia.com
  baseurl_source: declared
  description: The deliberately-public integration surface of Aibidia's OTP Management solution. It accepts automated multi-level segmentation data injections for a given year, month and Extract Type, and returns th
  name: Aibidia Public OTP Management API
  slug: aibidia-public-otp-management-api
- baseURL: https://tpai-api.aibidia.com
  baseurl_source: declared
  description: Backend service for the Aibidia TP AI solution surfaced at platform.aibidia.com/tpai/. It serves an OpenAPI 3.1.0 document anonymously at https://tpai-api.aibidia.com/openapi.json describing a healthc
  name: Aibidia TP AI API
  slug: aibidia-tp-ai-api
artifact_total: 7
common:
- group: company
  title: ''
  type: Website
  url: https://www.aibidia.com/
- group: docs
  title: ''
  type: Documentation
  url: https://aibidia.my.site.com/help/support
- group: operate
  title: ''
  type: Support
  url: https://aibidia.my.site.com/help/support
- group: operate
  title: ''
  type: HelpCenter
  url: https://aibidia.my.site.com/help/support
- group: docs
  title: ''
  type: APIReference
  url: https://otpm-api.aibidia.com/swagger/index.html
- group: start
  title: ''
  type: Login
  url: https://platform.aibidia.com/
- group: company
  title: ''
  type: Blog
  url: https://www.aibidia.com/blog
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/Aibidia
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.aibidia.com/terms-of-service
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.aibidia.com/privacy-policy
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/aibidia-llms.txt
- group: agent
  title: ''
  type: WellKnown
  url: well-known/aibidia-well-known.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/aibidia-authentication.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/aibidia-conventions.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/aibidia-lifecycle.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/aibidia-conformance.yml
- group: auth
  title: ''
  type: Compliance
  url: conformance/aibidia-conformance.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/aibidia-domain-security.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/aibidia-problem-types.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/aibidia-data-model.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/aibidia-rate-limits.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/aibidia-plans-pricing.yml
- group: build
  title: ''
  type: Packages
  url: packages/aibidia-packages.yml
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/aibidia-changelog.yml
- group: operate
  title: ''
  type: ChangeLog
  url: https://www.aibidia.com/product-news
- group: agent
  title: ''
  type: MCPServer
  url: mcp/aibidia-mcp.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
created: '2026-09-13'
description: 'Aibidia is a Helsinki-based transfer pricing technology company whose cloud platform lets multinational enterprises manage transfer pricing policy, intercompany transaction data, documentation and country-by-country reporting in one place. The platform is delivered as a set of solution modules — TPDoc (documentation), CbCR, OTP Management, Strategic TP Management, Value Chain Analysis, Data Studio, Horizon and TP AI — behind a single Azure AD B2C sign-in at platform.aibidia.com, each backed by its own first-party API service on an aibidia.com subdomain. Aibidia publishes a small deliberately-public integration surface: the Public OTP Management API, which accepts automated multi-level segmentation data injections from a customer''s ERP or finance stack using an X-DATAINGESTION-API-KEY header. There is no open developer portal, no public API reference and no self-serve signup; the platform is sold to enterprise tax teams and the help centre and release notes sit behind client-rendered
  portals.'
image: https://cdn.prod.website-files.com/652d101c1d03208622e683de/65686f3212a45fa956dd35a9_Social%20Share%20Aibidia.png
layout: provider
mcp_servers:
- description: ''
  name: Aibidia MCP Server
  slug: aibidia-mcp-server
modified: '2026-09-13'
name: Aibidia
nav: Providers
network: true
overview: 'Aibidia publishes 2 APIs on the [APIs.io](https://apis.io/) network: Public OTP Management API and TP AI API. Tagged areas include Company, Transfer Pricing, Tax Technology, Tax Compliance, and Regulatory Reporting.


  Aibidia''s developer surface includes documentation, support, API reference, engineering blog, authentication, changelog, and 21 more developer resources.'
plans:
- name: Aibidia Plans Pricing
  plan_count: 0
  slug: aibidia-plans-pricing
random_paper: 14
rate_limits:
- limit_count: 1
  name: Aibidia Rate Limits
  slug: aibidia-rate-limits
security:
- kind: authentication
  name: Aibidia Authentication
  slug: aibidia-authentication
  summary_line: apiKey/oauth2/openIdConnect · 2 schemes
- kind: domain-security
  name: Aibidia Domain Security
  slug: aibidia-domain-security
  summary_line: TLSv1.3 · HSTS
slug: aibidia
tags:
- Company
- Transfer Pricing
- Tax Technology
- Tax Compliance
- Regulatory Reporting
- Country-by-Country Reporting
- Financial Data
- Enterprise Software
- Data Ingestion
- Finland
website: https://www.aibidia.com/
---
