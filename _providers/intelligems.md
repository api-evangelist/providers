---
access_model:
  confidence: high
  label: Paid plans with a 14-day free trial; API included with the subscription
  onboarding: self-serve
  pricing: paid
  public: false
  source:
  - https://www.intelligems.io/pricing
  - plans/intelligems-plans-pricing.yml
  - authentication
  trial: true
  try_now: false
agent_readiness:
  band: agent-ready
  band_gated_from: agent-native
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: served
    consent_identity: false
    delegated_identity: served
    dry_run_mode: false
    dynamic_client_registration: true
    error_semantics: documented
    event_surface_described: true
    idempotency: false
    mcp_server: verified
    openapi_examples: partial
    protected_resource_metadata: verified
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 55.2
  scored_at: '2026-09-16'
agentic_access:
- acting_count: 13
  human_in_the_loop: 0
  name: Intelligems Agentic Access
  operation_count: 16
  slug: intelligems-agentic-access
  summary_line: 16 operations · 13 acting
api_count: 1
apis:
- description: Official hosted Model Context Protocol server exposing 46 tools over HTTP and SSE — experiment discovery and lifecycle, price-test prepare/commit, experiment and sitewide analytics, seasonal benchmark
  name: Intelligems MCP Server
  slug: intelligems-mcp-server
- baseURL: https://api.intelligems.io
  baseurl_source: declared
  description: 'The following custom event types are supported by the Intelligems Custom Events API: - `clickEvent` — Fires when a visitor clicks an element matching one or more CSS selectors - `scrollDepth` — Fires '
  name: Intelligems Create Custom Event API
  slug: intelligems-create-custom-event-api
- baseURL: https://api.intelligems.io
  baseurl_source: declared
  description: 'The following experience types are supported by the Intelligems Experiments API: - `content/advanced` — Advanced content test (custom CSS/JS injection) - `content/onsiteEdits` — Onsite edits (visual e'
  name: Intelligems Create Experience API
  slug: intelligems-create-experience-api
- baseURL: https://api.intelligems.io
  baseurl_source: declared
  description: The Fetch Experience Data API from Intelligems — 3 operation(s) for fetch experience data.
  name: Intelligems Fetch Experience Data API
  slug: intelligems-fetch-experience-data-api
- baseURL: https://api.intelligems.io
  baseurl_source: declared
  description: The Fetch Experience List API from Intelligems — 1 operation(s) for fetch experience list.
  name: Intelligems Fetch Experience List API
  slug: intelligems-fetch-experience-list-api
- baseURL: https://api.intelligems.io
  baseurl_source: declared
  description: The Fetch Sitewide Analytics API from Intelligems — 4 operation(s) for fetch sitewide analytics.
  name: Intelligems Fetch Sitewide Analytics API
  slug: intelligems-fetch-sitewide-analytics-api
- baseURL: https://api.intelligems.io
  baseurl_source: declared
  description: The Get Experience Export API from Intelligems — 1 operation(s) for get experience export.
  name: Intelligems Get Experience Export API
  slug: intelligems-get-experience-export-api
- baseURL: https://api.intelligems.io
  baseurl_source: declared
  description: The Get Holiday Benchmark Data API from Intelligems — 2 operation(s) for get holiday benchmark data.
  name: Intelligems Get Holiday Benchmark Data API
  slug: intelligems-get-holiday-benchmark-data-api
- baseURL: https://api.intelligems.io
  baseurl_source: declared
  description: Lifecycle actions for managing experience state transitions (start, pause, end).
  name: Intelligems Perform Experience Action API
  slug: intelligems-perform-experience-action-api
- baseURL: https://api.intelligems.io
  baseurl_source: declared
  description: Updates an existing experience. This is a full PUT replacement — the entire experience configuration is replaced with the provided data. All required fields must be included in every request. Any opti
  name: Intelligems Update Experience API
  slug: intelligems-update-experience-api
artifact_total: 23
asyncapis:
- description: ''
  name: Intelligems Webhooks
  slug: intelligems-webhooks
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Intelligems External Analytics API
  slug: open-intelligems-analytics-api
- collection_type: open
  name: Intelligems External Custom Events API
  slug: open-intelligems-custom-events-api
- collection_type: open
  name: Intelligems External Experiences API
  slug: open-intelligems-experiences-api
- collection_type: open
  name: Intelligems External Holiday Benchmark API
  slug: open-intelligems-holiday-benchmark-api
common:
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/intelligems/refs/heads/main/overlays/intelligems-external-api-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/intelligems-external-api-overlay.yaml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/intelligems/refs/heads/main/agentic-access/intelligems-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/intelligems-agentic-access.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/intelligems/refs/heads/main/security/intelligems-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/intelligems-domain-security.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/intelligems/refs/heads/main/mcp/intelligems-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/intelligems-mcp.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/intelligems/refs/heads/main/packages/intelligems-packages.yml
  title: ''
  type: Packages
  url: packages/intelligems-packages.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/intelligems/refs/heads/main/packages/intelligems-packages.yml
  title: ''
  type: SDKs
  url: packages/intelligems-packages.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/intelligems/refs/heads/main/components/intelligems-components.yml
  title: ''
  type: Components
  url: components/intelligems-components.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/intelligems/refs/heads/main/llms/intelligems-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/intelligems-llms.txt
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/intelligems/refs/heads/main/llms/intelligems-docs-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/intelligems-docs-llms.txt
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/intelligems/refs/heads/main/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/intelligems/refs/heads/main/mcp/intelligems-tool-crosswalk.yml
  title: ''
  type: ToolCrosswalk
  url: mcp/intelligems-tool-crosswalk.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/intelligems/refs/heads/main/well-known/intelligems-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/intelligems-well-known.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/intelligems/refs/heads/main/scopes/intelligems-scopes.yml
  title: ''
  type: OAuthScopes
  url: scopes/intelligems-scopes.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/intelligems/refs/heads/main/asyncapi/intelligems-webhooks.yml
  title: ''
  type: Webhooks
  url: asyncapi/intelligems-webhooks.yml
