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
    error_semantics: documented
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: partial
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 33.5
  scored_at: '2026-08-19'
agentic_access:
- acting_count: 6
  human_in_the_loop: 0
  name: Twentyci Agentic Access
  operation_count: 58
  slug: twentyci-agentic-access
  summary_line: 58 operations · 6 acting
api_count: 9
apis:
- description: The single documented authentication endpoint for TwentyAPI. Exchanges a TwentyCi-issued client_id, client_secret, username and password for a bearer access token and refresh token, which is then pres
  name: TwentyAPI OAuth Token API
  slug: twentyapi-oauth-token-api
- description: 'The core DOMUS property surface of TwentyAPI. Retrieves property information and detail by UPRN, recent sales and comparable properties for sale in the area, average property values and AVM valuation '
  name: TwentyAPI Properties API
  slug: twentyapi-properties-api
- description: Estate-agent and letting-agent benchmarking built on TwentyCi sales and rental data. Ranks brands by SSTC, new instructions, exchange, PIPA (percentage of initial price achieved) and days from new ins
  name: TwentyAPI Agent Performance API
  slug: twentyapi-agent-performance-api
- description: 'Home-mover event triggers - the transaction-lifecycle signals TwentyCi is built on. Retrieves a specific trigger, lists properties by trigger type (including properties with no UPRN), and returns the '
  name: TwentyAPI Trigger Information API
  slug: twentyapi-trigger-information-api
- description: Lists the attribute categories available for a property and returns a specific category, providing the vocabulary that the Properties API's attribute endpoints are organised around.
  name: TwentyAPI Categories API
  slug: twentyapi-categories-api
- description: Partial address matching. Submits a fragmentary or unstructured UK address to a match-address process and resolves it against TwentyCi's addressing layer, the capability marketed as AddressMaster / In
  name: TwentyAPI Address Match API
  slug: twentyapi-address-match-api
- description: Returns nearby schools for a given UK postcode, one of the neighbourhood-context datasets TwentyCi layers onto a property record.
  name: TwentyAPI Schools API
  slug: twentyapi-schools-api
- description: Aggregate UK housing market metrics for a specified timeframe - new instructions, SSTCs (sold subject to contract) and PCDs (predicted to complete date) - the market-level view behind TwentyCi's publi
  name: TwentyAPI UK Housing Market Metrics API
  slug: twentyapi-uk-housing-market-metrics-api
- description: '"This is Now" retail propensity to buy goods. Local and national search endpoints returning consumer propensity signal derived from home-mover events, aimed at retailers and media agencies targeting p'
  name: TwentyAPI This is Now API
  slug: twentyapi-this-is-now-api
artifact_total: 16
collections:
- collection_type: open
  name: TwentyAPI (TwentyCi) OAuth 2.0 Token API
  slug: open-twentyci-twentyapi-oauth
- collection_type: open
  name: TwentyAPI (TwentyCi) v2
  slug: open-twentyci-twentyapi
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/twentyci-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/twentyci-domain-security.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/twentyci-scopes.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/twentyci-authentication.yml
- group: design
  title: ''
  type: Vocabulary
  url: vocabulary/twentyci-vocabulary.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/twentyci-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/twentyci-problem-types.yml
- group: build
  title: ''
  type: Examples
  url: examples/twentyci-examples.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/twentyci-data-model.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/twentyci-lifecycle.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/twentyci-conformance.yml
- group: auth
  title: ''
  type: Compliance
  url: https://www.twentyci.co.uk/privacy-policy/
- group: build
  title: ''
  type: Packages
  url: packages/twentyci-packages.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/twentyci-mcp.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/twentyci-llms.txt
- group: other
  title: ''
  type: Overlay
  url: overlays/twentyci-twentyapi-overlay.yaml
- group: other
  title: ''
  type: Overlay
  url: overlays/twentyci-twentyapi-oauth-overlay.yaml
- group: company
  title: ''
  type: Website
  url: https://www.twentyci.co.uk/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://api.twentyci.co.uk/documentation
- group: docs
  title: ''
  type: Documentation
  url: https://api.twentyci.co.uk/documentation
- group: docs
  title: ''
  type: APIReference
  url: https://api.twentyci.co.uk/documentation#properties
- group: start
  title: ''
  type: GettingStarted
  url: https://api.twentyci.co.uk/documentation#overview
- group: operate
  title: ''
  type: Contact
  url: https://www.twentyci.co.uk/contact/
