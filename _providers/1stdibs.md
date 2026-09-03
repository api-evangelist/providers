---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source: []
  trial: false
  try_now: false
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    agentic_commerce: false
    auth_clarity: false
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: verified
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 8.6
  scored_at: '2026-09-03'
api_count: 1
apis:
- description: Official remote Model Context Protocol server (com.1stdibs/1stDibs) for browsing and searching luxury design items on the 1stDibs marketplace. Streamable-HTTP transport, API-key authentication.
  name: 1stDibs MCP Server
  slug: 1stdibs-mcp-server
artifact_total: 3
common:
- group: company
  title: ''
  type: Website
  url: https://www.1stdibs.com
- group: agent
  title: ''
  type: MCPServer
  url: mcp/1stdibs-mcp.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/1stdibs-llms.txt
- group: auth
  title: ''
  type: DomainSecurity
  url: security/1stdibs-domain-security.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/1stdibs
- group: operate
  title: ''
  type: Support
  url: https://support.1stdibs.com/hc/en-us/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.1stdibs.com/about/user-agreement/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.1stdibs.com/about/privacy-policy/
created: '2026-07-17'
description: 1stDibs is an online marketplace for luxury antiques, vintage and modern furniture, fine art, jewelry, watches, and fashion. It connects a global network of vetted sellers and design dealers with buyers seeking curated, authenticated high-end goods, backed by purchase-protection and authenticity guarantees. 1stDibs does not operate a public REST/OpenAPI developer program; its documented machine-facing surface is an official Model Context Protocol (MCP) server, registered as com.1stdibs/1stDibs, that lets agents browse and search the marketplace.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/1stdibs.png
layout: provider
mcp_servers:
- description: MCP server for browsing and searching items on 1stDibs marketplace.
  name: 1stDibs
  slug: 1stdibs
modified: '2026-07-17'
name: 1stdibs
nav: Providers
network: true
overview: '1stdibs publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Retail, Marketplace, Luxury Goods, and E-Commerce.


  1stdibs'' developer surface includes support and 7 more developer resources.'
random_paper: 5
score:
  band: emerging
  composite: 13.1
  coverage:
    artifact_dirs: 5
    catalog_gap: 78.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 21.1
    commercial_clarity: 21.1
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 4.8
    discoverability: 75.9
    governance: 0.0
    operational_transparency: 2.6
  previous_composite: 13.1
  provenance:
    mcp: first-party
  schema_version: 0.18.2
  scored_at: '2026-09-03'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/1stdibs/refs/heads/main/screenshots/1stdibs-2026-08-07T160656.png
security:
- kind: domain-security
  name: 1Stdibs Domain Security
  slug: 1stdibs-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: 1stdibs
tags:
- Company
- Retail
- Marketplace
- Luxury Goods
- E-Commerce
- Furniture
- Art
- Jewelry
- MCP
website: https://www.1stdibs.com
---
