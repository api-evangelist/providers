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
  band: agent-aware
  dimensions:
    agent_skills: true
    agentic_access: false
    asyncapi_events: false
    auth_clarity: true
    consent_identity: false
    error_semantics: false
    idempotency: false
    mcp_server: true
    openapi_examples: false
    rate_limit_signal: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.1
  score: 43.3
  scored_at: '2026-07-27'
api_count: 7
apis:
- description: The core API from Goodays — 22 operation(s) for core.
  name: Goodays core API
  slug: goodays-core-api
- description: The dashboard API from Goodays — 1 operation(s) for dashboard.
  name: Goodays dashboard API
  slug: goodays-dashboard-api
- description: The events API from Goodays — 5 operation(s) for events.
  name: Goodays events API
  slug: goodays-events-api
- description: The response API from Goodays — 9 operation(s) for response.
  name: Goodays response API
  slug: goodays-response-api
- description: The session API from Goodays — 1 operation(s) for session.
  name: Goodays session API
  slug: goodays-session-api
- description: The solicitation API from Goodays — 3 operation(s) for solicitation.
  name: Goodays solicitation API
  slug: goodays-solicitation-api
- description: The stats API from Goodays — 8 operation(s) for stats.
  name: Goodays stats API
  slug: goodays-stats-api
artifact_total: 10
common:
- group: start
  title: ''
  type: DeveloperPortal
  url: https://developers.goodays.co/docs/welcome-to-goodays-developer-platform
- group: docs
  title: ''
  type: Documentation
  url: https://apidocs.goodays.co/docs/welcome-to-goodays-api-platform
- group: docs
  title: ''
  type: APIReference
  url: https://apidocs.goodays.co/reference/places_list
- group: start
  title: ''
  type: GettingStarted
  url: https://apidocs.goodays.co/docs/welcome-to-goodays-api-platform
- group: auth
  title: ''
  type: Authentication
  url: authentication/goodays-authentication.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/goodays-conventions.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/goodays-data-model.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/goodays-lifecycle.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/goodays-mcp.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/goodays-llms.txt
- group: build
  title: ''
  type: Packages
  url: packages/goodays-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/goodays-packages.yml
- group: design
  title: ''
  type: Components
  url: components/goodays-components.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/goodays-conformance.yml
- group: auth
  title: ''
  type: Compliance
  url: https://community.goodays.co/privacy-policy
- group: auth
  title: ''
  type: DomainSecurity
  url: security/goodays-domain-security.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/goodays-collect-feedback.md
- group: agent
  title: ''
  type: AgentSkill
  url: skills/goodays-respond-to-reviews.md
- group: agent
  title: ''
  type: AgentSkill
  url: skills/goodays-track-experience-metrics.md
- group: operate
  title: ''
  type: Support
  url: https://help.goodays.co/en
- group: company
  title: ''
  type: Blog
  url: https://community.goodays.co/en/blog
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/critizr
- group: start
  title: ''
  type: Login
  url: https://app.goodays.co/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://community.goodays.co/privacy-policy
- group: company
  title: ''
  type: Website
  url: https://goodays.co
created: '2026-07-17'
description: Goodays (formerly Critizr) is Europe's leading customer experience management platform, founded in 2012 and headquartered in Lille, France, helping retailers and multi-location brands understand and act on customer feedback across every point of sale. Its REST API v2 (api.goodays.co/v2) exposes a Core API for the place/level/survey/user hierarchy, a Response API to read and reply to customer reviews, a Solicitation API to request feedback by email/SMS, a Collect API for first-party collection sources, and a Metrics API for NPS, satisfaction, relationship, Google-score, dissatisfaction and retained-customer statistics. Goodays also ships Web, iOS and Android SDKs and embeddable feedback widgets. Added to the API Evangelist network as a point-nine portfolio lead and enriched by the pipeline from Goodays' public developer documentation.
image: https://assets.goodays.prod.verveagency.com/assets/illu-social-en.png
layout: provider
mcp_servers:
- description: ''
  name: goodays-mcp.yml
  slug: goodays-mcpyml
modified: '2026-07-19'
name: Goodays
nav: Providers
network: true
overview: 'Goodays publishes 7 APIs on the [APIs.io](https://apis.io/) network, including core API, dashboard API, events API, and 4 more. Tagged areas include Company, Customer Experience, Customer Feedback, Voice of the Customer, and Surveys.


  Goodays'' developer surface includes documentation, API reference, getting-started guide, authentication, support, engineering blog, and 19 more developer resources.'
random_paper: 10
score:
  band: thin
  composite: 41.8
  delta: 0.0
  facets:
    commercial_clarity: 31.6
    contract_quality: 40.2
    developer_ergonomics: 73.9
    discoverability: 100.0
    governance: 0.0
    operational_transparency: 5.3
  previous_composite: 41.8
  schema_version: 0.5
  scored_at: '2026-07-27'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/goodays/refs/heads/main/screenshots/goodays-2026-07-25T220046.png
security:
- kind: authentication
  name: Goodays Authentication
  slug: goodays-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Goodays Domain Security
  slug: goodays-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: goodays
tags:
- Company
- Customer Experience
- Customer Feedback
- Voice of the Customer
- Surveys
- NPS
- Reviews
- Retail
- CRM
- SaaS
website: https://goodays.co
---
