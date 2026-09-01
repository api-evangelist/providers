---
agent_readiness:
  band: human-only
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
    mcp_server: documented
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 3.5
  scored_at: '2026-09-01'
api_count: 0
artifact_total: 2
common:
- group: company
  title: ''
  type: Website
  url: https://www.newlight.com/
- group: other
  title: ''
  type: Company
  url: https://www.newlight.com/company
- group: operate
  title: ''
  type: Support
  url: https://www.newlight.com/contact
- group: operate
  title: ''
  type: FAQ
  url: https://www.newlight.com/faq
- group: company
  title: ''
  type: Careers
  url: https://www.newlight.com/careers-1
- group: company
  title: ''
  type: Press
  url: https://www.newlight.com/newlight-media
- group: commercial
  title: ''
  type: TermsOfService
  url: https://aircarbon.com/legal
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/Newlight-Technologies
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/newlight-technologies-llms.txt
- group: agent
  title: ''
  type: MCPServer
  url: mcp/newlight-technologies-mcp.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/newlight-technologies-domain-security.yml
coverage:
  checked: '2026-08-26'
  detail: 'Newlight Technologies manufactures AirCarbon biomaterial and sells resin and finished foodware/accessories — software is not the product, and there is no developer program to profile: api., developer., developers. and docs.newlight.com all return NXDOMAIN, the Wix marketing site and the Webflow aircarbon.com product site expose no reference or spec, and the company''s GitHub org holds only three unreleased Elixir Req plugins that consume OTHER vendors'' APIs (Acumatica, Amazon SP-API, Wix eCommerce) rather than publish one of its own.'
  evidence:
  - note: DNS NXDOMAIN
    status: 0
    url: https://api.newlight.com/
  - note: DNS NXDOMAIN
    status: 0
    url: https://developer.newlight.com/
  - status: 400
    url: https://www.newlight.com/openapi.json
  - status: 404
    url: https://aircarbon.com/openapi.json
  - status: 400
    url: https://www.newlight.com/.well-known/agent-card.json
  - status: 200
    url: https://www.newlight.com/llms.txt
  - note: anonymous POST tools/list returned 9 Wix platform Site MCP tools
    status: 200
    url: https://www.newlight.com/_api/mcp
  reason: not-a-software-company
  state: none
created: '2026-08-26'
description: 'Newlight Technologies, Inc. is a Huntington Beach, California biotechnology company founded in 2003 and incorporated in Delaware that produces AirCarbon, a PHB biomaterial made by naturally-occurring ocean microorganisms that consume air and greenhouse gas. The company operates a commercial-scale biomanufacturing plant and sells AirCarbon as resin to industrial partners and as finished goods under the Restore foodware and Covalent fashion-accessory brands, positioning the material as a carbon-negative, home-compostable, ocean-degradable replacement for petroleum plastic. Newlight is a materials manufacturer, not a software vendor: it publishes no developer program, no API reference and no machine-readable contract. Its only agent-reachable surface is the Wix platform Site MCP endpoint that its marketing site advertises in its own llms.txt.'
image: https://static.wixstatic.com/media/218375_ff4ad9528ae44cdd8a47215d9b4fd1da%7Emv2.jpg/v1/fit/w_2500,h_1330,al_c/218375_ff4ad9528ae44cdd8a47215d9b4fd1da%7Emv2.jpg
layout: provider
mcp_servers:
- description: ''
  name: Newlight Technologies MCP Server
  slug: newlight-technologies-mcp-server
modified: '2026-08-26'
name: Newlight Technologies
nav: Providers
network: true
overview: 'Newlight Technologies is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Biotechnology, Biomaterials, Materials Science, and Sustainability.


  Newlight Technologies'' developer surface includes support, FAQ, and 9 more developer resources.'
random_paper: 11
score:
  band: minimal
  composite: 9.1
  coverage:
    artifact_dirs: 4
    catalog_gap: 88.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 10.5
    commercial_clarity: 10.5
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 4.8
    discoverability: 57.4
    governance: 0.0
    operational_transparency: 2.6
  previous_composite: 9.1
  provenance:
    mcp: first-party
  schema_version: 0.17.2
  scored_at: '2026-09-01'
  trend: flat
security:
- kind: domain-security
  name: Newlight Technologies Domain Security
  slug: newlight-technologies-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: newlight-technologies
tags:
- Company
- Biotechnology
- Biomaterials
- Materials Science
- Sustainability
- Carbon Capture
- Manufacturing
- Bioplastics
- Climate Technology
- Consumer Products
website: https://www.newlight.com/
---
