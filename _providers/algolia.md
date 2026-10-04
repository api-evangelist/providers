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
    mcp_server: verified
    openapi_examples: partial
    protected_resource_metadata: verified
    rate_limit_signal: verified
    reversibility_documented: verified
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 61.5
  scored_at: '2026-10-03'
api_count: 15
apis:
- baseURL: https://{appid}-dsn.algolia.net
  baseurl_source: declared
  description: Core indexing and search API for adding, updating and deleting records and querying them with typo-tolerant, faceted, geo-aware and rule-driven search served from globally distributed search nodes. Th
  name: Algolia Search API
  phrasing_intents:
  - id: customGet
    intent: Send a custom GET request to the Search API
    question: Can I call a Search API endpoint the client library doesn't wrap yet with a raw GET?
  - id: customPost
    intent: Send a custom POST request to the Search API
    question: What's the way to POST to a new Search API endpoint before the SDK supports it?
  - id: customPut
    intent: Send a custom PUT request to the Search API
    question: How can I send a PUT to a Search API path that has no dedicated method?
  - id: customDelete
    intent: Send a custom DELETE request to the Search API
    question: How do I send a raw DELETE to a Search API path the client doesn't cover?
  - id: searchSingleIndex
    intent: Search one index
    question: How do I run a search query against my products index?
  - id: search
    intent: Run several search queries in one request
    question: Can I search my products and my articles indices in a single API call?
  - id: searchForFacetValues
    intent: Search the values of a facet
    question: How can I let users search within a long list of brand filter values?
  - id: browse
    intent: Browse records in an index page by page
    question: What's the difference between browsing and searching when I want raw matching records?
  phrasing_ops: 78
  slug: algolia-search-api
- baseURL: https://insights.algolia.io
  baseurl_source: declared
  description: Inbound event-ingestion API for click, conversion, view and purchase signals that feed Personalization, Recommend, A/B Testing and Analytics. Accepts events; does not emit them, which is why Algolia p
  name: Algolia Insights API
  phrasing_intents:
  - id: customGet
    intent: Send a custom GET request to the Insights API
    question: Can I call an Insights API endpoint the client library doesn't wrap yet with a raw GET?
  - id: customPost
    intent: Send a custom POST request to the Insights API
    question: What's the way to POST to a new Insights API endpoint before the SDK supports it?
  - id: customPut
    intent: Send a custom PUT request to the Insights API
    question: How can I send a PUT to an Insights API path that has no dedicated method?
  - id: customDelete
    intent: Send a custom DELETE request to the Insights API
    question: How do I send a raw DELETE to an Insights API path the client doesn't cover?
  - id: pushEvents
    intent: Send click, conversion and view events
    question: How do I send click and conversion events from my search UI to Algolia?
  - id: deleteUserToken
    intent: Delete all events for a user token
    question: How can I erase every event recorded for one user, for example for a privacy request?
  - id: setClientApiKey
    intent: Switch the API key the Insights client uses
    question: Can I change which API key my Insights client authenticates with without recreating it?
  phrasing_ops: 7
  slug: algolia-insights-api
- baseURL: https://{appid}-dsn.algolia.net
  baseurl_source: declared
  description: Returns related-products, frequently-bought-together, trending and look-alike recommendations trained from Insights events and catalog data, plus the Recommend rules that override them.
  name: Algolia Recommend API
  phrasing_intents:
  - id: customGet
    intent: Send a custom GET request to the Recommend API
    question: Can I call a Recommend API endpoint the client library doesn't wrap yet with a raw GET?
  - id: customPost
    intent: Send a custom POST request to the Recommend API
    question: What's the way to POST to a new Recommend API endpoint before the SDK supports it?
  - id: customPut
    intent: Send a custom PUT request to the Recommend API
    question: How can I send a PUT to a Recommend API path that has no dedicated method?
  - id: customDelete
    intent: Send a custom DELETE request to the Recommend API
    question: How do I send a raw DELETE to a Recommend API path the client doesn't cover?
  - id: getRecommendations
    intent: Get product recommendations from AI models
    question: How do I get 'frequently bought together' or related-product recommendations for an item?
  - id: getRecommendRule
    intent: Retrieve a Recommend rule
    question: How can I look up one Recommend rule I set up in the dashboard?
  - id: deleteRecommendRule
    intent: Delete a Recommend rule
    question: How do I remove a rule from a recommendation scenario?
  - id: getRecommendStatus
    intent: Check the status of a Recommend task
    question: How can I tell whether my Recommend rule deletion has finished?
  phrasing_ops: 11
  slug: algolia-recommend-api
