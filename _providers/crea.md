---
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
    dynamic_client_registration: false
    error_semantics: verified
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
  score: 34.7
  scored_at: '2026-08-30'
agentic_access:
- acting_count: 2
  human_in_the_loop: 0
  name: Crea Agentic Access
  operation_count: 38
  slug: crea-agentic-access
  summary_line: 38 operations · 2 acting
api_count: 3
apis:
- description: Get details about each destination linked to the Technology Provider
  name: CREA (REALTOR.ca) Destination API
  slug: crea-destination-api
- description: Create Lead
  name: CREA (REALTOR.ca) Lead API
  slug: crea-lead-api
- description: This transaction is used to retrieve Member list for the specific board. Boards can access Member information of other Boards based on permissions granted.
  name: CREA (REALTOR.ca) Member API
  slug: crea-member-api
- description: This transaction is used to retrieve Office details for the specific board. Boards can access Office information of other Boards based on permissions granted.
  name: CREA (REALTOR.ca) Office API
  slug: crea-office-api
- description: The OpenHouse API from CREA (REALTOR.ca) — 2 operation(s) for openhouse.
  name: CREA (REALTOR.ca) Open House API
  slug: crea-openhouse-api
- description: Get Properties
  name: CREA (REALTOR.ca) Property API
  slug: crea-property-api
artifact_total: 16
collections:
- collection_type: open
  name: API Collection
  slug: open-crea-identity-openid-configuration
- collection_type: open
  name: REALTOR.ca Board API Documentation
  slug: open-crea-realtor-ca-board-api
- collection_type: open
  name: REALTOR.ca DDF® Web API Documentation
  slug: open-crea-realtor-ca-ddf-web-api-swagger-endpoint
- collection_type: open
  name: REALTOR.ca DDF® Web API Documentation
  slug: open-crea-realtor-ca-ddf-web-api
common:
- group: other
  title: ''
  type: CapabilityMap
  url: capabilities/crea-capability-edges.yml
- group: other
  title: ''
  type: Overlay
  url: overlays/crea-realtor-ca-ddf-web-api-overlay.yaml
- group: other
  title: ''
  type: Overlay
  url: overlays/crea-realtor-ca-ddf-web-api-swagger-endpoint-overlay.yaml
- group: other
  title: ''
  type: Overlay
  url: overlays/crea-realtor-ca-board-api-overlay.yaml
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
- description: CREA publishes no official MCP server for any REALTOR.ca API. Searches of the DDF and Board API documentation, the MCP registries and npm turned up no CREA-operated hosted or stdio server, and there i
  name: Candidate MCP tool surface derived from the OpenAPI, plus the third-party crea-ddf-mcp server
  slug: candidate-mcp-tool-surface-derived-from-the-openapi-plus-the-third-party-crea-ddf-mcp-server
modified: '2026-07-26'
name: CREA (REALTOR.ca)
nav: Providers
network: true
overview: 'CREA (REALTOR.ca) publishes 6 APIs on the [APIs.io](https://apis.io/) network, including Destination API, Lead API, Member API, and 3 more. Tagged areas include Real-Estate, Canada, Property Listings, MLS, and IDX.


  CREA (REALTOR.ca)''s developer surface includes authentication, changelog, getting-started guide, documentation, support, engineering blog, and 41 more developer resources.'
random_paper: 12
scopes:
- name: Crea Scopes
  scope_count: 5
  slug: crea-scopes
  summary_line: 5 scopes · clientCredentials/authorizationCode
score:
  band: developing
  composite: 41.7
  coverage:
    artifact_dirs: 22
    catalog_gap: 75.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: -1.2
  facets:
    access_clarity: 27.6
    commercial_clarity: 27.6
    contract_governance: 18.2
    contract_quality: 44.8
    developer_ergonomics: 50.6
    discoverability: 92.6
    governance: 18.2
    operational_transparency: 26.3
  previous_composite: 42.9
  provenance:
    agentic_access: derived
    conformance: first-party
    contracts:
      callable: 33.3
      derived: 0
      marker_coverage: 0.0
      total: 3
    mcp: derived
    skills: derived
  schema_version: 0.17.2
  scored_at: '2026-08-30'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/crea/refs/heads/main/screenshots/crea-2026-08-07T163831.png
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
- Real-Estate
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
