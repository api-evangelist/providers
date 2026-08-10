---
agent_readiness:
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: derived
    auth_clarity: true
    consent_identity: true
    dry_run_mode: false
    error_semantics: verified
    event_surface_described: derived
    idempotency: false
    mcp_server: derived
    openapi_examples: partial
    rate_limit_signal: false
    spec_presence: true
    well_known_catalog: true
  schema_version: 0.2
  score: 49.3
  scored_at: '2026-08-10'
agentic_access:
- acting_count: 48
  human_in_the_loop: 0
  name: Alto Vebra Agentic Access
  operation_count: 121
  slug: alto-vebra-agentic-access
  summary_line: 121 operations · 48 acting
api_count: 4
apis:
- description: The full Alto REST API for UK estate agency operations — 95 documented paths across 27 resource families covering contacts and applicants, property inventory, listings and media, appraisals and valuat
  name: Alto API
  slug: alto-api
- description: Swagger 2.0 poll API for retrieving applicant leads and appraisal (valuation) leads generated on the Zoopla portal, published by Houseful for contracted Zoopla agency customers and their software part
  name: Zoopla Leads API
  slug: zoopla-leads-api
- description: OpenAPI 3.0.0 contract for activating and inspecting Zoopla Premium Listing products against a property listing, exposed at /products/premium-listings and /products/premium-listings/{uuid}. OAuth2 cli
  name: Zoopla Premium Listing Activations API
  slug: zoopla-premium-listing-activations-api
- description: OpenAPI 3.0.0 contract for activating Zoopla Weekly Featured Property placements against a listing, exposed at /products/weekly-featured-properties and /products/weekly-featured-properties/{uuid}. OAu
  name: Zoopla Weekly Featured Property (WFP) Activations API
  slug: zoopla-weekly-featured-property-api
artifact_total: 12
asyncapis:
- description: 'Event notifications Alto delivers to a partner-hosted HTTPS endpoint when data changes in an Alto agency tenancy. Faithfully transcribed by API Evangelist from the webhook catalogue Alto publishes at '
  name: Alto Webhooks
  slug: alto-vebra-alto-webhooks-asyncapi
- description: Real-time delivery of Zoopla portal leads to a partner-hosted endpoint. Faithfully transcribed by API Evangelist from the push-service documentation Zoopla publishes at https://developers.zoopla.co.uk
  name: Zoopla Lead Push Service
  slug: alto-vebra-zoopla-leads-push-asyncapi
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/alto-vebra-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/alto-vebra-domain-security.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/alto-vebra-scopes.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/alto-vebra-authentication.yml
- group: company
  title: ''
  type: Website
  url: https://www.altosoftware.co.uk/
- group: docs
  title: ''
  type: Documentation
  url: https://developers.vebraalto.com/
- group: start
  title: ''
  type: Portal
  url: https://connect.vebraalto.com/connect
- group: company
  title: ''
  type: Blog
  url: https://www.altosoftware.co.uk/blog/
- group: company
  title: ''
  type: BlogRSS
  url: https://www.altosoftware.co.uk/feed/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://developers.vebraalto.com/api-terms-of-use
- group: operate
  title: ''
  type: Support
  url: https://partnerfeedback.vebraalto.com/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/AltoSoftware
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/zoopla-eng
- group: agent
  title: ''
  type: WellKnown
  url: well-known/alto-vebra-well-known.yml
- group: auth
  title: ''
  type: SecurityTxt
  url: well-known/alto-vebra-security.txt
- group: other
  title: ''
  type: OpenIDConnect
  url: well-known/alto-vebra-openid-configuration.json
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/alto-vebra-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: Security
  url: https://www.zoopla.co.uk/vulnerability-disclosure/
- group: build
  title: ''
  type: Packages
  url: packages/alto-vebra-packages.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/alto-vebra-mcp.yml
- group: build
  title: ''
  type: ToolCrosswalk
  url: mcp/alto-vebra-tool-crosswalk.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/alto-vebra-llms.txt
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/alto-vebra-api-llms.txt
- group: design
  title: ''
  type: Conformance
  url: conformance/alto-vebra-conformance.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/alto-vebra-problem-types.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/alto-vebra-error-codes.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/alto-vebra-lifecycle.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/alto-vebra-conventions.yml
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/alto-vebra-changelog.yml
- group: start
  title: ''
  type: Sandbox
  url: sandbox/alto-vebra-sandbox.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/alto-vebra-data-model.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: docs
  title: ''
  type: AsyncAPI
  url: asyncapi/alto-vebra-alto-webhooks-asyncapi.yml
- group: design
  title: ''
  type: Webhooks
  url: https://developers.vebraalto.com/guides/webhooks/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://developers.vebraalto.com/
- group: docs
  title: ''
  type: APIReference
  url: https://developers.vebraalto.com/api