- baseURL: https://analytics.algolia.com
  baseurl_source: declared
  description: Reports top searches, no-result searches, click and conversion rates, revenue and other search analytics aggregated from query and Insights data. One of only six Algolia APIs that returns machine-read
  name: Algolia Analytics API
  phrasing_intents:
  - id: customGet
    intent: Send a custom GET request to the Analytics API
    question: Can I call an Analytics API endpoint the client library doesn't wrap yet with a raw GET?
  - id: customPost
    intent: Send a custom POST request to the Analytics API
    question: What's the way to POST to a new Analytics API endpoint before the SDK supports it?
  - id: customPut
    intent: Send a custom PUT request to the Analytics API
    question: How can I send a PUT to an Analytics API path that has no dedicated method?
  - id: customDelete
    intent: Send a custom DELETE request to the Analytics API
    question: How do I send a raw DELETE to an Analytics API path the client doesn't cover?
  - id: getTopSearches
    intent: Get the most popular search queries
    question: What are people searching for most on my site?
  - id: getSearchesCount
    intent: Count searches over a period
    question: How many searches did my index get each day this week?
  - id: getSearchesNoResults
    intent: List frequent searches that returned no results
    question: Which queries are coming back empty for my users?
  - id: getSearchesNoClicks
    intent: List popular searches that got no clicks
    question: Which searches return results that nobody clicks?
  phrasing_ops: 30
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
  phrasing_intents:
  - id: customGet
    intent: Send a raw GET request to the Personalization API
    question: Can I read a Personalization endpoint that the client library doesn't wrap?
  - id: customPost
    intent: Send a raw POST request to the Personalization API
    question: Can I POST to a Personalization endpoint the SDK doesn't expose as a method?
  - id: customPut
    intent: Send a raw PUT request to the Personalization API
    question: Can I send a custom PUT to a Personalization path that has no dedicated method?
  - id: customDelete
    intent: Send a raw DELETE request to the Personalization API
    question: Can I issue a DELETE against an arbitrary Personalization API path?
  - id: getUserTokenProfile
    intent: Get a user's personalization profile and affinities
    question: Which facet values does a particular shopper have the strongest affinity for?
  - id: deleteUserProfile
    intent: Delete a user's personalization profile
    question: How do I erase a user's personalization profile, for example after a privacy request?
  - id: getPersonalizationStrategy
    intent: Get the current personalization strategy
    question: What events and facets is my personalization strategy currently scoring?
  - id: setPersonalizationStrategy
    intent: Define the personalization strategy
    question: How do I tell Personalization which events and facets should drive ranking?
  phrasing_ops: 9
  slug: algolia-personalization-api
- baseURL: https://ai-personalization.{region}.algolia.com
  baseurl_source: declared
  description: 'The successor to classic Personalization: real-time user profiles, personalization strategies and a dedicated error-code reference. Runs on its own AI personalization host and publishes the only per-p'
  name: Algolia Advanced Personalization API
  phrasing_intents:
  - id: customGet
    intent: Send a raw GET request to Advanced Personalization
    question: Can I read an Advanced Personalization endpoint that the client library doesn't wrap?
  - id: customPost
    intent: Send a raw POST request to Advanced Personalization
    question: Can I POST to an Advanced Personalization endpoint the SDK doesn't expose?
  - id: customPut
    intent: Send a raw PUT request to Advanced Personalization
    question: Can I send a custom PUT to an Advanced Personalization path with no dedicated method?
  - id: customDelete
    intent: Send a raw DELETE request to Advanced Personalization
    question: Can I issue a DELETE against an arbitrary Advanced Personalization path?
  - id: getConfig
    intent: Get the Advanced Personalization configuration
    question: Which indices have Advanced Personalization configured, and with what settings?
  - id: putConfig
    intent: Update the Advanced Personalization configuration
    question: How do I turn on Advanced Personalization for a new index?
  - id: getUsers
    intent: List Advanced Personalization user profiles
    question: How do I page through all the user profiles Advanced Personalization has built?
  - id: getUser
    intent: Get one Advanced Personalization user profile
    question: What has Advanced Personalization stored about one specific user ID?
  phrasing_ops: 12
  slug: algolia-advanced-personalization-api
