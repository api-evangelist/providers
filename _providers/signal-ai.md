---
access_model:
  confidence: high
  label: Contact sales
  onboarding: unknown
  pricing: unknown
  public: false
  source:
  - plans/signal-ai-plans-pricing.yml
  - https://signal-ai.com/solutions/api
  trial: false
  try_now: false
agent_readiness:
  band: agent-ready
  band_gated_from: agent-native
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: false
    agentic_commerce: false
    auth_clarity: served
    consent_identity: false
    delegated_identity: served
    dry_run_mode: false
    dynamic_client_registration: true
    error_semantics: documented
    event_surface_described: false
    idempotency: false
    mcp_server: documented
    openapi_examples: partial
    protected_resource_metadata: verified
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 43.9
  scored_at: '2026-09-05'
api_count: 1
apis:
- baseURL: https://api.signal-ai.com
  baseurl_source: declared
  description: 'The Affinity API endpoints allow API users to leverage the power of the Signal AI Knowledge Graph, derived from billions of documents and updated regularly. The Signal AI Knowledge Graph consists of: '
  name: Signal AI Affinity API
  slug: signal-ai-affinity-api
- baseURL: https://api.signal-ai.com
  baseurl_source: declared
  description: The Categories API from Signal AI — 2 operation(s) for categories.
  name: Signal AI Categories API
  slug: signal-ai-categories-api
- baseURL: https://api.signal-ai.com
  baseurl_source: declared
  description: The Content Metrics API from Signal AI — 1 operation(s) for content metrics.
  name: Signal AI Content Metrics API
  slug: signal-ai-content-metrics-api
- baseURL: https://api.signal-ai.com
  baseurl_source: declared
  description: The Content Search API from Signal AI — 2 operation(s) for content search.
  name: Signal AI Content Search API
  slug: signal-ai-content-search-api
- baseURL: https://api.signal-ai.com
  baseurl_source: declared
  description: The Entities API from Signal AI — 2 operation(s) for entities.
  name: Signal AI Entities API
  slug: signal-ai-entities-api
- baseURL: https://api.signal-ai.com
  baseurl_source: declared
  description: 'The Events API endpoint identifies significant clusters of news coverage about entities and topics of interest, allowing users to easily identify news events that could impact them or their business, '
  name: Signal AI Events API
  slug: signal-ai-events-api
- baseURL: https://api.signal-ai.com
  baseurl_source: declared
  description: The Openapi.json API from Signal AI — 1 operation(s) for openapi.json.
  name: Signal AI Openapi.json API
  slug: signal-ai-openapi-json-api
- baseURL: https://api.signal-ai.com
  baseurl_source: declared
  description: The Publication sources API from Signal AI — 3 operation(s) for publication sources.
  name: Signal AI Publication sources API
  slug: signal-ai-publication-sources-api
- baseURL: https://api.signal-ai.com
  baseurl_source: declared
  description: The Risk Events API from Signal AI — 3 operation(s) for risk events.
  name: Signal AI Risk Events API
  slug: signal-ai-risk-events-api
- baseURL: https://api.signal-ai.com
  baseurl_source: declared
  description: The Topics API from Signal AI — 2 operation(s) for topics.
  name: Signal AI Topics API
  slug: signal-ai-topics-api
- baseURL: https://api.signal-ai.com
  baseurl_source: declared
  description: 'Organisation administration for the Signal AI API. `GET /users` returns all users in the organisation of the authenticated API credential, and requires a credential carrying the `manage-organisation` '
  name: Signal AI Organisation API
  slug: signal-ai-organisation-api
artifact_total: 29
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Signal AI Affinity API
  slug: open-signal-ai-affinity-api
- collection_type: open
  name: Signal AI Affinity Categories API
  slug: open-signal-ai-categories-api
- collection_type: open
  name: Signal AI Affinity Content Metrics API
  slug: open-signal-ai-content-metrics-api
- collection_type: open
  name: Signal AI Affinity Content Search API
  slug: open-signal-ai-content-search-api
