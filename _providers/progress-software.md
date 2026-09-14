---
api_count: 5
apis:
- baseURL: https://automate.chef.io
  baseurl_source: declared
  description: The Chef Automate API is the HTTP surface of Progress Chef Automate, the dashboard and control plane for Chef Infra, Chef InSpec and Chef Habitat. It covers configuration management node and run histo
  name: Chef Automate API
  slug: progress-software-chef-automate
- baseURL: https://{moveit-transfer-host}/api/v1
  baseurl_source: declared
  description: The MOVEit Transfer REST API is an optionally licensed interface that runs at a customer's own MOVEit Transfer server. It exposes authentication, files and folders, folder content, users and groups, a
  name: MOVEit Transfer REST API
  slug: progress-software-moveit-transfer
- baseURL: https://{whatsupgold-host}:9644/api/v1
  baseurl_source: declared
  description: The WhatsUp Gold REST API is the automation interface of Progress WhatsUp Gold network monitoring, served from the customer's own WhatsUp Gold host on port 9644. It covers device discovery and managem
  name: WhatsUp Gold REST API
  slug: progress-software-whatsup-gold
- description: The ShareFile API v3 is the OData-based REST interface of Progress ShareFile, covering Items, Folders, Accounts, Users, Groups, Shares, Access Controls, Capabilities, Connector Groups, Devices, Encryp
  name: ShareFile API v3
  slug: progress-software-sharefile
- description: Sitefinity CMS exposes its content as OData v4 web services under a configurable service route (by default /api/default) on the customer's own Sitefinity instance. The headless API serves content type
  name: Sitefinity CMS Headless OData Services
  slug: progress-software-sitefinity-odata
artifact_total: 14
asyncapis:
- description: ''
  name: Progress Software Sharefile Webhooks
  slug: progress-software-sharefile-webhooks
common:
- group: auth
  title: ''
  type: TrustCenter
  url: security/progress-software-trust-center.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/progress-software-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/progress-software-domain-security.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/progress-software-scopes.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/progress-software-authentication.yml
- group: company
  title: ''
  type: Website
  url: https://www.progress.com/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://docs.progress.com/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.progress.com/
- group: docs
  title: ''
  type: APIReference
  url: https://docs.chef.io/automate/api/
- group: start
  title: ''
  type: GettingStarted
  url: https://api.sharefile.com/gettingstarted/quickstart
- group: operate
  title: ''
  type: Support
  url: https://www.progress.com/support
- group: operate
  title: ''
  type: HelpCenter
  url: https://community.progress.com/s/knowledge-base
- group: company
  title: ''
  type: Blog
  url: https://www.progress.com/blogs
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/progress
- group: commercial
  title: ''
  type: Pricing
  url: https://www.telerik.com/purchase.aspx
- group: start
  title: ''
  type: SignUp
  url: https://www.progress.com/trials
- group: start
  title: ''
  type: Login
  url: https://www.progress.com/support/customer-portal
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.progress.com/legal/terms-of-use
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.progress.com/legal/privacy-center
- group: docs
  title: ''
  type: OpenAPI
  url: openapi/progress-software-chef-automate-openapi-original.json
- group: docs
  title: ''
  type: OpenAPI
  url: openapi/progress-software-moveit-transfer-openapi-original.json
- group: docs
  title: ''
  type: OpenAPI
  url: openapi/progress-software-whatsup-gold-openapi-original.json
- group: build
  title: ''
  type: Packages
  url: packages/progress-software-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/progress-software-packages.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/progress-software-well-known.yml
- group: auth
  title: ''
  type: SecurityTxt
  url: well-known/progress-software-security.txt
- group: agent
  title: ''
  type: MCPServer
  url: mcp/progress-software-mcp.yml
- group: build
  title: ''
  type: ToolCrosswalk
  url: mcp/progress-software-tool-crosswalk.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/progress-software-llms.txt
- group: other
  title: ''
  type: Overlay
  url: overlays/progress-software-chef-automate-overlay.yaml
- group: other
  title: ''
  type: Overlay
  url: overlays/progress-software-moveit-transfer-overlay.yaml
- group: other
  title: ''
  type: Overlay
  url: overlays/progress-software-whatsup-gold-overlay.yaml
- group: design
  title: ''
  type: Conformance
  url: conformance/progress-software-conformance.yml
