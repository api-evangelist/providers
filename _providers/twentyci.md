---
access_model:
  confidence: low
  label: Self-serve signup
  onboarding: self-serve
  pricing: unknown
  public: false
  source:
  - authentication
  - security
  trial: false
  try_now: false
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: documented
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: partial
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 23.6
  scored_at: '2026-09-03'
agentic_access:
- acting_count: 6
  human_in_the_loop: 0
  name: Twentyci Agentic Access
  operation_count: 58
  slug: twentyci-agentic-access
  summary_line: 58 operations · 6 acting
api_count: 2
apis:
- baseURL: https://api.twentyci.co.uk
  baseurl_source: declared
  description: '- Partial Address Matching'
  name: TwentyCi Address Match API
  slug: twentyci-address-match-api
- baseURL: https://api.twentyci.co.uk
  baseurl_source: declared
  description: '- Agent Performance based on Sales Data - Agent Performance based on Rental Data'
  name: TwentyCi Agent Performance API
  slug: twentyci-agent-performance-api
- baseURL: https://api.twentyci.co.uk
  baseurl_source: declared
  description: Bearer-token issuance for TwentyAPI.
  name: TwentyCi Authorisation API
  slug: twentyci-authorisation-api
- baseURL: https://api.twentyci.co.uk
  baseurl_source: declared
  description: '- Obtain a List of Categories for a Property - Obtain a Specific Categories for a Property'
  name: TwentyCi Categories API
  slug: twentyci-categories-api
- baseURL: https://api.twentyci.co.uk
  baseurl_source: declared
  description: '- Property Information by Pagination - Properties Information by UPRN - Properties Details by UPRN - Recent Property Sales in the Area - Similar properties for sale in the area - Average Property Valu'
  name: TwentyCi Properties API
  slug: twentyci-properties-api
- baseURL: https://api.twentyci.co.uk
  baseurl_source: declared
  description: '- Nearby Schools by Postcode'
  name: TwentyCi Schools API
  slug: twentyci-schools-api
- baseURL: https://api.twentyci.co.uk
  baseurl_source: declared
  description: '- Local Search - National Search'
  name: TwentyCi This is Now | Retail Propensity To Buy Goods API
  slug: twentyci-this-is-now-retail-propensity-to-buy-goods-api
- baseURL: https://api.twentyci.co.uk
  baseurl_source: declared
  description: '- Obtain a Specific Trigger - Get Properties by Trigger Type - Get no UPRN Properties by Trigger Type - Trigger History'
  name: TwentyCi Trigger Information API
  slug: twentyci-trigger-information-api
- baseURL: https://api.twentyci.co.uk
  baseurl_source: declared
  description: '- New Instructions, SSTC''s and PCD''s for a Specific Timeframe'
  name: TwentyCi UK Housing Market Metrics API
  slug: twentyci-uk-housing-market-metrics-api
artifact_total: 15
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
  type: X-MCPServerCandidate
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
modified: '2026-07-26'
name: TwentyCi
nav: Providers
network: true
overview: 'TwentyCi publishes 9 APIs on the [APIs.io](https://apis.io/) network, including Address Match API, Agent Performance API, Authorisation API, and 6 more. Tagged areas include Real-Estate, United Kingdom, PropTech, Property Data, and Valuation.


  TwentyCi''s developer surface includes authentication, code examples, documentation, API reference, getting-started guide, engineering blog, and 29 more developer resources.'
random_paper: 5
scopes:
- name: Twentyci Scopes
  scope_count: 1
  slug: twentyci-scopes
  summary_line: 1 scope · password
score:
  band: thin
  composite: 30.5
  coverage:
    artifact_dirs: 21
    catalog_gap: 73.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 18.4
    commercial_clarity: 18.4
    contract_governance: 33.3
    contract_quality: 16.4
    developer_ergonomics: 54.2
    discoverability: 75.9
    governance: 33.3
    operational_transparency: 2.6
  previous_composite: 30.5
  provenance:
    agentic_access: derived
    conformance: first-party
    contracts:
      callable: 100.0
      derived: 9
      marker_coverage: 100.0
      total: 9
    mcp: derived
    skills: derived
  schema_version: 0.18.2
  scored_at: '2026-09-03'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/twentyci/refs/heads/main/screenshots/twentyci-2026-09-02T164620.png
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
- Real-Estate
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
