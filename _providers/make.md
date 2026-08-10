---
access_model:
  confidence: high
  label: Freemium · Self-serve signup
  onboarding: self-serve
  pricing: freemium
  public: false
  source:
  - plans
  - authentication
  trial: false
  try_now: true
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 30.6
  scored_at: '2026-08-10'
agentic_access:
- acting_count: 12
  human_in_the_loop: 1
  name: Make Agentic Access
  operation_count: 20
  slug: make-agentic-access
  summary_line: 20 operations · 12 acting · 1 human-in-the-loop
api_count: 8
apis:
- description: The Make REST API allows using HTTP requests to access Make data and control the Make platform without opening its graphical interface. It provides endpoints for managing scenarios, connections, organ
  name: Make API
  slug: make-api
- description: The Make Custom Apps platform enables developers to create their own applications for the Make automation platform using the Apps Editor or the VS Code extension. It provides documentation for buildin
  name: Make Custom Apps
  slug: custom-apps
- description: The Make MCP Server allows AI systems such as large language models to run scenarios and manage the contents of a Make account using the Model Context Protocol (MCP) standard. It is available as a clo
  name: Make MCP Server
  slug: mcp-server
- description: Make White Label provides OEM customers with the ability to manage and administrate their own white-labeled instance of Make, including rebranding appearance, managing user access roles, creating orga
  name: Make White Label
  slug: white-label
- description: The AI Agents API from Make — 1 operation(s) for ai agents.
  name: Make AI Agents API
  slug: make-ai-agents-api
- description: The Scenario Execution API from Make — 5 operation(s) for scenario execution.
  name: Make Scenario Execution API
  slug: make-scenario-execution-api
- description: The Scenario Variables API from Make — 1 operation(s) for scenario variables.
  name: Make Scenario Variables API
  slug: make-scenario-variables-api
- description: The Scenarios API from Make — 6 operation(s) for scenarios.
  name: Make Scenarios API
  slug: make-scenarios-api
artifact_total: 31
collections:
- collection_type: open
  name: Make API
  slug: open-make
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/make-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/make-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/make-authentication.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/itsmakehq
- group: start
  title: ''
  type: Portal
  url: https://developers.make.com/
- group: start
  title: ''
  type: GettingStarted
  url: https://developers.make.com/api-documentation/getting-started
- group: company
  title: ''
  type: Blog
  url: https://www.make.com/en/blog
- group: start
  title: ''
  type: Login
  url: https://www.make.com/en/login
- group: start
  title: ''
  type: Signup
  url: https://www.make.com/en/register
- group: commercial
  title: ''
  type: Pricing
  url: https://www.make.com/en/pricing
- group: operate
  title: ''
  type: HelpCenter
  url: https://help.make.com/
- group: operate
  title: ''
  type: StatusPage
  url: https://status.make.com/
- group: auth
  title: ''
  type: Security
  url: https://www.make.com/en/security
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.make.com/en/privacy-notice
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.make.com/en/terms-and-conditions
- group: operate
  title: ''
  type: Community
  url: https://community.make.com/
- group: learn
  title: ''
  type: Academy
  url: https://academy.make.com/
- group: build
  title: ''
  type: GitHubOrg
  url: https://github.com/integromat
- group: build
  title: ''
  type: TypeScriptSDK
  url: https://github.com/integromat/make-typescript-sdk
- group: build
  title: ''
  type: VSCodeExtension
  url: https://github.com/integromat/vscode-apps-sdk
- group: auth
  title: ''
  type: GDPR
  url: https://www.make.com/en/privacy-and-gdpr
- group: agent
  title: ''
  type: LlmsText
  url: https://developers.make.com/llms.txt
created: '2026-03-03'
description: Make (formerly Integromat) is a visual scenario-based automation builder with advanced data transformation and routing logic.
features:
- 'Free: 1,000 ops/month, 15-min minimum scheduling'
- 'Core $12/mo: 10K ops, unlimited scenarios, minute scheduling'
- 'Pro $21/mo: priority execution, custom variables, log search'
- 'Teams $38/mo: team roles, shared templates'
- 'Enterprise: custom functions, advanced security, 24/7 support'
- 3,000+ pre-built apps
- Visual scenario builder with routers and filters
- Make API on Core+ at 60 req/min/org
- 'Webhook scenarios: 100 req/sec'
- Make AI Tools (formerly Make Apps Cloud)
- Make Bridge for embedded iPaaS
- Custom apps via Make App Builder
- Conditional logic (routers, filters, iterators)
- Aggregators for batched processing
- Error handlers per module
- OAuth + API tokens
finops:
- name: Make Finops
  service_category: iPaaS
  slug: make-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/make.png
layout: provider
modified: '2026-05-04'
name: Make
nav: Providers
network: true
overview: 'Make publishes 4 APIs on the [APIs.io](https://apis.io/) network, including AI Agents API, Scenario Execution API, Scenario Variables API, and 1 more. Tagged areas include Automation, Integration, iPaaS, No-Code, and Scenarios.


  Make''s developer surface includes authentication, developer portal, getting-started guide, engineering blog, signup flow, pricing, academy / training, and 15 more developer resources.'
plans:
- name: Make Plans Pricing
  plan_count: 5
  slug: make-plans-pricing
random_paper: 66
rate_limits:
- limit_count: 2
  name: Make Rate Limits
  slug: make-rate-limits
score:
  band: developing
  composite: 51.0
  delta: 0.0
  facets:
    commercial_clarity: 84.2
    contract_quality: 57.4
    developer_ergonomics: 37.0
    discoverability: 55.6
    governance: 0.0
    operational_transparency: 52.6
  previous_composite: 51.0
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 4
  schema_version: 0.9.1
  scored_at: '2026-08-10'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/make/refs/heads/main/screenshots/make-2026-06-20T184908.png
security:
- kind: authentication
  name: Make Authentication
  slug: make-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Make Domain Security
  slug: make-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: make
tags:
- Automation
- Integration
- iPaaS
- No-Code
- Scenarios
- Workflows
website: https://developers.make.com/
---
