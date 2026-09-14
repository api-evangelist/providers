---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source:
  - authentication
  - security
  trial: false
  try_now: false
agentic_access:
- acting_count: 1
  human_in_the_loop: 0
  name: Automat Agentic Access
  operation_count: 1
  slug: automat-agentic-access
  summary_line: 1 operation · 1 acting
api_count: 1
apis:
- baseURL: https://studio.runautomat.com
  baseurl_source: declared
  description: The extract API from Automat — 1 operation(s) for extract.
  name: Automat extract API
  slug: automat-extract-api
artifact_total: 8
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: extract API
  slug: open-automat-extract-api
common:
- group: other
  title: ''
  type: Overlay
  url: overlays/automat-extract-overlay.yaml
- group: company
  title: ''
  type: Website
  url: https://www.runautomat.com/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://docs.runautomat.com/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.runautomat.com/
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.runautomat.com/guides/getting-started/introduction
- group: docs
  title: ''
  type: APIReference
  url: https://docs.runautomat.com/api-reference
- group: agent
  title: ''
  type: MCPServer
  url: mcp/automat-mcp.yml
- group: company
  title: ''
  type: Blog
  url: https://www.runautomat.com/blog
- group: operate
  title: ''
  type: Support
  url: https://www.runautomat.com/contact
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.runautomat.com/terms-of-service
- group: auth
  title: ''
  type: TrustCenter
  url: https://trust.runautomat.com/
- group: auth
  title: ''
  type: Compliance
  url: https://trust.runautomat.com/
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/automat-llms.txt
- group: auth
  title: ''
  type: Authentication
  url: authentication/automat-authentication.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/automat-domain-security.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/automat-conformance.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
created: '2026-07-17'
description: Automat builds AI agents that operate computers the way people do, replacing legacy RPA tools like UiPath, Automation Anywhere, and Blue Prism with intelligent, self-healing managed automations. Founded in 2022 by ex-Google engineers, the platform combines UI-based AI agents (RPA using Computer Use), AI document extraction (IDP with vision language models), and API-based automations (iPaaS) into unified workflows delivered as a managed service. Automat exposes a REST Extract API (studio.runautomat.com) for pulling structured data from PDFs, images, and other documents against a configured extractor, plus a hosted MCP server for AI client integration. Used across banking, mortgage and lending, insurance, manufacturing, healthcare, and e-commerce operations, with SOC 2, GDPR, HIPAA, and ISO 27001 certification.
image: https://cdn.prod.website-files.com/690942210854e5c7d0b74b4e/690fc6fc0297c12536ccca4b_ab7962bb06ce21cd863411aefecd6599_Frame%20427322741.png
layout: provider
mcp_servers:
- description: Hosted MCP server published by Automat for AI client integration (Claude Code, Cursor, and other MCP clients). Advertised in the Automat documentation and llms.txt. Exposes the Automat documentation a
  name: Automat MCP Server
  slug: automat-mcp-server
modified: '2026-07-18'
name: Automat
nav: Providers
network: true
overview: 'Automat publishes 1 API on the [APIs.io](https://apis.io/) network: extract API. Tagged areas include Company, Enterprise Saas, Automation, RPA, and Robotic Process Automation.


  Automat''s developer surface includes documentation, getting-started guide, API reference, engineering blog, support, authentication, and 11 more developer resources.'
random_paper: 7
screenshot: https://raw.githubusercontent.com/api-evangelist/automat/refs/heads/main/screenshots/automat-2026-07-25T201833.png
security:
- kind: authentication
  name: Automat Authentication
  slug: automat-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Automat Domain Security
  slug: automat-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
- kind: trust-center
  name: Automat Trust Center
  slug: automat-trust-center
  summary_line: SOC 2, ISO 27001, HIPAA, GDPR
slug: automat
tags:
- Company
- Enterprise Saas
- Automation
- RPA
- Robotic Process Automation
- Document Extraction
- IDP
- iPaaS
- AI Agents
- Computer Use
- Document Processing
website: https://www.runautomat.com/
---
