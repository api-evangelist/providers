---
agent_readiness:
  band: agent-native
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: true
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: documented
    event_surface_described: false
    idempotency: documented
    mcp_server: true
    openapi_examples: false
    rate_limit_signal: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 53.8
  scored_at: '2026-08-12'
agentic_access:
- acting_count: 0
  human_in_the_loop: 0
  name: Fnatic Agentic Access
  operation_count: 8
  slug: fnatic-agentic-access
  summary_line: 8 operations
api_count: 2
apis:
- description: 'The Shopify Storefront GraphQL API as served from Fnatic''s own shop domain. Introspection is anonymous — the full schema (416 types, 35 query fields, 41 mutations, 28 Relay connections) was retrieved '
  name: Fnatic Shop Storefront GraphQL API
  slug: storefront-graphql
- description: A Universal Commerce Protocol shopping service exposed over MCP (JSON-RPC 2.0) on Fnatic's own shop host, advertised in Fnatic's /.well-known/ucp merchant profile and in its own /agents.md. The profil
  name: Fnatic Shop UCP Commerce MCP Endpoint
  slug: ucp-mcp
artifact_total: 7
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/fnatic-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://fnatic.com/
- group: docs
  title: ''
  type: Documentation
  url: https://shop.fnatic.com/agents.md
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/fnatic-llms.txt
- group: agent
  title: ''
  type: WellKnown
  url: well-known/fnatic-well-known.yml
- group: docs
  title: ''
  type: GraphQL
  url: graphql/fnatic-storefront.graphql
- group: agent
  title: ''
  type: MCPServer
  url: mcp/fnatic-mcp.yml
- group: build
  title: ''
  type: ToolCrosswalk
  url: mcp/fnatic-tool-crosswalk.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/fnatic-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/fnatic-scopes.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/fnatic-conventions.yml
- group: design
  title: ''
  type: Idempotency
  url: conventions/fnatic-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/fnatic-problem-types.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/fnatic-lifecycle.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/fnatic-conformance.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/fnatic-data-model.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/fnatic-agentic-access.yml
- group: build
  title: ''
  type: Packages
  url: packages/fnatic-packages.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/FNATIC
- group: operate
  title: ''
  type: Support
  url: https://help.fnatic.com/
- group: operate
  title: ''
  type: HelpCenter
  url: https://help.fnatic.com/
- group: company
  title: ''
  type: Blog
  url: https://fnatic.com/news
- group: company
  title: ''
  type: About
  url: https://fnatic.com/about
- group: company
  title: ''
  type: Careers
  url: https://fnatic.com/careers
- group: company
  title: ''
  type: Partners
  url: https://fnatic.com/partners
- group: other
  title: ''
  type: Brand
  url: https://fnatic.com/brand
- group: operate
  title: ''
  type: Community
  url: https://fnatic.com/community
- group: start
  title: ''
  type: SignUp
  url: https://fnatic.com/account/register
- group: start
  title: ''
  type: Login
  url: https://fnatic.com/account/login
- group: commercial
  title: ''
  type: TermsOfService
  url: https://fnatic.com/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://fnatic.com/privacy
- group: other
  title: ''
  type: Shop
  url: https://shop.fnatic.com/
- group: other
  title: ''
  type: RefundPolicy
  url: https://shop.fnatic.com/policies/refund-policy
- group: company
  title: ''
  type: Twitter
  url: https://twitter.com/fnatic
- group: company
  title: ''
  type: Instagram
  url: https://www.instagram.com/fnatic/
- group: company
  title: ''
  type: Facebook
  url: https://www.facebook.com/fnatic
- group: learn
  title: ''
  type: YouTube
  url: https://www.youtube.com/c/fnatic
- group: other
  title: ''
  type: TikTok
  url: https://www.tiktok.com/@fnatic
- group: other
  title: ''
  type: Twitch
  url: https://www.twitch.tv/fnatic
- group: operate
  title: ''
  type: Discord
  url: https://discord.com/invite/fnatic
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/fnatic/
- group: other
  title: ''
  type: Wikipedia
  url: https://en.wikipedia.org/wiki/Fnatic
- group: other
  title: ''
  type: SecondaryMarket
  url: https://forgeglobal.com/fnatic_stock/
created: '2026-08-04'
description: 'Fnatic is a London-headquartered global esports performance brand founded in 2004, fielding 20+ professional players across five game titles, operating four offices and facilities in London, Berlin, Belgrade and Tokyo with 100+ staff, and claiming $16m+ in prize money, 33m+ social followers and $55m raised from institutional investors. Beyond competition it runs two commercial businesses: Fnatic Gear, an award-winning esports hardware line (mice, keyboards, headsets and pads) launched in 2016, and an apparel and merchandise store. Fnatic operates no developer program and publishes no OpenAPI, no developer portal and no API documentation — fnatic.com is a Next.js front end over a Sanity CMS with a first-party member-account system ("Fnatic ID") that exposes no discovery document. Its one machine-readable surface is the Shopify-hosted store at shop.fnatic.com, which serves an anonymously introspectable Storefront GraphQL API, a Universal Commerce Protocol merchant profile with
  a UCP MCP commerce endpoint, OpenID Connect and RFC 8414/9728 discovery for customer accounts, and a provider-authored /agents.md (mirrored at /llms.txt) that tells AI agents which surface to use and requires explicit buyer approval before any agent completes a payment.'
image: https://cdn.sanity.io/images/5gii1snx/production/a1e70e04e9186899208f8b42117b105a1126ce16-1200x630.png
layout: provider
mcp_servers:
- description: ''
  name: fnatic-mcp.yml
  slug: fnatic-mcpyml
modified: '2026-08-04'
name: Fnatic
nav: Providers
network: true
overview: 'Fnatic publishes 2 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Esports, Gaming, Entertainment, and Sports.


  Fnatic''s developer surface includes documentation, authentication, support, engineering blog, signup flow, YouTube channel, and 38 more developer resources.'
random_paper: 29
scopes:
- name: Fnatic Scopes
  scope_count: 4
  slug: fnatic-scopes
  summary_line: 4 scopes · authorizationCode
score:
  band: thin
  composite: 37.0
  delta: 0.0
  facets:
    commercial_clarity: 34.2
    contract_quality: 48.1
    developer_ergonomics: 36.4
    discoverability: 87.0
    governance: 12.5
    operational_transparency: 5.3
  previous_composite: 37.0
  provenance:
    agentic_access: first-party
    conformance: first-party
    mcp: first-party
    skills: derived
  schema_version: 0.11.0
  scored_at: '2026-08-12'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/fnatic/refs/heads/main/screenshots/fnatic-2026-08-07T165400.png
security:
- kind: authentication
  name: Fnatic Authentication
  slug: fnatic-authentication
  summary_line: none/openIdConnect/oauth2/other · 5 schemes
- kind: domain-security
  name: Fnatic Domain Security
  slug: fnatic-domain-security
  summary_line: TLSv1.3 · DMARC
slug: fnatic
tags:
- Company
- Esports
- Gaming
- Entertainment
- Sports
- Consumer Electronics
- Gaming Hardware
- Apparel
- Ecommerce
- Direct to Consumer
- Agentic Commerce
- Shopify
- GraphQL
- Universal Commerce Protocol
- Model Context Protocol
- United Kingdom
website: https://fnatic.com/
---
