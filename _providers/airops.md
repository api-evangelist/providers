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
  band_gated_from: agent-native
  dimensions:
    agent_card: false
    agent_skills: true
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: served
    consent_identity: false
    delegated_identity: served
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: documented
    event_surface_described: true
    idempotency: false
    mcp_server: verified
    openapi_examples: partial
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 51.7
  scored_at: '2026-09-05'
agentic_access:
- acting_count: 29
  human_in_the_loop: 1
  name: Airops Agentic Access
  operation_count: 42
  slug: airops-agentic-access
  summary_line: 42 operations · 29 acting · 1 human-in-the-loop
api_count: 2
apis:
- baseURL: https://api.airops.com
  baseurl_source: declared
  description: An endpoint for interacting with Agent apps using chat messages.
  name: AirOps Agent API
  slug: airops-agent-api
- baseURL: https://api.airops.com
  baseurl_source: declared
  description: The Analytics API from AirOps — 1 operation(s) for analytics.
  name: AirOps Analytics API
  slug: airops-analytics-api
- baseURL: https://api.airops.com
  baseurl_source: declared
  description: The Answers API from AirOps — 2 operation(s) for answers.
  name: AirOps Answers API
  slug: airops-answers-api
- baseURL: https://api.airops.com
  baseurl_source: declared
  description: Endpoints for listing and retrieving app information.
  name: AirOps Apps API
  slug: airops-apps-api
- baseURL: https://api.airops.com
  baseurl_source: declared
  description: Endpoints for managing brand kits and their associated resources.
  name: AirOps Brand Kits API
  slug: airops-brand-kits-api
- baseURL: https://api.airops.com
  baseurl_source: declared
  description: The Citations API from AirOps — 2 operation(s) for citations.
  name: AirOps Citations API
  slug: airops-citations-api
- baseURL: https://api.airops.com
  baseurl_source: declared
  description: The Competitors API from AirOps — 2 operation(s) for competitors.
  name: AirOps Competitors API
  slug: airops-competitors-api
- baseURL: https://api.airops.com
  baseurl_source: declared
  description: The Content Updates API from AirOps — 3 operation(s) for content updates.
  name: AirOps Content Updates API
  slug: airops-content-updates-api
- baseURL: https://api.airops.com
  baseurl_source: declared
  description: An execution is a single run of an app, it contains the inputs, outputs, and status of the run, and can be used to check the status of the run.
  name: AirOps Executions API
  slug: airops-executions-api
- baseURL: https://api.airops.com
  baseurl_source: declared
  description: Endpoints for managing workspace files.
  name: AirOps Files API
  slug: airops-files-api
- baseURL: https://api.airops.com
  baseurl_source: declared
  description: Endpoints for working with grid data and CSV exports.
  name: AirOps Grids API
  slug: airops-grids-api
- baseURL: https://api.airops.com
  baseurl_source: declared
  description: Endpoints for managing memory stores (vector stores) and document search.
  name: AirOps Memory Stores API
  slug: airops-memory-stores-api
- baseURL: https://api.airops.com
  baseurl_source: declared
  description: The Personas API from AirOps — 2 operation(s) for personas.
  name: AirOps Personas API
  slug: airops-personas-api
- baseURL: https://api.airops.com
  baseurl_source: declared
  description: The Prompts API from AirOps — 2 operation(s) for prompts.
  name: AirOps Prompts API
  slug: airops-prompts-api
- baseURL: https://api.airops.com
  baseurl_source: declared
  description: The Sentiment Theme Answers API from AirOps — 1 operation(s) for sentiment theme answers.
  name: AirOps Sentiment Theme Answers API
  slug: airops-sentiment-theme-answers-api
- baseURL: https://api.airops.com
  baseurl_source: declared
  description: The Tags API from AirOps — 2 operation(s) for tags.
  name: AirOps Tags API
  slug: airops-tags-api
- baseURL: https://api.airops.com
  baseurl_source: declared
  description: The Topics API from AirOps — 2 operation(s) for topics.
  name: AirOps Topics API
  slug: airops-topics-api
- baseURL: https://api.airops.com
  baseurl_source: declared
  description: The Web Pages API from AirOps — 1 operation(s) for web pages.
  name: AirOps Web Pages API
  slug: airops-web-pages-api
artifact_total: 28
asyncapis:
- description: ''
  name: Airops Webhooks
  slug: airops-webhooks
collections:
- collection_type: open
  name: API V1
  slug: open-airops-api
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/airops-agentic-access.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/airops-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/airops-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.airops.com/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://docs.airops.com/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.airops.com/
- group: docs
  title: ''
  type: APIReference
  url: https://docs.airops.com/api-reference/api-reference/executions
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.airops.com/getting-started/readme
- group: auth
  title: ''
  type: Authentication
  url: authentication/airops-authentication.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/airops-mcp.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/airops-llms.txt
- group: agent
  title: ''
  type: WellKnown
  url: well-known/airops-well-known.yml