- baseURL: https://crawler.algolia.com/api
  baseurl_source: declared
  description: Manages Algolia's hosted web crawler that extracts content from websites and pushes it into indices on a schedule. The only Algolia API that authenticates with HTTP Basic rather than the x-algolia-* h
  name: Algolia Crawler API
  phrasing_intents:
  - id: listCrawlers
    intent: List crawlers
    question: Which website crawlers do I have set up?
  - id: createCrawler
    intent: Create a website crawler
    question: How do I set up a new crawler to index my website?
  - id: getCrawler
    intent: Retrieve a crawler's details
    question: How can I check the state of one crawler, such as whether it's running or blocked?
  - id: patchCrawler
    intent: Rename a crawler or replace its configuration
    question: How do I rename a crawler?
  - id: deleteCrawler
    intent: Delete a crawler
    question: How do I permanently remove a crawler I no longer use?
  - id: runCrawler
    intent: Unpause a crawler
    question: How do I resume a crawler I paused?
  - id: pauseCrawler
    intent: Pause a crawler
    question: How can I temporarily stop a crawler from running?
  - id: startReindex
    intent: Start a full crawl
    question: How do I trigger a full recrawl of my website right now?
  phrasing_ops: 20
  slug: algolia-crawler-api
- baseURL: https://data.{region}.algolia.com
  baseurl_source: declared
  description: Connector-based data ingestion that pulls records from databases, storage and ecommerce platforms into Algolia indices via managed sources, destinations, transformations and tasks. The largest connect
  name: Algolia Ingestion API
  phrasing_intents:
  - id: customGet
    intent: Send a raw GET request to the Ingestion API
    question: Can I read an Ingestion endpoint that the client library doesn't wrap?
  - id: customPost
    intent: Send a raw POST request to the Ingestion API
    question: Can I POST to an Ingestion endpoint the SDK doesn't expose as a method?
  - id: customPut
    intent: Send a raw PUT request to the Ingestion API
    question: Can I send a custom PUT to an Ingestion path that has no dedicated method?
  - id: customDelete
    intent: Send a raw DELETE request to the Ingestion API
    question: Can I issue a DELETE against an arbitrary Ingestion API path?
  - id: push
    intent: Push records to an index through the pipeline
    question: How do I send records through my transformation pipeline straight into an index by name?
  - id: listAuthentications
    intent: List authentication resources
    question: Which stored credentials do my ingestion connectors use?
  - id: createAuthentication
    intent: Create an authentication resource
    question: How do I store credentials so a data source or destination can connect?
  - id: searchAuthentications
    intent: Look up several authentication resources by ID
    question: Can I fetch a batch of authentication resources when I have a list of their IDs?
  phrasing_ops: 61
  slug: algolia-ingestion-api
- baseURL: https://query-suggestions.{region}.algolia.com
  baseurl_source: declared
  description: Generates and maintains query-suggestion indices from popular searches to power as-you-type autocomplete.
  name: Algolia Query Suggestions API
  phrasing_intents:
  - id: customGet
    intent: Send a custom GET request to Query Suggestions
    question: Can I call a Query Suggestions endpoint the client library doesn't wrap yet with a raw GET?
  - id: customPost
    intent: Send a custom POST request to Query Suggestions
    question: What's the way to POST to a new Query Suggestions endpoint before the SDK supports it?
  - id: customPut
    intent: Send a custom PUT request to Query Suggestions
    question: How can I send a PUT to a Query Suggestions API path that has no dedicated method?
  - id: customDelete
    intent: Send a custom DELETE request to Query Suggestions
    question: How do I send a raw DELETE to a Query Suggestions API path the client doesn't cover?
  - id: getAllConfigs
    intent: List all Query Suggestions configurations
    question: Which Query Suggestions configurations exist in my Algolia application?
  - id: createConfig
    intent: Create a Query Suggestions configuration
    question: How do I set up query suggestions built from my product index?
  - id: getConfig
    intent: Retrieve a Query Suggestions configuration
    question: How can I see the settings behind one of my query suggestions indices?
  - id: updateConfig
    intent: Update a Query Suggestions configuration
    question: How do I change the source indices of an existing query suggestions configuration?
  phrasing_ops: 12
  slug: algolia-query-suggestions-api
