---
agent_readiness:
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: derived
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
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 31.3
  scored_at: '2026-09-05'
agentic_access:
- acting_count: 0
  human_in_the_loop: 0
  name: Chocodata Agentic Access
  operation_count: 11
  slug: chocodata-agentic-access
  summary_line: 11 operations
api_count: 1
apis:
- baseURL: https://api.chocodata.com
  baseurl_source: declared
  description: REST API (HTTP + JSON, API-key auth via ?api_key=) returning structured data from a catalog of sites. Endpoints include Product, Search, Universal Web Scraper, and Batch (async). Base host is api.choc
  name: Chocodata Scraper API
  slug: chocodata-scraper-api
artifact_total: 8
asyncapis:
- description: ''
  name: Chocodata Webhooks
  slug: chocodata-webhooks
common:
- group: company
  title: ''
  type: Website
  url: https://chocodata.com
- group: auth
  title: ''
  type: DomainSecurity
  url: security/chocodata-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/chocodata-authentication.yml
- group: build
  title: ''
  type: Packages
  url: packages/chocodata-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/chocodata-packages.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/chocodata-well-known.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/chocodata-mcp.yml
- group: build
  title: ''
  type: ToolCrosswalk
  url: mcp/chocodata-tool-crosswalk.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/chocodata-llms.txt
- group: other
  title: ''
  type: Overlay
  url: overlays/chocodata-openapi-overlay.yaml
- group: design
  title: ''
  type: Conformance
  url: conformance/chocodata-conformance.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/chocodata-problem-types.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/chocodata-lifecycle.yml
- group: operate
  title: ''
  type: StatusPage
  url: https://chocodata.com/status
- group: operate
  title: ''
  type: Deprecation
  url: lifecycle/chocodata-lifecycle.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/chocodata-conventions.yml
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/chocodata-changelog.yml
- group: build
  title: ''
  type: CLI
  url: cli/chocodata-cli.yml
- group: design
  title: ''
  type: Webhooks
  url: asyncapi/chocodata-webhooks.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/chocodata-agentic-access.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/chocodata-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/chocodata-rate-limits.yml
- group: docs
  title: ''
  type: Documentation
  url: https://chocodata.com/docs
- group: docs
  title: ''
  type: APIReference
  url: https://chocodata.com/docs/endpoint-reference
- group: start
  title: ''
  type: GettingStarted
  url: https://chocodata.com/docs/getting-started
- group: commercial
  title: ''
  type: Pricing
  url: https://chocodata.com/pricing
- group: commercial
  title: ''
  type: TermsOfService
  url: https://chocodata.com/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://chocodata.com/privacy
- group: start
  title: ''
  type: SignUp
  url: https://app.chocodata.com/sign-up
- group: start
  title: ''
  type: Login
  url: https://app.chocodata.com/login
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/ChocoData-com
- group: start
  title: ''
  type: DeveloperPortal
  url: https://app.chocodata.com
- group: start
  title: ''
  type: Console
  url: https://app.chocodata.com
created: '2026-07-16'
description: Web-scraping REST API that returns structured JSON from a large catalog of target sites (e-commerce, search engines, social, real estate, finance, and more), with proxies, CAPTCHA, and anti-bot handling managed server-side. Ships an OpenAPI 3.1 contract, official Node/Python/Go SDKs, a CLI, an npm-distributed stdio MCP server (chocodata-mcp), live llms.txt manifests with markdown twins of every docs page, and an ai-plugin.json discovery manifest. Bills only for successful (2xx) responses.
image: https://chocodata.com/logo-512.png
layout: provider
mcp_servers:
- description: ''
  name: Chocodata MCP Server
  slug: chocodata-mcp-server
modified: '2026-09-03'
name: Chocodata
nav: Providers
network: true
overview: 'Chocodata publishes 1 API on the [APIs.io](https://apis.io/) network: Scraper API. Tagged areas include Web Scraping, Data Extraction, SERP, E-Commerce Data, and social-media-data.


  The Chocodata catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  Chocodata''s developer surface includes authentication, changelog, CLI, documentation, API reference, getting-started guide, pricing, and 27 more developer resources.'
plans:
- name: Chocodata Plans Pricing
  plan_count: 5
  slug: chocodata-plans-pricing
random_paper: 10
rate_limits:
- limit_count: 4
  name: Chocodata Rate Limits
  slug: chocodata-rate-limits
score:
  band: strong
  composite: 62.6
  coverage:
    artifact_dirs: 20
    catalog_earned: 61.0
    catalog_earned_first_party: 24.0
    catalog_gap: 54.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.4
  facets:
    access_clarity: 76.3
    commercial_clarity: 76.3
    contract_governance: 4.5
    contract_quality: 55.7
    developer_ergonomics: 73.2
    discoverability: 75.9
    governance: 4.5
    operational_transparency: 81.6
  previous_composite: 62.2
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 1
    mcp: first-party
    skills: derived
  schema_version: 0.18.3
  scored_at: '2026-09-05'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/chocodata/refs/heads/main/screenshots/chocodata-2026-07-25T205249.png
security:
- kind: authentication
  name: Chocodata Authentication
  slug: chocodata-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Chocodata Domain Security
  slug: chocodata-domain-security
  summary_line: TLSv1.3 · HSTS
slug: chocodata
tags:
- Web Scraping
- Data Extraction
- SERP
- E-Commerce Data
- social-media-data
- Proxy
- MCP
- agent-native
- structured-json
website: https://chocodata.com
---
