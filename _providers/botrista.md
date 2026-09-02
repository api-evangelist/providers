---
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
    well_known_catalog: true
  schema_version: 0.2
  score: 11.5
  scored_at: '2026-09-01'
api_count: 1
apis:
- description: The Model Context Protocol endpoint served on Botrista's Wix-hosted content site (botrista.info). It is a platform-provided site MCP — supplied by the Wix website builder rather than authored by Botri
  name: Botrista Site MCP
  slug: site-mcp
artifact_total: 3
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/botrista-domain-security.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/botrista-mcp.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/botrista-llms.txt
- group: design
  title: ''
  type: Conformance
  url: conformance/botrista-conformance.yml
- group: company
  title: ''
  type: Website
  url: https://botrista.com/
- group: company
  title: ''
  type: Blog
  url: https://www.botrista.info/blog
- group: company
  title: ''
  type: BlogRSS
  url: https://www.botrista.info/blog-feed.xml
- group: operate
  title: ''
  type: Support
  url: https://botrista.com/frequently-asked-questions/
- group: start
  title: ''
  type: Login
  url: https://cloudbar.botrista.io/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://botrista.com/terms-of-service/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://botrista.com/privacy-policy/
- group: other
  title: ''
  type: Resources
  url: https://botrista.com/resources/
- group: company
  title: ''
  type: Jobs
  url: https://botrista.com/careers/jobs/
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/botrista
- group: company
  title: ''
  type: CrunchBase
  url: https://www.crunchbase.com/organization/botrista-technology-inc
- group: other
  title: ''
  type: SecondaryMarket
  url: https://forgeglobal.com/botrista_stock/
created: '2026-08-02'
description: 'Botrista, Inc. is a San Francisco based beverage-automation company founded in 2017 that builds the DrinkBot robotic beverage dispenser and the CloudBar cloud platform behind it. The DrinkBot automates craft beverages — infused teas, flavored lemonades, iced coffees and mocktails — dispensing a drink in roughly twenty seconds from a touchscreen order, and every unit is internet connected so it pulls recipes, reports consumption, tracks ingredient levels and pushes maintenance alerts back to Botrista. CloudBar is the operator-facing web application used by restaurant, campus dining, convenience and theme-park operators to manage recipes, inventory replenishment and sales/menu performance analytics across a fleet of machines, alongside a separate Botrista Data Portal. Botrista sells beverage automation as a service rather than as a developer platform: as of this profiling pass it publishes no public developer portal, no API reference and no machine-readable API contract, and
  POS integrations are handled case-by-case through its commercial team.'
image: https://static.wixstatic.com/media/3e2957_4cab0c5391c3485993af28df133a1162%7Emv2.jpg/v1/fit/w_2500,h_1330,al_c/3e2957_4cab0c5391c3485993af28df133a1162%7Emv2.jpg
layout: provider
mcp_servers:
- description: ''
  name: Botrista MCP Server
  slug: botrista-mcp-server
modified: '2026-08-02'
name: Botrista
nav: Providers
network: true
overview: 'Botrista publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Robotics, Beverage, Food Service, and Automation.


  Botrista''s developer surface includes engineering blog, support, and 14 more developer resources.'
random_paper: 11
score:
  band: emerging
  composite: 11.6
  coverage:
    artifact_dirs: 8
    catalog_gap: 78.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 6.6
    commercial_clarity: 6.6
    contract_governance: 18.2
    contract_quality: 0.0
    developer_ergonomics: 2.4
    discoverability: 75.9
    governance: 18.2
    operational_transparency: 0.0
  previous_composite: 11.6
  provenance:
    conformance: first-party
    mcp: first-party
  schema_version: 0.18.0
  scored_at: '2026-09-01'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/botrista/refs/heads/main/screenshots/botrista-2026-08-07T162727.png
security:
- kind: domain-security
  name: Botrista Domain Security
  slug: botrista-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
slug: botrista
tags:
- Company
- Robotics
- Beverage
- Food Service
- Automation
- Restaurant Technology
- IoT
- Hardware
website: https://botrista.com/
---
