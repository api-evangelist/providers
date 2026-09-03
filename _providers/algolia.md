---
access_model:
  confidence: medium
  label: Paid
  onboarding: unknown
  pricing: paid
  public: false
  source:
  - plans
  trial: false
  try_now: false
agent_readiness:
  band: agent-ready
  band_gated_from: agent-native
  dimensions:
    agent_card: false
    agent_skills: true
    agentic_access: false
    agentic_commerce: false
    auth_clarity: served
    consent_identity: false
    delegated_identity: served
    dry_run_mode: false
    dynamic_client_registration: true
    error_semantics: verified
    event_surface_described: false
    idempotency: false
    mcp_server: documented
    openapi_examples: partial
    protected_resource_metadata: verified
    rate_limit_signal: verified
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 52.0
  scored_at: '2026-09-03'
api_count: 15
apis:
- baseURL: https://{appid}-dsn.algolia.net
  baseurl_source: declared
  description: Core indexing and search API for adding, updating and deleting records and querying them with typo-tolerant, faceted, geo-aware and rule-driven search served from globally distributed search nodes. Th
  name: Algolia Search API
  slug: algolia-search-api
- baseURL: https://insights.algolia.io
  baseurl_source: declared
  description: Inbound event-ingestion API for click, conversion, view and purchase signals that feed Personalization, Recommend, A/B Testing and Analytics. Accepts events; does not emit them, which is why Algolia p
  name: Algolia Insights API
  slug: algolia-insights-api
- baseURL: https://{appid}-dsn.algolia.net
  baseurl_source: declared
  description: Returns related-products, frequently-bought-together, trending and look-alike recommendations trained from Insights events and catalog data, plus the Recommend rules that override them.
  name: Algolia Recommend API
  slug: algolia-recommend-api
- baseURL: https://analytics.algolia.com
  baseurl_source: declared
  description: Reports top searches, no-result searches, click and conversion rates, revenue and other search analytics aggregated from query and Insights data. One of only six Algolia APIs that returns machine-read
  name: Algolia Analytics API
  slug: algolia-analytics-api
- baseURL: https://analytics.algolia.com
  baseurl_source: declared
  description: 'Creates and manages A/B tests across index configurations and relevance settings, scoring variants on click-through and conversion. Two live versions: v3 is current, and the entire v2 surface is marke'
  name: Algolia A/B Testing API
  slug: algolia-ab-testing-api
- baseURL: https://personalization.{region}.algolia.com
  baseurl_source: declared
  description: Configures and applies user-affinity profiles built from Insights events to re-rank search and browse results per user.
  name: Algolia Personalization API
  slug: algolia-personalization-api
- baseURL: https://ai-personalization.{region}.algolia.com
  baseurl_source: declared
  description: 'The successor to classic Personalization: real-time user profiles, personalization strategies and a dedicated error-code reference. Runs on its own AI personalization host and publishes the only per-p'
  name: Algolia Advanced Personalization API
  slug: algolia-advanced-personalization-api
- baseURL: https://crawler.algolia.com/api
  baseurl_source: declared
  description: Manages Algolia's hosted web crawler that extracts content from websites and pushes it into indices on a schedule. The only Algolia API that authenticates with HTTP Basic rather than the x-algolia-* h
  name: Algolia Crawler API
  slug: algolia-crawler-api
- baseURL: https://data.{region}.algolia.com
  baseurl_source: declared
  description: Connector-based data ingestion that pulls records from databases, storage and ecommerce platforms into Algolia indices via managed sources, destinations, transformations and tasks. The largest connect
  name: Algolia Ingestion API
  slug: algolia-ingestion-api
- baseURL: https://query-suggestions.{region}.algolia.com
  baseurl_source: declared
  description: Generates and maintains query-suggestion indices from popular searches to power as-you-type autocomplete.
  name: Algolia Query Suggestions API
  slug: algolia-query-suggestions-api
- baseURL: https://{appId}.algolia.net
  baseurl_source: declared
  description: Composes multiple search sources into one curated result set - smart groups, curated queries and composition rules - so a single request returns a merchandised, multi-source response.
  name: Algolia Composition API
  slug: algolia-composition-api
- baseURL: https://{APPLICATION_ID}.algolia.net/agent-studio
  baseurl_source: declared
  description: 'Algolia''s agent-building runtime: agents, conversations, tools, memory, guardrails and per-turn context, exposed as 42 REST operations. Notably, Agent Studio can itself consume third-party MCP tools, '
  name: Algolia Agent Studio API
  slug: algolia-agent-studio-api
- baseURL: https://status.algolia.com
  baseurl_source: declared
  description: 'Exposes server status, latency, indexing and reachability metrics for a specific application''s Algolia infrastructure. More than a status page: an agent can query the health of its own cluster rather '
  name: Algolia Monitoring API
  slug: algolia-monitoring-api
- description: Returns per-application usage metrics (operations, records, search volume) for cost and quota tracking. The one documented Algolia REST API for which no OpenAPI document is published in the api-client
  name: Algolia Usage API
  slug: algolia-usage-api
- description: Algolia-managed remote MCP server giving an agent user-scoped, read-only access to search, index listing and the full analytics surface, authorized by the signed-in user's own Algolia permissions. OAu
  name: Algolia Productivity MCP Server
  slug: algolia-productivity-mcp-server
