---
agent_readiness:
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: true
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: documented
    event_surface_described: true
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: documented
    spec_presence: true
    well_known_catalog: true
  schema_version: 0.2
  score: 50.0
  scored_at: '2026-08-10'
agentic_access:
- acting_count: 8
  human_in_the_loop: 1
  name: Zillapi Agentic Access
  operation_count: 29
  slug: zillapi-agentic-access
  summary_line: 29 operations · 8 acting · 1 human-in-the-loop
api_count: 7
apis:
- description: The Account API from Zillapi — 2 operation(s) for account.
  name: Zillapi Account API
  slug: zillapi-account-api
- description: The Buildings API from Zillapi — 1 operation(s) for buildings.
  name: Zillapi Buildings API
  slug: zillapi-buildings-api
- description: The Jobs API from Zillapi — 3 operation(s) for jobs.
  name: Zillapi Jobs API
  slug: zillapi-jobs-api
- description: The Listings API from Zillapi — 4 operation(s) for listings.
  name: Zillapi Listings API
  slug: zillapi-listings-api
- description: The Properties API from Zillapi — 13 operation(s) for properties.
  name: Zillapi Properties API
  slug: zillapi-properties-api
- description: The Search API from Zillapi — 2 operation(s) for search.
  name: Zillapi Search API
  slug: zillapi-search-api
- description: The Webhooks API from Zillapi — 3 operation(s) for webhooks.
  name: Zillapi Webhooks API
  slug: zillapi-webhooks-api
artifact_total: 15
asyncapis:
- description: ''
  name: Zillapi Webhooks
  slug: zillapi-webhooks
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/zillapi-domain-security.yml
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/zillapi-agentic-access.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/zillapi-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/zillapi-scopes.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/zillapi-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/zillapi-error-codes.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/zillapi-lifecycle.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/zillapi-conformance.yml
- group: build
  title: ''
  type: Packages
  url: packages/zillapi-packages.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/zillapi-well-known.yml
- group: other
  title: ''
  type: APICatalog
  url: https://zillapi.com/.well-known/api-catalog
- group: design
  title: ''
  type: Webhooks
  url: asyncapi/zillapi-webhooks.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/zillapi-rate-limits.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/zillapi-plans.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/zillapi-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: Security
  url: https://github.com/ZeroPointRepo/zillow-skills/blob/main/SECURITY.md
- group: start
  title: ''
  type: DeveloperPortal
  url: https://zillapi.com/
- group: docs
  title: ''
  type: Documentation
  url: https://zillapi.com/quickstart/
- group: docs
  title: ''
  type: APIReference
  url: https://zillapi.com/api/properties/
- group: start
  title: ''
  type: GettingStarted
  url: https://zillapi.com/quickstart/
- group: company
  title: ''
  type: Blog
  url: https://zillapi.com/blog/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/ZeroPointRepo/zillow-skills
- group: commercial
  title: ''
  type: Pricing
  url: https://zillapi.com/pricing/
- group: start
  title: ''
  type: SignUp
  url: https://zillapi.com/signup
- group: start
  title: ''
  type: Login
  url: https://zillapi.com/login
- group: commercial
  title: ''
  type: TermsOfService
  url: https://zillapi.com/legal/terms/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://zillapi.com/legal/privacy/
- group: operate
  title: ''
  type: Support
  url: mailto:hello@zillapi.com
created: '2026-07-13'
description: Independent third-party provider of Zillow-sourced U.S. residential property data via a REST API, hosted MCP server, and agent skills. Returns ~300+ fields per property including price, Zestimate, rent Zestimate, photos, schools, taxes, and full price history, plus listing search, building extraction, async batch jobs, and signed webhooks.
image: https://zillapi.com/og.png
layout: provider
modified: '2026-08-09'
name: Zillapi
nav: Providers
network: true
overview: 'Zillapi publishes 7 APIs on the [APIs.io](https://apis.io/) network, including Account API, Buildings API, Jobs API, and 4 more. Tagged areas include real estate, proptech, property data, zillow, and zestimate.


  The Zillapi catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  Zillapi''s developer surface includes authentication, documentation, API reference, getting-started guide, engineering blog, pricing, signup flow, and 21 more developer resources.'
plans:
- name: Zillapi Plans
  plan_count: 4
  slug: zillapi-plans
random_paper: 61
rate_limits:
- limit_count: 3
  name: Zillapi Rate Limits
  slug: zillapi-rate-limits
scopes:
- name: Zillapi Scopes
  scope_count: 1
  slug: zillapi-scopes
  summary_line: 1 scope · authorizationCode
score:
  band: strong
  composite: 60.6
  facets:
    commercial_clarity: 76.3
    contract_quality: 64.0
    developer_ergonomics: 52.2
    discoverability: 92.6
    governance: 20.8
    operational_transparency: 55.3
  schema_version: 0.9.1
  scored_at: '2026-08-10'
security:
- kind: authentication
  name: Zillapi Authentication
  slug: zillapi-authentication
  summary_line: http/oauth2 · 2 schemes
- kind: domain-security
  name: Zillapi Domain Security
  slug: zillapi-domain-security
  summary_line: TLSv1.3 · DMARC
- kind: vulnerability-disclosure
  name: Zillapi Vulnerability Disclosure
  slug: zillapi-vulnerability-disclosure
  summary_line: Hackerone · contact published
slug: zillapi
tags:
- real estate
- proptech
- property data
- zillow
- zestimate
- valuation
- AVM
- listings
- MCP
- AI agent
- REST API
website: https://zillapi.com/
---
