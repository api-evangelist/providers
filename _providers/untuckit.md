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
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: true
    agentic_access: false
    agentic_commerce: platform
    auth_clarity: served
    consent_identity: false
    delegated_identity: served
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: platform
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: '0.2'
  score: 17.4
  scored_at: '2026-09-20'
api_count: 2
apis:
- description: 'Live MCP endpoint implementing the Universal Commerce Protocol shopping service for the UNTUCKit store: catalog search, cart, checkout, fulfillment, discounts, and orders, with Shop Pay / Google Pay /'
  name: UNTUCKit Storefront Agent Commerce (UCP/MCP) API
  slug: untuckit-storefront-agent-commerce-ucpmcp-api
- description: 'Unauthenticated read-only Shopify storefront JSON documented in the store''s agents.md: product JSON at /products/{handle}.json, collection product listings at /collections/{handle}/products.json, prod'
  name: UNTUCKit Storefront Catalog JSON API
  slug: untuckit-storefront-catalog-json-api
artifact_total: 6
common:
- group: company
  title: ''
  type: Website
  url: https://untuckit.com
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/untuckit/refs/heads/main/mcp/untuckit-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/untuckit-mcp.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/untuckit/refs/heads/main/llms/untuckit-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/untuckit-llms.txt
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/untuckit/refs/heads/main/well-known/untuckit-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/untuckit-well-known.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/untuckit/refs/heads/main/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/untuckit/refs/heads/main/scopes/untuckit-scopes.yml
  title: ''
  type: OAuthScopes
  url: scopes/untuckit-scopes.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/untuckit/refs/heads/main/authentication/untuckit-authentication.yml
  title: ''
  type: Authentication
  url: authentication/untuckit-authentication.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/untuckit/refs/heads/main/conformance/untuckit-conformance.yml
  title: ''
  type: Conformance
  url: conformance/untuckit-conformance.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/untuckit/refs/heads/main/conventions/untuckit-conventions.yml
  title: ''
  type: Conventions
  url: conventions/untuckit-conventions.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/untuckit/refs/heads/main/lifecycle/untuckit-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/untuckit-lifecycle.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/untuckit/refs/heads/main/security/untuckit-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/untuckit-domain-security.yml
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.untuckit.com/policies/privacy-policy
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.untuckit.com/policies/terms-of-service
- group: operate
  title: ''
  type: Support
  url: https://www.untuckit.com/pages/contact-us
- group: company
  title: ''
  type: Blog
  url: https://www.untuckit.com/blogs/news
- group: start
  title: ''
  type: Login
  url: https://www.untuckit.com/account/login
created: '2026-07-17'
description: 'UNTUCKit is a US apparel brand and omnichannel retailer best known for shirts designed to be worn untucked, selling menswear and womenswear through untuckit.com and its retail stores. Its Shopify-powered storefront is notably agent-ready: the store publishes agents.md and llms.txt operating instructions, a Universal Commerce Protocol (UCP) merchant profile at /.well-known/ucp, a live MCP endpoint at /api/ucp/mcp for catalog search, cart, and buyer-approved checkout, OIDC/OAuth discovery for the Shopify Customer Account API, and unauthenticated product and collection JSON.'
image: https://avatars.githubusercontent.com/u/48734252?v=4
layout: provider
mcp_servers:
- description: UNTUCKit's Shopify storefront operates a live, first-party-hosted MCP endpoint as the transport for the Universal Commerce Protocol (UCP) shopping service. The endpoint, its OpenRPC schema, and the ag
  name: UNTUCKit MCP Server
  slug: untuckit-mcp-server
modified: '2026-07-21'
name: UNTUCKit
nav: Providers
network: true
overview: 'UNTUCKit publishes 2 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Apparel, Retail, E-Commerce, and Shopify.


  UNTUCKit''s developer surface includes authentication, support, engineering blog, and 13 more developer resources.'
random_paper: 7
scopes:
- name: Untuckit Scopes
  scope_count: 4
  slug: untuckit-scopes
  summary_line: 4 scopes
score:
  band: emerging
  composite: 22.4
  coverage:
    artifact_dirs: 13
    catalog_earned: 37.0
    catalog_earned_first_party: 0.0
    catalog_gap: 78.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 27.6
    contract_governance: 18.2
    contract_quality: 0.0
    developer_ergonomics: 35.7
    discoverability: 75.9
    operational_transparency: 0.0
  previous_composite: 22.4
  provenance:
    conformance: first-party
    mcp: first-party
    skills: first-party
  schema_version: 0.22.0
  scored_at: '2026-09-20'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
screenshot: https://raw.githubusercontent.com/api-evangelist/untuckit/refs/heads/main/screenshots/untuckit-2026-09-02T165005.png
security:
- kind: authentication
  name: Untuckit Authentication
  slug: untuckit-authentication
  summary_line: 3 schemes
- kind: domain-security
  name: Untuckit Domain Security
  slug: untuckit-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: untuckit
tags:
- Company
- Apparel
- Retail
- E-Commerce
- Shopify
- Agentic Commerce
- MCP
- Universal Commerce Protocol
website: https://untuckit.com
---
