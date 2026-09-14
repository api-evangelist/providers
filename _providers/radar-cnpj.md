---
api_count: 1
apis:
- description: 'Public REST API over the Brazilian CNPJ registry: business-idea evaluation, CNPJ lookup, advanced search/export, free-text-to-filters IA translation, geolocation, and anonymous monitoring. Mostly no-a'
  name: Radar CNPJ API
  slug: radar-cnpj-api
artifact_total: 8
common:
- group: company
  title: ''
  type: Website
  url: https://radar-cnpj.com
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/radar-cnpj-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: Security
  url: security/radar-cnpj-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/radar-cnpj-domain-security.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/radar-cnpj-well-known.yml
- group: auth
  title: ''
  type: SecurityTxt
  url: well-known/radar-cnpj-security.txt
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://radar-cnpj.com/termos
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://radar-cnpj.com/privacidade
- group: other
  title: ''
  type: X-OKF
  url: okf/radar-cnpj-okf-index.md
created: '2026-09-05'
description: Brazilian company-data service built on the Receita Federal CNPJ registry. Paste a business idea in plain text to see how many companies already operate in that space, plus CNPJ lookup, advanced search, geolocation, and change-monitoring. Explicitly agent-first, shipping a full stack of machine-readable discovery artifacts including OpenAPI, a hosted MCP server, and llms.txt.
image: https://radar-cnpj.com/icon.svg
layout: provider
mcp_servers:
- description: ''
  name: Radar CNPJ MCP Server
  slug: radar-cnpj-mcp-server
- description: Official hosted MCP server for Radar CNPJ (Streamable HTTP, JSON-RPC 2.0). GET /mcp returns a server card; POST /mcp answers initialize, tools/list and tools/call with no authentication. Every tool is
  name: Radar CNPJ MCP Server
  slug: radar-cnpj-mcp-server-2
modified: '2026-09-05'
name: Radar CNPJ
nav: Providers
network: true
overview: Radar CNPJ publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Business & Company Data, Government/Open Data, Receita Federal, CNPJ, and Brazil.
plans:
- name: Radar Cnpj Plans Pricing
  plan_count: 2
  slug: radar-cnpj-plans-pricing
random_paper: 7
rate_limits:
- limit_count: 3
  name: Radar Cnpj Rate Limits
  slug: radar-cnpj-rate-limits
security:
- kind: authentication
  name: Radar Cnpj Authentication
  slug: radar-cnpj-authentication
  summary_line: 5 schemes
- kind: domain-security
  name: Radar Cnpj Domain Security
  slug: radar-cnpj-domain-security
  summary_line: TLSv1.3 · DMARC
- kind: vulnerability-disclosure
  name: Radar Cnpj Vulnerability Disclosure
  slug: radar-cnpj-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: radar-cnpj
tags:
- Business & Company Data
- Government/Open Data
- Receita Federal
- CNPJ
- Brazil
- Regulatory & Compliance
- KYB
- Search
- Data Enrichment
- Geolocation
- Monitoring & Alerts
- Agent-native
- MCP
- Micropayments
- x402
website: https://radar-cnpj.com
---