- group: auth
  title: ''
  type: SecurityTxt
  url: well-known/airops-security.txt
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/airops-scopes.yml
- group: build
  title: ''
  type: SDKs
  url: packages/airops-packages.yml
- group: build
  title: ''
  type: Packages
  url: packages/airops-packages.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/airops-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/airops-error-codes.yml
- group: design
  title: ''
  type: Webhooks
  url: asyncapi/airops-webhooks.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/airops-lifecycle.yml
- group: operate
  title: ''
  type: StatusPage
  url: https://status.airops.com/
- group: design
  title: ''
  type: Conformance
  url: conformance/airops-conformance.yml
- group: docs
  title: ''
  type: OpenAPI
  url: openapi/airops-api-openapi.yml
- group: other
  title: ''
  type: Overlay
  url: overlays/airops-api-overlay.yaml
- group: design
  title: ''
  type: DataModel
  url: data-model/airops-data-model.yml
- group: build
  title: ''
  type: ToolCrosswalk
  url: mcp/airops-tool-crosswalk.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/airops-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/airops-rate-limits.yml
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/airops-changelog.yml
- group: start
  title: ''
  type: Sandbox
  url: sandbox/airops-sandbox.yml
- group: auth
  title: ''
  type: Security
  url: https://app.airops.com/.well-known/security.txt
- group: company
  title: ''
  type: Blog
  url: https://www.airops.com/blog
- group: commercial
  title: ''
  type: Pricing
  url: https://www.airops.com/pricing
- group: start
  title: ''
  type: SignUp
  url: https://app.airops.com/users/sign_up
- group: start
  title: ''
  type: Login
  url: https://app.airops.com/users/sign_in
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.airops.com/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.airops.com/privacy-policy
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/airopshq
- group: operate
  title: ''
  type: Support
  url: https://university.airops.com/
created: '2026-07-17'
description: AirOps is a growth platform for AI search and answer engine optimization (AEO) that helps brands measure and improve their visibility across AI assistants and search engines including ChatGPT, Perplexity, Gemini, Claude, and Google. The platform pairs Insights (citation tracking, share-of-voice, sentiment, and competitor intelligence) with Action (Playbooks, Workflows, Grids, and Campaigns that draft and ship content at scale) and Context (Brand Kits and Knowledge Bases). AirOps exposes a public REST API at api.airops.com for executing Workflows/Apps, managing Knowledge Bases, and pulling AEO analytics, a hosted Model Context Protocol (MCP) server at app.airops.com/mcp with roughly ninety tools, incoming webhook triggers, and first-party JavaScript and Python SDKs. It was surfaced as a portfolio company of Greylock and enriched into the API Evangelist network.
image: https://cdn.prod.website-files.com/61fae48cb5979577435753f6/69fe76ac41d8f24a95a59e72_1200x630-Homepage.jpg
layout: provider
mcp_servers:
- description: ''
  name: AirOps MCP Server
  slug: airops-mcp-server
modified: '2026-08-13'
name: AirOps
nav: Providers
network: true
overview: 'AirOps publishes 18 APIs on the [APIs.io](https://apis.io/) network, including Agent API, Analytics API, Answers API, and 15 more. Tagged areas include Company, Application, Artificial Intelligence, Content, and SEO.


  The AirOps catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  AirOps'' developer surface includes documentation, API reference, getting-started guide, authentication, changelog, sandbox, engineering blog, and 33 more developer resources.'
plans:
- name: Airops Plans Pricing
  plan_count: 3
  slug: airops-plans-pricing
random_paper: 3
rate_limits:
- limit_count: 0
  name: Airops Rate Limits
  slug: airops-rate-limits
scopes:
- name: Airops Scopes
  scope_count: 4
  slug: airops-scopes
  summary_line: 4 scopes · authorizationCode
score:
  band: strong
  composite: 61.0
  coverage:
    artifact_dirs: 24
    catalog_earned: 49.0
    catalog_earned_first_party: 12.0
    catalog_gap: 66.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 1.0
  facets:
    access_clarity: 76.3
    commercial_clarity: 76.3
    contract_governance: 18.2
    contract_quality: 60.5
    developer_ergonomics: 78.6
    discoverability: 75.9
    governance: 18.2
    operational_transparency: 39.5
  previous_composite: 60.0
  provenance:
    agentic_access: derived
    conformance: first-party
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 18
    mcp: first-party
    skills: first-party
  schema_version: 0.18.3
  scored_at: '2026-09-05'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/airops/refs/heads/main/screenshots/airops-2026-07-25T195431.png
security:
- kind: authentication
  name: Airops Authentication
  slug: airops-authentication
  summary_line: http/oauth2 · 2 schemes
- kind: domain-security
  name: Airops Domain Security
  slug: airops-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Airops Vulnerability Disclosure
  slug: airops-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: airops
tags:
- Company
- Application
- Artificial Intelligence
- Content
- SEO
- AEO
- Answer Engine Optimization
- Generative Engine Optimization
- Workflows
- MCP
- Analytics
- Agent Skills
- OpenAPI
- Knowledge Base
- Content Marketing
- Citations
website: https://www.airops.com/
---
