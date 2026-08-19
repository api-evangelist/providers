---
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: true
    agentic_access: false
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: documented
    event_surface_described: false
    idempotency: documented
    mcp_server: verified
    openapi_examples: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 30.3
  scored_at: '2026-08-19'
api_count: 3
apis:
- description: Anonymous Model Context Protocol server served from the Feastables origin. Answers initialize and tools/list with no credential (probed 2026-08-01, HTTP 200) and returns five tools with full JSON Sche
  name: Feastables Storefront MCP
  slug: feastables-storefront-mcp
- description: Universal Commerce Protocol shopping service over MCP transport, advertised in the store's own /.well-known/ucp profile at UCP version 2026-04-08 (also serving 2026-01-23). Carries the full commerce l
  name: Feastables UCP Shopping Service
  slug: feastables-ucp-shopping-service
- description: Read-only JSON endpoints the store documents in /agents.md for agents that only need to read store data without transacting - GET /products.json, /products/{handle}.json, /collections/{handle}/product
  name: Feastables Storefront JSON
  slug: feastables-storefront-json
artifact_total: 7
common:
- group: company
  title: ''
  type: Website
  url: https://feastables.com
- group: docs
  title: ''
  type: Documentation
  url: https://feastables.com/agents.md
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/feastables-llms.txt
- group: agent
  title: ''
  type: WellKnown
  url: well-known/feastables-well-known.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/feastables-mcp.yml
- group: build
  title: ''
  type: ToolCrosswalk
  url: mcp/feastables-tool-crosswalk.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/feastables-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/feastables-scopes.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/feastables-conformance.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/feastables-conventions.yml
- group: design
  title: ''
  type: Idempotency
  url: conventions/feastables-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/feastables-problem-types.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/feastables-lifecycle.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/feastables-data-model.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/feastables-domain-security.yml
- group: operate
  title: ''
  type: Support
  url: https://feastables.com/pages/contact-us
- group: operate
  title: ''
  type: HelpCenter
  url: https://feastables.com/pages/faq
- group: commercial
  title: ''
  type: TermsOfService
  url: https://feastables.com/policies/terms-of-service
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://feastables.com/policies/privacy-policy
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/Feastables-Inc
- group: other
  title: ''
  type: SecondaryMarket
  url: https://forgeglobal.com/feastables_stock/
created: '2026-08-01'
description: 'Feastables is the consumer snack brand founded by Jimmy Donaldson (MrBeast), selling chocolate bars, peanut butter cups, sour gummies, milk and variety boxes direct at feastables.com and across roughly 30,000 retail locations in the US, Canada and Mexico. Its stated mission is to eradicate child labor in the chocolate industry. Feastables ships no developer API and no OpenAPI, but its Shopify-hosted storefront exposes a substantial agentic-commerce surface on its own origin: an /agents.md and mirrored /llms.txt declaring how AI agents should transact, a dedicated agentic-discovery sitemap, a Universal Commerce Protocol merchant profile at /.well-known/ucp, OAuth 2.0 and OpenID Connect discovery documents for customer accounts, an anonymous Storefront MCP server at /api/mcp answering tools/list with five real tools, and a gated UCP Shopping MCP server at /api/ucp/mcp carrying the cart, checkout, fulfillment and discount capabilities.'
image: https://feastables.com/cdn/shop/files/Feastables_Logo_2024.png
layout: provider
mcp_servers:
- description: ''
  name: feastables-mcp.yml
  slug: feastables-mcpyml
modified: '2026-08-01'
name: Feastables
nav: Providers
network: true
overview: 'Feastables publishes 3 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Consumer Packaged Goods, Food and Beverage, Chocolate, and Ecommerce.


  Feastables'' developer surface includes documentation, authentication, support, and 19 more developer resources.'
random_paper: 7
scopes:
- name: Feastables Scopes
  scope_count: 4
  slug: feastables-scopes
  summary_line: 4 scopes · authorizationCode
score:
  band: emerging
  composite: 22.7
  delta: -0.8
  facets:
    access_clarity: 21.1
    commercial_clarity: 21.1
    contract_governance: 18.2
    contract_quality: 0.0
    developer_ergonomics: 33.3
    discoverability: 92.6
    governance: 18.2
    operational_transparency: 2.6
  previous_composite: 23.5
  provenance:
    conformance: first-party
    mcp: first-party
    skills: first-party
  schema_version: 0.12.0
  scored_at: '2026-08-19'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/feastables/refs/heads/main/screenshots/feastables-2026-08-07T165236.png
security:
- kind: authentication
  name: Feastables Authentication
  slug: feastables-authentication
  summary_line: none/oauth2/openIdConnect/ucp-agent-profile · 5 schemes
- kind: domain-security
  name: Feastables Domain Security
  slug: feastables-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: feastables
tags:
- Company
- Consumer Packaged Goods
- Food and Beverage
- Chocolate
- Ecommerce
- Retail
- Agentic Commerce
- Model Context Protocol
- Universal Commerce Protocol
- Shopify
website: https://feastables.com
---
