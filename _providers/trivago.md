---
access_model:
  confidence: medium
  label: Requires approval
  onboarding: approval
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
    asyncapi_events: false
    auth_clarity: false
    consent_identity: true
    dry_run_mode: false
    error_semantics: false
    idempotency: false
    mcp_server: true
    openapi_examples: false
    rate_limit_signal: false
    spec_presence: false
    well_known_catalog: true
  schema_version: 0.2
  score: 17.1
  scored_at: '2026-07-28'
api_count: 1
apis:
- description: 'Public Model Context Protocol connector (search_hotels) plus an invite-only direct hotel-search API delivering live prices ranked by value, enriched property data, and destination price trends across '
  name: trivago Hotel Search (MCP + direct API)
  slug: trivago-hotel-search-mcp-direct-api
artifact_total: 4
common:
- group: company
  title: ''
  type: Website
  url: https://www.trivago.com/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://developer.trivago.com/
- group: docs
  title: ''
  type: Documentation
  url: https://developer.trivago.com/fastconnect/fast-connect-overview.html
- group: docs
  title: ''
  type: APIReference
  url: https://developer.trivago.com/fastconnect/api-updates.html
- group: start
  title: ''
  type: GettingStarted
  url: https://company.trivago.com/get-listed/
- group: start
  title: ''
  type: SignUp
  url: https://company.trivago.com/get-listed/booking-sites-contact
- group: operate
  title: ''
  type: Support
  url: https://support.trivago.com/hc/en-us
- group: company
  title: ''
  type: Blog
  url: https://businessblog.trivago.com/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/trivago
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.trivago.com/en-US/sp/privacy-policy
- group: auth
  title: ''
  type: Compliance
  url: https://www.trivago.com/en-US/sp/privacy-policy
- group: agent
  title: ''
  type: MCPServer
  url: mcp/trivago-mcp.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/trivago-llms.txt
- group: agent
  title: ''
  type: WellKnown
  url: well-known/trivago-well-known.yml
- group: auth
  title: ''
  type: SecurityTxt
  url: well-known/trivago-security.txt
- group: design
  title: ''
  type: Conformance
  url: conformance/trivago-conformance.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/trivago-domain-security.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/trivago-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: Security
  url: https://www.trivago.com/cyber-security
created: '2026-07-17'
description: 'trivago (trivago N.V.) is a global hotel and accommodation metasearch engine, founded in Düsseldorf, Germany in 2005, that aggregates prices, ratings, and reviews from 250+ booking sites across more than 7 million properties in 190 countries and 31 languages. trivago does not hold inventory — its role is to surface the full competitive market and connect travelers to the best available deal, including member, loyalty, and direct-hotel rates that individual booking platforms do not show by default. For programmatic access, trivago is AI-native: it publishes a public, no-auth Model Context Protocol (MCP) connector exposing a search_hotels tool, an invite-only direct hotel-search API, and a partner Connectivity Suite (FastConnect for real-time rates and availability, plus a Conversion Tracking API). It also operates trivago Hotel Manager (Business Studio) for hoteliers.'
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/trivago.png
layout: provider
mcp_servers:
- description: ''
  name: trivago-mcp.yml
  slug: trivago-mcpyml
modified: '2026-07-21'
name: Trivago
nav: Providers
network: true
overview: 'Trivago publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Travel, Hotels, Accommodation, and Metasearch.


  Trivago''s developer surface includes documentation, API reference, getting-started guide, signup flow, support, engineering blog, and 13 more developer resources.'
random_paper: 44
score:
  band: thin
  composite: 28.6
  delta: 1.0
  facets:
    commercial_clarity: 31.6
    contract_quality: 0.0
    developer_ergonomics: 50.0
    discoverability: 87.0
    governance: 12.5
    operational_transparency: 15.8
  previous_composite: 27.6
  provenance:
    conformance: first-party
    mcp: first-party
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: flat
security:
- kind: domain-security
  name: Trivago Domain Security
  slug: trivago-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Trivago Vulnerability Disclosure
  slug: trivago-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: trivago
tags:
- Company
- Travel
- Hotels
- Accommodation
- Metasearch
- Hotel Search
- Price Comparison
- Booking
- Hospitality
- MCP
- AI Agents
website: https://www.trivago.com/
---
