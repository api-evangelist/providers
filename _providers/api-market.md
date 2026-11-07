---
access_model:
  confidence: high
  gated: none
  gated_source:
  - onboarding
  label: Free · Self-serve signup
  onboarding: self-serve
  pricing: free
  public: false
  source:
  - plans
  - authentication
  - scopes
  - rate-limits
  - security
  trial: false
  try_now: true
agent_readiness:
  band: agent-ready
  band_gated_from: agent-native
  dimensions:
    agent_card: false
    agent_skills: false
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
    mcp_tool_quality: na
    openapi_examples: partial
    operation_distinctiveness: distinct
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 42.4
  scored_at: '2026-11-06'
api_count: 15
apis:
- description: 'Hosted remote MCP server (Streamable HTTP) that lets AI agents discover and call the APIs listed on API.market through five tools: search_apis, get_api_tools, call_api, check_usage and manage_subscrip'
  name: API.market MCP Gateway
  slug: api-market-mcp-gateway
- description: REST API for reading a marketplace product and its pricing plans, reading the caller's current subscription, creating/upgrading/downgrading a subscription to a pricing plan (with a dry-run option) and
  name: API.market Subscription Management API
  slug: api-market-subscription-management-api
- description: Read-only REST API that returns quota, calls made and renewal dates for one subscription or for all of the caller's active subscriptions. Authenticated with the x-api-market-key header.
  name: API.market Usage API
  slug: api-market-usage-api
- baseURL: https://prod.api.market
  baseurl_source: declared
  description: The API.market API API from API.market — 2 operation(s) for api.market api.
  name: API.market API.market API
  slug: api-market-api-market-api-api
- baseURL: https://prod.api.market
  baseurl_source: declared
  description: The Bridgeml API from API.market — 2 operation(s) for bridgeml.
  name: API.market Bridgeml API
  slug: api-market-bridgeml-api
- baseURL: https://prod.api.market
  baseurl_source: declared
  description: The Images API from API.market — 2 operation(s) for images.
  name: API.market Images API
  slug: api-market-images-api
- baseURL: https://prod.api.market
  baseurl_source: declared
  description: The Magicapi API from API.market — 33 operation(s) for magicapi.
  name: API.market Magicapi API
  slug: api-market-magicapi-api
- baseURL: https://prod.api.market
  baseurl_source: declared
  description: The MCP API from API.market — 1 operation(s) for mcp.
  name: API.market MCP API
  slug: api-market-mcp-api
- baseURL: https://prod.api.market
  baseurl_source: declared
  description: The Models API from API.market — 1 operation(s) for models.
  name: API.market Models API
  slug: api-market-models-api
- baseURL: https://prod.api.market
  baseurl_source: declared
  description: The Pipfeed API from API.market — 3 operation(s) for pipfeed.
  name: API.market Pipfeed API
  slug: api-market-pipfeed-api
- baseURL: https://prod.api.market
  baseurl_source: declared
  description: The Predictions API from API.market — 1 operation(s) for predictions.
  name: API.market Predictions API
  slug: api-market-predictions-api
- baseURL: https://prod.api.market
  baseurl_source: declared
  description: The Status API from API.market — 1 operation(s) for status.
  name: API.market Status API
  slug: api-market-status-api
- baseURL: https://prod.api.market
  baseurl_source: declared
  description: The Subscription API from API.market — 2 operation(s) for subscription.
  name: API.market Subscription API
  slug: api-market-subscription-api
- baseURL: https://prod.api.market
  baseurl_source: declared
  description: The Toonme Api API from API.market — 4 operation(s) for toonme api.
  name: API.market Toonme API
  slug: api-market-toonme-api-api
- baseURL: https://prod.api.market
  baseurl_source: declared
  description: The User API from API.market — 3 operation(s) for user.
  name: API.market User API
  slug: api-market-user-api
artifact_total: 23
common:
- group: commercial
  title: ''
  type: Pricing
  url: https://api.market/seller
- group: operate
  href: https://artifacts.apis.io/api-market/rate-limits/api-market-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/api-market-rate-limits.yml
- group: commercial
  href: https://artifacts.apis.io/api-market/plans/api-market-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/api-market-plans-pricing.yml
- group: operate
  href: https://artifacts.apis.io/api-market/changelog/api-market-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/api-market-changelog.yml
- group: design
  href: https://artifacts.apis.io/api-market/conventions/api-market-conventions.yml
  title: ''
  type: Conventions
  url: conventions/api-market-conventions.yml
- group: auth
  href: https://artifacts.apis.io/api-market/authentication/api-market-authentication.yml
  title: ''
  type: Authentication
  url: authentication/api-market-authentication.yml
- group: auth
  href: https://artifacts.apis.io/api-market/scopes/api-market-scopes.yml
  title: ''
  type: OAuthScopes
  url: scopes/api-market-scopes.yml
- group: operate
  title: ''
  type: StatusPage
  url: https://status.api.market/status/dash
- group: design
  href: https://artifacts.apis.io/api-market/lifecycle/api-market-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/api-market-lifecycle.yml
- group: design
  href: https://artifacts.apis.io/api-market/errors/api-market-error-codes.yml
  title: ''
  type: ErrorCatalog
  url: errors/api-market-error-codes.yml
- group: design
  href: https://artifacts.apis.io/api-market/conformance/api-market-conformance.yml
  title: ''
  type: Conformance
  url: conformance/api-market-conformance.yml
- group: agent
  href: https://artifacts.apis.io/api-market/llms/api-market-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/api-market-llms.txt
