---
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    agentic_commerce: false
    auth_clarity: bearer
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
  score: 11.2
  scored_at: '2026-09-01'
api_count: 1
apis:
- description: An anonymous Model Context Protocol endpoint served from Calviri's own host at https://www.calviri.com/_api/mcp. It is the standard Wix "Site Visitor Assistant" server that the Wix platform provisions
  name: Calviri Site MCP
  slug: calviri-site-mcp
artifact_total: 4
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/calviri-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.calviri.com/
- group: company
  title: ''
  type: About
  url: https://www.calviri.com/about-us
- group: company
  title: ''
  type: Newsroom
  url: https://www.calviri.com/newsroom
- group: company
  title: ''
  type: Careers
  url: https://www.calviri.com/careers
- group: company
  title: ''
  type: InvestorRelations
  url: https://www.calviri.com/investor-relations
- group: other
  title: ''
  type: Products
  url: https://www.calviri.com/ourproducts
- group: other
  title: ''
  type: Science
  url: https://www.calviri.com/our-science
- group: other
  title: ''
  type: Email
  url: mailto:info@calviri.com
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/calviri
- group: learn
  title: ''
  type: YouTube
  url: https://www.youtube.com/channel/UCQF7bNAdJWrIYyhNO7RNaKg
- group: company
  title: ''
  type: Twitter
  url: https://x.com/CalviriSciences
- group: other
  title: ''
  type: SecondaryMarket
  url: https://forgeglobal.com/calviri_stock/
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/calviri-llms.txt
- group: agent
  title: ''
  type: MCPServer
  url: mcp/calviri-mcp.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/calviri-authentication.yml
created: '2026-08-09'
description: Calviri is a Phoenix, Arizona biotechnology company, founded in 2017, that develops multi-cancer diagnostic tests and therapeutic and preventative cancer vaccines for dogs and people. Its science rests on RNA-Error Derived Neoantigens (REDNs) — abnormal proteins thrown off by the error-prone RNA processing of tumor cells — which Calviri builds as peptides on semiconductor chips and then queries against an individual's blood for antibody responses, using those antibodies as sensitive biomarkers of cancer. Its lead product, StageOne Plus, is a canine multi-cancer blood test designed to detect stage 1 disease before signs appear, alongside a pipeline of canine and human therapeutic and preventative vaccines and a preventative-vaccine trial (VACCS) that enrolled 800+ dogs. Calviri is a life-sciences company with no developer program, no product API and no developer portal; the only machine-readable surface on calviri.com is the Wix-platform-generated llms.txt and the anonymous site
  MCP endpoint it advertises.
image: https://static.wixstatic.com/media/0c6e92_2823fb63b9514e718b52ff84460faf97~mv2.png/v1/fill/w_192,h_192,lg_1,usm_0.66_1.00_0.01/0c6e92_2823fb63b9514e718b52ff84460faf97~mv2.png
layout: provider
mcp_servers:
- description: Calviri serves a live, anonymous Model Context Protocol endpoint from its own host at https://www.calviri.com/_api/mcp. The endpoint is PLATFORM-PROVIDED by Wix (calviri.com is a Wix site) rather than
  name: Calviri MCP Server
  slug: calviri-mcp-server
modified: '2026-08-09'
name: Calviri
nav: Providers
network: true
overview: 'Calviri publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Biotechnology, Life Sciences, Health, and Cancer Diagnostics.


  Calviri''s developer surface includes YouTube channel, authentication, and 14 more developer resources.'
random_paper: 11
score:
  band: minimal
  composite: 9.4
  coverage:
    artifact_dirs: 5
    catalog_gap: 78.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 0.0
    commercial_clarity: 0.0
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 11.9
    discoverability: 75.9
    governance: 0.0
    operational_transparency: 0.0
  previous_composite: 9.4
  provenance:
    mcp: first-party
  regulatory:
    applies: true
    matched_via: tags
    regime: Health
    regime_id: health
    score: 15.0
  schema_version: 0.18.0
  scored_at: '2026-09-01'
  trend: flat
security:
- kind: authentication
  name: Calviri Authentication
  slug: calviri-authentication
  summary_line: 0 schemes
- kind: domain-security
  name: Calviri Domain Security
  slug: calviri-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: calviri
tags:
- Company
- Biotechnology
- Life Sciences
- Health
- Cancer Diagnostics
- Vaccines
- Veterinary
- Animal Health
- Research
website: https://www.calviri.com/
---
