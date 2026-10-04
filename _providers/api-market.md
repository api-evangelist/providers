---
agent_readiness:
  band: agent-aware
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
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: '0.2'
  score: 24.0
  scored_at: '2026-10-03'
api_count: 3
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
artifact_total: 9
common:
- group: operate
  href: https://raw.githubusercontent.com/api-evangelist/api-market/refs/heads/main/rate-limits/api-market-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/api-market-rate-limits.yml
- group: commercial
  href: https://raw.githubusercontent.com/api-evangelist/api-market/refs/heads/main/plans/api-market-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/api-market-plans-pricing.yml
- group: operate
  href: https://raw.githubusercontent.com/api-evangelist/api-market/refs/heads/main/changelog/api-market-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/api-market-changelog.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/api-market/refs/heads/main/conventions/api-market-conventions.yml
  title: ''
  type: Conventions
  url: conventions/api-market-conventions.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/api-market/refs/heads/main/authentication/api-market-authentication.yml
  title: ''
  type: Authentication
  url: authentication/api-market-authentication.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/api-market/refs/heads/main/scopes/api-market-scopes.yml
  title: ''
  type: OAuthScopes
  url: scopes/api-market-scopes.yml
- group: operate
  title: ''
  type: StatusPage
  url: https://status.api.market/status/dash
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/api-market/refs/heads/main/lifecycle/api-market-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/api-market-lifecycle.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/api-market/refs/heads/main/errors/api-market-error-codes.yml
  title: ''
  type: ErrorCatalog
  url: errors/api-market-error-codes.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/api-market/refs/heads/main/conformance/api-market-conformance.yml
  title: ''
  type: Conformance
  url: conformance/api-market-conformance.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/api-market/refs/heads/main/llms/api-market-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/api-market-llms.txt
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/api-market/refs/heads/main/mcp/api-market-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/api-market-mcp.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/api-market/refs/heads/main/well-known/api-market-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/api-market-well-known.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/api-market/refs/heads/main/hosts/api-market-hosts.yml
  title: ''
  type: Hosts
  url: hosts/api-market-hosts.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/api-market/refs/heads/main/vendors/api-market-vendors.yml
  title: ''
  type: Vendors
  url: vendors/api-market-vendors.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/api-market/refs/heads/main/packages/api-market-packages.yml
  title: ''
  type: SDKs
  url: packages/api-market-packages.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/api-market/refs/heads/main/packages/api-market-packages.yml
  title: ''
  type: Packages
  url: packages/api-market-packages.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/api-market/refs/heads/main/security/api-market-domain-security.yml
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
  href: https://raw.githubusercontent.com/api-evangelist/api-market/refs/heads/main/llms/api-market-docs-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/api-market-docs-llms.txt
- group: start
  title: ''
  type: GettingStarted
  url: https://api.market/mcp
created: '2026-09-25'
description: API.market (Noveum) is an API marketplace launched in April 2024 where developers discover, subscribe to and call third-party APIs and AI models with one account, one x-api-market-key and unified billing, and where sellers import an OpenAPI source, set pricing plans and get paid. The platform itself exposes a hosted MCP gateway at https://api.market/api/mcp/gateway (Streamable HTTP, OAuth 2.1 with dynamic client registration, or API key) with five tools (search_apis, get_api_tools, call_api, check_usage, manage_subscription), a Subscription Management REST API and a read-only Usage API. Individual APIs sold on the marketplace belong to their own providers and are not listed here.
image: https://api.market/favicon.ico
layout: provider
mcp_servers:
- description: ''
  name: API.market MCP Gateway
  slug: apimarket-mcp-gateway
modified: '2026-09-27'
name: API.market
nav: Providers
network: true
overview: 'API.market publishes 3 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include API Marketplace, MCP, AI Agents, API Monetization, and Subscription.


  API.market''s developer surface includes changelog, authentication, documentation, getting-started guide, engineering blog, support, YouTube channel, and 29 more developer resources.'
plans:
- name: Api Market Plans Pricing
  plan_count: 1
  slug: api-market-plans-pricing
random_paper: 13
rate_limits:
- limit_count: 2
  name: Api Market Rate Limits
  slug: api-market-rate-limits
scopes:
- name: Api Market Scopes
  scope_count: 0
  slug: api-market-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: developing
  composite: 41.1
  coverage:
    artifact_dirs: 18
    catalog_earned: 56.0
    catalog_earned_first_party: 16.0
    catalog_gap: 59.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 8.5
  facets:
    access_clarity: 55.3
    contract_governance: 18.2
    contract_quality: 0.0
    developer_ergonomics: 47.6
    discoverability: 80.0
    operational_transparency: 57.9
  previous_composite: 32.6
  provenance:
    conformance: first-party
    mcp: first-party
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 34.3
  schema_version: 0.23.0
  scored_at: '2026-10-03'
  trend: rising
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
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
- Authentication
website: https://api.market/
---
