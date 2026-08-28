---
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: false
    agentic_commerce: platform
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: documented
    event_surface_described: false
    idempotency: documented
    mcp_server: verified
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 19.1
  scored_at: '2026-08-26'
api_count: 2
apis:
- description: Backcountry, a CSC Generation brand, publishes a Universal Commerce Protocol merchant profile at its own /.well-known/ucp declaring UCP 2026-01-23 with both REST and MCP transports for the shopping se
  name: Backcountry Agent Commerce (UCP)
  slug: backcountry-agent-commerce-ucp
- description: Seattle Coffee Gear, a CSC Generation brand, publishes a Universal Commerce Protocol merchant profile at /.well-known/ucp declaring UCP 2026-04-08 (Shopify-native) with MCP and embedded transports, pl
  name: Seattle Coffee Gear Agent Commerce (UCP)
  slug: seattle-coffee-gear-agent-commerce-ucp
artifact_total: 5
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/csc-generation-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.cscgeneration.com/
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/csc-generation/
- group: company
  title: ''
  type: Careers
  url: https://www.cscgeneration.com/careers
- group: other
  title: ''
  type: SecondaryMarket
  url: https://forgeglobal.com/csc-generation_stock/
- group: agent
  title: ''
  type: WellKnown
  url: well-known/csc-generation-well-known.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/csc-generation-mcp.yml
- group: build
  title: ''
  type: ToolCrosswalk
  url: mcp/csc-generation-tool-crosswalk.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/csc-generation-llms.txt
- group: design
  title: ''
  type: Conventions
  url: conventions/csc-generation-conventions.yml
- group: design
  title: ''
  type: Idempotency
  url: conventions/csc-generation-conventions.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/csc-generation-authentication.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/csc-generation-problem-types.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/csc-generation-conformance.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/csc-generation-lifecycle.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
created: '2026-08-01'
description: CSC Generation is an AI-native retail holding company that acquires overlooked store- and catalogue-based retailers and rebuilds them on Genesis, its agent-orchestrated operating platform. Genesis combines a Data Fabric — a Data Management Platform that ingests and normalizes data across every brand without replatforming, and a Data Intelligence Platform that turns it into decision-ready signals for operators and AI agents — with an automation engine, proprietary retail AI tools, and centralized shared services covering customer experience, supply chain, technology and compliance. The company powers 13 brands and more than $1B in revenue, including Backcountry, Competitive Cyclist, Steep & Cheap, MotoSport, BikeTiresDirect, Level Nine Sports, Sur La Table, One Kings Lane, Seattle Coffee Gear and Home Consignment Center, and operates from Chicago, Austin, Los Angeles, Toronto, Seattle and Salt Lake City. CSC Generation publishes no corporate developer API; its machine-readable
  surface is per-brand — portfolio storefronts advertise Universal Commerce Protocol (UCP) merchant profiles at /.well-known/ucp that point agents at MCP endpoints for catalog search, cart and checkout.
image: https://www.cscgeneration.com/lovable-uploads/eccc3cb7-1376-4c88-a582-2a4ca479b43e.png
layout: provider
mcp_servers:
- description: ''
  name: CSC Generation MCP Server
  slug: csc-generation-mcp-server
modified: '2026-08-01'
name: CSC Generation
nav: Providers
network: true
overview: 'CSC Generation publishes 2 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Retail, E-Commerce, Agent Commerce, and Artificial Intelligence.


  CSC Generation''s developer surface includes authentication and 15 more developer resources.'
random_paper: 19
score:
  band: emerging
  composite: 18.6
  delta: 6.1
  facets:
    access_clarity: 21.1
    commercial_clarity: 21.1
    contract_governance: 18.2
    contract_quality: 0.0
    developer_ergonomics: 23.2
    discoverability: 75.9
    governance: 18.2
    operational_transparency: 0.0
  previous_composite: 12.5
  provenance:
    conformance: first-party
    mcp: first-party
    skills: derived
  schema_version: 0.15.0
  scored_at: '2026-08-26'
  trend: rising
screenshot: https://raw.githubusercontent.com/api-evangelist/csc-generation/refs/heads/main/screenshots/csc-generation-2026-08-07T163939.png
security:
- kind: authentication
  name: Csc Generation Authentication
  slug: csc-generation-authentication
  summary_line: apiKey/agent-profile-handshake · 2 schemes
- kind: domain-security
  name: Csc Generation Domain Security
  slug: csc-generation-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: csc-generation
tags:
- Company
- Retail
- E-Commerce
- Agent Commerce
- Artificial Intelligence
- Universal Commerce Protocol
- MCP
- Holding Company
- Shopping
website: https://www.cscgeneration.com/
---
