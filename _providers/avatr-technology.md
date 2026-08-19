---
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    auth_clarity: false
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: verified
    openapi_examples: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 10.3
  scored_at: '2026-08-19'
api_count: 1
apis:
- description: Wix Site MCP endpoint served from the official AVATR Hong Kong site. Answers an anonymous JSON-RPC tools/list with 9 tools over the public marketing site (business details, in-site search, plus Wix do
  name: AVATR Hong Kong site MCP
  slug: avatr-hong-kong-site-mcp
artifact_total: 3
common:
- group: company
  title: ''
  type: Website
  url: https://www.avatr.com/en
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/avatr-technology-llms.txt
- group: agent
  title: ''
  type: MCPServer
  url: mcp/avatr-technology-mcp.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/avatr-technology-domain-security.yml
- group: company
  title: ''
  type: About
  url: https://www.avatr.com/en/about
- group: other
  title: ''
  type: Product
  url: https://www.avatr.com/en/11
- group: other
  title: ''
  type: Product
  url: https://www.avatr.com/en/12
- group: other
  title: ''
  type: Product
  url: https://www.avatr.com/en/06
- group: other
  title: ''
  type: Product
  url: https://www.avatr.com/en/07
- group: other
  title: ''
  type: Product
  url: https://www.avatr.com/en/chn
- group: other
  title: ''
  type: Design
  url: https://www.avatr.com/en/design
- group: company
  title: ''
  type: Newsroom
  url: https://www.avatr.com/newscenter
- group: operate
  title: ''
  type: Contact
  url: mailto:contactus@avatr.com
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.avatr.com/protocol?type=10181001
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.avatr.com/protocol?type=10181009
- group: other
  title: ''
  type: MobileApp
  url: https://www.avatr.com/en/download
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/%E9%98%BF%E7%BB%B4%E5%A1%94%E7%A7%91%E6%8A%80/
- group: company
  title: ''
  type: Instagram
  url: https://instagram.com/avatr_design
- group: other
  title: ''
  type: SecondaryMarket
  url: https://www.hiive.com/securities/avatr-technology-stock
created: '2026-08-06'
description: 'AVATR Technology (Chongqing) Co., Ltd. (阿维塔科技) is a Chinese premium intelligent electric-vehicle manufacturer headquartered in Chongqing, founded in 2018 as a joint venture in which Changan Automobile and CATL are the two largest shareholders and Huawei supplies the smart-cockpit and advanced driver-assistance stack. Its vehicles — the AVATR 11 and 12, the volume 06 and 07 (battery-electric and range-extended), and the limited 011 and 012 — are built on the jointly developed CHN smart-EV platform, a six-layer architecture spanning the mechanical, energy, electronic/electrical architecture, vehicle operating system, vehicle function application and cloud big-data layers. AVATR produced 73,606 vehicles in 2024 and sells through mainland China plus overseas markets including Hong Kong, Singapore, Thailand, Sri Lanka, the UAE and Qatar, with design and engineering offices in Shanghai and Munich. AVATR is a vehicle manufacturer, not a software vendor: www.avatr.com is a marketing
  and configurator site with no developer portal, no public API, no SDK and no machine-readable specification. The only live agent surface anywhere on an AVATR hostname is platform-provided — the official Hong Kong site runs on Wix and exposes the Wix Site MCP endpoint plus a Wix-generated llms.txt over its public marketing content.'
image: https://static.avatr.com/pc-website/favicon.ico
layout: provider
mcp_servers:
- description: ''
  name: avatr-technology-mcp.yml
  slug: avatr-technology-mcpyml
modified: '2026-08-06'
name: Avatr Technology
nav: Providers
network: true
overview: Avatr Technology publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Automotive, Electric Vehicles, Smart Cockpit, and Autonomous Driving.
random_paper: 32
score:
  band: emerging
  composite: 11.8
  delta: -1.8
  facets:
    access_clarity: 21.1
    commercial_clarity: 21.1
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 0.0
    discoverability: 75.9
    governance: 0.0
    operational_transparency: 0.0
  previous_composite: 13.6
  provenance:
    mcp: first-party
  schema_version: 0.12.0
  scored_at: '2026-08-19'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/avatr-technology/refs/heads/main/screenshots/avatr-technology-2026-08-07T162016.png
security:
- kind: domain-security
  name: Avatr Technology Domain Security
  slug: avatr-technology-domain-security
  summary_line: TLSv1.3 · HSTS
slug: avatr-technology
tags:
- Company
- Automotive
- Electric Vehicles
- Smart Cockpit
- Autonomous Driving
- Manufacturing
- China
- Consumer
website: https://www.avatr.com/en
---