- collection_type: open
  name: Signal AI Affinity Entities API
  slug: open-signal-ai-entities-api
- collection_type: open
  name: Signal AI Affinity Events API
  slug: open-signal-ai-events-api
- collection_type: open
  name: Signal AI Affinity Openapi.json API
  slug: open-signal-ai-openapi-json-api
- collection_type: open
  name: Signal AI Organisation API
  slug: open-signal-ai-organisation-api
- collection_type: open
  name: Signal AI Affinity Publication sources API
  slug: open-signal-ai-publication-sources-api
- collection_type: open
  name: Signal AI Affinity Risk Events API
  slug: open-signal-ai-risk-events-api
- collection_type: open
  name: Signal AI Affinity Topics API
  slug: open-signal-ai-topics-api
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
- group: build
  title: ''
  type: Packages
  url: packages/signal-ai-packages.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/signal-ai-problem-types.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/signal-ai-rate-limits.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/signal-ai-plans-pricing.yml
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/signal-ai-changelog.yml
- group: build
  title: ''
  type: ToolCrosswalk
  url: mcp/signal-ai-tool-crosswalk.yml
- group: docs
  title: ''
  type: APIReference
  url: https://api.signal-ai.com/docs
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/signal-ai
- group: build
  title: ''
  type: SourceCode
  url: https://github.com/signal-ai/signal-api-tools
- group: start
  title: ''
  type: GettingStarted
  url: https://github.com/signal-ai/signal-api-tools#getting-started-with-the-signal-ai-api
created: '2026-07-17'
description: Signal AI (Signal Media Ltd) is an AI-powered reputation and risk intelligence platform that turns the world's largest real-time dataset of global news, social, broadcast and regulatory content into actionable insight. Its proprietary AIQ framework understands, enriches and surfaces relevant coverage across 226 markets and 120+ languages, ingesting 5.5M+ articles and labelling 100M+ entities and topics daily. The Signal AI API is an HTTP+JSON API offering programmatic access to the platform via Content Search, Content Metrics, Affinity (the Signal AI Knowledge Graph), Events, and Risk Events endpoints, secured with OAuth2 client-credentials.
image: https://login.signal-ai.com/auth/resources/hlcwe/login/signal/img/apple-touch-icon.png
layout: provider
mcp_servers:
- description: ''
  name: Signal AI MCP Server
  slug: signal-ai-mcp-server
modified: '2026-08-13'
name: Signal AI
nav: Providers
network: true
overview: 'Signal AI publishes 11 APIs on the [APIs.io](https://apis.io/) network, including Affinity API, Categories API, Content Metrics API, and 8 more. Tagged areas include Company, Media Intelligence, Reputation Management, Risk Intelligence, and News.


  Signal AI''s developer surface includes authentication, documentation, engineering blog, support, changelog, API reference, getting-started guide, and 24 more developer resources.'
plans:
- name: Signal Ai Plans Pricing
  plan_count: 0
  slug: signal-ai-plans-pricing
random_paper: 3
rate_limits:
- limit_count: 8
  name: Signal Ai Rate Limits
  slug: signal-ai-rate-limits
scopes:
- name: Signal Ai Scopes
  scope_count: 7
  slug: signal-ai-scopes
  summary_line: 7 scopes · clientCredentials
score:
  band: developing
  composite: 42.1
  coverage:
    artifact_dirs: 21
    catalog_earned: 49.0
    catalog_earned_first_party: 12.0
    catalog_gap: 66.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 6.6
    commercial_clarity: 6.6
    contract_governance: 18.2
    contract_quality: 51.7
    developer_ergonomics: 42.3
    discoverability: 75.9
    governance: 18.2
    operational_transparency: 73.7
  previous_composite: 42.1
  provenance:
    conformance: first-party
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 11
    mcp: first-party
    skills: derived
  schema_version: 0.18.3
  scored_at: '2026-09-05'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/signal-ai/refs/heads/main/screenshots/signal-ai-2026-08-17T081853.png
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