artifact_total: 24
common:
- group: company
  title: ''
  type: Website
  url: https://www.algolia.com
- group: start
  title: ''
  type: DeveloperPortal
  url: https://www.algolia.com/developers/
- group: docs
  title: ''
  type: Documentation
  url: https://www.algolia.com/doc/
- group: docs
  title: ''
  type: APIReference
  url: https://www.algolia.com/doc/api-reference/
- group: start
  title: ''
  type: GettingStarted
  url: https://www.algolia.com/doc/guides/getting-started/quick-start/
- group: operate
  title: ''
  type: Support
  url: https://support.algolia.com/hc/en-us
- group: company
  title: ''
  type: Blog
  url: https://www.algolia.com/blog/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/algolia
- group: start
  title: ''
  type: Signup
  url: https://dashboard.algolia.com/users/sign_up
- group: commercial
  title: ''
  type: Pricing
  url: https://www.algolia.com/pricing/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.algolia.com/policies/terms/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.algolia.com/policies/privacy/
- group: operate
  title: ''
  type: Status
  url: https://status.algolia.com
- group: operate
  title: ''
  type: StatusPage
  url: https://status.algolia.com
- group: operate
  title: ''
  type: ChangeLog
  url: https://www.algolia.com/doc/libraries/sdk/changelog/javascript
- group: commercial
  title: ''
  type: Plans
  url: plans/algolia-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/algolia-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/algolia-finops.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/algolia-authentication.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/algolia-domain-security.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/algolia-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: Security
  url: security/algolia-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: TrustCenter
  url: security/algolia-trust-center.yml
- group: auth
  title: ''
  type: Compliance
  url: security/algolia-trust-center.yml
- group: build
  title: ''
  type: Packages
  url: packages/algolia-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/algolia-packages.yml
- group: build
  title: ''
  type: CLI
  url: cli/algolia-cli.yml
- group: design
  title: ''
  type: Components
  url: components/algolia-components.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/algolia-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/algolia-problem-types.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/algolia-lifecycle.yml
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/algolia-changelog.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/algolia-conformance.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/algolia-data-model.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/algolia-scopes.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/algolia-well-known.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/algolia-llms.txt
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/algolia-mcp.yml
- group: build
  title: ''
  type: ToolCrosswalk
  url: mcp/algolia-tool-crosswalk.yml
created: '2026-05-04'
description: Algolia is a hosted search and discovery platform that delivers fast, typo-tolerant search, browse, recommendations and personalization through a suite of REST APIs and edge-distributed infrastructure. It powers search experiences for ecommerce, media, SaaS and content sites, pairing a synchronous indexing and query control plane with event-driven Insights, Recommend, A/B Testing and Personalization products. Algolia generates every first-party API client and its reference documentation from 15 public OpenAPI documents totalling 342 operations, and has extended the platform into the agent layer with two managed MCP servers, an Agent Studio runtime and 18 self-published Agent Skills.
finops:
- name: Algolia Finops
  service_category: Search
  slug: algolia-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/algolia.png
layout: provider
mcp_servers:
- description: Algolia ships TWO first-party, Algolia-managed remote MCP servers. Neither is a stdio package a developer runs locally - both are hosted HTTPS endpoints an MCP client POSTs to, which is the agent-reac
  name: Algolia MCP Server
  slug: algolia-mcp-server
modified: '2026-08-27'
name: Algolia
nav: Providers
network: true
overview: 'Algolia publishes 13 APIs on the [APIs.io](https://apis.io/) network, including Search API, Insights API, Recommend API, and 10 more. Tagged areas include Search, Discovery, Recommendations, Personalization, and Analytics.


  Algolia''s developer surface includes documentation, API reference, getting-started guide, support, engineering blog, signup flow, pricing, and 33 more developer resources.'
plans:
- name: Algolia Plans Pricing
  plan_count: 4
  slug: algolia-plans-pricing
random_paper: 15
rate_limits:
- limit_count: 12
  name: Algolia Rate Limits
  slug: algolia-rate-limits
scopes:
- name: Algolia Scopes
  scope_count: 0
  slug: algolia-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: exemplar
  composite: 68.8
  coverage:
    artifact_dirs: 23
    catalog_gap: 48.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 100.0
    commercial_clarity: 100.0
    contract_governance: 4.5
    contract_quality: 58.0
    developer_ergonomics: 78.6
    discoverability: 81.5
    governance: 4.5
    operational_transparency: 76.3
  previous_composite: 68.8
  provenance:
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 15
    mcp: first-party
    skills: first-party
  schema_version: 0.18.2
  scored_at: '2026-09-03'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/algolia/refs/heads/main/screenshots/algolia-2026-06-20T171526.png
security:
- kind: authentication
  name: Algolia Authentication
  slug: algolia-authentication
  summary_line: apiKey/http · 5 schemes
- kind: domain-security
  name: Algolia Domain Security
  slug: algolia-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Algolia Vulnerability Disclosure
  slug: algolia-vulnerability-disclosure
  summary_line: Hackerone
- kind: trust-center
  name: Algolia Trust Center
  slug: algolia-trust-center
  summary_line: read, named, reason, probed
slug: algolia
tags:
- Search
- Discovery
- Recommendations
- Personalization
- Analytics
- E-Commerce
website: https://www.algolia.com
---
