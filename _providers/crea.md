---
agent_readiness:
  band: agent-native
  dimensions:
    agent_skills: true
    agentic_access: true
    asyncapi_events: false
    auth_clarity: true
    consent_identity: true
    error_semantics: true
    idempotency: false
    mcp_server: true
    openapi_examples: false
    rate_limit_signal: false
    spec_presence: true
    well_known_catalog: true
  schema_version: 0.1
  score: 72.1
  scored_at: '2026-07-27'
agentic_access:
- acting_count: 2
  human_in_the_loop: 0
  name: Crea Agentic Access
  operation_count: 38
  slug: crea-agentic-access
  summary_line: 38 operations · 2 acting
api_count: 3
apis:
- description: The REALTOR.ca DDF (Data Distribution Facility) Web API is CREA's national listing syndication API. CREA documents it as a platform that "allows you to query MLS System data using the RESO Web API spe
  name: REALTOR.ca DDF Web API
  slug: realtor-ca-ddf-web-api
- description: The DDF Lead API is a single documented POST endpoint, /v1/Lead/CreateLead, on the same ddfapi.realtor.ca host as the DDF Web API. CREA requires it because REALTOR email addresses are deliberately exc
  name: REALTOR.ca DDF Lead API
  slug: realtor-ca-ddf-lead-api
- description: 'The REALTOR.ca Board API is a separate, smaller roster-distribution API for CREA''s member boards and associations rather than for listing consumers. CREA describes it as "a data distribution API that '
  name: REALTOR.ca Board API
  slug: realtor-ca-board-api
artifact_total: 9
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/crea-agentic-access.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/crea-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: Security
  url: https://www.crea.ca/.well-known/security.txt
- group: auth
  title: ''
  type: DomainSecurity
  url: security/crea-domain-security.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/crea-well-known.yml
- group: auth
  title: ''
  type: SecurityTxt
  url: well-known/crea-security.txt
- group: auth
  title: ''
  type: Authentication
  url: authentication/crea-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/crea-scopes.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/crea-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/crea-problem-types.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/crea-lifecycle.yml
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/crea-changelog.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/crea-conformance.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/crea-data-model.yml
- group: build
  title: ''
  type: Packages
  url: packages/crea-packages.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/crea-mcp.yml
- group: build
  title: ''
  type: ToolCrosswalk
  url: mcp/crea-tool-crosswalk.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/crea-llms.txt
- group: design
  title: ''
  type: Components
  url: components/crea-components.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/crea-authenticate-and-query-listings.md
- group: agent
  title: ''
  type: AgentSkill
  url: skills/crea-replicate-ddf-feed.md
- group: agent
  title: ''
  type: AgentSkill
  url: skills/crea-send-lead-to-realtor.md
- group: agent
  title: ''
  type: AgentSkill
  url: skills/crea-pull-board-roster.md
- group: agent
  title: ''
  type: AgentSkill
  url: skills/crea-comply-with-ddf-display-rules.md
- group: start
  title: ''
  type: DeveloperPortal
  url: https://ddfapi-docs.realtor.ca/
- group: start
  title: ''
  type: GettingStarted
  url: https://ddfapi-docs.realtor.ca/#section/Quickstart-Overview
- group: company
  title: ''
  type: Website
  url: https://www.crea.ca/
- group: company
  title: ''
  type: Website
  url: https://www.realtor.ca/
- group: company
  title: ''
  type: About
  url: https://www.crea.ca/who-we-are/
- group: docs
  title: ''
  type: Documentation
  url: https://ddfapi-docs.realtor.ca/
- group: docs
  title: ''
  type: Documentation
  url: https://boardapi-docs.realtor.ca/
- group: auth
  title: ''
  type: Authentication
  url: https://identity.crea.ca/.well-known/openid-configuration
- group: start
  title: ''
  type: Login
  url: https://ddf.realtor.ca/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.crea.ca/files/technology/english/DDFR-Policy-and-Rules-February-2024-ENG.pdf
- group: operate
  title: ''
  type: SupportForum
  url: https://support.crea.ca/DDF
- group: operate
  title: ''
  type: Support
  url: mailto:support@realtor.ca
- group: auth
  title: ''
  type: SecurityTxt
  url: https://www.crea.ca/.well-known/security.txt
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.crea.ca/privacy/
- group: other
  title: ''
  type: Statistics
  url: https://www.crea.ca/housing-market-stats/