- group: company
  title: ''
  type: About
  url: https://www.twentyci.co.uk/about-us/
- group: company
  title: ''
  type: Blog
  url: https://news.twentyci.co.uk/blog
- group: company
  title: ''
  type: BlogRSS
  url: https://www.twentyci.co.uk/feed/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.twentyci.co.uk/privacy-policy/
- group: other
  title: ''
  type: CookiePolicy
  url: https://www.twentyci.co.uk/cookies-policy/
- group: other
  title: ''
  type: SustainabilityPolicy
  url: https://www.twentyci.co.uk/sustainability-policy/
- group: company
  title: ''
  type: Careers
  url: https://www.twentyci.co.uk/careers/
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/twentyci/
- group: company
  title: ''
  type: Twitter
  url: https://twitter.com/TwentyCi
- group: company
  title: ''
  type: Facebook
  url: https://www.facebook.com/TwentyCi
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/twentyci
created: '2026-07-26'
description: TwentyCi is a United Kingdom residential property data and home-mover intelligence company. It aggregates roughly 31.5 million UK addresses and tens of billions of data points from hundreds of primary sources into the DOMUS property database, and sells that data to estate agents, lenders, insurers, conveyancers, house builders, retailers and media agencies through the TwentyCi, TwentyEA and TwentyConvey brands. In the UK value chain it sits on the data-supply side rather than the listing side - there is no UK MLS, listings are controlled by the Rightmove and Zoopla portals, and TwentyCi is one of the private aggregators that resells transaction, valuation and home-mover signal on top of that closed market. Its API posture is honest but commercial - TwentyAPI is a genuine RESTful v2 API at https://api.twentyci.co.uk/api/v2 with a live, publicly readable documentation portal covering roughly 57 documented operations across properties, AVM valuation, transaction triggers, agent
  performance, address matching, schools, housing market metrics and retail propensity - but every endpoint returns 401 without a TwentyCi-issued OAuth 2.0 bearer token, there is no self-serve signup, no published pricing, and the specification download TwentyCi advertises at https://api.twentyci.co.uk/docs/v2/spec.json returns HTTP 404. Access is sales-led and partner-only. RESO is entirely absent - the UK has no MLS or RESO regime and TwentyCi identifies property by UPRN, the Ordnance Survey/GeoPlace Unique Property Reference Number, rather than by any RESO Universal Property Identifier.
image: https://www.twentyci.co.uk/favicon.ico
layout: provider
mcp_servers:
- description: ''
  name: twentyci-mcp.yml
  slug: twentyci-mcpyml
modified: '2026-07-26'
name: TwentyCi
nav: Providers
network: true
overview: 'TwentyCi publishes 9 APIs on the [APIs.io](https://apis.io/) network, including TwentyAPI OAuth Token API, TwentyAPI Properties API, TwentyAPI Agent Performance API, and 6 more. Tagged areas include Real Estate, United Kingdom, PropTech, Property Data, and Valuation.


  TwentyCi''s developer surface includes authentication, code examples, documentation, API reference, getting-started guide, engineering blog, and 29 more developer resources.'
random_paper: 142
scopes:
- name: Twentyci Scopes
  scope_count: 1
  slug: twentyci-scopes
  summary_line: 1 scope · password
score:
  band: thin
  composite: 32.0
  delta: 1.7
  facets:
    access_clarity: 18.4
    commercial_clarity: 18.4
    contract_governance: 45.5
    contract_quality: 14.1
    developer_ergonomics: 54.2
    discoverability: 81.5
    governance: 45.5
    operational_transparency: 2.6
  previous_composite: 30.3
  provenance:
    agentic_access: derived
    conformance: first-party
    contracts:
      callable: 100.0
      derived: 2
      marker_coverage: 100.0
      total: 2
    mcp: derived
    skills: derived
  schema_version: 0.12.0
  scored_at: '2026-08-19'
  trend: flat
security:
- kind: authentication
  name: Twentyci Authentication
  slug: twentyci-authentication
  summary_line: oauth2 · 1 scheme
- kind: domain-security
  name: Twentyci Domain Security
  slug: twentyci-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: twentyci
tags:
- Real Estate
- United Kingdom
- PropTech
- Property Data
- Valuation
- AVM
- Rentals
- Address Data
- Conveyancing
- Homemover Data
- Agent Performance
- Data as a Service
website: https://www.twentyci.co.uk/
---
