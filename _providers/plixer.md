---
access_model:
  confidence: medium
  label: Paid
  onboarding: unknown
  pricing: paid
  public: false
  source:
  - plans
  trial: false
  try_now: false
api_count: 1
apis:
- description: REST API for Plixer Scrutinizer flow analytics — run flow reports, manage alarms, tune detections, trigger packet captures, and work with Collections. Scrutinizer is deployed as a self-hosted applianc
  name: Plixer Scrutinizer REST API
  slug: plixer-scrutinizer-rest-api
artifact_total: 4
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/plixer-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.plixer.com
- group: start
  title: ''
  type: DeveloperPortal
  url: https://docs.plixer.com
- group: docs
  title: ''
  type: Documentation
  url: https://docs.plixer.com
- group: company
  title: ''
  type: Blog
  url: https://www.plixer.com/blog/
- group: operate
  title: ''
  type: Support
  url: https://www.plixer.com/customers/support/open-case/
- group: commercial
  title: ''
  type: Pricing
  url: https://www.plixer.com/pricing/
- group: start
  title: ''
  type: SignUp
  url: https://www.plixer.com/demo/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.plixer.com/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.plixer.com/privacy
- group: agent
  title: ''
  type: MCPServer
  url: mcp/plixer-mcp.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/plixer-plans.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/plixer-llms.txt
created: '2026-07-17'
description: Plixer is a network observability and defense company whose platform combines network flow (NetFlow/IPFIX) data with AI-driven analysis to help IT and security teams investigate incidents, detect threats, and optimize performance across on-premises, cloud, and zero-trust environments. Its products include Plixer One (unified observability), Plixer Scrutinizer (flow-first visibility with a native MCP server), FlowPro (threat detection), Replicator (NetFlow distribution), Machine Learning behavioral analytics, Endpoint Analytics, and an AI Assistant for natural-language queries grounded in flow data. Plixer Scrutinizer exposes a REST API and, as of Plixer 19.8, a native Model Context Protocol server. Backed by Battery Ventures.
image: https://www.plixer.com/favicon.ico
layout: provider
mcp_servers:
- description: Plixer ships a native Model Context Protocol (MCP) server as part of Plixer Scrutinizer / Plixer One, released in Plixer 19.8 and available to all Scrutinizer and Plixer One customers at no additional
  name: Plixer MCP Server
  slug: plixer-mcp-server
modified: '2026-07-20'
name: Plixer
nav: Providers
network: true
overview: 'Plixer publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Network Observability, Network Security, Network Detection and Response, and NetFlow.


  Plixer''s developer surface includes documentation, engineering blog, support, pricing, signup flow, and 8 more developer resources.'
plans:
- name: Plixer Plans
  plan_count: 3
  slug: plixer-plans
random_paper: 9
screenshot: https://raw.githubusercontent.com/api-evangelist/plixer/refs/heads/main/screenshots/plixer-2026-09-02T151521.png
security:
- kind: domain-security
  name: Plixer Domain Security
  slug: plixer-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
slug: plixer
tags:
- Company
- Network Observability
- Network Security
- Network Detection and Response
- NetFlow
- IPFIX
- Network Traffic Analysis
- Cybersecurity
website: https://www.plixer.com
---
