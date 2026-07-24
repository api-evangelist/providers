---
access_model:
  confidence: medium
  label: Self-serve signup
  onboarding: self-serve
  pricing: unknown
  public: false
  source:
  - authentication
  trial: false
  try_now: false
agent_readiness:
  band: agent-ready
  dimensions:
    agent_skills: true
    agentic_access: false
    asyncapi_events: true
    auth_clarity: true
    consent_identity: false
    error_semantics: false
    idempotency: true
    mcp_server: true
    openapi_examples: false
    rate_limit_signal: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.1
  score: 57.7
  scored_at: '2026-07-23'
api_count: 11
apis:
- description: The Auth Tokens API from Tollbit — 3 operation(s) for auth tokens.
  name: Tollbit Auth Tokens API
  slug: tollbit-auth-tokens-api
- description: The Dev API from Tollbit — 1 operation(s) for dev.
  name: Tollbit Dev API
  slug: tollbit-dev-api
- description: The Get Catalog of Pages for Property API from Tollbit — 1 operation(s) for get catalog of pages for property.
  name: Tollbit Get Catalog of Pages for Property API
  slug: tollbit-get-catalog-of-pages-for-property-api
- description: The Get Tollbit Content API from Tollbit — 1 operation(s) for get tollbit content.
  name: Tollbit Get Tollbit Content API
  slug: tollbit-get-tollbit-content-api
- description: The Get Tollbit Rates API from Tollbit — 2 operation(s) for get tollbit rates.
  name: Tollbit Get Tollbit Rates API
  slug: tollbit-get-tollbit-rates-api
- description: The Report Content Usage API from Tollbit — 1 operation(s) for report content usage.
  name: Tollbit Report Content Usage API
  slug: tollbit-report-content-usage-api
- description: The Reporting API from Tollbit — 1 operation(s) for reporting.
  name: Tollbit Reporting API
  slug: tollbit-reporting-api
- description: The Search API from Tollbit — 1 operation(s) for search.
  name: Tollbit Search API
  slug: tollbit-search-api
- description: The Search Content API from Tollbit — 1 operation(s) for search content.
  name: Tollbit Search Content API
  slug: tollbit-search-content-api
- description: The Tollbit Content API from Tollbit — 4 operation(s) for tollbit content.
  name: Tollbit Tollbit Content API
  slug: tollbit-tollbit-content-api
- description: The Tollbit Subdomain API from Tollbit — 1 operation(s) for tollbit subdomain.
  name: Tollbit Tollbit Subdomain API
  slug: tollbit-tollbit-subdomain-api
artifact_total: 15
asyncapis:
- description: TollBit pushes real-time webhook notifications to subscriber applications when content becomes available (created or updated) from TollBit publisher properties, so consumers do not have to poll. Deliv
  name: TollBit Content Events (Webhooks)
  slug: tollbit-content-events-webhooks
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/tollbit-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/tollbit-authentication.yml
- group: build
  title: ''
  type: Packages
  url: packages/tollbit-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/tollbit-packages.yml
- group: build
  title: ''
  type: CLI
  url: cli/tollbit-cli.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/tollbit-mcp.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/tollbit-llms.txt
- group: design
  title: ''
  type: Components
  url: components/tollbit-components.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/tollbit-conformance.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/tollbit-lifecycle.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/tollbit-conventions.yml
- group: design
  title: ''
  type: Idempotency
  url: conventions/tollbit-conventions.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: start
  title: ''
  type: DeveloperPortal
  url: https://hack.tollbit.com
- group: docs
  title: ''
  type: Documentation
  url: https://docs.tollbit.com
- group: docs
  title: ''
  type: APIReference
  url: https://docs.tollbit.com/reference
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.tollbit.com/docs/quickstart
- group: operate
  title: ''
  type: Support
  url: https://docs.tollbit.com/docs/feedback-support
- group: company
  title: ''
  type: Blog
  url: https://tollbit.com/blog/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/tollbit
- group: start
  title: ''
  type: SignUp
  url: https://app.tollbit.com/sign-up
- group: start
  title: ''
  type: Login
  url: https://app.tollbit.com/sign-in
- group: commercial
  title: ''
  type: TermsOfService
  url: https://tollbit.com/legal/developer-platform-agreement/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://tollbit.com/privacy-policy/
- group: company
  title: ''
  type: Website
  url: https://tollbit.com
created: '2026-07-17'
description: TollBit is the web stack for the agentic internet, giving publishers and commerce sites the infrastructure to analyze, control, and monetize AI agent access to their content. Publishers verify a property, stream logs for AI-bot analytics, and stand up an "Agent Site" front door (the tollbit.<domain> subdomain) that separates bot traffic from humans and applies content controls, licensing, and usage-based paywalls. Its developer API lets AI agents and builders discover licensable content through Licensed Search, fetch rates and license options, mint cryptographically signed one-time access tokens, retrieve licensed or indexed content as markdown or HTML, self-report usage, and receive webhook notifications when content changes. TollBit ships official Python and Node SDKs, a native CLI with a bundled Agent Skill, an MCP toolbox server, and additional agent access methods (NLWeb, Agent2Agent). Added to the API Evangelist network as a portfolio company of Lightspeed Venture Partners
  and enriched from its public developer surface.
image: https://avatars.githubusercontent.com/u/159727288?v=4
layout: provider
mcp_servers:
- description: ''
  name: tollbit-mcp.yml
  slug: tollbit-mcpyml
modified: '2026-07-21'
name: Tollbit
nav: Providers
network: true
overview: 'Tollbit publishes 11 APIs on the [APIs.io](https://apis.io/) network, including Auth Tokens API, Dev API, Get Catalog of Pages for Property API, and 8 more. Tagged areas include Company, Content Licensing, Content Monetization, AI Agents, and Agentic Web.


  The Tollbit catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  Tollbit''s developer surface includes authentication, CLI, documentation, API reference, getting-started guide, support, engineering blog, and 18 more developer resources.'
random_paper: 48
score:
  band: developing
  composite: 48.4
  delta: 0.0
  facets:
    commercial_clarity: 34.2
    contract_quality: 59.1
    developer_ergonomics: 80.4
    discoverability: 100.0
    governance: 0.0
    operational_transparency: 5.3
  previous_composite: 48.4
  schema_version: 0.5
  scored_at: '2026-07-23'
  trend: flat
security:
- kind: authentication
  name: Tollbit Authentication
  slug: tollbit-authentication
  summary_line: apiKey/http · 3 schemes
- kind: domain-security
  name: Tollbit Domain Security
  slug: tollbit-domain-security
  summary_line: TLSv1.3 · DMARC
slug: tollbit
tags:
- Company
- Content Licensing
- Content Monetization
- AI Agents
- Agentic Web
- Search
- Bot Management
- Web Infrastructure
- Developer API
website: https://tollbit.com
---
