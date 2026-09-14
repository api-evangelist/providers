---
api_count: 1
apis:
- description: REST API for fetching public YouTube transcripts synchronously and in bulk, with account/balance endpoints, job polling, and completion webhooks. Bearer API key or X-API-Key auth.
  name: Media Caption Public API
  slug: media-caption-public-api
artifact_total: 7
asyncapis:
- description: ''
  name: Mediacaption Api Webhooks
  slug: mediacaption-api-webhooks
common:
- group: company
  title: ''
  type: Website
  url: https://mediacaption.io
- group: auth
  title: ''
  type: DomainSecurity
  url: security/mediacaption-api-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/mediacaption-api-authentication.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/mediacaption-api-well-known.yml
- group: design
  title: ''
  type: Webhooks
  url: asyncapi/mediacaption-api-webhooks.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/mediacaption-api-mcp.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/mediacaption-api-llms.txt
- group: design
  title: ''
  type: Conformance
  url: conformance/mediacaption-api-conformance.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/mediacaption-api-problem-types.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/mediacaption-api-lifecycle.yml
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/mediacaption-api-changelog.yml
- group: operate
  title: ''
  type: ChangeLog
  url: https://www.mediacaption.io/docs/changelog
- group: design
  title: ''
  type: Conventions
  url: conventions/mediacaption-api-conventions.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/mediacaption-api-data-model.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/mediacaption-api-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/mediacaption-api-rate-limits.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: commercial
  title: ''
  type: Pricing
  url: https://www.mediacaption.io/pricing
- group: operate
  title: ''
  type: Support
  url: https://www.mediacaption.io/report
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.mediacaption.io/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.mediacaption.io/privacy
created: '2026-07-18'
description: A credit-billed REST API for retrieving public YouTube transcripts, with single and bulk transcript jobs, job-level webhooks, and AI transcription/translation capabilities. Backed by a public OpenAPI 3.1 contract with bearer/X-API-Key authentication.
image: https://www.mediacaption.io/android-chrome-512x512.png
layout: provider
mcp_servers:
- description: Media Caption ships no MCP server — no hosted endpoint, no stdio package, no MCP mention anywhere in the docs, and a web search finds only unaffiliated third-party YouTube-caption servers. This is a c
  name: MediaCaption API MCP Server
  slug: mediacaption-api-mcp-server
modified: '2026-09-03'
name: MediaCaption API
nav: Providers
network: true
overview: 'MediaCaption API publishes 1 API on the [APIs.io](https://apis.io/) network: Media Caption Public API. Tagged areas include YouTube, Transcription, Captions, Subtitles, and Video.


  The MediaCaption API catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  MediaCaption API''s developer surface includes authentication, changelog, pricing, support, and 17 more developer resources.'
plans:
- name: Mediacaption Api Plans Pricing
  plan_count: 2
  slug: mediacaption-api-plans-pricing
random_paper: 4
rate_limits:
- limit_count: 4
  name: Mediacaption Api Rate Limits
  slug: mediacaption-api-rate-limits
screenshot: https://raw.githubusercontent.com/api-evangelist/mediacaption-api/refs/heads/main/screenshots/mediacaption-api-2026-08-07T172332.png
security:
- kind: authentication
  name: Mediacaption Api Authentication
  slug: mediacaption-api-authentication
  summary_line: apiKey/http · 2 schemes
- kind: domain-security
  name: Mediacaption Api Domain Security
  slug: mediacaption-api-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: mediacaption-api
tags:
- YouTube
- Transcription
- Captions
- Subtitles
- Video
- REST
- OpenAPI
- Webhook
- Speech-to-Text
- Media
- Developer Tools
website: https://mediacaption.io
---