- group: auth
  title: ''
  type: Compliance
  url: https://trust.progress.com/
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/progress-software-problem-types.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/progress-software-lifecycle.yml
- group: operate
  title: ''
  type: StatusPage
  url: https://status.chef.io/
- group: operate
  title: ''
  type: StatusPage
  url: https://status.sharefile.com/
- group: operate
  title: ''
  type: StatusPage
  url: https://status.moveitcloud.com/
- group: operate
  title: ''
  type: Deprecation
  url: https://www.progress.com/support/maintenance-and-support-policy
- group: auth
  title: ''
  type: Security
  url: https://www.progress.com/security/vulnerability-reporting-policy
- group: design
  title: ''
  type: Conventions
  url: conventions/progress-software-conventions.yml
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/progress-software-changelog.yml
- group: build
  title: ''
  type: CLI
  url: cli/progress-software-cli.yml
- group: design
  title: ''
  type: Components
  url: components/progress-software-components.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/progress-software-data-model.yml
- group: design
  title: ''
  type: Webhooks
  url: asyncapi/progress-software-sharefile-webhooks.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/progress-software-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/progress-software-rate-limits.yml
created: '2026-09-13'
description: 'Progress Software Corporation (NASDAQ: PRGS) is a Burlington, Massachusetts enterprise software company that builds and acquires infrastructure and digital-experience products. Its portfolio spans application development and data (OpenEdge, MarkLogic, Semaphore, DataDirect, Corticon, Nuclia agentic RAG), digital experience (Sitefinity CMS, Sitefinity Insight), developer tooling and UI components (Telerik, Kendo UI, Fiddler, Test Studio), secure file transfer and collaboration (MOVEit, ShareFile), infrastructure automation and monitoring (Chef, WhatsUp Gold, Flowmon, LoadMaster by Kemp). Most of its API surface is shipped inside self-hosted products — MOVEit Transfer, WhatsUp Gold and Chef Automate each publish a full Swagger 2.0 contract against the customer''s own installation — alongside SaaS surfaces such as the ShareFile OData API and Sitefinity''s headless OData services.'
image: https://www.progress.com/images/default-source/default-album/progress-album/images-album/social-image.png
layout: provider
mcp_servers:
- description: ''
  name: Progress Software MCP Server
  slug: progress-software-mcp-server
modified: '2026-09-13'
name: Progress Software
nav: Providers
network: true
overview: 'Progress Software publishes 3 APIs on the [APIs.io](https://apis.io/) network: Chef Automate API, MOVEit Transfer REST API, and WhatsUp Gold REST API. Tagged areas include Company, Enterprise Software, Managed File Transfer, Infrastructure Automation, and Network Monitoring.


  The Progress Software catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  Progress Software''s developer surface includes authentication, documentation, API reference, getting-started guide, support, engineering blog, pricing, and 43 more developer resources.'
plans:
- name: Progress Software Plans Pricing
  plan_count: 21
  slug: progress-software-plans-pricing
random_paper: 20
rate_limits:
- limit_count: 0
  name: Progress Software Rate Limits
  slug: progress-software-rate-limits
scopes:
- name: Progress Software Scopes
  scope_count: 0
  slug: progress-software-scopes
  summary_line: OAuth 2.0 · no documented scopes
security:
- kind: authentication
  name: Progress Software Authentication
  slug: progress-software-authentication
  summary_line: apiKey/oauth2 · 3 schemes
- kind: domain-security
  name: Progress Software Domain Security
  slug: progress-software-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Progress Software Vulnerability Disclosure
  slug: progress-software-vulnerability-disclosure
  summary_line: Bugcrowd · security.txt · contact published
- kind: trust-center
  name: Progress Software Trust Center
  slug: progress-software-trust-center
  summary_line: SOC 1, SOC 2 Type I, SOC 2 Type II, SOC 3, ISO 27001, ISO 27017, ISO 27018, PCI DSS, HIPAA, FedRAMP, CSA STAR, TISAX, GDPR
slug: progress-software
tags:
- Company
- Enterprise Software
- Managed File Transfer
- Infrastructure Automation
- Network Monitoring
- Content Management
- Developer Tools
- Data Platform
- Application Development
- DevOps
- Agentic RAG
- File Sharing
website: https://www.progress.com/
---
