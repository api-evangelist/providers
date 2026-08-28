---
agent_readiness:
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: false
    agentic_commerce: false
    auth_clarity: served
    consent_identity: false
    delegated_identity: served
    dry_run_mode: false
    dynamic_client_registration: true
    error_semantics: documented
    event_surface_described: true
    idempotency: false
    mcp_server: false
    openapi_examples: documented
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 37.4
  scored_at: '2026-08-26'
api_count: 9
apis:
- description: The IESO's open market and system data surface. A flat HTTPS file repository publishing 139 report directories — hourly Ontario and market demand, HOEP and nodal/zonal prices, day-ahead and pre-dispat
  name: IESO Public Reports Repository
  slug: ieso-public-reports-repository
- description: A RESTful file-access API provided by Axway SecureTransport, used to automate retrieval of reports from the IESO Reports Site. Accepts and returns both JSON and XML, and exposes file and directory lis
  name: IESO Reports Site REST API
  slug: ieso-reports-site-rest-api
- description: SOAP web services that let registered Ontario market participants submit and retrieve market information programmatically. The published WSDL (service name emim-web-service, target namespace http://we
  name: IESO Market Information Management (MIM) Web Services
  slug: ieso-mim-web-services
- description: 'A REST API on the Appian-based Online IESO platform for retrieving and maintaining facility registration data. SPEC-249 documents the base path https://online.ieso.ca/suite/webapi/ and the facilities '
  name: IESO Registration System Facilities API
  slug: ieso-registration-facilities-api
- description: A web service API for the Retrofit program under Save on Energy, IESO's conservation and demand management portfolio, allowing participants to integrate with the Retrofit application and project workf
  name: IESO Retrofit System API
  slug: ieso-retrofit-api
- description: A companion web service API documented in SPEC-232 for service providers participating in the Save on Energy Retrofit program, covering the service-provider side of project submission and management o
  name: IESO Retrofit Service Provider API
  slug: ieso-retrofit-service-provider-api
- description: A web service, specified in SPEC-154, through which registered market participants retrieve dispatch instructions issued by the IESO and send back acknowledgements and responses. This is the machine i
  name: IESO Dispatch Service Web Service
  slug: ieso-dispatch-service-web-service
- description: 'A push-notification web service, specified in SPEC-155, that delivers automated notifications of dispatch instructions to registered market participants rather than requiring them to poll. The design '
  name: IESO Dispatch Notification Service Web Service
  slug: ieso-dispatch-notification-service
- description: A web service, specified in SPEC-113, for submitting and managing transmission and generation outage requests in IESO's Outage Coordination and Scheduling System. The design specification is public; t
  name: IESO Outage Coordination and Scheduling System (OCSS) Web Service
  slug: ieso-ocss-web-service
artifact_total: 15
asyncapis:
- description: ''
  name: Ieso Dispatch Notification Webhooks
  slug: ieso-dispatch-notification-webhooks
common:
- group: company
  title: ''
  type: Website
  url: https://www.ieso.ca/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://www.ieso.ca/sector-participants/technical-interfaces
- group: docs
  title: ''
  type: Documentation
  url: https://www.ieso.ca/sector-participants/technical-interfaces
- group: docs
  title: ''
  type: Documentation
  url: https://www.ieso.ca/en/Power-Data/Data-Directory
- group: docs
  title: ''
  type: APIReference
  url: https://www.ieso.ca/-/media/Files/IESO/technical-interfaces/xml-automated-docs/IMO_SPEC_0100.pdf
- group: operate
  title: ''
  type: Support
  url: https://www.ieso.ca/Corporate-IESO/Contact
- group: start
  title: ''
  type: SignUp
  url: https://www.ieso.ca/Sector-Participants/Connection-Process/Overview
- group: start
  title: ''
  type: Login
  url: https://online.ieso.ca/
- group: operate
  title: ''
  type: Roadmap
  url: https://www.ieso.ca/sector-participants/change-management/it-release-schedule
- group: operate
  title: ''
  type: Deprecation
  url: https://www.ieso.ca/sector-participants/change-management/it-release-schedule
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.ieso.ca/Terms-of-Use
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.ieso.ca/privacy
- group: auth
  title: ''
  type: Security
  url: https://www.ieso.ca/Sector-Participants/Cyber-Security/Cyber-Security-Incident-Reporting
- group: company
  title: ''
  type: Blog
  url: https://www.ieso.ca/en/Corporate-IESO/Blog
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/ieso
- group: other
  title: ''
  type: Email
  url: mailto:customer.relations@ieso.ca
- group: auth
  title: ''
  type: Authentication
  url: authentication/ieso-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/ieso-scopes.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/ieso-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/ieso-error-codes.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/ieso-data-model.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/ieso-lifecycle.yml
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/ieso-changelog.yml
- group: start
  title: ''
  type: Sandbox
  url: sandbox/ieso-sandbox.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/ieso-conformance.yml
- group: build
  title: ''
  type: Packages
  url: packages/ieso-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/ieso-packages.yml
- group: design
  title: ''
  type: Webhooks
  url: asyncapi/ieso-dispatch-notification-webhooks.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/ieso-well-known.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/ieso-mcp.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/ieso-llms.txt
- group: auth
  title: ''
  type: DomainSecurity
  url: security/ieso-domain-security.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/ieso-vulnerability-disclosure.yml
created: '2026-07-27'
description: 'The Independent Electricity System Operator (IESO) is the Crown corporation that operates Ontario''s bulk electricity system and administers the province''s wholesale electricity market, balancing supply and demand in real time, running the day-ahead and real-time energy and operating reserve markets, procuring capacity and transmission rights, planning the provincial grid, and delivering the Save on Energy conservation programs. It sits at the top of Canada''s largest provincial electricity value chain — upstream of the licensed local distribution companies that bill retail customers — which is why its API posture splits cleanly in two. Its market and system data surface is genuinely open: a public report repository at reports-public.ieso.ca serves 139 report directories of demand, price, generation-by-fuel, intertie flow, outage, adequacy and settlement data as CSV, XML and XLSX over anonymous HTTPS with no account, key or registration, backed by published XSD schemas and
  a public interface specification. Its programmatic APIs are the opposite: the Axway SecureTransport REST API at reports.ieso.ca/api/v1.4, the SOAP Market Information Management web services, and the Appian-based Online IESO registration, retrofit, dispatch and outage web services are all reserved for registered Ontario market participants with IESO-issued machine accounts. IESO publishes no consumer energy-data API: Ontario''s Green Button mandate (O. Reg. 633/21) binds licensed electricity and gas distributors, not the system operator, so there is no retail usage or billing surface here at all.'
image: https://www.ieso.ca/-/media/Images/IESO/Logo/ieso-logo-lrg.png
layout: provider
mcp_servers:
- description: ''
  name: IESO MCP Server
  slug: ieso-mcp-server
modified: '2026-07-27'
name: IESO
nav: Providers
network: true
overview: 'IESO publishes 9 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Energy, Canada, Electricity, Energy Markets, and Grid.


  The IESO catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  IESO''s developer surface includes documentation, API reference, support, signup flow, engineering blog, authentication, changelog, and 27 more developer resources.'
random_paper: 12
scopes:
- name: Ieso Scopes
  scope_count: 7
  slug: ieso-scopes
  summary_line: 7 scopes · authorizationCode/implicit/password/deviceCode/refreshToken
score:
  band: developing
  composite: 52.1
  delta: 1.7
  facets:
    access_clarity: 34.2
    commercial_clarity: 34.2
    contract_governance: 4.5
    contract_quality: 49.3
    developer_ergonomics: 58.9
    discoverability: 75.9
    governance: 4.5
    operational_transparency: 47.4
  previous_composite: 50.4
  provenance:
    conformance: derived
    mcp: derived
    skills: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Energy & Utilities
    regime_id: energy_utilities
    score: 64.9
  schema_version: 0.15.0
  scored_at: '2026-08-26'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/ieso/refs/heads/main/screenshots/ieso-2026-08-07T170612.png
security:
- kind: authentication
  name: Ieso Authentication
  slug: ieso-authentication
  summary_line: none/http/apiKey/oauth2/openIdConnect · 6 schemes
- kind: domain-security
  name: Ieso Domain Security
  slug: ieso-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Ieso Vulnerability Disclosure
  slug: ieso-vulnerability-disclosure
  summary_line: Hackerone · security.txt · contact published
slug: ieso
tags:
- Energy
- Canada
- Electricity
- Energy Markets
- Grid
- System Operator
- Market Data
- Open Data
- Ontario
- Demand Response
- Renewables
website: https://www.ieso.ca/
---
