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
    agent_card: false
    agent_skills: derived
    agentic_access: derived
    auth_clarity: false
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: true
    openapi_examples: false
    rate_limit_signal: verified
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 36.7
  scored_at: '2026-08-03'
agentic_access:
- acting_count: 12
  human_in_the_loop: 0
  name: Intelligems Agentic Access
  operation_count: 15
  slug: intelligems-agentic-access
  summary_line: 15 operations · 12 acting
api_count: 3
apis:
- description: Experience-level and sitewide analytics.
  name: Intelligems Analytics API
  slug: intelligems-analytics-api
- description: Create, read, update, and control A/B tests and personalizations.
  name: Intelligems Experiences API
  slug: intelligems-experiences-api
- description: Event/holiday benchmark analytics.
  name: Intelligems Holiday Benchmark API
  slug: intelligems-holiday-benchmark-api
artifact_total: 8
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/intelligems-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/intelligems-domain-security.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/intelligems-mcp.yml
- group: build
  title: ''
  type: Packages
  url: packages/intelligems-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/intelligems-packages.yml
- group: design
  title: ''
  type: Components
  url: components/intelligems-components.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/intelligems-llms.txt
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: start
  title: ''
  type: DeveloperPortal
  url: https://docs.intelligems.io/getting-started/getting-started
- group: docs
  title: ''
  type: Documentation
  url: https://docs.intelligems.io/
- group: docs
  title: ''
  type: APIReference
  url: https://docs.intelligems.io/developer-resources/external-api
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.intelligems.io/getting-started/getting-started
- group: company
  title: ''
  type: Blog
  url: https://www.intelligems.io/resources/blog
- group: operate
  title: ''
  type: Support
  url: https://www.intelligems.io/company/get-in-touch
- group: commercial
  title: ''
  type: Pricing
  url: https://www.intelligems.io/pricing
- group: start
  title: ''
  type: SignUp
  url: https://apps.shopify.com/intelligems
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.intelligems.io/terms-of-service
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.intelligems.io/privacy-policy
- group: company
  title: ''
  type: Website
  url: https://intelligems.io/
created: '2026-07-17'
description: Intelligems is an AI-powered A/B testing, pricing optimization, and personalization platform for ecommerce stores, built primarily as a Shopify app. Merchants use it to test and personalize product and subscription pricing, discounts and offers, shipping strategies, content and landing pages, the checkout experience, and post-purchase offers, then measure the profit impact with built-in analytics. For developers, Intelligems exposes a REST External API (manage experiences and pull experiment and sitewide analytics), a client-side JavaScript API (window.igData), a headless React SDK (@intelligems/headless), and an official hosted MCP server with 30 tools that connects experiments, Shopify store data, and analytics to Claude, ChatGPT, and Gemini.
image: https://intelligems.io/favicon.ico
layout: provider
mcp_servers:
- description: ''
  name: intelligems-mcp.yml
  slug: intelligems-mcpyml
modified: '2026-07-19'
name: Intelligems
nav: Providers
network: true
overview: 'Intelligems publishes 3 APIs on the [APIs.io](https://apis.io/) network: Analytics API, Experiences API, and Holiday Benchmark API. Tagged areas include Company, A/B Testing, Ecommerce, Pricing, and Personalization.


  Intelligems'' developer surface includes documentation, API reference, getting-started guide, engineering blog, support, pricing, signup flow, and 12 more developer resources.'
random_paper: 41
rate_limits:
- limit_count: 3
  name: Intelligems Rate Limits
  slug: intelligems-rate-limits
score:
  band: developing
  composite: 50.5
  delta: 0.0
  facets:
    commercial_clarity: 44.7
    contract_quality: 65.1
    developer_ergonomics: 58.2
    discoverability: 81.5
    governance: 11.5
    operational_transparency: 31.6
  previous_composite: 50.5
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 3
    mcp: first-party
    skills: derived
  schema_version: 0.9
  scored_at: '2026-08-03'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/intelligems/refs/heads/main/screenshots/intelligems-2026-07-25T222646.png
security:
- kind: authentication
  name: Intelligems Authentication
  slug: intelligems-authentication
  summary_line: apiKey/oauth2 · 2 schemes
- kind: domain-security
  name: Intelligems Domain Security
  slug: intelligems-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: intelligems
tags:
- Company
- A/B Testing
- Ecommerce
- Pricing
- Personalization
- Conversion Rate Optimization
- Shopify
- Analytics
- Experimentation
website: https://intelligems.io/
---
