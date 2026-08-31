---
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: false
    agentic_commerce: platform
    auth_clarity: served
    consent_identity: false
    delegated_identity: served
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: documented
    event_surface_described: false
    idempotency: false
    mcp_server: verified
    openapi_examples: false
    protected_resource_metadata: verified
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 27.7
  scored_at: '2026-08-30'
api_count: 4
apis:
- description: The Blue Origin Shop storefront exposes an anonymous Model Context Protocol endpoint at https://shop.blueorigin.com/api/mcp. A live tools/list returned five tools with full JSON Schema draft 2020-12 i
  name: Blue Origin Shop MCP Server
  slug: blue-origin-shop-mcp-server
- description: 'The read-only JSON surface of the Blue Origin Shop Shopify storefront, documented by the store''s own llms.txt/agents.md: GET /products.json and GET /collections/{handle}/products.json return the produ'
  name: Blue Origin Shop Storefront JSON
  slug: blue-origin-shop-storefront-json
- description: payloads.blueorigin.com is Blue Origin's customer portal for payload customers, running on Salesforce Experience Cloud. Blue Origin publishes no documentation or machine-readable description for it, b
  name: Blue Origin Customer Portal (Payloads) Platform API
  slug: blue-origin-customer-portal-payloads-platform-api
- description: bodp.blueorigin.com is the Blue Origin Data Portal, a second Salesforce Experience Cloud community on the same Salesforce org as the payloads customer portal. Like that portal it publishes no document
  name: Blue Origin Data Portal (BODP) Platform API
  slug: blue-origin-data-portal-bodp-platform-api
artifact_total: 8
common:
- group: company
  title: ''
  type: Website
  url: https://www.blueorigin.com/
- group: other
  title: ''
  type: SecondaryMarket
  url: https://www.hiive.com/securities/blue-origin-stock
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/BlueOrigin
- group: company
  title: ''
  type: Blog
  url: https://www.blueorigin.com/news
- group: company
  title: ''
  type: Careers
  url: https://www.blueorigin.com/careers
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.blueorigin.com/terms-of-use
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.blueorigin.com/privacy-policy
- group: start
  title: ''
  type: SignUp
  url: https://shop.blueorigin.com/account/register
- group: agent
  title: ''
  type: MCPServer
  url: mcp/blue-origin-mcp.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/blue-origin-shop-llms.txt
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/blue-origin-llms.txt
- group: agent
  title: ''
  type: WellKnown
  url: well-known/blue-origin-well-known.yml
- group: other
  title: ''
  type: OpenIDConnect
  url: well-known/blue-origin-shop-openid-configuration.json
- group: auth
  title: ''
  type: Authentication
  url: authentication/blue-origin-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/blue-origin-scopes.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/blue-origin-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/blue-origin-problem-types.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/blue-origin-lifecycle.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/blue-origin-conformance.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/blue-origin-domain-security.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
created: '2026-08-02'
description: Blue Origin is an American private aerospace manufacturer and spaceflight services company founded in 2000 by Jeff Bezos and headquartered in Kent, Washington. It builds and flies the reusable New Shepard suborbital vehicle, the heavy-lift New Glenn orbital launch vehicle, the BE-3 and BE-4 rocket engines, the Blue Moon lunar lander and the Blue Ring orbital transfer vehicle, and it owns Honeybee Robotics. Blue Origin publishes no public developer portal, no API documentation and no machine-readable API description for any of its space products; customer, payload and supplier relationships run through authenticated portals — payloads.blueorigin.com and bodp.blueorigin.com on Salesforce Experience Cloud, and supplierportal.blueorigin.com on AWS GovCloud. The only genuinely agent-addressable surface on a blueorigin.com host is the Blue Origin Shop, a Shopify storefront that publishes a real llms.txt and agents.md, a Universal Commerce Protocol (UCP) merchant profile, RFC 9728
  protected-resource metadata, and an anonymous MCP server at /api/mcp exposing five tools. The corporate site itself sits behind a Vercel Security Checkpoint that answers HTTP 429 to every non-browser request, including /robots.txt.
image: https://shop.blueorigin.com/cdn/shop/files/shoplogo_28118316-c90f-44eb-b740-03b5c523988d.png?v=1645467696
layout: provider
mcp_servers:
- description: ''
  name: Blue Origin MCP Server
  slug: blue-origin-mcp-server
modified: '2026-08-02'
name: Blue Origin
nav: Providers
network: true
overview: 'Blue Origin publishes 4 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Aerospace, Space, Spaceflight, and Launch Services.


  Blue Origin''s developer surface includes engineering blog, signup flow, authentication, and 18 more developer resources.'
random_paper: 4
scopes:
- name: Blue Origin Scopes
  scope_count: 38
  slug: blue-origin-scopes
  summary_line: 38 scopes · authorizationCode
score:
  band: emerging
  composite: 18.4
  coverage:
    artifact_dirs: 12
    catalog_gap: 75.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 23.7
    commercial_clarity: 23.7
    contract_governance: 18.2
    contract_quality: 0.0
    developer_ergonomics: 14.9
    discoverability: 81.5
    governance: 18.2
    operational_transparency: 2.6
  previous_composite: 18.4
  provenance:
    conformance: first-party
    mcp: first-party
    skills: derived
  schema_version: 0.17.2
  scored_at: '2026-08-30'
  trend: flat
security:
- kind: authentication
  name: Blue Origin Authentication
  slug: blue-origin-authentication
  summary_line: oauth2/openIdConnect/none · 3 schemes
- kind: domain-security
  name: Blue Origin Domain Security
  slug: blue-origin-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: blue-origin
tags:
- Company
- Aerospace
- Space
- Spaceflight
- Launch Services
- Satellites
- Rocket Engines
- Defense
- Manufacturing
- E-Commerce
- MCP
website: https://www.blueorigin.com/
---
