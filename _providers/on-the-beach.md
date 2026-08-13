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
    mcp_server: true
    openapi_examples: false
    rate_limit_signal: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 10.8
  scored_at: '2026-08-12'
api_count: 0
artifact_total: 2
common:
- group: agent
  title: ''
  type: MCPServer
  url: mcp/on-the-beach-mcp.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/on-the-beach-well-known.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/on-the-beach-llms.txt
- group: build
  title: ''
  type: Packages
  url: packages/on-the-beach-packages.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/on-the-beach-domain-security.yml
- group: operate
  title: ''
  type: Support
  url: https://help.onthebeach.co.uk/hc/en-gb
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.onthebeach.co.uk/terms-and-conditions
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.onthebeach.co.uk/privacy
- group: other
  title: ''
  type: AffiliateProgram
  url: https://www.onthebeach.co.uk/affiliates
- group: company
  title: ''
  type: Website
  url: https://www.onthebeachgroupplc.com/
- group: company
  title: ''
  type: ConsumerWebsite
  url: https://www.onthebeach.co.uk/
- group: company
  title: ''
  type: About
  url: https://www.onthebeachgroupplc.com/about-us/who-we-are
- group: other
  title: ''
  type: Strategy
  url: https://www.onthebeachgroupplc.com/about-us/strategy
- group: company
  title: ''
  type: InvestorRelations
  url: https://www.onthebeachgroupplc.com/investor-centre
- group: other
  title: ''
  type: AnnualReport
  url: https://www.onthebeachgroupplc.com/~/media/Files/O/On-The-Beach/investor-docs/results-and-presentations/on-the-beach-group-final-results-2025.pdf
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/onthebeach
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/on-the-beach
- group: operate
  title: ''
  type: Contact
  url: https://www.onthebeachgroupplc.com/contact
created: '2026-07-28'
description: 'On the Beach Group plc (LSE: OTB) is a Manchester-headquartered online travel agent and the United Kingdom''s largest online short-haul beach package holiday specialist, founded in 2004 by Simon Cooper and registered at Aeroworks, 5 Adair Street, Manchester M1 2NQ. It sits on the demand side of the travel distribution chain: an asset-light dynamic packager that buys real-time seats from 42 airlines and hotel inventory from bedbanks and direct hotel contracts, combines them into ATOL-protected packages, and sells them direct to UK and Republic of Ireland consumers through onthebeach.co.uk, sunshine.co.uk and its mobile app. FY25 total transaction value was GBP 1.25bn across 1.7 million customers. It is a consumer of other operators'' distribution APIs rather than a publisher of its own - it was the first UK OTA to take a direct NDC connection to Emirates'' Online B2B API in 2019 and signed a direct Ryanair "Approved OTA" partnership in 2024 - and it explicitly bypasses the GDS
  layer entirely. Its API posture as a producer is almost non-existent. The FY25 results describe an "API-first microservices architecture" and a proprietary Hotel Discovery Cache managing more than 5 billion hotel prices, but none of that surface is published: there is no developer portal, no API documentation, no OpenAPI or other machine-readable contract, no partner or trade API, and no self-serve access of any kind. Its only remaining B2B channel, Classic Collection, was put into orderly wind-down on 23 September 2025. The single exception, and the first externally addressable machine surface the company has ever shipped, is a ChatGPT App launched on 1 April 2026 - claimed as the first by a UK OTA - which serves live, bookable package combinations to ChatGPT users over MCP. That surface is distribution-gated rather than developer-facing: no endpoint, tool list, schema, auth flow or terms are documented, and a deliberate mcp.onthebeach.co.uk host exists but is Cloudflare WAF-blocked to
  every probe.'
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/apis-json-logo.jpg
layout: provider
mcp_servers:
- description: ''
  name: On the Beach ChatGPT App (MCP, distribution-gated)
  slug: on-the-beach-chatgpt-app-mcp-distribution-gated
modified: '2026-07-28'
name: On the Beach
nav: Providers
network: true
overview: 'On the Beach is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Travel, United Kingdom, OTA, Online Travel Agency, and Booking.


  On the Beach''s developer surface includes support and 17 more developer resources.'
random_paper: 51
score:
  band: emerging
  composite: 13.2
  delta: 0.0
  facets:
    commercial_clarity: 21.1
    contract_quality: 0.0
    developer_ergonomics: 13.0
    discoverability: 57.4
    governance: 0.0
    operational_transparency: 5.3
  previous_composite: 13.2
  provenance:
    mcp: first-party
  schema_version: 0.11.0
  scored_at: '2026-08-12'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/on-the-beach/refs/heads/main/screenshots/on-the-beach-2026-08-07T190211.png
security:
- kind: domain-security
  name: On The Beach Domain Security
  slug: on-the-beach-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: on-the-beach
tags:
- Travel
- United Kingdom
- OTA
- Online Travel Agency
- Booking
- Package Holidays
- Aviation
- Airline
- Distribution
- NDC
- Hotels
- Hospitality
- MCP
- Artificial Intelligence
website: https://www.onthebeachgroupplc.com/
---
