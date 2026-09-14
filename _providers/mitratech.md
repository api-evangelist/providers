---
api_count: 2
apis:
- baseURL: https://{tenant}.tap.thinksmart.com/{tenant}/api
  baseurl_source: declared
  description: REST API for the TAP (ThinkSmart Automation Platform) no-code workflow automation product. Covers workflow initiation and continuation, form retrieval and save, task assignment and re-assignment, dash
  name: Mitratech TAP Workflow Automation API
  slug: mitratech-tap-workflow-automation-api
- description: Modernized REST API shipped with TeamConnect Enterprise 7.2 and later, served from each customer's own TeamConnect instance at /webservice/enterprise/. Exposes Accounts, Appointments, Contacts, Docume
  name: Mitratech TeamConnect REST API
  slug: mitratech-teamconnect-rest-api
- description: Remote Model Context Protocol server served from mitratech.com over Streamable HTTP. Advertises OAuth 2.0 authorization-server metadata at /.well-known/oauth-authorization-server and protected-resourc
  name: Mitratech MCP Server
  slug: mitratech-mcp-server
artifact_total: 10
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/mitratech-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://mitratech.com/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://success.mitratech.com/
- group: docs
  title: ''
  type: Documentation
  url: https://success.mitratech.com/TAP/TAP_Solutions/APIs_and_Integrations/TAP_API_Documentation
- group: docs
  title: ''
  type: APIReference
  url: https://default.stagingtap.thinksmart.com/default/api/swagger/ui/index
- group: start
  title: ''
  type: GettingStarted
  url: https://success.mitratech.com/TAP/TAP_Solutions/APIs_and_Integrations
- group: operate
  title: ''
  type: Support
  url: https://success.mitratech.com/
- group: company
  title: ''
  type: Blog
  url: https://mitratech.com/resource-hub/mitratech-blog/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://mitratech.com/privacy-policy/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://mitratech.com/legal-notice/
- group: start
  title: ''
  type: SignUp
  url: https://mitratech.com/contact-us/
- group: operate
  title: ''
  type: ChangeLog
  url: https://success.mitratech.com/TAP/ReleaseNotes
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/mitratech-changelog.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/mitratech-lifecycle.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/mitratech-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/mitratech-scopes.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/mitratech-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/mitratech-problem-types.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/mitratech-conformance.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/mitratech-data-model.yml
- group: start
  title: ''
  type: Sandbox
  url: sandbox/mitratech-sandbox.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/mitratech-mcp.yml
- group: build
  title: ''
  type: ToolCrosswalk
  url: mcp/mitratech-tool-crosswalk.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/mitratech-llms.txt
- group: agent
  title: ''
  type: WellKnown
  url: well-known/mitratech-well-known.yml
- group: build
  title: ''
  type: Packages
  url: packages/mitratech-packages.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/mitratech-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/mitratech-rate-limits.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/ThinkSmart
- group: build
  title: ''
  type: Examples
  url: https://github.com/ThinkSmart/API_Examples
created: '2026-09-13'
description: 'Mitratech is an Austin, Texas based enterprise software company supplying legal operations, governance, risk and compliance, and HR compliance software to corporate legal departments, compliance teams and human resources organizations. Its platform spans enterprise legal management and matter management (TeamConnect), legal spend and e-billing, no-code workflow automation and intake (TAP Workflow Automation, acquired with ThinkSmart), policy and risk management (PolicyHub, Alyne), immigration case management (INSZoom), HR compliance, talent and background screening (Mineral, Trakstar, AssureHire, Circa), and contract lifecycle management. Programmatic access is delivered per-product and per-tenant rather than through a single public developer portal: TAP publishes an OData-style REST API with a live Swagger 2.0 API Explorer, TeamConnect 7.2+ ships a modernized OAuth 2.0 REST API on each customer instance, and mitratech.com itself serves an OAuth-protected Model Context Protocol
  server.'
image: https://mitratech.com/wp-content/uploads/Mitratech_Web-Assets_Home-Feature-Image-HD-1024x577.png
layout: provider
mcp_servers:
- description: ''
  name: Mitratech MCP Server
  slug: mitratech-mcp-server
- description: ''
  name: Mitratech MCP Server
  slug: mitratech-mcp-server-2
modified: '2026-09-13'
name: Mitratech
nav: Providers
network: true
overview: 'Mitratech publishes 1 API on the [APIs.io](https://apis.io/) network: TAP Workflow Automation API. Tagged areas include Legal, Legal Operations, Enterprise Legal Management, Matter Management, and Governance Risk and Compliance.


  Mitratech''s developer surface includes documentation, API reference, getting-started guide, support, engineering blog, signup flow, changelog, and 24 more developer resources.'
plans:
- name: Mitratech Plans Pricing
  plan_count: 0
  slug: mitratech-plans-pricing
random_paper: 16
rate_limits:
- limit_count: 0
  name: Mitratech Rate Limits
  slug: mitratech-rate-limits
scopes:
- name: Mitratech Scopes
  scope_count: 0
  slug: mitratech-scopes
  summary_line: OAuth 2.0 · no documented scopes
security:
- kind: authentication
  name: Mitratech Authentication
  slug: mitratech-authentication
  summary_line: 0 schemes
- kind: domain-security
  name: Mitratech Domain Security
  slug: mitratech-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: mitratech
tags:
- Legal
- Legal Operations
- Enterprise Legal Management
- Matter Management
- Governance Risk and Compliance
- Compliance
- Workflow Automation
- Contract Lifecycle Management
- HR Compliance
- Risk Management
- Immigration
- OData
- MCP
website: https://mitratech.com/
---
