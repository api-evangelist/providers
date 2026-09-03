---
access_model:
  confidence: medium
  label: Self-serve signup
  onboarding: self-serve
  pricing: unknown
  public: false
  source:
  - authentication
  - scopes
  - security
  trial: false
  try_now: false
agent_readiness:
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: served
    consent_identity: false
    delegated_identity: served
    dry_run_mode: false
    dynamic_client_registration: true
    error_semantics: documented
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 35.4
  scored_at: '2026-09-03'
agentic_access:
- acting_count: 38
  human_in_the_loop: 1
  name: Ki Insurance Agentic Access
  operation_count: 109
  slug: ki-insurance-agentic-access
  summary_line: 109 operations · 38 acting · 1 human-in-the-loop
api_count: 1
apis:
- baseURL: https://app.ki-insurance.com
  baseurl_source: declared
  description: The Administration API from Ki Insurance — 4 operation(s) for administration.
  name: Ki Insurance Administration API
  slug: ki-insurance-administration-api
- baseURL: https://app.ki-insurance.com
  baseurl_source: declared
  description: The Broking Houses API from Ki Insurance — 5 operation(s) for broking houses.
  name: Ki Insurance Broking Houses API
  slug: ki-insurance-broking-houses-api
- baseURL: https://app.ki-insurance.com
  baseurl_source: declared
  description: The Classes of Business API from Ki Insurance — 1 operation(s) for classes of business.
  name: Ki Insurance Classes of Business API
  slug: ki-insurance-classes-of-business-api
- baseURL: https://app.ki-insurance.com
  baseurl_source: declared
  description: The Configuration API from Ki Insurance — 1 operation(s) for configuration.
  name: Ki Insurance Configuration API
  slug: ki-insurance-configuration-api
- baseURL: https://app.ki-insurance.com
  baseurl_source: declared
  description: The Dashboard API from Ki Insurance — 2 operation(s) for dashboard.
  name: Ki Insurance Dashboard API
  slug: ki-insurance-dashboard-api
- baseURL: https://app.ki-insurance.com
  baseurl_source: declared
  description: The Facilities API from Ki Insurance — 4 operation(s) for facilities.
  name: Ki Insurance Facilities API
  slug: ki-insurance-facilities-api
- baseURL: https://app.ki-insurance.com
  baseurl_source: declared
  description: The Indications API from Ki Insurance — 2 operation(s) for indications.
  name: Ki Insurance Indications API
  slug: ki-insurance-indications-api
- baseURL: https://app.ki-insurance.com
  baseurl_source: declared
  description: The Leads API from Ki Insurance — 3 operation(s) for leads.
  name: Ki Insurance Leads API
  slug: ki-insurance-leads-api
- baseURL: https://app.ki-insurance.com
  baseurl_source: declared
  description: The Market Leaders API from Ki Insurance — 4 operation(s) for market leaders.
  name: Ki Insurance Market Leaders API
  slug: ki-insurance-market-leaders-api
- baseURL: https://app.ki-insurance.com
  baseurl_source: declared
  description: The Master Data API from Ki Insurance — 39 operation(s) for master data.
  name: Ki Insurance Master Data API
  slug: ki-insurance-master-data-api
- baseURL: https://app.ki-insurance.com
  baseurl_source: declared
  description: The Pipeline API from Ki Insurance — 2 operation(s) for pipeline.
  name: Ki Insurance Pipeline API
  slug: ki-insurance-pipeline-api
- baseURL: https://app.ki-insurance.com
  baseurl_source: declared
  description: The Quotes API from Ki Insurance — 15 operation(s) for quotes.
  name: Ki Insurance Quotes API
  slug: ki-insurance-quotes-api
- baseURL: https://app.ki-insurance.com
  baseurl_source: declared
  description: The Risk Codes API from Ki Insurance — 1 operation(s) for risk codes.
  name: Ki Insurance Risk Codes API
  slug: ki-insurance-risk-codes-api
- baseURL: https://app.ki-insurance.com
  baseurl_source: declared
  description: The Schedule of Values API from Ki Insurance — 2 operation(s) for schedule of values.
  name: Ki Insurance Schedule of Values API
  slug: ki-insurance-schedule-of-values-api
- baseURL: https://app.ki-insurance.com
  baseurl_source: declared
  description: The Slip Extraction API from Ki Insurance — 5 operation(s) for slip extraction.
  name: Ki Insurance Slip Extraction API
  slug: ki-insurance-slip-extraction-api
- baseURL: https://app.ki-insurance.com
  baseurl_source: declared
  description: The Support API from Ki Insurance — 1 operation(s) for support.
  name: Ki Insurance Support API
  slug: ki-insurance-support-api
- baseURL: https://app.ki-insurance.com
  baseurl_source: declared
  description: The Telemetry API from Ki Insurance — 1 operation(s) for telemetry.
  name: Ki Insurance Telemetry API
  slug: ki-insurance-telemetry-api
- baseURL: https://app.ki-insurance.com
  baseurl_source: declared
  description: The Users API from Ki Insurance — 10 operation(s) for users.
  name: Ki Insurance Users API
  slug: ki-insurance-users-api
arazzos:
- description: Create a quote on Ki's partner-gated broker platform, attach the schedule of values, geocode it, run Ki's algorithmic pricing and retrieve the priced quote document. Every operationId below exists ver
  name: Ki — quote a risk and run the follow algorithm
  slug: ki-insurance-quote-and-price
- description: 'Ki''s slip extraction pipeline: register the slip upload, execute the extraction job, poll it to completion, read the result and promote it into a quote. Every operationId exists verbatim in the refere'
  name: Ki — turn a broker slip into a quote
  slug: ki-insurance-slip-to-quote
