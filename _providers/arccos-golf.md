---
agent_readiness:
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: false
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: documented
    event_surface_described: true
    idempotency: documented
    mcp_server: documented
    openapi_examples: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 41.5
  scored_at: '2026-08-24'
api_count: 6
apis:
- description: 'Universal Commerce Protocol (UCP) MCP endpoint published on the Arccos Golf Shopify storefront for agent-driven commerce. An anonymous JSON-RPC tools/list returns 13 tools covering catalog search and '
  name: Arccos Golf Storefront UCP MCP Server
  slug: arccos-golf-storefront-ucp-mcp-server
- description: The Clubs API from Arccos Golf — 2 operation(s) for clubs.
  name: Arccos Golf Clubs API
  slug: arccos-golf-clubs-api
- description: The Courses API from Arccos Golf — 3 operation(s) for courses.
  name: Arccos Golf Courses API
  slug: arccos-golf-courses-api
- description: The Rounds API from Arccos Golf — 3 operation(s) for rounds.
  name: Arccos Golf Rounds API
  slug: arccos-golf-rounds-api
- description: The Users API from Arccos Golf — 1 operation(s) for users.
  name: Arccos Golf Users API
  slug: arccos-golf-users-api
- description: The Webhooks API from Arccos Golf — 2 operation(s) for webhooks.
  name: Arccos Golf Webhooks API
  slug: arccos-golf-webhooks-api
artifact_total: 19
asyncapis:
- description: ''
  name: Arccos Golf Webhooks
  slug: arccos-golf-webhooks
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Arccos On-Course Data Clubs API
  slug: open-arccos-golf-clubs-api
- collection_type: open
  name: Arccos On-Course Data Courses API
  slug: open-arccos-golf-courses-api
- collection_type: open
  name: Arccos On-Course Data API
  slug: open-arccos-golf-on-course-data-api
- collection_type: open
  name: Arccos On-Course Data Rounds API
  slug: open-arccos-golf-rounds-api
- collection_type: open
  name: Arccos On-Course Data Users API
  slug: open-arccos-golf-users-api
- collection_type: open
  name: Arccos On-Course Data Webhooks API
  slug: open-arccos-golf-webhooks-api
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
  url: openapi/_original/arccos-golf-on-course-data-api-openapi.yml
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
  name: Arccos Golf Storefront UCP MCP Server
  slug: arccos-golf-storefront-ucp-mcp-server
- description: ''
  name: Arccos Golf MCP Server
  slug: arccos-golf-mcp-server
modified: '2026-08-06'
name: Arccos Golf
nav: Providers
network: true
overview: 'Arccos Golf publishes 5 APIs on the [APIs.io](https://apis.io/) network, including Clubs API, Courses API, Rounds API, and 2 more. Tagged areas include Company, Golf, Sports Technology, Wearables, and IoT.


  The Arccos Golf catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  Arccos Golf''s developer surface includes documentation, API reference, getting-started guide, support, engineering blog, signup flow, authentication, and 25 more developer resources.'
random_paper: 12
scopes:
- name: Arccos Golf Scopes
  scope_count: 4
  slug: arccos-golf-scopes
  summary_line: 4 scopes · authorizationCode
score:
  band: developing
  composite: 44.6
  delta: 0.0
  facets:
    access_clarity: 34.2
    commercial_clarity: 34.2
    contract_governance: 16.7
    contract_quality: 53.3
    developer_ergonomics: 58.9
    discoverability: 92.6
    governance: 16.7
    operational_transparency: 10.5
  previous_composite: 44.6
  provenance:
    conformance: derived
    contracts:
      callable: 0.0
      derived: 0
      marker_coverage: 0.0
      total: 6
    mcp: first-party
    skills: derived
  schema_version: 0.12.1
  scored_at: '2026-08-24'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/arccos-golf/refs/heads/main/screenshots/arccos-golf-2026-08-07T161622.png
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
- Golf
- Sports Technology
- Wearables
- IoT
- shot-tracking
- Sports Analytics
- Performance Analytics
- Geospatial
- Consumer Hardware
- Webhook
- Authentication
- MCP
- E-Commerce
website: https://www.arccosgolf.com/
---
