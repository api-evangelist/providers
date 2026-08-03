---
agent_readiness:
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: derived
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: verified
    event_surface_described: false
    idempotency: false
    mcp_server: true
    openapi_examples: partial
    rate_limit_signal: false
    spec_presence: true
    well_known_catalog: true
  schema_version: 0.2
  score: 53.4
  scored_at: '2026-08-03'
agentic_access:
- acting_count: 124
  human_in_the_loop: 0
  name: Starfish Space Agentic Access
  operation_count: 225
  slug: starfish-space-agentic-access
  summary_line: 225 operations · 124 acting
api_count: 2
apis:
- description: The public WordPress REST API served by Starfish Space at https://www.starfishspace.com/wp-json/wp/v2. It exposes the content behind starfishspace.com — news and press releases, pages (The Otter, Comp
  name: Starfish Space Website Content API
  slug: starfish-space-website-content-api
- description: A live Model Context Protocol (MCP) server exposed by Starfish Space at https://www.starfishspace.com/wp-json/mcp/mcp-oauth-server, served through the WordPress MCP adapter. Access is OAuth 2.1 protec
  name: Starfish Space MCP Server
  slug: starfish-space-mcp-server
artifact_total: 18
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/starfish-space-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/starfish-space-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/starfish-space-authentication.yml
- group: company
  title: ''
  type: Website
  url: https://www.starfishspace.com/
- group: company
  title: ''
  type: Blog
  url: https://www.starfishspace.com/news/
- group: company
  title: ''
  type: BlogRSS
  url: https://www.starfishspace.com/feed/
- group: operate
  title: ''
  type: Support
  url: https://www.starfishspace.com/contact/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.starfishspace.com/privacy-policy/
- group: company
  title: ''
  type: About
  url: https://www.starfishspace.com/company/
- group: company
  title: ''
  type: Careers
  url: https://www.starfishspace.com/careers/
- group: other
  title: ''
  type: Products
  url: https://www.starfishspace.com/the-otter/
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/starfish-space/
- group: company
  title: ''
  type: Twitter
  url: https://twitter.com/StarfishSpace/
- group: agent
  title: ''
  type: MCPServer
  url: mcp/starfish-space-mcp.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/starfish-space-well-known.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/starfish-space-scopes.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/starfish-space-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/starfish-space-problem-types.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/starfish-space-lifecycle.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/starfish-space-conformance.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/starfish-space-data-model.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/starfish-space-llms.txt
- group: other
  title: ''
  type: Overlay
  url: overlays/starfish-space-wordpress-overlay.yaml
created: '2026-08-02'
description: Starfish Space is a satellite-servicing company founded in 2019 by Trevor Bennett and Austin Link and headquartered in the Seattle, Washington area (Tukwila). It builds Otter, a small, low-cost, electrically propelled servicing vehicle that performs autonomous rendezvous, proximity operations and docking (RPOD) with satellites that were never designed to be serviced — extending their life, relocating them, or disposing of them at end of mission. Its Otter Pup demonstration missions target the first-ever commercial satellite docking in low Earth orbit, and the company has been awarded a $54.5M U.S. Space Force contract for a dedicated Otter servicing vehicle. Starfish Space publishes no developer product API; the machine-readable surface catalogued here is the public WordPress REST API and the OAuth-protected Model Context Protocol (MCP) server served from starfishspace.com.
image: https://www.starfishspace.com/wp-content/uploads/2023/06/starfishspace-logo-fullcolor.png
json_schemas:
- name: category
  property_count: 10
  slug: starfish-space-categories.schema
- name: comment
  property_count: 17
  slug: starfish-space-comments.schema
- name: attachment
  property_count: 33
  slug: starfish-space-media.schema
- name: page
  property_count: 26
  slug: starfish-space-pages.schema
- name: post
  property_count: 28
  slug: starfish-space-posts.schema
- name: search-result
  property_count: 5
  slug: starfish-space-search.schema
- name: status
  property_count: 8
  slug: starfish-space-statuses.schema
- name: tag
  property_count: 8
  slug: starfish-space-tags.schema
- name: taxonomy
  property_count: 11
  slug: starfish-space-taxonomies.schema
- name: type
  property_count: 16
  slug: starfish-space-types.schema
- name: user
  property_count: 19
  slug: starfish-space-users.schema
layout: provider
mcp_servers:
- description: ''
  name: starfish-space-mcp.yml
  slug: starfish-space-mcpyml
modified: '2026-08-02'
name: Starfish Space
nav: Providers
network: true
overview: 'Starfish Space publishes 1 API on the [APIs.io](https://apis.io/) network: Website Content API. Tagged areas include Company, Aerospace, Space, Satellites, and Satellite Servicing.


  Starfish Space''s developer surface includes authentication, engineering blog, support, and 21 more developer resources.'
random_paper: 12
scopes:
- name: Starfish Space Scopes
  scope_count: 1
  slug: starfish-space-scopes
  summary_line: 1 scope · authorizationCode
score:
  band: thin
  composite: 35.2
  facets:
    commercial_clarity: 10.5
    contract_quality: 69.8
    developer_ergonomics: 27.7
    discoverability: 87.0
    governance: 11.5
    operational_transparency: 0.0
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 1
    mcp: first-party
    skills: derived
  schema_version: 0.9
  scored_at: '2026-08-03'
security:
- kind: authentication
  name: Starfish Space Authentication
  slug: starfish-space-authentication
  summary_line: apiKey/http · 2 schemes
- kind: domain-security
  name: Starfish Space Domain Security
  slug: starfish-space-domain-security
  summary_line: TLSv1.3
slug: starfish-space
tags:
- Company
- Aerospace
- Space
- Satellites
- Satellite Servicing
- Spacecraft
- Space Robotics
- Defense
- Content Management
- Model Context Protocol
website: https://www.starfishspace.com/
---
