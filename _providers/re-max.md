---
access_model:
  confidence: high
  label: Partner-only · Franchise/vendor credentials required
  onboarding: unknown
  pricing: unknown
  public: false
  source:
  - collections
  - authentication
  trial: false
  try_now: false
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: false
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: documented
    event_surface_described: false
    idempotency: false
    mcp_server: true
    openapi_examples: false
    rate_limit_signal: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 24.5
  scored_at: '2026-08-11'
api_count: 3
apis:
- description: The RE/MAX Europe Datahub API is the franchise-operations API behind the RE/MAX EU Datahub application. It exposes offices, persons, RE/MAX Titles (the agent/broker role records), teams, regions and m
  name: RE/MAX Europe Datahub API
  slug: re-max-eu-datahub-api
- description: The RE/MAX Europe Listings API is used in conjunction with the RE/MAX EU Datahub application to add, update, retrieve and delete property listing data and listing images across RE/MAX European regions
  name: RE/MAX Europe Listings API
  slug: re-max-eu-listings-api
- description: The RE/MAX Europe marketing site at remax.eu runs WordPress and exposes the WordPress REST API anonymously at /wp-json/. The route descriptor published there is the only self-describing, machine-reada
  name: RE/MAX Europe Site API (WordPress REST)
  slug: re-max-eu-site-api
artifact_total: 6
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/re-max-domain-security.yml
- group: start
  title: ''
  type: DeveloperPortal
  url: https://apidocs.datahub.remax.eu/
- group: build
  title: ''
  type: Postman
  url: https://apidocs.datahub.remax.eu/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.remax.eu/privacy-policy/
- group: auth
  title: ''
  type: Authentication
  url: authentication/re-max-authentication.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/re-max-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/re-max-error-codes.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/re-max-lifecycle.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/re-max-conformance.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/re-max-data-model.yml
- group: build
  title: ''
  type: Packages
  url: packages/re-max-packages.yml
- group: start
  title: ''
  type: Sandbox
  url: sandbox/re-max-sandbox.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/re-max-mcp.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/re-max-well-known.yml
- group: other
  title: ''
  type: APICatalog
  url: well-known/re-max-eu-wp-json.json
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/re-max-llms.txt
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/re-max-eu-site-llms.txt
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: company
  title: ''
  type: Website
  url: https://www.remax.com/
- group: company
  title: ''
  type: Website
  url: https://www.remax.eu/
- group: company
  title: ''
  type: Blog
  url: https://news.remax.com/
- group: company
  title: ''
  type: InvestorRelations
  url: https://investors.remaxholdings.com/
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/remax
- group: docs
  title: ''
  type: Documentation
  url: https://apidocs.datahub.remax.eu/
- group: auth
  title: ''
  type: Authentication
  url: https://oauth.datahub.remax.eu/token
created: '2026-07-26'
description: 'RE/MAX Holdings, Inc. (NYSE: RMAX, SIC 6531, Denver, Colorado) is one of the world''s largest real estate brokerage franchisors, licensing the RE/MAX brand to independently owned and operated brokerages across more than 110 countries and territories, and franchising mortgage brokerages in the United States under the Motto Mortgage brand with loan processing through wemlo. Its home market is the United States, where it sits in the value chain as a franchisor and consumer portal operator rather than as a data owner: the listing content behind remax.com is licensed from roughly 500 local Multiple Listing Services under IDX and syndication agreements, so RE/MAX is a consumer of MLS data, not a publisher of it. Its API posture reflects that position honestly. RE/MAX is a RESO Class D member (Brokers, Agents and Appraisers) and holds a seat on the RESO Board of Directors, but it does not appear in the RESO certification directory of certified data providers and publishes no RESO
  Web API, no OData $metadata document and no Universal Property Identifier surface. In the United States there is no developer portal, no published API program and no machine-readable contract of any kind; developer.remax.com, developers.remax.com and docs.remax.com are only wildcard DNS entries pointing at the kvCORE agent website platform, and api.remax.com is a dangling CNAME to a decommissioned booj host that no longer resolves. The only real, publicly documented RE/MAX API surface belongs to RE/MAX Europe, whose Datahub franchise-operations API and Listings API are published as public Postman documentation with OAuth 2.0 authentication, but whose credentials are issued only to RE/MAX regional master franchisees, offices and their vendors — documented, but not self-serve. The only anonymously callable, self-describing RE/MAX endpoint family found anywhere in the estate is the WordPress REST API on the RE/MAX Europe marketing site (remax.eu/wp-json, 42 namespaces and 791 routes), which
  also exposes an auth-gated Model Context Protocol endpoint via the WordPress MCP Adapter — a CMS surface rather than an API product, but the closest thing to agent-accessible RE/MAX infrastructure that exists today.'
image: https://remax.eu/wp-content/uploads/2026/03/REMAX-Balloon-RGB.svg
layout: provider
mcp_servers:
- description: ''
  name: re-max-mcp.yml
  slug: re-max-mcpyml
modified: '2026-07-26'
name: RE/MAX
nav: Providers
network: true
overview: 'RE/MAX publishes 2 APIs on the [APIs.io](https://apis.io/) network: Europe Datahub API and Europe Listings API. Tagged areas include Real Estate, United States, Brokerage, Property Listings, and MLS.


  RE/MAX''s developer surface includes authentication, sandbox, engineering blog, documentation, and 21 more developer resources.'
random_paper: 6
score:
  band: emerging
  composite: 25.0
  delta: 0.0
  facets:
    commercial_clarity: 10.5
    contract_quality: 0.0
    developer_ergonomics: 51.6
    discoverability: 92.6
    governance: 12.5
    operational_transparency: 0.0
  previous_composite: 25.0
  provenance:
    conformance: first-party
    mcp: first-party
    skills: derived
  regulatory:
    applies: true
    matched_via: weak_tags
    regime: Securities & Market Data
    regime_id: securities_market_data
    score: 35.0
  schema_version: 0.11.0
  scored_at: '2026-08-11'
  trend: flat
security:
- kind: authentication
  name: Re Max Authentication
  slug: re-max-authentication
  summary_line: oauth2 · 3 schemes
- kind: domain-security
  name: Re Max Domain Security
  slug: re-max-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: re-max
tags:
- Real Estate
- United States
- Brokerage
- Property Listings
- MLS
- RESO
- IDX
- PropTech
- Franchising
- Mortgage
- Rentals
website: https://www.remax.com/
---
