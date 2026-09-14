---
api_count: 1
apis:
- baseURL: https://skills.workera.ai/api/v1
  baseurl_source: declared
  description: First-party REST API for the Workera skills-intelligence platform. Read-oriented, task-shaped endpoints expose capabilities (domains) and their competency models, programs, v2 capability scores and se
  name: Workera API
  slug: workera-api
artifact_total: 9
asyncapis:
- description: Workera delivers HTTP POST webhooks to a customer-configured endpoint when assessment, program and appeal events occur. Endpoints, event-type subscriptions and the shared signing secret are provisione
  name: Workera Webhooks
  slug: workera-events-asyncapi
common:
- group: auth
  title: ''
  type: TrustCenter
  url: security/workera-trust-center.yml
- group: company
  title: ''
  type: Website
  url: https://www.workera.ai/
- group: company
  title: ''
  type: Blog
  url: https://www.workera.ai/resources/blog
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/workera-ai
- group: operate
  title: ''
  type: Support
  url: https://www.workera.ai/resources/faq
- group: start
  title: ''
  type: Login
  url: https://skills.workera.ai/app/login
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.workera.ai/legal/terms-of-use
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.workera.ai/legal/privacy-policy
- group: operate
  title: ''
  type: StatusPage
  url: https://status.workera.ai/
- group: auth
  title: ''
  type: TrustCenter
  url: https://trust.workera.ai/
- group: auth
  title: ''
  type: Security
  url: https://www.workera.ai/legal/responsible-vulnerability-disclosure-program
- group: auth
  title: ''
  type: Compliance
  url: https://www.workera.ai/legal/security
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/workera-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/workera-domain-security.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/workera-mcp.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/workera-well-known.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/workera-llms.txt
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/workera-plans-pricing.yml
- group: build
  title: ''
  type: Packages
  url: packages/workera-packages.yml
created: '2026-09-04'
description: Workera is an enterprise skills-intelligence platform that measures, verifies and develops workforce capability. Adaptive AI assessments score individuals against a granular skill ontology spanning AI, machine learning, data science, data engineering, cloud, cybersecurity and software engineering, then benchmark those verified scores against role requirements and industry cohorts so L&D leaders, technical leaders and CHROs can plan hiring, upskilling and internal mobility on measured capability rather than self-reported data. The platform integrates with HRIS, ATS, LMS and credentialing systems (Workday, SAP SuccessFactors, Oracle HCM, Greenhouse, Degreed, Udemy, Coursera, LinkedIn Learning, Udacity, O'Reilly, Credly) and exposes a first-party REST API plus an OAuth-protected remote MCP server for programmatic access to capabilities, programs, scores, self-ratings, benchmarks and SIEM-compatible audit events.
image: https://cdn.prod.website-files.com/68f1fe758b057338579c914a/691af34214ea5b2bbdf49f55_webclip.png
layout: provider
mcp_servers:
- description: ''
  name: Workera MCP Server
  slug: workera-mcp-server
modified: '2026-09-04'
name: Workera
nav: Providers
network: true
overview: 'Workera publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Skills Intelligence, Skills Assessment, Human Resources, Learning and Development, and Talent Management.


  The Workera catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  Workera''s developer surface includes engineering blog, support, and 18 more developer resources.'
plans:
- name: Workera Plans Pricing
  plan_count: 0
  slug: workera-plans-pricing
random_paper: 7
rate_limits:
- limit_count: 0
  name: Workera Rate Limits
  slug: workera-rate-limits
security:
- kind: authentication
  name: Workera Authentication
  slug: workera-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Workera Domain Security
  slug: workera-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Workera Vulnerability Disclosure
  slug: workera-vulnerability-disclosure
  summary_line: disclosure policy published
- kind: trust-center
  name: Workera Trust Center
  slug: workera-trust-center
  summary_line: ISO/IEC 27001, ISO/IEC 42001, SOC 2 Type II, GDPR
slug: workera
tags:
- Skills Intelligence
- Skills Assessment
- Human Resources
- Learning and Development
- Talent Management
- Workforce Analytics
- Artificial Intelligence
- Benchmarking
- Enterprise Software
- MCP
- Company
website: https://www.workera.ai/
---