- group: operate
  href: https://raw.githubusercontent.com/api-evangelist/intelligems/refs/heads/main/changelog/intelligems-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/intelligems-changelog.yml
- group: operate
  title: ''
  type: ChangeLog
  url: https://www.intelligems.io/resources/product-updates
- group: commercial
  href: https://raw.githubusercontent.com/api-evangelist/intelligems/refs/heads/main/plans/intelligems-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/intelligems-plans-pricing.yml
- group: start
  href: https://raw.githubusercontent.com/api-evangelist/intelligems/refs/heads/main/sandbox/intelligems-sandbox.yml
  title: ''
  type: Sandbox
  url: sandbox/intelligems-sandbox.yml
- group: operate
  href: https://raw.githubusercontent.com/api-evangelist/intelligems/refs/heads/main/rate-limits/intelligems-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/intelligems-rate-limits.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/intelligems/refs/heads/main/authentication/intelligems-authentication.yml
  title: ''
  type: Authentication
  url: authentication/intelligems-authentication.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/intelligems/refs/heads/main/conventions/intelligems-conventions.yml
  title: ''
  type: Conventions
  url: conventions/intelligems-conventions.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/intelligems/refs/heads/main/errors/intelligems-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/intelligems-problem-types.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/intelligems/refs/heads/main/lifecycle/intelligems-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/intelligems-lifecycle.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/intelligems/refs/heads/main/conformance/intelligems-conformance.yml
  title: ''
  type: Conformance
  url: conformance/intelligems-conformance.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/intelligems/refs/heads/main/data-model/intelligems-data-model.yml
  title: ''
  type: DataModel
  url: data-model/intelligems-data-model.yml
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
description: Intelligems is an AI-powered A/B testing, pricing optimization, and personalization platform for ecommerce stores, built primarily as a Shopify app. Merchants use it to test and personalize product and subscription pricing, discounts and offers, shipping strategies, content and landing pages, the checkout experience, and post-purchase offers, then measure the profit impact with built-in analytics. For developers, Intelligems publishes a REST External API (v25-10-beta) that manages experiences, defines custom events, and pulls experiment, sitewide and seasonal-benchmark analytics — with its own OpenAPI 3.1 published inside the reference — plus signed webhooks for the experience lifecycle, a client-side JavaScript API (window.igData), a headless React SDK (@intelligems/headless), and an official hosted MCP server with 46 OAuth-authenticated tools that connects experiments, Shopify store data, and analytics to Claude, ChatGPT, and Gemini.
image: https://intelligems.io/favicon.ico
layout: provider
mcp_servers:
- description: ''
  name: Intelligems MCP Server
  slug: intelligems-mcp-server
modified: '2026-08-13'
name: Intelligems
nav: Providers
network: true
overview: 'Intelligems publishes 9 APIs on the [APIs.io](https://apis.io/) network, including Create Custom Event API, Create Experience API, Fetch Experience Data API, and 6 more. Tagged areas include Company, A/B Testing, E-Commerce, Pricing, and Personalization.


  The Intelligems catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  Intelligems'' developer surface includes changelog, sandbox, authentication, documentation, API reference, getting-started guide, engineering blog, and 29 more developer resources.'
plans:
- name: Intelligems Plans Pricing
  plan_count: 2
  slug: intelligems-plans-pricing
random_paper: 15
rate_limits:
- limit_count: 3
  name: Intelligems Rate Limits
  slug: intelligems-rate-limits
scopes:
- name: Intelligems Scopes
  scope_count: 1
  slug: intelligems-scopes
  summary_line: 1 scope · authorizationCode
score:
  band: strong
  composite: 59.3
  coverage:
    artifact_dirs: 25
    catalog_earned: 57.0
    catalog_earned_first_party: 20.0
    catalog_gap: 58.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -2.7
  facets:
    access_clarity: 65.8
    contract_governance: 4.5
    contract_quality: 63.0
    developer_ergonomics: 73.2
    discoverability: 75.9
    operational_transparency: 55.3
  previous_composite: 62.0
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 9
    mcp: first-party
    skills: derived
  schema_version: 0.22.0
  scored_at: '2026-09-16'
  trend: flat
  upsert:
    applies: true
    score: 11.1
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
- E-Commerce
- Pricing
- Personalization
- Conversion Rate Optimization
- Shopify
- Analytics
- Experimentation
- MCP
- Webhook
- Profit Optimization
website: https://intelligems.io/
---
