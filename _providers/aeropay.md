---
api_count: 1
apis:
- baseURL: https://api.aeropay.com/v2
  baseurl_source: declared
  description: The Aeropay v2 REST API for pay-by-bank money movement. Issue merchant- or userForMerchant-scoped bearer tokens, create and confirm users, obtain Aerosync bank-linking credentials and attach the resul
  name: Aeropay v2 API
  slug: aeropay-v2-api
- description: 'Outbound HTTPS webhook deliveries covering nine topics across the ACH, RfP and RTP rails — transaction_completed, transaction_voided, transaction_refunded, transaction_declined, transaction_resolved, '
  name: Aeropay Webhooks
  slug: aeropay-webhooks
- description: A remote Model Context Protocol server hosted by Aeropay at https://dev.aero.inc/mcp, documented for Cursor, Windsurf and Claude Desktop. Anonymous tools/list returns four spec-driven tools — list-end
  name: Aeropay API MCP Server
  slug: aeropay-mcp
artifact_total: 11
asyncapis:
- description: Aeropay delivers transaction and user lifecycle events to a merchant-registered callback URL over HTTPS POST. A subscription is created with POST /v2/webhook by naming a topic and a url; the same call
  name: Aeropay Webhooks
  slug: aeropay-webhooks-asyncapi
common:
- group: company
  title: ''
  type: Website
  url: https://www.aeropay.com/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://www.aeropay.com/developers
- group: docs
  title: ''
  type: Documentation
  url: https://dev.aero.inc/docs/getting-started
- group: docs
  title: ''
  type: APIReference
  url: https://dev.aero.inc/reference/post_v2-token
- group: start
  title: ''
  type: GettingStarted
  url: https://dev.aero.inc/docs/api-quick-start
- group: operate
  title: ''
  type: Support
  url: https://www.aeropay.com/personal/support
- group: operate
  title: ''
  type: HelpCenter
  url: https://help.aeropay.com/
- group: company
  title: ''
  type: Blog
  url: https://www.aeropay.com/blog
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/Aeropay-inc
- group: start
  title: ''
  type: SignUp
  url: https://portal.aeropay.com/login
- group: commercial
  title: ''
  type: Pricing
  url: https://www.aeropay.com/demo
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.aeropay.com/legal/terms-of-service
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.aeropay.com/legal/privacy-policy
- group: auth
  title: ''
  type: TrustCenter
  url: security/aeropay-trust-center.yml
- group: auth
  title: ''
  type: Trust
  url: https://www.aeropay.com/trust-center
- group: auth
  title: ''
  type: Compliance
  url: https://www.aeropay.com/trust-center
- group: design
  title: ''
  type: Conformance
  url: conformance/aeropay-conformance.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/aeropay-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/aeropay-authentication.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/aeropay-conventions.yml
- group: design
  title: ''
  type: Idempotency
  url: conventions/aeropay-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/aeropay-problem-types.yml
- group: design
  title: ''
  type: ErrorCodes
  url: errors/aeropay-error-codes.yml
- group: build
  title: ''
  type: DeclineCodes
  url: errors/aeropay-decline-codes.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/aeropay-data-model.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/aeropay-lifecycle.yml
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/aeropay-changelog.yml
- group: operate
  title: ''
  type: ChangeLog
  url: https://dev.aero.inc/docs/release-notes
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/aeropay-rate-limits.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/aeropay-plans-pricing.yml
- group: build
  title: ''
  type: Packages
  url: packages/aeropay-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/aeropay-packages.yml
- group: build
  title: ''
  type: SDKs
  url: https://dev.aero.inc/docs/npm-sdk
- group: design
  title: ''
  type: Components
  url: components/aeropay-components.yml
- group: start
  title: ''
  type: Sandbox
  url: sandbox/aeropay-sandbox.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/aeropay-mcp.yml
- group: build
  title: ''
  type: ToolCrosswalk
  url: mcp/aeropay-tool-crosswalk.yml
- group: design
  title: ''
  type: Webhooks
  url: asyncapi/aeropay-webhooks-asyncapi.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/aeropay-llms.txt
- group: agent
  title: ''
  type: LLMsTxt
  url: https://dev.aero.inc/llms.txt
- group: agent
  title: ''
  type: LLMsTxt
  url: https://www.aeropay.com/llms.txt
- group: other
  title: ''
  type: Overlay
  url: overlays/aeropay-v2-overlay.yaml
created: '2026-09-10'
description: Aeropay is a Chicago-based fintech operating a pay-by-bank network that moves money directly between consumer bank accounts and merchants over ACH, Request for Payment (RfP) and RTP rails, without cards. The product suite is Aerosync (branded bank linking and account connectivity), Pay (merchant acceptance of bank payments), Payout (real-time merchant-to-consumer credits) and Guard (risk decisioning and fraud prevention). Integrators use the Aeropay v2 REST API — a 32-operation OpenAPI 3.0.0 contract covering token issuance, user creation and MFA confirmation, bank linking through an aggregator widget, standard, preauthorized, payout and reversal transactions, transaction search, payment links, webhook subscriptions, reporting and merchant reputation — alongside first-party Aerosync bank-linking SDKs for web, React Native, Android, iOS and Flutter. Aeropay publishes a documentation llms.txt, a remote MCP server for the API reference, a nine-topic webhook catalog, a 91-entry
  error glossary, a NACHA ACH return-code glossary and a substantial sandbox exception-scenario harness. It is SOC 2 compliant and audits its ACH operations annually against NACHA standards.
image: https://cdn.prod.website-files.com/6883a0f9156861b50901e79e/68d3ffdc98b692fcb2df6fa4_Aeropay-256xv2.png
layout: provider
mcp_servers:
- description: ''
  name: Aeropay MCP Server
  slug: aeropay-mcp-server
- description: ''
  name: Aeropay MCP Server
  slug: aeropay-mcp-server-2
modified: '2026-09-10'
name: Aeropay
nav: Providers
network: true
overview: 'Aeropay publishes 1 API on the [APIs.io](https://apis.io/) network: v2 API. Tagged areas include Payments, Pay by bank, ACH, Open Banking, and Fintech.


  The Aeropay catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  Aeropay''s developer surface includes documentation, API reference, getting-started guide, support, engineering blog, signup flow, pricing, and 36 more developer resources.'
plans:
- name: Aeropay Plans Pricing
  plan_count: 0
  slug: aeropay-plans-pricing
random_paper: 18
rate_limits:
- limit_count: 0
  name: Aeropay Rate Limits
  slug: aeropay-rate-limits
security:
- kind: authentication
  name: Aeropay Authentication
  slug: aeropay-authentication
  summary_line: http-bearer/credentials-exchange · 2 schemes
- kind: domain-security
  name: Aeropay Domain Security
  slug: aeropay-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: trust-center
  name: Aeropay Trust Center
  slug: aeropay-trust-center
  summary_line: SOC 2, Nacha ACH Operating Rules
slug: aeropay
tags:
- Payments
- Pay by bank
- ACH
- Open Banking
- Fintech
- Bank linking
- Financial Services
- Real-time payments
- Webhook
- Payouts
- MCP
- Risk & fraud
website: https://www.aeropay.com/
---