- group: start
  title: ''
  type: GettingStarted
  url: https://developers.vebraalto.com/guides/authenticating-your-requests/
- group: start
  title: ''
  type: SignUp
  url: https://www.altosoftware.co.uk/become-a-partner/
- group: start
  title: ''
  type: Login
  url: https://connect.vebraalto.com/connect
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.altosoftware.co.uk/privacy-notice/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.altosoftware.co.uk/alto-terms/
- group: operate
  title: ''
  type: Support
  url: https://www.altosoftware.co.uk/contact-us/
- group: operate
  title: ''
  type: HelpCenter
  url: https://support.zoopla.co.uk/hc/en-gb
created: '2026-07-26'
description: 'Alto — formerly Vebra Alto, and still trading through vebra.com — is the United Kingdom''s most widely deployed estate agency CRM, used by more than 6,000 sales and lettings agency branches to run valuations, listings, applicant matching, offers, sales and lettings progression, tenancies, property management, work orders and client accounting. It is owned by Houseful Limited, the parent of the Zoopla portal, which places Alto at the exact chokepoint of the UK residential market — the country has no MLS, so listings reach Rightmove and Zoopla through agency CRM software rather than a shared cooperative database, and Alto is the largest of those pipes. Its API posture is genuinely strong on the contract side and closed on the access side: Alto publishes an open, unauthenticated developer portal at developers.vebraalto.com carrying a complete OpenAPI 3.0.4 document (95 paths, 112 operations across 27 resource families) served verbatim from api-docs.vebraalto.com, alongside 26
  documented CloudEvents 1.0 webhook event types and 101 published OAuth scope strings. But credentials are partner-only — a developer must register an integration in Alto Connect, be bound by an existing contract with Vebra Solutions, and then wait for an individual agency to activate the integration and issue an AgencyRef before a single call can be made. Sibling Zoopla portal product APIs (Leads, Premium Listing Activations, Weekly Featured Property) are documented publicly at developers.zoopla.co.uk with downloadable specs but are likewise restricted to contracted Zoopla agency customers. There is no SDK, CLI, Postman collection, MCP server or status page anywhere in the estate, and no RESO Web API or Data Dictionary certification exists — RESO is a North American NAR-driven standard with no UK counterpart. Alto publishes no open data; the UK''s open property layer sits with HM Land Registry and Ordnance Survey, not with the private CRM duopoly feeders.'
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/groq.png
layout: provider
mcp_servers:
- description: ''
  name: Candidate MCP tool surface derived from the OpenAPIs
  slug: candidate-mcp-tool-surface-derived-from-the-openapis
modified: '2026-07-26'
name: Alto (Vebra / Zoopla)
nav: Providers
network: true
overview: 'Alto (Vebra / Zoopla) publishes 4 APIs on the [APIs.io](https://apis.io/) network, including Alto API, Zoopla Leads API, Zoopla Premium Listing Activations API, and 1 more. Tagged areas include Real Estate, United Kingdom, PropTech, Property Listings, and CRM.


  The Alto (Vebra / Zoopla) catalog on APIs.io includes 2 event-driven AsyncAPI specifications.


  Alto (Vebra / Zoopla)''s developer surface includes authentication, documentation, developer portal, engineering blog, support, changelog, sandbox, and 36 more developer resources.'
random_paper: 77
scopes:
- name: Alto Vebra Scopes
  scope_count: 104
  slug: alto-vebra-scopes
  summary_line: 104 scopes · clientCredentials
score:
  band: developing
  composite: 50.5
  delta: 0.0
  facets:
    commercial_clarity: 34.2
    contract_quality: 61.4
    developer_ergonomics: 62.5
    discoverability: 92.6
    governance: 11.5
    operational_transparency: 39.5
  previous_composite: 50.5
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 4
    mcp: derived
    skills: derived
  schema_version: 0.9.1
  scored_at: '2026-08-10'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/alto-vebra/refs/heads/main/screenshots/alto-vebra-2026-08-07T161256.png
security:
- kind: authentication
  name: Alto Vebra Authentication
  slug: alto-vebra-authentication
  summary_line: apiKey/oauth2 · 5 schemes
- kind: domain-security
  name: Alto Vebra Domain Security
  slug: alto-vebra-domain-security
  summary_line: TLSv1.2 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Alto Vebra Vulnerability Disclosure
  slug: alto-vebra-vulnerability-disclosure
  summary_line: Hackerone · security.txt · contact published
slug: alto-vebra
tags:
- Real Estate
- United Kingdom
- PropTech
- Property Listings
- CRM
- Property Management
- Rentals
- Conveyancing
- Estate Agency
- Tenancy
- Webhooks
- Events
- Lettings
- Sales Progression
- Property Data
- Real Estate Software
website: https://www.altosoftware.co.uk/
---