- baseURL: https://{appId}.algolia.net
  baseurl_source: declared
  description: Composes multiple search sources into one curated result set - smart groups, curated queries and composition rules - so a single request returns a merchandised, multi-source response.
  name: Algolia Composition API
  phrasing_intents:
  - id: customGet
    intent: Send a raw GET request to the Composition API
    question: Can I read a Composition endpoint that the client library doesn't wrap?
  - id: customPost
    intent: Send a raw POST request to the Composition API
    question: Can I POST to a Composition endpoint the SDK doesn't expose as a method?
  - id: customPut
    intent: Send a raw PUT request to the Composition API
    question: Can I send a custom PUT to a Composition path that has no dedicated method?
  - id: customDelete
    intent: Send a raw DELETE request to the Composition API
    question: Can I issue a DELETE against an arbitrary Composition API path?
  - id: search
    intent: Run a search query against a composition
    question: How do I get search results from a composition instead of querying an index directly?
  - id: searchForFacetValues
    intent: Search facet values in a composition's main source
    question: How do I autocomplete brand names from a facet on my composition's main index?
  - id: listCompositions
    intent: List compositions in the application
    question: Which compositions exist in my Algolia application?
  - id: getComposition
    intent: Get one composition's configuration
    question: How do I see how a specific composition is configured?
  phrasing_ops: 20
  slug: algolia-composition-api
- baseURL: https://{APPLICATION_ID}.algolia.net/agent-studio
  baseurl_source: declared
  description: 'Algolia''s agent-building runtime: agents, conversations, tools, memory, guardrails and per-turn context, exposed as 42 REST operations. Notably, Agent Studio can itself consume third-party MCP tools, '
  name: Algolia Agent Studio API
  phrasing_intents:
  - id: listAgents
    intent: List Agent Studio agents
    question: Which AI agents have I built in Algolia Agent Studio?
  - id: createAgent
    intent: Create a new AI agent
    question: How do I create a new conversational agent with its own instructions?
  - id: getAgent
    intent: Get an agent's details
    question: How do I see the instructions, model and tools one agent is configured with?
  - id: updateAgent
    intent: Update an existing agent
    question: How do I change the system prompt of an agent I already built?
  - id: deleteAgent
    intent: Delete an agent
    question: How do I permanently remove an agent I no longer need?
  - id: listAgentAllowedDomains
    intent: List an agent's allowed domains
    question: Which websites are allowed to call my agent?
  - id: createAgentAllowedDomain
    intent: Allow one domain to use an agent
    question: How do I let my app's domain call my agent?
  - id: bulkCreateAllowedDomains
    intent: Allow many domains for an agent at once
    question: How do I add a whole list of domains to an agent's allowlist in one go?
  phrasing_ops: 42
  slug: algolia-agent-studio-api
- baseURL: https://status.algolia.com
  baseurl_source: declared
  description: 'Exposes server status, latency, indexing and reachability metrics for a specific application''s Algolia infrastructure. More than a status page: an agent can query the health of its own cluster rather '
  name: Algolia Monitoring API
  phrasing_intents:
  - id: customGet
    intent: Send a raw GET request to the Monitoring API
    question: Can I read a Monitoring endpoint that the client library doesn't wrap?
  - id: customPost
    intent: Send a raw POST request to the Monitoring API
    question: Can I POST to a Monitoring endpoint the SDK doesn't expose as a method?
  - id: customPut
    intent: Send a raw PUT request to the Monitoring API
    question: Can I send a custom PUT to a Monitoring path that has no dedicated method?
  - id: customDelete
    intent: Send a raw DELETE request to the Monitoring API
    question: Can I issue a DELETE against an arbitrary Monitoring API path?
  - id: getStatus
    intent: Check the status of all Algolia clusters
    question: Is Algolia up right now across all clusters?
  - id: getClusterStatus
    intent: Check the status of specific clusters
    question: Is the cluster my application runs on operational?
  - id: getIncidents
    intent: List known incidents across all clusters
    question: Are there any known incidents affecting Algolia clusters?
  - id: getClusterIncidents
    intent: List incidents for specific clusters
    question: Has my cluster had any incidents lately?
  phrasing_ops: 14
  slug: algolia-monitoring-api
- description: Returns per-application usage metrics (operations, records, search volume) for cost and quota tracking. The one documented Algolia REST API for which no OpenAPI document is published in the api-client
  name: Algolia Usage API
  slug: algolia-usage-api
- description: Algolia-managed remote MCP server giving an agent user-scoped, read-only access to search, index listing and the full analytics surface, authorized by the signed-in user's own Algolia permissions. OAu
  name: Algolia Productivity MCP Server
  slug: algolia-productivity-mcp-server
