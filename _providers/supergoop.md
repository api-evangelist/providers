---
access_model:
  confidence: medium
  label: Self-serve signup
  onboarding: self-serve
  pricing: unknown
  public: false
  source:
  - authentication
  - scopes
  - rate-limits
  - security
  trial: false
  try_now: false
agent_readiness:
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: false
    agentic_commerce: platform
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: documented
    event_surface_described: false
    idempotency: documented
    mcp_server: documented
    openapi_examples: documented
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 30.6
  scored_at: '2026-09-05'
api_count: 2
apis:
- description: A live remote Model Context Protocol server implementing the Universal Commerce Protocol dev.ucp.shopping service for the Supergoop! store. An anonymous tools/list returns 13 tools with full JSON Sche
  name: Supergoop! UCP Shopping MCP Server
  slug: supergoop-ucp-shopping-mcp-server
- description: 'The Shopify Storefront GraphQL API as served for supergoop.com. Introspection is open and anonymous, returning 428 types, 34 root query fields and 41 mutations covering products, collections, search, '
  name: Supergoop! Storefront GraphQL API
  slug: supergoop-storefront-graphql-api
artifact_total: 12
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/supergoop-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://supergoop.com/
- group: docs
  title: ''
  type: Documentation
  url: https://supergoop.com/agents.md
- group: operate
  title: ''
  type: Support
  url: https://supergoop.com/pages/faq-help
- group: start
  title: ''
  type: SignUp
  url: https://supergoop.com/account/register
- group: start
  title: ''
  type: Login
  url: https://supergoop.com/account/login
- group: commercial
  title: ''
  type: TermsOfService
  url: https://supergoop.com/policies/terms-of-service
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://supergoop.com/policies/privacy-policy
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/supergoop
- group: other
  title: ''
  type: SecondaryMarketListing
  url: https://www.hiive.com/securities/supergoop-stock
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/supergoop-llms.txt
- group: agent
  title: ''
  type: WellKnown
  url: well-known/supergoop-well-known.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/supergoop-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/supergoop-scopes.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/supergoop-problem-types.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/supergoop-rate-limits.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/supergoop-mcp.yml
- group: build
  title: ''
  type: ToolCrosswalk
  url: mcp/supergoop-tool-crosswalk.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/supergoop-conventions.yml
- group: design
  title: ''
  type: Idempotency
  url: conventions/supergoop-conventions.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/supergoop-lifecycle.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/supergoop-conformance.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/supergoop-data-model.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: build
  title: ''
  type: Examples
  url: examples/_index.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/supergoop-plans-pricing.yml
created: '2026-08-29'
description: 'Supergoop! is a prestige suncare brand founded in 2005 by Holly Thaggard and headquartered in San Antonio, Texas, selling SPF-first skincare, body, makeup and kids products direct-to-consumer at supergoop.com and through retail partners; Blackstone Growth took a majority stake in 2021 at a reported $600-700 million valuation. It is not a software company and runs no developer program, but its Shopify storefront exposes three live, anonymous machine surfaces on its own domain: a Universal Commerce Protocol (UCP) shopping MCP server at /api/ucp/mcp with 13 tools, a fully introspectable Storefront GraphQL API at /api/2026-07/graphql.json with 428 types, and agent-facing instructions at /agents.md and /llms.txt that publish the discovery paths, the six-step agent purchase flow and a hard human-approval rule on payment.'
examples:
- key_count: 1
  name: Supergoop Products Json Response
  slug: supergoop-products-json-response
- key_count: 2
  name: Supergoop Storefront Graphql Products Response
  slug: supergoop-storefront-graphql-products-response
- key_count: 3
  name: Supergoop Ucp Mcp Error Authentication Required
  slug: supergoop-ucp-mcp-error-authentication-required
- key_count: 3
  name: Supergoop Ucp Mcp Error Profile Unreachable
  slug: supergoop-ucp-mcp-error-profile-unreachable
image: https://supergoop.com/cdn/shop/files/logo_desktop.svg
layout: provider
mcp_servers:
- description: Supergoop! serves a live, remote Model Context Protocol server at https://supergoop.com/api/ucp/mcp implementing the Universal Commerce Protocol (UCP) shopping service. An anonymous tools/list POST re
  name: Supergoop! UCP Shopping MCP Server
  slug: supergoop-ucp-shopping-mcp-server
modified: '2026-08-29'
name: Supergoop!
nav: Providers
network: true
overview: 'Supergoop! publishes 2 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Sunscreen, Skincare, Beauty, and Cosmetics.


  Supergoop!''s developer surface includes documentation, support, signup flow, authentication, code examples, and 21 more developer resources.'
plans:
- name: Supergoop Plans Pricing
  plan_count: 0
  slug: supergoop-plans-pricing
random_paper: 9
rate_limits:
- limit_count: 0
  name: Supergoop Rate Limits
  slug: supergoop-rate-limits
scopes:
- name: Supergoop Scopes
  scope_count: 0
  slug: supergoop-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: thin
  composite: 34.3
  coverage:
    artifact_dirs: 18
    catalog_earned: 37.0
    catalog_earned_first_party: 0.0
    catalog_gap: 78.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 34.2
    commercial_clarity: 34.2
    contract_governance: 18.2
    contract_quality: 46.8
    developer_ergonomics: 28.0
    discoverability: 75.9
    governance: 18.2
    operational_transparency: 2.6
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
    regions:
    - north-america
  previous_composite: 34.3
  provenance:
    conformance: first-party
    mcp: first-party
    skills: derived
  schema_version: 0.18.3
  scored_at: '2026-09-05'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/supergoop/refs/heads/main/screenshots/supergoop-2026-09-02T161239.png
security:
- kind: authentication
  name: Supergoop Authentication
  slug: supergoop-authentication
  summary_line: 5 schemes
- kind: domain-security
  name: Supergoop Domain Security
  slug: supergoop-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: supergoop
tags:
- Company
- Sunscreen
- Skincare
- Beauty
- Cosmetics
- Consumer Goods
- Retail
- E-Commerce
- Direct to Consumer
- Shopify
- Agentic Commerce
- Universal Commerce Protocol
- MCP
- GraphQL
website: https://supergoop.com/
---
