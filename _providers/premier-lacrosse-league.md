---
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: false
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: documented
    event_surface_described: false
    idempotency: false
    mcp_server: verified
    openapi_examples: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 23.3
  scored_at: '2026-08-19'
api_count: 2
apis:
- description: 'Apollo Server GraphQL API that backs premierlacrosseleague.com and stats.premierlacrosseleague.com (teams, players, games, standings, stats). Undocumented and unadvertised: there is no developer porta'
  name: Premier Lacrosse League Web GraphQL API
  slug: premier-lacrosse-league-web-graphql-api
- description: The league's Shopify-hosted merchandise store exposes a public, unauthenticated product/collection JSON surface, a Universal Commerce Protocol (UCP) merchant profile at /.well-known/ucp, an MCP endpoi
  name: Premier Lacrosse League Shop Storefront and Agent Commerce API
  slug: premier-lacrosse-league-shop-storefront-and-agent-commerce-api
artifact_total: 6
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/premier-lacrosse-league-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://premierlacrosseleague.com/
- group: company
  title: ''
  type: Blog
  url: https://premierlacrosseleague.com/articles
- group: operate
  title: ''
  type: Support
  url: https://premierlacrosseleague.com/contact-page
- group: commercial
  title: ''
  type: TermsOfService
  url: https://premierlacrosseleague.com/terms-of-service
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://premierlacrosseleague.com/privacy-policy
- group: start
  title: ''
  type: SignUp
  url: https://shop.premierlacrosseleague.com/account/register
- group: start
  title: ''
  type: Login
  url: https://shop.premierlacrosseleague.com/account/login
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/Premier-Lacrosse-League
- group: agent
  title: ''
  type: WellKnown
  url: well-known/premier-lacrosse-league-well-known.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/premier-lacrosse-league-llms.txt
- group: agent
  title: ''
  type: MCPServer
  url: mcp/premier-lacrosse-league-mcp.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/premier-lacrosse-league-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/premier-lacrosse-league-scopes.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/premier-lacrosse-league-problem-types.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/premier-lacrosse-league-conventions.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/premier-lacrosse-league-conformance.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/premier-lacrosse-league-lifecycle.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/premier-lacrosse-league-data-model.yml
created: '2026-08-02'
description: The Premier Lacrosse League (PLL) is the professional field lacrosse league of North America, founded in 2018 by brothers Paul and Mike Rabil and headquartered in El Segundo, California. It played its inaugural season in 2019 as a tour-based league, absorbed Major League Lacrosse in December 2020, and now fields eight city-affiliated clubs across an Eastern and a Western conference. Games are carried by ESPN, ESPN2, ABC and ESPN+, and investors include The Chernin Group, The Raine Group, Arctos Partners and ESPN itself. Digitally the league runs a Next.js web property with an Apollo GraphQL API behind it (premierlacrosseleague.com/api/graphql), a dedicated stats site, iOS and Android apps, and a Shopify-hosted merchandise store that publishes an llms.txt, a Universal Commerce Protocol (UCP) profile and an MCP endpoint for agent-driven commerce. The league publishes no developer portal, no OpenAPI and no public API documentation; every machine-readable surface below was discovered
  by probing.
image: https://premierlacrosseleague.com/wp-content/uploads/2019/03/PLL__Square_Logo_Social.png
layout: provider
mcp_servers:
- description: ''
  name: premier-lacrosse-league-mcp.yml
  slug: premier-lacrosse-league-mcpyml
modified: '2026-08-02'
name: Premier Lacrosse League
nav: Providers
network: true
overview: 'Premier Lacrosse League publishes 2 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Sports, Lacrosse, Professional Sports League, and Sports Statistics.


  Premier Lacrosse League''s developer surface includes engineering blog, support, signup flow, authentication, and 16 more developer resources.'
random_paper: 2
scopes:
- name: Premier Lacrosse League Scopes
  scope_count: 4
  slug: premier-lacrosse-league-scopes
  summary_line: 4 scopes · authorizationCode/refreshToken/urn:ietf:params:oauth:grant-type:jwt-bearer
score:
  band: emerging
  composite: 22.2
  delta: -1.1
  facets:
    access_clarity: 34.2
    commercial_clarity: 34.2
    contract_governance: 18.2
    contract_quality: 0.0
    developer_ergonomics: 20.8
    discoverability: 87.0
    governance: 18.2
    operational_transparency: 2.6
  previous_composite: 23.3
  provenance:
    conformance: first-party
    mcp: first-party
    skills: derived
  schema_version: 0.12.0
  scored_at: '2026-08-19'
  trend: flat
security:
- kind: authentication
  name: Premier Lacrosse League Authentication
  slug: premier-lacrosse-league-authentication
  summary_line: none/oauth2/openIdConnect · 4 schemes
- kind: domain-security
  name: Premier Lacrosse League Domain Security
  slug: premier-lacrosse-league-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: premier-lacrosse-league
tags:
- Company
- Sports
- Lacrosse
- Professional Sports League
- Sports Statistics
- Media and Entertainment
- Ecommerce
- Agent Commerce
- GraphQL
- Fantasy Sports
website: https://premierlacrosseleague.com/
---
