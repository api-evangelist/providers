---
api_count: 1
apis:
- baseURL: https://secure.agree.com/api/v1
  baseurl_source: declared
  description: 'REST API for the Agree contract-to-cash platform. 56 operations across six resources: Agreements (create from templates, assign signature fields to recipients, send, fetch executed PDFs, soft delete),'
  name: Agree API
  slug: agree-api
artifact_total: 8
asyncapis:
- description: Real-time event notifications from the Agree contract-to-cash platform. Agree POSTs a signed JSON body to endpoints you register through POST /api/v1/webhooks. Twelve event types are published, coveri
  name: Agree.com Webhooks
  slug: agree-com-webhooks-asyncapi
common:
- group: company
  title: ''
  type: Website
  url: https://agree.com/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://agree.com/developers
- group: docs
  title: ''
  type: Documentation
  url: https://secure.agree.com/documentation
- group: docs
  title: ''
  type: APIReference
  url: https://secure.agree.com/documentation
- group: start
  title: ''
  type: GettingStarted
  url: https://secure.agree.com/documentation#section/Introduction/Quick-Start
- group: commercial
  title: ''
  type: Pricing
  url: https://agree.com/pricing
- group: start
  title: ''
  type: SignUp
  url: https://secure.agree.com/signup
- group: start
  title: ''
  type: Login
  url: https://secure.agree.com/signin
- group: commercial
  title: ''
  type: TermsOfService
  url: https://agree.com/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://agree.com/privacy
- group: docs
  title: ''
  type: OpenAPI
  url: openapi/agree-com-api-openapi.json
- group: agent
  title: ''
  type: MCPServer
  url: mcp/agree-com-mcp.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/agree-com-well-known.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/agree-com-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/agree-com-scopes.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/agree-com-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/agree-com-problem-types.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/agree-com-data-model.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/agree-com-lifecycle.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/agree-com-conformance.yml
- group: docs
  title: ''
  type: AsyncAPI
  url: asyncapi/agree-com-webhooks-asyncapi.yml
- group: design
  title: ''
  type: Webhooks
  url: asyncapi/agree-com-webhooks-asyncapi.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/agree-com-llms.txt
- group: other
  title: ''
  type: Overlay
  url: overlays/agree-com-api-overlay.yaml
- group: commercial
  title: ''
  type: Plans
  url: plans/agree-com-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/agree-com-rate-limits.yml
- group: build
  title: ''
  type: Packages
  url: packages/agree-com-packages.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/agree-com-domain-security.yml
created: '2026-09-12'
description: Agree.com is a contract-to-cash platform that combines free, unlimited e-signatures with invoicing, billing and integrated payments, positioning itself directly against DocuSign and Bill.com by giving the signature product away and monetizing the money movement that follows it. The company raised a $7.2M seed round led by Pelion Venture Partners in May 2025 after a $3M pre-seed led by Better Tomorrow Ventures. It markets an "agentic revenue operating system" built from named AI agents for contracts, billing, collections, recovery, reconciliation and insight. For developers it publishes a 56-operation REST API covering agreements, invoices, contacts, customers, cash-flow and recovery reporting, and webhooks, described by a real OpenAPI 3.0 document served anonymously at secure.agree.com/documentation/openapi, plus a hosted remote MCP server at secure.agree.com/mcp discoverable through RFC 9728 protected resource metadata and guarded by an OAuth 2.1 authorization server with PKCE
  and dynamic client registration.
image: https://agree.com/img/social/social-media-card.png
layout: provider
mcp_servers:
- description: 'Agree.com operates a hosted, remote Model Context Protocol server at https://secure.agree.com/mcp. It was discovered through RFC 9728 protected-resource metadata rather than the documentation: the res'
  name: Agree.com MCP Server
  slug: agreecom-mcp-server
modified: '2026-09-12'
name: Agree.com
nav: Providers
network: true
overview: 'Agree.com publishes 1 API on the [APIs.io](https://apis.io/) network: Agree API. Tagged areas include Agreements, Electronic Signature, Contract Management, Invoicing, and Billing.


  The Agree.com catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  Agree.com''s developer surface includes documentation, API reference, getting-started guide, pricing, signup flow, authentication, and 23 more developer resources.'
plans:
- name: Agree Com Plans Pricing
  plan_count: 3
  slug: agree-com-plans-pricing
random_paper: 19
rate_limits:
- limit_count: 0
  name: Agree Com Rate Limits
  slug: agree-com-rate-limits
scopes:
- name: Agree Com Scopes
  scope_count: 0
  slug: agree-com-scopes
  summary_line: OAuth 2.0 · no documented scopes
security:
- kind: authentication
  name: Agree Com Authentication
  slug: agree-com-authentication
  summary_line: http/oauth2 · 2 schemes
- kind: domain-security
  name: Agree Com Domain Security
  slug: agree-com-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: agree-com
tags:
- Agreements
- Electronic Signature
- Contract Management
- Invoicing
- Billing
- Payments
- Accounts Receivable
- Fintech
- Financial-Services
- Webhooks
- MCP
- agent-native
website: https://agree.com/
---