artifact_total: 26
collections:
- collection_type: open
  name: Ki Broker Trading Platform API (observed)
  slug: open-ki-insurance-broker-platform
common:
- group: other
  title: ''
  type: Overlay
  url: overlays/ki-insurance-broker-platform-overlay.yaml
- group: company
  title: ''
  type: Website
  url: https://ki-insurance.com/
- group: company
  title: ''
  type: About
  url: https://ki-insurance.com/about/
- group: company
  title: ''
  type: Blog
  url: https://ki-insurance.com/news/
- group: company
  title: ''
  type: Partners
  url: https://ki-insurance.com/capacity-partners/
- group: start
  title: ''
  type: SignUp
  url: https://app.ki-insurance.com/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://app.ki-insurance.com/policies/2025/11/16/Ki_Website_Terms.pdf
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://app.ki-insurance.com/policies/2025/V2/Ki_Privacy_Policy.pdf
- group: other
  title: ''
  type: CookiePolicy
  url: https://app.ki-insurance.com/policies/2025/Ki_Cookie_Policy.pdf
- group: auth
  title: ''
  type: Authentication
  url: authentication/ki-insurance-authentication.yml
- group: other
  title: ''
  type: OpenIDConnect
  url: https://login.ki-insurance.com/.well-known/openid-configuration
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/ki-insurance-scopes.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/ki-insurance-well-known.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/ki-insurance-domain-security.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/ki-insurance-conformance.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/ki-insurance-lifecycle.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/ki-insurance-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/ki-insurance-problem-types.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/ki-insurance-data-model.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/ki-insurance-llms.txt
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/ki-insurance-mcp.yml
- group: build
  title: ''
  type: ToolCrosswalk
  url: mcp/ki-insurance-tool-crosswalk.yml
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/ki-insurance-agentic-access.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/ki-insurance-quote-and-price.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/ki-insurance-slip-to-quote.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/Ki-Insurance
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/ki-insurance
- group: company
  title: ''
  type: Careers
  url: https://ki-insurance.com/careers/
created: '2026-07-25'
description: 'Ki is the first fully digital, algorithmically driven syndicate at Lloyd''s of London, launched in 2020 out of Brit with Google Cloud and University College London and capitalised with US$500m from Blackstone Tactical Opportunities and Fairfax Financial. Operating from the United Kingdom as Lloyd''s Syndicate 1618, Ki writes follow-only capacity across specialty lines — property, casualty and specialty — quoting risks that a lead underwriter has already priced, in seconds rather than days, through an algorithm rather than a face-to-face negotiation in the Room. Brokers reach Ki through app.ki-insurance.com, a partner-gated single-page platform behind an Auth0 authorization-code login, and Ki announced a "Broker API" in May 2021 that lets partner broking platforms request quotes directly from the algorithm. That API posture is entirely partner-gated: there is no developer portal, no public reference documentation, no self-serve signup, no provider-published OpenAPI or Postman
  collection, and no public webhook or event catalog. What is observable is the platform API itself — Ki''s own broker client ships a complete endpoint registry in its public JavaScript bundle, exposing a same-origin REST surface of roughly a hundred JSON operations across quotes, quote lines, pricing, schedules of values, slip extraction, leads, pipeline, broking houses, nominated leads and Lloyd''s risk codes, all authorised with an Auth0 bearer token. API Evangelist has derived an observed OpenAPI from that bundle. Ki remains the archetype of the United Kingdom''s London-market pattern: genuinely advanced machine-to-machine insurance placement infrastructure, aimed at brokers and syndicates rather than at developers, and therefore effectively invisible from the outside.'
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/apis-json-logo.jpg
layout: provider
mcp_servers:
- description: ''
  name: Ki Insurance MCP Server
  slug: ki-insurance-mcp-server
modified: '2026-07-25'
name: Ki Insurance
nav: Providers
network: true
overview: 'Ki Insurance publishes 18 APIs on the [APIs.io](https://apis.io/) network, including Administration API, Broking Houses API, Classes of Business API, and 15 more. Tagged areas include Insurance, United Kingdom, Lloyd''s of London, Specialty Insurance, and Property and Casualty.


  Ki Insurance''s developer surface includes engineering blog, signup flow, authentication, and 26 more developer resources.'
random_paper: 7
scopes:
- name: Ki Insurance Scopes
  scope_count: 14
  slug: ki-insurance-scopes
  summary_line: 14 scopes · authorizationCode
score:
  band: emerging
  composite: 24.9
  coverage:
    artifact_dirs: 19
    catalog_gap: 78.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 21.1
    commercial_clarity: 21.1
    contract_governance: 4.5
    contract_quality: 14.3
    developer_ergonomics: 16.1
    discoverability: 75.9
    governance: 4.5
    operational_transparency: 2.6
  previous_composite: 24.9
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 18
      marker_coverage: 100.0
      total: 18
    mcp: derived
    skills: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Insurance
    regime_id: insurance
    score: 63.6
  schema_version: 0.18.2
  scored_at: '2026-09-03'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/ki-insurance/refs/heads/main/screenshots/ki-insurance-2026-07-25T223715.png
security:
- kind: authentication
  name: Ki Insurance Authentication
  slug: ki-insurance-authentication
  summary_line: http/openIdConnect/oauth2 · 3 schemes
- kind: domain-security
  name: Ki Insurance Domain Security
  slug: ki-insurance-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: ki-insurance
tags:
- Insurance
- United Kingdom
- Lloyd's of London
- Specialty Insurance
- Property and Casualty
- Underwriting
- Insurtech
- Brokers
- Algorithmic Underwriting
- Reinsurance
website: https://ki-insurance.com/
---
