---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source: []
  trial: false
  try_now: false
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    asyncapi_events: false
    auth_clarity: false
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    idempotency: false
    mcp_server: true
    openapi_examples: false
    rate_limit_signal: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 10.8
  scored_at: '2026-07-28'
api_count: 4
apis:
- description: The Check Payroll API is a comprehensive REST API for embedding end-to-end U.S. payroll inside another platform. It models companies, workplaces, employees, contractors, pay schedules, paydays, payrol
  name: Check Payroll API
  slug: payroll-api
- description: Check Components is a library of white-labeled, drop-in React UI elements that handle the highest-friction surfaces of embedded payroll — company onboarding, terms of service, bank linking, employee t
  name: Check Components
  slug: components
- description: The Check MCP Server exposes the Check Payroll API to AI tools and agents via the Model Context Protocol. It is offered as both a hosted (remote) endpoint requiring no infrastructure and a self-hosted
  name: Check MCP Server
  slug: mcp-server
- description: The Check Command-Line Interface is a Python-based CLI installed via the uv package manager that exposes 270 functions across 18 resource groups of the Check Payroll API. It is designed for shell scri
  name: Check CLI
  slug: cli
artifact_total: 12
common:
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/check-hq-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/check-hq-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.checkhq.com
- group: docs
  title: ''
  type: Documentation
  url: https://docs.checkhq.com
- group: start
  title: ''
  type: Portal
  url: https://console.checkhq.com
- group: start
  title: ''
  type: Console
  url: https://console.checkhq.com/login
- group: start
  title: ''
  type: Sandbox
  url: https://sandbox.checkhq.com
- group: company
  title: ''
  type: Blog
  url: https://www.checkhq.com/resources
- group: operate
  title: ''
  type: ChangeLog
  url: https://www.checkhq.com/resources/changelog
- group: operate
  title: ''
  type: HelpCenter
  url: https://help.checkhq.com
- group: operate
  title: ''
  type: StatusPage
  url: https://docs.checkhq.com/docs/status-page
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/checkhq
- group: agent
  title: ''
  type: LlmsText
  url: https://docs.checkhq.com/llms.txt
- group: company
  title: ''
  type: Careers
  url: https://www.checkhq.com/company/careers
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/check-technologies
- group: company
  title: ''
  type: Crunchbase
  url: https://www.crunchbase.com/organization/check-2a75
- group: other
  title: ''
  type: Customers
  url: ''
- group: other
  title: ''
  type: Funding
  url: ''
- group: agent
  title: ''
  type: MCPServer
  url: https://github.com/check-technologies/mcp-server-check
- group: docs
  title: ''
  type: MCPDocumentation
  url: https://docs.checkhq.com/docs/overview
created: '2026-05-25'
description: Check is an embedded payroll infrastructure platform that allows vertical SaaS, HR, workforce management, and financial services companies to natively offer payroll inside their own products. Check provides a comprehensive REST API, a library of white-labeled React components (Check Components and Check Onboard), a CLI, and a Model Context Protocol (MCP) server that together cover company and employee onboarding, pay schedules, payroll preview and approval, contractor payments, tax calculation, multi-state withholdings, tax filings, tax deposits, money movement, paystubs, garnishments, post-tax deductions, net pay splits, benefits (health, 401k, workers' comp), W-2 and 1099 generation, and webhook event delivery. Check operates in all 50 U.S. states plus D.C., has been incubated and led-funded by Stripe (Series B and Series C), and powers payroll for partners such as Homebase, ServiceTitan, 7shifts, Housecall Pro, Wave, Zoho, and Procare — collectively paying more than 1M employees
  across 35,000+ businesses and moving $15B+ annually.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/check-hq.png
layout: provider
mcp_servers:
- description: ''
  name: MCP Server
  slug: mcp-server
modified: '2026-07-12'
name: Check
nav: Providers
network: true
overview: 'Check publishes 4 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Payroll, Embedded Payroll, Payroll Infrastructure, Payroll API, and Tax Filing.


  Check''s developer surface includes documentation, developer portal, developer console, sandbox, engineering blog, changelog, and 12 more developer resources.'
random_paper: 2
score:
  band: emerging
  composite: 19.1
  delta: -2.3
  facets:
    commercial_clarity: 0.0
    contract_quality: 0.0
    developer_ergonomics: 39.1
    discoverability: 64.8
    governance: 0.0
    operational_transparency: 36.8
  previous_composite: 21.4
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/check-hq/refs/heads/main/screenshots/check-hq-2026-06-20T174239.png
security:
- kind: domain-security
  name: Check Hq Domain Security
  slug: check-hq-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Check Hq Vulnerability Disclosure
  slug: check-hq-vulnerability-disclosure
  summary_line: disclosure policy published
slug: check-hq
solutions:
- description: Drop-in Components let early-stage platforms launch payroll quickly without bespoke UI.
  name: Startups
- description: Flexible API enables deeply customized payroll experiences for large vertical SaaS and workforce platforms.
  name: Enterprise Platforms
- description: Couple scheduling and timekeeping with end-to-end payroll, taxes, and money movement.
  name: Workforce Management
- description: Embed native payroll inside industry-specific software for trades, hospitality, fitness, and more.
  name: Vertical SaaS
- description: Sync payroll journals and tax events into accounting platforms with workplace breakdowns.
  name: Accounting and Financial Management
tags:
- Payroll
- Embedded Payroll
- Payroll Infrastructure
- Payroll API
- Tax Filing
- Tax Calculation
- Money Movement
- HR
- Human Resources
- Workforce Management
- Fintech
- Compensation
- Benefits
- '1099'
- W-2
- Contractor Payments
- Embedded Finance
website: https://www.checkhq.com
---
