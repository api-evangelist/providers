---
api_count: 4
apis:
- description: Token-authenticated REST API behind the AccuKnox SaaS console, serving asset inventory, security findings, AI/ML model risk (ModelKnox) and tenant configuration under an /api/v1/ path prefix. Served p
  name: AccuKnox SaaS Platform API
  slug: accuknox-saas-platform-api
- description: gRPC services for AccuKnox Discovery Engine (knoxAutoPolicy), which auto-discovers least-permissive network and system policies from observed workload behaviour. Nine published proto3 contracts coveri
  name: AccuKnox Discovery Engine gRPC API
  slug: accuknox-discovery-engine
- description: gRPC services for SentryFlow, AccuKnox's API observability and classification component. Streams API access logs, API events and Envoy/API metrics from service mesh and ingress data planes, and classi
  name: AccuKnox SentryFlow API Observability gRPC API
  slug: accuknox-sentryflow
- description: First-party Model Context Protocol server published by AccuKnox that exposes the SaaS Platform API to agents as MCP tools for asset search, finding retrieval, finding filters and funnels, and AI/ML mo
  name: AccuKnox MCP Server
  slug: accuknox-mcp-server
artifact_total: 12
asyncapis:
- description: ''
  name: Accuknox Webhooks
  slug: accuknox-webhooks
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/accuknox-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://accuknox.com/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://help.accuknox.com/
- group: docs
  title: ''
  type: Documentation
  url: https://help.accuknox.com/
- group: start
  title: ''
  type: GettingStarted
  url: https://help.accuknox.com/how-to/
- group: operate
  title: ''
  type: Support
  url: https://accu-knox.atlassian.net/servicedesk/customer/portal/1
- group: company
  title: ''
  type: Blog
  url: https://accuknox.com/blog
- group: company
  title: ''
  type: BlogRSS
  url: https://accuknox.com/feed
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/accuknox
- group: commercial
  title: ''
  type: Pricing
  url: https://accuknox.com/pricing
- group: start
  title: ''
  type: SignUp
  url: https://accuknox.com/free-trial
- group: commercial
  title: ''
  type: TermsOfService
  url: https://accuknox.com/terms-of-use
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://accuknox.com/privacy-policy
- group: operate
  title: ''
  type: StatusPage
  url: https://status.accuknox.com/
- group: operate
  title: ''
  type: ChangeLog
  url: https://help.accuknox.com/getting-started/accuknox-release-notes/
- group: build
  title: ''
  type: SourceCode
  url: https://accuknox.com/open-source-repos
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/accuknox-llms.txt
- group: build
  title: ''
  type: Packages
  url: packages/accuknox-packages.yml
- group: build
  title: ''
  type: CLI
  url: cli/accuknox-cli.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/accuknox-mcp.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/accuknox-authentication.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/accuknox-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/accuknox-error-codes.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/accuknox-lifecycle.yml
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/accuknox-changelog.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/accuknox-conformance.yml
- group: design
  title: ''
  type: Webhooks
  url: asyncapi/accuknox-webhooks.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/accuknox-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/accuknox-rate-limits.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/accuknox-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: Security
  url: https://accuknox.com/security-advisories
created: '2026-09-06'
description: AccuKnox is a cloud-native application protection platform (CNAPP) vendor built on a Zero Trust model, covering cloud security posture management (CSPM), workload and Kubernetes runtime security (CWPP), application security posture management (ASPM), AI/ML model security (AI-SPM / ModelKnox) and API security. It originated the open source KubeArmor eBPF/LSM runtime enforcement engine (a CNCF project) and publishes the Discovery Engine and SentryFlow gRPC services, a knoxctl CLI, a Terraform provider, a first-party Model Context Protocol server, and a token-authenticated REST API on per-tenant cspm.*.accuknox.com hosts.
image: https://accuknox.com/wp-content/uploads/accuknox-logo-2.png
layout: provider
mcp_servers:
- description: ''
  name: AccuKnox Asset Manager
  slug: accuknox-asset-manager
modified: '2026-09-06'
name: AccuKnox
nav: Providers
network: true
overview: 'AccuKnox publishes 4 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Security, Cloud Security, Cloud Native Application Protection Platform, and Kubernetes Security.


  The AccuKnox catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  AccuKnox''s developer surface includes documentation, getting-started guide, support, engineering blog, pricing, signup flow, changelog, and 24 more developer resources.'
plans:
- name: Accuknox Plans Pricing
  plan_count: 0
  slug: accuknox-plans-pricing
random_paper: 20
rate_limits:
- limit_count: 0
  name: Accuknox Rate Limits
  slug: accuknox-rate-limits
scopes:
- name: Accuknox Scopes
  scope_count: 0
  slug: accuknox-scopes
  summary_line: OAuth 2.0 · no documented scopes
security:
- kind: authentication
  name: Accuknox Authentication
  slug: accuknox-authentication
  summary_line: http/oauth2 · 3 schemes
- kind: domain-security
  name: Accuknox Domain Security
  slug: accuknox-domain-security
  summary_line: TLSv1.3 · DMARC
- kind: vulnerability-disclosure
  name: Accuknox Vulnerability Disclosure
  slug: accuknox-vulnerability-disclosure
  summary_line: Hackerone · contact published
slug: accuknox
tags:
- Company
- Security
- Cloud Security
- Cloud Native Application Protection Platform
- Kubernetes Security
- Runtime Security
- Zero Trust
- DevSecOps
- Compliance
- AI Security
- Vulnerability Management
- Container Security
website: https://accuknox.com/
---