- group: agent
  href: https://artifacts.apis.io/api-market/mcp/api-market-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/api-market-mcp.yml
- group: agent
  href: https://artifacts.apis.io/api-market/well-known/api-market-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/api-market-well-known.yml
- group: other
  href: https://artifacts.apis.io/api-market/hosts/api-market-hosts.yml
  title: ''
  type: Hosts
  url: hosts/api-market-hosts.yml
- group: other
  href: https://artifacts.apis.io/api-market/vendors/api-market-vendors.yml
  title: ''
  type: Vendors
  url: vendors/api-market-vendors.yml
- group: build
  href: https://artifacts.apis.io/api-market/packages/api-market-packages.yml
  title: ''
  type: SDKs
  url: packages/api-market-packages.yml
- group: build
  href: https://artifacts.apis.io/api-market/packages/api-market-packages.yml
  title: ''
  type: Packages
  url: packages/api-market-packages.yml
- group: auth
  href: https://artifacts.apis.io/api-market/security/api-market-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/api-market-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://api.market/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.api.market/
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.api.market/getting-started
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/Noveum
- group: build
  title: ''
  type: GitHubRepository
  url: https://github.com/Noveum/api-market-agent-integrations
- group: company
  title: ''
  type: Blog
  url: https://api.market/blog
- group: operate
  title: ''
  type: Support
  url: https://api.market/contact
- group: operate
  title: ''
  type: HelpCenter
  url: https://api.market/faq
- group: start
  title: ''
  type: Login
  url: https://api.market/auth/login
- group: company
  title: ''
  type: About
  url: https://api.market/about
- group: other
  title: ''
  type: Enterprise
  url: https://api.market/enterprise
- group: commercial
  title: ''
  type: TermsOfService
  url: https://api.market/terms_of_service
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://api.market/privacy_policy
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/api.market
- group: other
  title: ''
  type: X
  url: https://x.com/apimarket_
- group: learn
  title: ''
  type: YouTube
  url: https://www.youtube.com/@api.market
- group: agent
  href: https://artifacts.apis.io/api-market/llms/api-market-docs-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/api-market-docs-llms.txt
- group: start
  title: ''
  type: GettingStarted
  url: https://api.market/mcp
created: '2026-09-25'
description: API.market (Noveum) is an API marketplace launched in April 2024 where developers discover, subscribe to and call third-party APIs and AI models with one account, one x-api-market-key and unified billing, and where sellers import an OpenAPI source, set pricing plans and get paid. The platform itself exposes a hosted MCP gateway at https://api.market/api/mcp/gateway (Streamable HTTP, OAuth 2.1 with dynamic client registration, or API key) with five tools (search_apis, get_api_tools, call_api, check_usage, manage_subscription), a Subscription Management REST API and a read-only Usage API. Individual APIs sold on the marketplace belong to their own providers and are not listed here.
finops:
- has_sources: true
  method: derived
  name: Api Market Finops
  primary_unit: ''
  service_category: ''
  slug: api-market-finops
  template: true
image: https://api.market/favicon.ico
layout: provider
mcp_servers:
- description: Remote MCP server at api.market over streamable HTTP requiring OAuth; 5 tools listed.
  name: API.market MCP Gateway
  slug: io-github-noveum-api-market-gateway
modified: '2026-09-27'
name: API.market
nav: Providers
network: true
overview: 'API.market is listed with 15 APIs on the [APIs.io](https://apis.io/) network, including API.market API, Bridgeml API, Images API, and 12 more. Tagged areas include API Marketplace, MCP, AI Agents, API Monetization, and Subscription.


  The API.market catalog on APIs.io includes 1 Spectral governance ruleset.


  API.market''s developer surface includes pricing, changelog, authentication, documentation, getting-started guide, engineering blog, support, and 30 more developer resources.'
plans:
- name: Api Market Plans Pricing
  plan_count: 1
  slug: api-market-plans-pricing
random_paper: 19
rate_limits:
- limit_count: 2
  name: Api Market Rate Limits
  slug: api-market-rate-limits
rules:
- authorship: generated
  effective_rule_count: 91
  extends:
  - spectral:oas
  name: API.market API Rules
  rule_count: 50
  severity_counts:
    error: 42
    hint: 0
    info: 4
    warn: 4
  slug: api-market-rules
scopes:
- name: Api Market Scopes
  scope_count: 2
  slug: api-market-scopes
  summary_line: 2 scopes
score:
  band: thin
  composite: 38.0
  coverage:
    artifact_dirs: 26
    catalog_earned: 60.5
    catalog_earned_first_party: 16.0
    catalog_gap: 54.5
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -6.6
  facets:
    access_clarity: 43.4
    contract_governance: 31.8
    contract_quality: 12.5
    developer_ergonomics: 33.3
    discoverability: 80.0
    operational_transparency: 47.4
  previous_composite: 44.6
  provenance:
    conformance: first-party
    contracts:
      callable: 100.0
      derived: 12
      marker_coverage: 100.0
      total: 12
    mcp: first-party
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 30.4
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: falling
  upsert:
    applies: true
    score: 0.0
screenshot: https://apis.io/screenshots/api-market/api-market-2026-10-11T095936.png
security:
- kind: authentication
  name: Api Market Authentication
  slug: api-market-authentication
  summary_line: 2 schemes
- kind: domain-security
  name: Api Market Domain Security
  slug: api-market-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: api-market
tags:
- API Marketplace
- MCP
- AI Agents
- API Monetization
- Subscription
- Usage Metering
- OAuth
- Authentication
website: https://api.market/
---
