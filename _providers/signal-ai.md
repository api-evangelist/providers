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
    agentic_access: false
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: true
    openapi_examples: partial
    rate_limit_signal: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 40.3
  scored_at: '2026-08-12'
api_count: 10
apis:
- description: 'The Affinity API endpoints allow API users to leverage the power of the Signal AI Knowledge Graph, derived from billions of documents and updated regularly. The Signal AI Knowledge Graph consists of: '
  name: Signal AI Affinity API
  slug: signal-ai-affinity-api
- description: The Categories API from Signal AI — 2 operation(s) for categories.
  name: Signal AI Categories API
  slug: signal-ai-categories-api
- description: The Content Metrics API from Signal AI — 1 operation(s) for content metrics.
  name: Signal AI Content Metrics API
  slug: signal-ai-content-metrics-api
- description: The Content Search API from Signal AI — 2 operation(s) for content search.
  name: Signal AI Content Search API
  slug: signal-ai-content-search-api
- description: The Entities API from Signal AI — 2 operation(s) for entities.
  name: Signal AI Entities API
  slug: signal-ai-entities-api
- description: 'The Events API endpoint identifies significant clusters of news coverage about entities and topics of interest, allowing users to easily identify news events that could impact them or their business, '
  name: Signal AI Events API
  slug: signal-ai-events-api
- description: The Openapi.json API from Signal AI — 1 operation(s) for openapi.json.
  name: Signal AI Openapi.json API
  slug: signal-ai-openapi-json-api
- description: The Publication sources API from Signal AI — 3 operation(s) for publication sources.
  name: Signal AI Publication sources API
  slug: signal-ai-publication-sources-api
- description: The Risk Events API from Signal AI — 3 operation(s) for risk events.
  name: Signal AI Risk Events API
  slug: signal-ai-risk-events-api
- description: The Topics API from Signal AI — 2 operation(s) for topics.
  name: Signal AI Topics API
  slug: signal-ai-topics-api
artifact_total: 14
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/signal-ai-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/signal-ai-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/signal-ai-scopes.yml
- group: start
  title: ''
  type: DeveloperPortal
  url: https://signal-ai.com/solutions/api
- group: docs
  title: ''
  type: Documentation
  url: https://api.signal-ai.com/docs
- group: company
  title: ''
  type: Blog
  url: https://signal-ai.com/insights
- group: operate
  title: ''
  type: Support
  url: https://signal-ai.com/contact-us
- group: start
  title: ''
  type: Login
  url: https://app.signal-ai.com/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://signal-ai.com/legal-policy
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://signal-ai.com/legal-policy
- group: operate
  title: ''
  type: StatusPage
  url: https://signalai.statuspage.io
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/signal-ai-llms.txt
- group: agent
  title: ''
  type: WellKnown
  url: well-known/signal-ai-well-known.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/signal-ai-mcp.yml
- group: other
  title: ''
  type: Overlay
  url: overlays/signal-ai-openapi-overlay.yaml
- group: design
  title: ''
  type: Conformance
  url: conformance/signal-ai-conformance.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/signal-ai-lifecycle.yml
- group: operate
  title: ''
  type: Deprecation
  url: lifecycle/signal-ai-lifecycle.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/signal-ai-conventions.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/signal-ai-data-model.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
created: '2026-07-17'
description: Signal AI (Signal Media Ltd) is an AI-powered reputation and risk intelligence platform that turns the world's largest real-time dataset of global news, social, broadcast and regulatory content into actionable insight. Its proprietary AIQ framework understands, enriches and surfaces relevant coverage across 226 markets and 120+ languages, ingesting 5.5M+ articles and labelling 100M+ entities and topics daily. The Signal AI API is an HTTP+JSON API offering programmatic access to the platform via Content Search, Content Metrics, Affinity (the Signal AI Knowledge Graph), Events, and Risk Events endpoints, secured with OAuth2 client-credentials.
image: https://login.signal-ai.com/auth/resources/hlcwe/login/signal/img/apple-touch-icon.png
layout: provider
mcp_servers:
- description: ''
  name: signal-ai-mcp.yml
  slug: signal-ai-mcpyml
modified: '2026-07-21'
name: Signal AI
nav: Providers
network: true
overview: 'Signal AI publishes 10 APIs on the [APIs.io](https://apis.io/) network, including Affinity API, Categories API, Content Metrics API, and 7 more. Tagged areas include Company, Media Intelligence, Reputation Management, Risk Intelligence, and News.


  Signal AI''s developer surface includes authentication, documentation, engineering blog, support, and 17 more developer resources.'
random_paper: 45
scopes:
- name: Signal Ai Scopes
  scope_count: 6
  slug: signal-ai-scopes
  summary_line: 6 scopes · clientCredentials
score:
  band: developing
  composite: 43.3
  delta: 0.0
  facets:
    commercial_clarity: 34.2
    contract_quality: 54.7
    developer_ergonomics: 45.1
    discoverability: 92.6
    governance: 11.5
    operational_transparency: 23.7
  previous_composite: 43.3
  provenance:
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 10
    mcp: first-party
    skills: derived
  schema_version: 0.11.0
  scored_at: '2026-08-12'
  trend: flat
security:
- kind: authentication
  name: Signal Ai Authentication
  slug: signal-ai-authentication
  summary_line: oauth2 · 1 scheme
- kind: domain-security
  name: Signal Ai Domain Security
  slug: signal-ai-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
slug: signal-ai
tags:
- Company
- Media Intelligence
- Reputation Management
- Risk Intelligence
- News
- Content Search
- Knowledge Graph
- ESG
- Artificial Intelligence
- Analytics
website: https://signal-ai.com/solutions/api
---
