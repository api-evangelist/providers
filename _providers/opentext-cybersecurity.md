---
api_count: 1
apis:
- baseURL: https://api.ams.fortify.com
  baseurl_source: declared
  description: The REST API behind OpenText Core Application Security, still branded Fortify on Demand across the contract and the tooling. 159 operations over 125 paths cover applications, releases, static, dynamic
  name: OpenText Core Application Security (Fortify on Demand) API
  slug: fortify-on-demand-api
- description: The Webroot Unity API is the multi-tenant REST platform OpenText Cybersecurity partners and managed service providers use to reach Webroot and Secure Cloud services — endpoint status, Global Site Mana
  name: Webroot Unity API
  slug: webroot-unity-api
artifact_total: 9
asyncapis:
- description: ''
  name: Opentext Cybersecurity Webroot Unity Webhooks
  slug: opentext-cybersecurity-webroot-unity-webhooks
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/opentext-cybersecurity-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://cybersecurity.opentext.com/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://community.opentext.com/cybersec/fortify
- group: docs
  title: ''
  type: Documentation
  url: https://community.opentext.com/cybersec/fortify/productdocs
- group: docs
  title: ''
  type: APIReference
  url: https://api.ams.fortify.com/swagger/ui/index
- group: start
  title: ''
  type: GettingStarted
  url: https://unityapi.webrootcloudav.com/Docs/en/APIDoc/GettingStarted
- group: operate
  title: ''
  type: Support
  url: https://cybersecurity.opentext.com/support/
- group: operate
  title: ''
  type: Community
  url: https://community.opentext.com/cybersec/fortify/f/discussions
- group: company
  title: ''
  type: Blog
  url: https://cybersecurity.opentext.com/blog/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/fortify
- group: operate
  title: ''
  type: StatusPage
  url: https://status.fortify.com/
- group: operate
  title: ''
  type: StatusPage
  url: https://status.opentext.com/
- group: start
  title: ''
  type: SignUp
  url: https://cybersecurity.opentext.com/account-login/
- group: start
  title: ''
  type: Login
  url: https://my.webrootanywhere.com/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://cybersecurity.opentext.com/legal/sdk-and-api-agreement/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.opentext.com/about/privacy
- group: commercial
  title: ''
  type: Pricing
  url: https://cybersecurity.opentext.com/contact-us/
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/opentext-cybersecurity-llms.txt
- group: build
  title: ''
  type: Packages
  url: packages/opentext-cybersecurity-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/opentext-cybersecurity-packages.yml
- group: build
  title: ''
  type: CLI
  url: cli/opentext-cybersecurity-cli.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/opentext-cybersecurity-mcp.yml
- group: build
  title: ''
  type: ToolCrosswalk
  url: mcp/opentext-cybersecurity-tool-crosswalk.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/opentext-cybersecurity-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/opentext-cybersecurity-scopes.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/opentext-cybersecurity-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/opentext-cybersecurity-problem-types.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/opentext-cybersecurity-lifecycle.yml
- group: operate
  title: ''
  type: Deprecation
  url: lifecycle/opentext-cybersecurity-lifecycle.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/opentext-cybersecurity-data-model.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/opentext-cybersecurity-rate-limits.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/opentext-cybersecurity-plans-pricing.yml
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/opentext-cybersecurity-changelog.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/opentext-cybersecurity-conformance.yml
- group: auth
  title: ''
  type: Compliance
  url: conformance/opentext-cybersecurity-conformance.yml
- group: design
  title: ''
  type: Webhooks
  url: asyncapi/opentext-cybersecurity-webroot-unity-webhooks.yml
- group: other
  title: ''
  type: Protobuf
  url: grpc/opentext-cybersecurity-aviator-issue.proto
- group: other
  title: ''
  type: Protobuf
  url: grpc/opentext-cybersecurity-aviator-correlation.proto
- group: other
  title: ''
  type: Protobuf
  url: grpc/opentext-cybersecurity-aviator-application.proto
- group: other
  title: ''
  type: Protobuf
  url: grpc/opentext-cybersecurity-aviator-entitlement.proto
- group: other
  title: ''
  type: Protobuf
  url: grpc/opentext-cybersecurity-aviator-dast-entitlement.proto
- group: other
  title: ''
  type: Protobuf
  url: grpc/opentext-cybersecurity-aviator-accesstoken.proto
created: '2026-09-13'
description: OpenText Cybersecurity is the security business of OpenText, assembled from the Micro Focus security portfolio (Fortify application security, ArcSight threat detection and response, NetIQ identity and access management, Voltage data privacy) and the SMB/MSP brands OpenText acquired through Webroot, Carbonite and Zix — endpoint protection, DNS protection, EDR/MDR, email threat protection and encryption, security awareness training, backup and disaster recovery. Two product lines expose a public developer surface. OpenText Core Application Security (Fortify on Demand) publishes a live Swagger 2.0 contract with 159 operations across applications, releases, static/dynamic/mobile scans, vulnerabilities, reports and tenant administration, served per region from api.ams / api.emea / api.apac.fortify.com. The Webroot Unity API is the multi-tenant REST platform managed service providers use to run Secure Cloud sites, endpoints, policies, licensing and near-real-time event notifications.
  Fortify also ships a first-party CLI (fcli), a first-party MCP server inside that CLI, and a published set of Agent Skills for Claude Code, GitHub Copilot, Codex and Gemini CLI.
image: https://cari01mstrop62eprod.dxcloud.episerver.net/globalassets/smb-media/images/banners/csot-homepage-hero-2.webp
layout: provider
mcp_servers:
- description: ''
  name: fcli MCP server (OpenText Fortify)
  slug: fcli-mcp-server-opentext-fortify
modified: '2026-09-13'
name: OpenText Cybersecurity
nav: Providers
network: true
overview: 'OpenText Cybersecurity publishes 1 API on the [APIs.io](https://apis.io/) network: OpenText Core Application Security (Fortify on Demand) API. Tagged areas include Cybersecurity, Application Security, Vulnerability Management, SAST, and DAST.


  The OpenText Cybersecurity catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  OpenText Cybersecurity''s developer surface includes documentation, API reference, getting-started guide, support, engineering blog, signup flow, pricing, and 36 more developer resources.'
plans:
- name: Opentext Cybersecurity Plans Pricing
  plan_count: 0
  slug: opentext-cybersecurity-plans-pricing
random_paper: 1
rate_limits:
- limit_count: 0
  name: Opentext Cybersecurity Rate Limits
  slug: opentext-cybersecurity-rate-limits
scopes:
- name: Opentext Cybersecurity Scopes
  scope_count: 0
  slug: opentext-cybersecurity-scopes
  summary_line: OAuth 2.0 · no documented scopes
security:
- kind: authentication
  name: Opentext Cybersecurity Authentication
  slug: opentext-cybersecurity-authentication
  summary_line: 0 schemes
- kind: domain-security
  name: Opentext Cybersecurity Domain Security
  slug: opentext-cybersecurity-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: opentext-cybersecurity
tags:
- Cybersecurity
- Application Security
- Vulnerability Management
- SAST
- DAST
- Endpoint Security
- Threat Detection
- Email Security
- Backup and Recovery
- Managed Service Providers
- Identity and Access
- Data Privacy
- Enterprise Software
website: https://cybersecurity.opentext.com/
---