- baseURL: https://{appid}-dsn.algolia.net
  baseurl_source: declared
  description: The Ab Testing API from Algolia — 6 operation(s) for ab testing.
  name: Algolia Ab Testing API
  slug: algolia-ab-testing-api
artifact_total: 25
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
  href: https://raw.githubusercontent.com/api-evangelist/algolia/refs/heads/main/plans/algolia-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/algolia-plans-pricing.yml
- group: operate
  href: https://raw.githubusercontent.com/api-evangelist/algolia/refs/heads/main/rate-limits/algolia-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/algolia-rate-limits.yml
- group: commercial
  href: https://raw.githubusercontent.com/api-evangelist/algolia/refs/heads/main/finops/algolia-finops.yml
  title: ''
  type: FinOps
  url: finops/algolia-finops.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/algolia/refs/heads/main/authentication/algolia-authentication.yml
  title: ''
  type: Authentication
  url: authentication/algolia-authentication.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/algolia/refs/heads/main/security/algolia-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/algolia-domain-security.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/algolia/refs/heads/main/security/algolia-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/algolia-vulnerability-disclosure.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/algolia/refs/heads/main/security/algolia-vulnerability-disclosure.yml
  title: ''
  type: Security
  url: security/algolia-vulnerability-disclosure.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/algolia/refs/heads/main/security/algolia-trust-center.yml
  title: ''
  type: TrustCenter
  url: security/algolia-trust-center.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/algolia/refs/heads/main/security/algolia-trust-center.yml
  title: ''
  type: Compliance
  url: security/algolia-trust-center.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/algolia/refs/heads/main/packages/algolia-packages.yml
  title: ''
  type: Packages
  url: packages/algolia-packages.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/algolia/refs/heads/main/packages/algolia-packages.yml
  title: ''
  type: SDKs
  url: packages/algolia-packages.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/algolia/refs/heads/main/cli/algolia-cli.yml
  title: ''
  type: CLI
  url: cli/algolia-cli.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/algolia/refs/heads/main/components/algolia-components.yml
  title: ''
  type: Components
  url: components/algolia-components.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/algolia/refs/heads/main/conventions/algolia-conventions.yml
  title: ''
  type: Conventions
  url: conventions/algolia-conventions.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/algolia/refs/heads/main/errors/algolia-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/algolia-problem-types.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/algolia/refs/heads/main/lifecycle/algolia-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/algolia-lifecycle.yml
- group: operate
  href: https://raw.githubusercontent.com/api-evangelist/algolia/refs/heads/main/changelog/algolia-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/algolia-changelog.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/algolia/refs/heads/main/conformance/algolia-conformance.yml
  title: ''
  type: Conformance
  url: conformance/algolia-conformance.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/algolia/refs/heads/main/data-model/algolia-data-model.yml
  title: ''
  type: DataModel
  url: data-model/algolia-data-model.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/algolia/refs/heads/main/scopes/algolia-scopes.yml
  title: ''
  type: OAuthScopes
  url: scopes/algolia-scopes.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/algolia/refs/heads/main/well-known/algolia-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/algolia-well-known.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/algolia/refs/heads/main/llms/algolia-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/algolia-llms.txt
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/algolia/refs/heads/main/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/algolia/refs/heads/main/mcp/algolia-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/algolia-mcp.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/algolia/refs/heads/main/mcp/algolia-tool-crosswalk.yml
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
overview: 'Algolia publishes 16 APIs on the [APIs.io](https://apis.io/) network, including Search API, Insights API, Recommend API, and 13 more. Tagged areas include Search, Discovery, Recommendations, Personalization, and Analytics.


  Algolia''s developer surface includes documentation, API reference, getting-started guide, support, engineering blog, signup flow, pricing, and 33 more developer resources.'
plans:
- name: Algolia Plans Pricing
  plan_count: 4
  slug: algolia-plans-pricing
random_paper: 3
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
  composite: 74.4
  coverage:
    artifact_dirs: 24
    catalog_earned: 67.0
    catalog_earned_first_party: 24.0
    catalog_gap: 48.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 100.0
    contract_governance: 4.5
    contract_quality: 52.5
    developer_ergonomics: 78.6
    discoverability: 80.0
    operational_transparency: 76.3
  previous_composite: 74.4
  provenance:
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 15
    mcp: first-party
    skills: first-party
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 45.1
  schema_version: 0.23.0
  scored_at: '2026-10-03'
  trend: flat
  upsert:
    applies: true
    score: 33.3
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
