---
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: derived
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: verified
    openapi_examples: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 25.0
  scored_at: '2026-08-19'
agentic_access:
- acting_count: 0
  human_in_the_loop: 0
  name: View Com Au Agentic Access
  operation_count: 3
  slug: view-com-au-agentic-access
  summary_line: 3 operations
api_count: 1
apis:
- description: A publicly reachable, unauthenticated Model Context Protocol server (streamable HTTP, serverInfo name "view-com-au-mcp-server" version 1.0.0, protocol 2024-11-05) exposing three tools over View.com.au
  name: View.com.au Property MCP Server
  slug: view-com-au-property-mcp-server
artifact_total: 9
common:
- group: auth
  title: ''
  type: Authentication
  url: authentication/view-com-au-authentication.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/view-com-au-conformance.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/view-com-au-lifecycle.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/view-com-au-llms.txt
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/view-com-au-property-search.md
- group: agent
  title: ''
  type: AgentSkill
  url: skills/view-com-au-listing-detail.md
- group: agent
  title: ''
  type: AgentSkill
  url: skills/view-com-au-off-market-lookup.md
- group: auth
  title: ''
  type: DomainSecurity
  url: security/view-com-au-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://view.com.au/
- group: company
  title: ''
  type: Website
  url: https://www.viewmediagroup.com.au/
- group: company
  title: ''
  type: About
  url: https://view.com.au/who-we-are/
- group: company
  title: ''
  type: Blog
  url: https://view.com.au/news/
- group: operate
  title: ''
  type: Support
  url: https://view.com.au/contact-us/
- group: operate
  title: ''
  type: HelpCenter
  url: https://view.com.au/frequently-asked-questions/
- group: start
  title: ''
  type: SignUp
  url: https://view.com.au/agency-hub/signup/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://view.com.au/terms-of-use/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://view.com.au/customer-terms-conditions/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://view.com.au/privacy-policy/
- group: other
  title: ''
  type: Sitemap
  url: https://view.com.au/sitemap.xml
- group: other
  title: ''
  type: Robots
  url: https://view.com.au/robots.txt
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/realestateview
created: '2026-07-26'
description: View.com.au is an Australian residential property portal operated by View Media Group Pty Ltd (ACN 619 657 680) through view.com.au Pty Ltd (ACN 088 369 395), based in Victoria. It is the challenger portal to the REA Group / Domain duopoly, carrying for-sale, for-rent and sold listings, agency and agent profiles, Victorian sales and auction results, off-market "Property 360" property records with price estimates and planning/zoning overlays, plus home loans and editorial. Its API posture is unusual and worth stating precisely. The company publishes no developer portal, no OpenAPI, and no self-serve API program, and every HTML page on view.com.au sits behind DataDome bot protection that returns HTTP 403 to non-browser clients — yet it operates a completely public, unauthenticated Model Context Protocol server at https://mcp.view.com.au/mcp that returns live listing data to any anonymous agent. The human web is closed to machines while the agent surface is wide open. RESO plays
  no part here. RESO is a US National Association of REALTORS construct, and the RESO certified-organizations directory lists no Australian organizations at all.
examples:
- key_count: 6
  name: View Com Au Mcp Tool Calls
  slug: view-com-au-mcp-tool-calls
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/view-com-au.png
layout: provider
mcp_servers:
- description: ''
  name: View.com.au MCP server manifest
  slug: viewcomau-mcp-server-manifest
- description: ''
  name: tools/list, harvested verbatim
  slug: toolslist-harvested-verbatim
- description: ''
  name: initialize, harvested verbatim
  slug: initialize-harvested-verbatim
modified: '2026-07-26'
name: View.com.au
nav: Providers
network: true
overview: 'View.com.au publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Real Estate, Australia, Property Listings, Property Portal, and PropTech.


  View.com.au''s developer surface includes authentication, engineering blog, support, signup flow, and 18 more developer resources.'
random_paper: 16
rate_limits:
- limit_count: 1
  name: View Com Au Rate Limits
  slug: view-com-au-rate-limits
score:
  band: emerging
  composite: 22.2
  delta: 0.2
  facets:
    access_clarity: 34.2
    commercial_clarity: 34.2
    contract_governance: 4.5
    contract_quality: 0.0
    developer_ergonomics: 20.8
    discoverability: 75.9
    governance: 4.5
    operational_transparency: 23.7
  previous_composite: 22.0
  provenance:
    agentic_access: derived
    conformance: derived
    mcp: first-party
    skills: derived
  schema_version: 0.12.0
  scored_at: '2026-08-19'
  trend: flat
security:
- kind: authentication
  name: View Com Au Authentication
  slug: view-com-au-authentication
  summary_line: none · 1 scheme
- kind: domain-security
  name: View Com Au Domain Security
  slug: view-com-au-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: view-com-au
tags:
- Real Estate
- Australia
- Property Listings
- Property Portal
- PropTech
- Rentals
- Off-Market Property Data
- Model Context Protocol
- Agent-Native
website: https://view.com.au/
---
