---
agent_readiness:
  band: agent-ready
  band_gated_from: agent-native
  dimensions:
    agent_card: false
    agent_skills: true
    agentic_access: false
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: documented
    event_surface_described: true
    idempotency: false
    mcp_server: documented
    openapi_examples: verified
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: true
  schema_version: 0.2
  score: 40.1
  scored_at: '2026-09-04'
api_count: 2
apis:
- baseURL: https://api.apitube.io
  baseurl_source: declared
  description: News search and retrieval — everything, top headlines, trends, companies, journalists, fact-checks and taxonomy suggestion. 26 operations, API key by header or query.
  name: APITube News API
  slug: apitube-news-api
- baseURL: https://api.apitube.io
  baseurl_source: declared
  description: API key balance and subscription plan information.
  name: APITube Account API
  slug: apitube-account-api
- baseURL: https://api.apitube.io
  baseurl_source: declared
  description: Verify factual claims against the live news corpus (retrieval-augmented). Returns per-claim verdicts on an 8-level scale with confidence, explanation, and supporting evidence.
  name: APITube Fact Check API
  slug: apitube-fact-check-api
- baseURL: https://api.apitube.io
  baseurl_source: declared
  description: The Reference API from APITube — 7 operation(s) for reference.
  name: APITube Reference API
  slug: apitube-reference-api
- baseURL: https://api.apitube.io
  baseurl_source: declared
  description: Autocomplete and typeahead suggestions for entities.
  name: APITube Suggest API
  slug: apitube-suggest-api
- baseURL: https://api.apitube.io
  baseurl_source: declared
  description: Health checks and service status.
  name: APITube System API
  slug: apitube-system-api
- baseURL: https://api.apitube.io
  baseurl_source: declared
  description: Helper endpoints for building queries
  name: APITube Utilities API
  slug: apitube-utilities-api
artifact_total: 14
asyncapis:
- description: ''
  name: Apitube Webhooks
  slug: apitube-webhooks
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/apitube-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/apitube-authentication.yml
- group: other
  title: ''
  type: APICatalog
  url: well-known/apitube-api-catalog.json
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/apitube-llms.txt
- group: agent
  title: ''
  type: MCPServer
  url: mcp/apitube-mcp.yml
- group: company
  title: ''
  type: Website
  url: https://apitube.io
- group: start
  title: ''
  type: DeveloperPortal
  url: https://docs.apitube.io
- group: agent
  title: ''
  type: WellKnown
  url: well-known/apitube-well-known.yml
- group: build
  title: ''
  type: Packages
  url: packages/apitube-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/apitube-packages.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/apitube-rate-limits.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/apitube-plans-pricing.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/apitube-problem-types.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/apitube-lifecycle.yml
- group: operate
  title: ''
  type: StatusPage
  url: https://status.apitube.io/
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/apitube-changelog.yml
- group: design
  title: ''
  type: Webhooks
  url: asyncapi/apitube-webhooks.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/apitube-conventions.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/apitube-conformance.yml
- group: start
  title: ''
  type: Sandbox
  url: sandbox/apitube-sandbox.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/apitube-data-model.yml
- group: build
  title: ''
  type: Postman
  url: https://www.postman.com/apitube/apitube/overview
- group: commercial
  title: ''
  type: Pricing
  url: https://apitube.io/pricing
- group: commercial
  title: ''
  type: TermsOfService
  url: https://apitube.io/terms/terms-of-service
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://apitube.io/terms/privacy-policy
- group: company
  title: ''
  type: Blog
  url: https://apitube.io/blog
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/apitube
- group: operate
  title: ''
  type: Support
  url: https://apitube.io/contact
- group: start
  title: ''
  type: GettingStarted
  url: https://apitube.io/product/news-api/quick-start
- group: start
  title: ''
  type: SignUp
  url: https://apitube.io/#sign-up
created: '2026-08-21'
description: APITube is a news data API providing search and retrieval across news articles, top headlines, trends, companies, journalists, and fact-checks, with taxonomy resolution for entities, topics and locations. The public contract is an OpenAPI 3.1 document of 26 operations served from api.apitube.io, authenticated with an API key by header or query parameter. APITube also operates a first-party MCP server at mcp.apitube.io over streamable HTTP, whose tool list is readable anonymously, and publishes an RFC 9727 api-catalog linkset at the apex that names the specification, the documentation, the llms.txt and the MCP server card.
layout: provider
mcp_servers:
- description: Search and filter global news articles by language, category, sentiment, entities, media and more.
  name: APITube MCP Server
  slug: apitube-mcp-server
- description: First-party hosted MCP server for the APITube News API. Streamable HTTP JSON-RPC at https://mcp.apitube.io/ — no package to install. Two tools (search_news, suggest) and four ready-made prompts (monit
  name: APITube News MCP-Server
  slug: apitube-news-mcp-server
modified: '2026-09-03'
name: APITube
nav: Providers
network: true
overview: 'APITube publishes 7 APIs on the [APIs.io](https://apis.io/) network, including News API, Account API, Fact Check API, and 4 more. Tagged areas include News, Media Monitoring, News API, Fact Check, and Journalists.


  The APITube catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  APITube''s developer surface includes authentication, changelog, sandbox, pricing, engineering blog, support, getting-started guide, and 24 more developer resources.'
plans:
- name: Apitube Plans Pricing
  plan_count: 5
  slug: apitube-plans-pricing
random_paper: 11
rate_limits:
- limit_count: 8
  name: Apitube Rate Limits
  slug: apitube-rate-limits
score:
  band: strong
  composite: 65.6
  coverage:
    artifact_dirs: 20
    catalog_earned: 59.0
    catalog_earned_first_party: 24.0
    catalog_gap: 56.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -1.6
  facets:
    access_clarity: 76.3
    commercial_clarity: 76.3
    contract_governance: 4.5
    contract_quality: 64.0
    developer_ergonomics: 83.3
    discoverability: 72.2
    governance: 4.5
    operational_transparency: 76.3
  previous_composite: 67.2
  provenance:
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 7
    mcp: first-party
    skills: first-party
  schema_version: 0.18.3
  scored_at: '2026-09-04'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/apitube/refs/heads/main/screenshots/apitube-2026-09-02T144120.png
security:
- kind: authentication
  name: Apitube Authentication
  slug: apitube-authentication
  summary_line: apiKey · 2 schemes
- kind: domain-security
  name: Apitube Domain Security
  slug: apitube-domain-security
  summary_line: TLSv1.3 · DMARC
slug: apitube
tags:
- News
- Media Monitoring
- News API
- Fact Check
- Journalists
website: https://apitube.io
---
