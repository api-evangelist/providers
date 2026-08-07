---
agent_readiness:
  band: agent-native
  dimensions:
    agent_card: false
    agent_skills: true
    agentic_access: false
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: documented
    event_surface_described: true
    idempotency: documented
    mcp_server: true
    openapi_examples: false
    rate_limit_signal: false
    spec_presence: true
    well_known_catalog: true
  schema_version: 0.2
  score: 57.2
  scored_at: '2026-08-06'
api_count: 2
apis:
- description: Restricted-access REST API that exposes the on-course data powering the Arccos apps — a golfer's rounds, per-round traditional and Strokes Gained stats, paired clubs and smart club distances, user pro
  name: Arccos On-Course Data API
  slug: arccos-on-course-data-api
- description: 'Universal Commerce Protocol (UCP) MCP endpoint published on the Arccos Golf Shopify storefront for agent-driven commerce. An anonymous JSON-RPC tools/list returns 13 tools covering catalog search and '
  name: Arccos Golf Storefront UCP MCP Server
  slug: arccos-golf-storefront-ucp-mcp-server
artifact_total: 7
asyncapis:
- description: ''
  name: Arccos Golf Webhooks
  slug: arccos-golf-webhooks
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/arccos-golf-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.arccosgolf.com/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://api.arccosgolf.com/swagger
- group: docs
  title: ''
  type: Documentation
  url: https://api.arccosgolf.com/swagger
- group: docs
  title: ''
  type: APIReference
  url: https://api.arccosgolf.com/swagger
- group: start
  title: ''
  type: GettingStarted
  url: https://github.com/arccosgolf/on-course-data-api-example-front-end
- group: build
  title: ''
  type: Postman
  url: https://www.postman.com/arccosgolf/workspace/arccos-public-api/collection/14095300-9001cc03-d9dd-4c77-a42d-ca6a0417350b
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/arccosgolf
- group: operate
  title: ''
  type: Support
  url: https://www.arccosgolf.com/pages/contact
- group: operate
  title: ''
  type: HelpCenter
  url: https://support.arccosgolf.com/hc/en-us
- group: company
  title: ''
  type: Blog
  url: https://www.arccosgolf.com/blogs/community
- group: start
  title: ''
  type: SignUp
  url: https://www.arccosgolf.com/account/register
- group: start
  title: ''
  type: Login
  url: https://dashboard.arccosgolf.com/login
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.arccosgolf.com/policies/terms-of-service
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.arccosgolf.com/policies/privacy-policy
- group: docs
  title: ''
  type: OpenAPI
  url: openapi/arccos-golf-on-course-data-api-openapi.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/arccos-golf-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/arccos-golf-scopes.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/arccos-golf-conventions.yml
- group: design
  title: ''
  type: Idempotency
  url: conventions/arccos-golf-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/arccos-golf-problem-types.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/arccos-golf-data-model.yml
- group: design
  title: ''
  type: Webhooks
  url: asyncapi/arccos-golf-webhooks.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/arccos-golf-lifecycle.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/arccos-golf-conformance.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/arccos-golf-well-known.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/arccos-golf-llms.txt
- group: agent
  title: ''
  type: MCPServer
  url: mcp/arccos-golf-mcp.yml
- group: build
  title: ''
  type: ToolCrosswalk
  url: mcp/arccos-golf-tool-crosswalk.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: other
  title: ''
  type: Overlay
  url: overlays/arccos-golf-on-course-data-api-overlay.yaml
- group: other
  title: ''
  type: SecondaryMarket
  url: https://forgeglobal.com/arccos-golf_stock/
created: '2026-08-06'
description: Arccos Golf is the golf performance-tracking platform behind the Arccos Caddie smart sensors, smart grips and the Arccos Air wearable — the Official Game Tracker of the PGA TOUR. Club-mounted sensors and the Arccos mobile app automatically capture every shot on the course, then AI-driven Strokes Gained analytics, Smart Club Distances, an AI rangefinder and Arccos Caddie strategy turn that shot data into per-round and per-hole insight. Arccos exposes that same data to approved third parties through the Arccos On-Course Data API, a Swagger 2.0-documented REST API over rounds, round stats, clubs, users and a public course/course-version catalog, secured with an OAuth 2.0 authorization-code flow and per-resource read scopes, plus registerable HTTPS webhooks for round and account-disconnect events. Its Shopify-hosted storefront additionally publishes an llms.txt and a Universal Commerce Protocol (UCP) MCP endpoint for agent-driven commerce.
image: https://www.arccosgolf.com/cdn/shop/files/Arccos_Logo-Inline.svg
layout: provider
mcp_servers:
- description: ''
  name: arccos-golf-mcp.yml
  slug: arccos-golf-mcpyml
modified: '2026-08-06'
name: Arccos Golf
nav: Providers
network: true
overview: 'Arccos Golf publishes 1 API on the [APIs.io](https://apis.io/) network: Arccos On-Course Data API. Tagged areas include Company, golf, sports-technology, wearables, and iot.


  The Arccos Golf catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  Arccos Golf''s developer surface includes documentation, API reference, getting-started guide, support, engineering blog, signup flow, authentication, and 25 more developer resources.'
random_paper: 87
scopes:
- name: Arccos Golf Scopes
  scope_count: 4
  slug: arccos-golf-scopes
  summary_line: 4 scopes · authorizationCode
score:
  band: developing
  composite: 48.6
  facets:
    commercial_clarity: 34.2
    contract_quality: 58.1
    developer_ergonomics: 71.7
    discoverability: 87.0
    governance: 20.8
    operational_transparency: 13.2
  schema_version: 0.9.1
  scored_at: '2026-08-06'
security:
- kind: authentication
  name: Arccos Golf Authentication
  slug: arccos-golf-authentication
  summary_line: oauth2/http · 2 schemes
- kind: domain-security
  name: Arccos Golf Domain Security
  slug: arccos-golf-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: arccos-golf
tags:
- Company
- golf
- sports-technology
- wearables
- iot
- shot-tracking
- sports-analytics
- performance-analytics
- geospatial
- consumer-hardware
- webhooks
- oauth2
- mcp
- ecommerce
website: https://www.arccosgolf.com/
---
