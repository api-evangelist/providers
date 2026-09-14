---
api_count: 1
apis:
- description: Public REST API over Brazil's PNCP procurement portal with full-text tender search, tender sheets and deadlines, edital markdown, eligibility extraction, alerts and watchers. Also exposes a hosted MCP
  name: EditalMD API
  slug: editalmd-api
artifact_total: 9
asyncapis:
- description: ''
  name: Editalmd Webhooks
  slug: editalmd-webhooks
common:
- group: company
  title: ''
  type: Website
  url: https://editalmd.com
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/editalmd-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/editalmd-domain-security.yml
- group: auth
  title: ''
  type: Security
  url: security/editalmd-vulnerability-disclosure.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/editalmd-well-known.yml
- group: auth
  title: ''
  type: SecurityTxt
  url: well-known/editalmd-security.txt
- group: commercial
  title: ''
  type: TermsOfService
  url: https://editalmd.com/termos
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://editalmd.com/privacidade
- group: commercial
  title: ''
  type: Pricing
  url: https://editalmd.com/#precos
created: '2026-09-05'
description: Agent-native data API over Brazil's public-procurement portal PNCP (Portal Nacional de Contratações Públicas). Provides full-text tender search, proposal and challenge deadlines, editais rendered as markdown with provenance and SHA-256 hashes, new-tender alerts by keyword or CNPJ, tender change-watchers, and extracted eligibility (habilitação) checklists. Search is free; other routes are paid per request (x402) or via prepaid credit with no signup.
image: https://editalmd.com/icon.svg
layout: provider
mcp_servers:
- description: ''
  name: EditalMD MCP Server
  slug: editalmd-mcp-server
- description: 'Hosted first-party MCP server (Streamable HTTP, JSON-RPC 2.0) dispatched by the same Cloudflare Worker as the REST API. Exposes 19 tools covering the whole product: free PNCP tender search, tender she'
  name: EditalMD MCP Server
  slug: editalmd-mcp-server-2
modified: '2026-09-05'
name: EditalMD
nav: Providers
network: true
overview: 'EditalMD publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include GovTech, Public Procurement, Brazil, PNCP, and Legal & Compliance.


  The EditalMD catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  EditalMD''s developer surface includes pricing and 8 more developer resources.'
plans:
- name: Editalmd Plans Pricing
  plan_count: 0
  slug: editalmd-plans-pricing
random_paper: 17
rate_limits:
- limit_count: 2
  name: Editalmd Rate Limits
  slug: editalmd-rate-limits
security:
- kind: authentication
  name: Editalmd Authentication
  slug: editalmd-authentication
  summary_line: 4 schemes
- kind: domain-security
  name: Editalmd Domain Security
  slug: editalmd-domain-security
  summary_line: TLSv1.3
- kind: vulnerability-disclosure
  name: Editalmd Vulnerability Disclosure
  slug: editalmd-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: editalmd
tags:
- GovTech
- Public Procurement
- Brazil
- PNCP
- Legal & Compliance
- Business Intelligence
- Company Data
- CNPJ
- CNAE
- SICAF
- Document Extraction
- Agent-Native
- MCP
- x402
- Machine-Payable
website: https://editalmd.com
---