- group: other
  title: ''
  type: Statistics
  url: https://stats.crea.ca/
- group: company
  title: ''
  type: Blog
  url: https://www.creacafe.ca/
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/canadian-real-estate-association
created: '2026-07-26'
description: 'The Canadian Real Estate Association (CREA) is the national industry body for Canadian residential real estate, representing roughly 160,000 REALTORS through some 60 member boards and associations, owning the MLS and REALTOR trademarks in Canada, and operating REALTOR.ca - the country''s single national consumer listing portal. Where the United States fragments into roughly 500 independently governed MLSs, Canada consolidates: CREA runs the REALTOR.ca Data Distribution Facility (DDF), one national syndication seam that collects listing content from member boards'' MLS Systems and redistributes it to member websites, franchisor pools, and a network of Real Estate Advertising Websites. That makes CREA simultaneously the standards-setter (it writes the DDF Policy and Rules that boards must adopt and enforce), the operator of the pipe, and the gatekeeper of the data. Its API posture is unusually good for an industry body and still firmly gated. Three real machine-readable contracts
  are downloadable anonymously - an OpenAPI 3.0.4 document for the DDF Web API served from ddfapi.realtor.ca/swagger/v1/swagger.json and embedded in the public Redoc site at ddfapi-docs.realtor.ca, an OpenAPI 3.0.1 document for the REALTOR.ca Board API at boardapi-docs.realtor.ca, and a full OpenID Connect discovery document at identity.crea.ca. The DDF Web API is an OData v4 surface normalized to the RESO Data Dictionary and described by CREA as built on the RESO Web API specification, but CREA is RESO-aligned rather than RESO-certified - it does not appear in RESO''s public certification directory of 578 organizations, where the only Canadian entries are individual boards such as the Toronto Regional Real Estate Board and Greater Vancouver REALTORS, none of them Certified Current. Nothing is self-serve. There is no signup, no sandbox and no free tier; client_id and client_secret are, in CREA''s own words, provided by CREA. A REALTOR must opt in through the DDF Dashboard on CREA''s member
  portal, and a third-party developer must enter a data access agreement with CREA as a Technology Provider operating a National Pool Website or Member Website on behalf of that opted-in member. The OData $metadata document, the actual RESO contract, returns HTTP 401 to anonymous callers. No open, unlicensed Canadian listing dataset exists behind any of it.'
image: https://www.crea.ca/dist/favicons/apple-touch-icon.png
layout: provider
mcp_servers:
- description: ''
  name: Candidate MCP tool surface derived from the OpenAPI, plus the third-party crea-ddf-mcp server
  slug: candidate-mcp-tool-surface-derived-from-the-openapi-plus-the-third-party-crea-ddf-mcp-server
modified: '2026-07-26'
name: CREA (REALTOR.ca)
nav: Providers
network: true
overview: 'CREA (REALTOR.ca) publishes 3 APIs on the [APIs.io](https://apis.io/) network: REALTOR.ca DDF Web API, REALTOR.ca DDF Lead API, and REALTOR.ca Board API. Tagged areas include Real Estate, Canada, Property Listings, MLS, and IDX.


  CREA (REALTOR.ca)''s developer surface includes authentication, changelog, getting-started guide, documentation, support, engineering blog, and 37 more developer resources.'
random_paper: 3
scopes:
- name: Crea Scopes
  scope_count: 5
  slug: crea-scopes
  summary_line: 5 scopes · clientCredentials/authorizationCode
score:
  band: thin
  composite: 41.9
  delta: 0.0
  facets:
    commercial_clarity: 34.2
    contract_quality: 37.7
    developer_ergonomics: 60.9
    discoverability: 100.0
    governance: 0.0
    operational_transparency: 26.3
  previous_composite: 41.9
  schema_version: 0.5
  scored_at: '2026-07-27'
  trend: flat
security:
- kind: authentication
  name: Crea Authentication
  slug: crea-authentication
  summary_line: oauth2/openIdConnect · 2 schemes
- kind: domain-security
  name: Crea Domain Security
  slug: crea-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Crea Vulnerability Disclosure
  slug: crea-vulnerability-disclosure
  summary_line: Hackerone · security.txt · contact published
slug: crea
tags:
- Real Estate
- Canada
- Property Listings
- MLS
- IDX
- RESO
- OData
- Industry Body
- PropTech
- Data Syndication
website: https://www.crea.ca/
---
