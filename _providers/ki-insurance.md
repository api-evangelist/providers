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
    openapi_examples: false
    rate_limit_signal: false
    reversibility_documented: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 32.6
  scored_at: '2026-08-24'
agentic_access:
- acting_count: 38
  human_in_the_loop: 1
  name: Ki Insurance Agentic Access
  operation_count: 109
  slug: ki-insurance-agentic-access
  summary_line: 109 operations · 38 acting · 1 human-in-the-loop
api_count: 1
apis:
- description: The same-origin REST API behind app.ki-insurance.com, the partner-gated broker trading platform where Lloyd's brokers place risks with Ki's follow algorithm. Ki publishes no reference documentation fo
  name: Ki Broker Trading Platform API
  slug: broker-platform
arazzos:
- description: Create a quote on Ki's partner-gated broker platform, attach the schedule of values, geocode it, run Ki's algorithmic pricing and retrieve the priced quote document. Every operationId below exists ver
  name: Ki — quote a risk and run the follow algorithm
  slug: ki-insurance-quote-and-price
- description: 'Ki''s slip extraction pipeline: register the slip upload, execute the extraction job, poll it to completion, read the result and promote it into a quote. Every operationId exists verbatim in the refere'
  name: Ki — turn a broker slip into a quote
  slug: ki-insurance-slip-to-quote
artifact_total: 9
collections:
- collection_type: open
  name: Ki Broker Trading Platform API (observed)
  slug: open-ki-insurance-broker-platform
common:
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
overview: 'Ki Insurance publishes 1 API on the [APIs.io](https://apis.io/) network: Ki Broker Trading Platform API. Tagged areas include Insurance, United Kingdom, Lloyd''s of London, Specialty Insurance, and Property and Casualty.


  Ki Insurance''s developer surface includes engineering blog, signup flow, authentication, and 25 more developer resources.'
random_paper: 7
scopes:
- name: Ki Insurance Scopes
  scope_count: 14
  slug: ki-insurance-scopes
  summary_line: 14 scopes · authorizationCode
score:
  band: thin
  composite: 38.6
  delta: 0.0
  facets:
    access_clarity: 21.1
    commercial_clarity: 21.1
    contract_governance: 16.7
    contract_quality: 58.7
    developer_ergonomics: 16.1
    discoverability: 87.0
    governance: 16.7
    operational_transparency: 2.6
  previous_composite: 38.6
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 1
    mcp: derived
    skills: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Insurance
    regime_id: insurance
    score: 63.6
  schema_version: 0.12.1
  scored_at: '2026-08-24'
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
