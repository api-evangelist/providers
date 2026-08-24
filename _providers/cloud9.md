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
  scored_at: '2026-08-24'
api_count: 3
apis:
- description: cloud9.gg runs on WordPress (WP Cloud / Automattic Atomic hosting) and serves the standard WordPress REST API anonymously at https://cloud9.gg/wp-json/. The discovery index enumerates 277 routes acros
  name: Cloud9 WordPress REST API
  slug: wordpress-rest-api
- description: A remote Model Context Protocol server published on cloud9.gg and advertised through RFC 8414 OAuth authorization-server metadata and RFC 9728 protected-resource metadata. It is the WordPress MCP adap
  name: Cloud9 MCP Server
  slug: mcp-server
- description: The official Cloud9 merchandise store at store.cloud9.gg is a Shopify storefront, and Shopify serves its standard anonymous product and collection JSON endpoints on it — /products.json returns the liv
  name: Cloud9 Store JSON Endpoints
  slug: store-json
artifact_total: 9
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/cloud9-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://cloud9.gg/
- group: company
  title: ''
  type: Blog
  url: https://cloud9.gg/news/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/cloud9esports
- group: operate
  title: ''
  type: Support
  url: https://cloud9.gg/contact/
- group: operate
  title: ''
  type: Community
  url: https://discordapp.com/invite/cloud9
- group: start
  title: ''
  type: SignUp
  url: https://club9.cloud9.gg/explore?callbackUrl=/explore&login=open
- group: commercial
  title: ''
  type: TermsOfService
  url: https://cloud9.gg/terms-of-service/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://cloud9.gg/privacy-policy/
- group: company
  title: ''
  type: About
  url: https://cloud9.gg/about/
- group: company
  title: ''
  type: Careers
  url: https://cloud9.gg/careers/
- group: other
  title: ''
  type: BrandAssets
  url: https://cloud9.gg/brand-assets/
- group: other
  title: ''
  type: Shop
  url: https://store.cloud9.gg/
- group: agent
  title: ''
  type: WellKnown
  url: well-known/cloud9-well-known.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/cloud9-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/cloud9-scopes.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/cloud9-mcp.yml
- group: build
  title: ''
  type: ToolCrosswalk
  url: mcp/cloud9-tool-crosswalk.yml
- group: docs
  title: ''
  type: JSONSchema
  url: json-schema/cloud9-wp-rest-schemas.json
- group: design
  title: ''
  type: DataModel
  url: data-model/cloud9-data-model.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/cloud9-conventions.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/cloud9-conformance.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/cloud9-problem-types.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/cloud9-lifecycle.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/cloud9-llms.txt
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: other
  title: ''
  type: SecondaryMarket
  url: https://forgeglobal.com/cloud9_stock/
created: '2026-08-09'
description: 'Cloud9 Esports, Inc. is a North American professional esports organization founded in 2013 by Jack and Paullie Etienne and headquartered in Santa Monica, California. It fields competitive rosters across League of Legends, VALORANT, VALORANT Game Changers, Call of Duty and Rainbow Six, and its trophy case includes the inaugural Overwatch World Championship, the 2018 Rocket League World Championship, multiple LCS titles and a Counter-Strike Major. Beyond competition it runs Club9 (a membership and fan community at club9.cloud9.gg), an official Shopify merchandise store at store.cloud9.gg, and a content and creator division. Cloud9 publishes no developer program and no OpenAPI, but its public web estate is machine-readable: cloud9.gg runs on WordPress and serves an anonymous, unauthenticated WordPress REST API at /wp-json/ covering news posts, pages, media and the Cloud9-specific players, teams, achievement and case-study content types, alongside a remote Model Context Protocol
  server advertised through RFC 8414 and RFC 9728 discovery metadata.'
image: https://cloud9.gg/wp-content/uploads/Team_C9_blu_80x80.svg
json_schemas:
- name: Cloud9 Wp Rest Index
  property_count: 0
  slug: cloud9-wp-rest-index
- name: Cloud9 Wp Rest Schemas
  property_count: 0
  slug: cloud9-wp-rest-schemas
layout: provider
mcp_servers:
- description: Cloud9 publishes a remote Model Context Protocol server on its primary marketing host, cloud9.gg. It is not listed in any MCP registry, is not mentioned anywhere on the Cloud9 site, and Cloud9 operate
  name: Cloud9 MCP Server
  slug: cloud9-mcp-server
modified: '2026-08-09'
name: Cloud9
nav: Providers
network: true
overview: 'Cloud9 publishes 3 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Esports, Gaming, Entertainment, and Media.


  Cloud9''s developer surface includes engineering blog, support, signup flow, authentication, and 23 more developer resources.'
random_paper: 4
scopes:
- name: Cloud9 Scopes
  scope_count: 1
  slug: cloud9-scopes
  summary_line: 1 scope · authorizationCode
score:
  band: emerging
  composite: 24.9
  delta: 0.0
  facets:
    access_clarity: 34.2
    commercial_clarity: 34.2
    contract_governance: 18.2
    contract_quality: 8.5
    developer_ergonomics: 20.8
    discoverability: 92.6
    governance: 18.2
    operational_transparency: 2.6
  previous_composite: 24.9
  provenance:
    conformance: first-party
    mcp: first-party
    skills: derived
  schema_version: 0.12.1
  scored_at: '2026-08-24'
  trend: flat
security:
- kind: authentication
  name: Cloud9 Authentication
  slug: cloud9-authentication
  summary_line: none/http/oauth2 · 4 schemes
- kind: domain-security
  name: Cloud9 Domain Security
  slug: cloud9-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: cloud9
tags:
- Company
- Esports
- Gaming
- Entertainment
- Media
- Sports
- Content
- WordPress
- Community
- Merchandise
website: https://cloud9.gg/
---
