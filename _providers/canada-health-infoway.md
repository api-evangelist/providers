---
access_model:
  confidence: medium
  label: Free registration · gated terminology content
  onboarding: unknown
  pricing: unknown
  public: false
  source:
  - review
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
    event_surface_described: derived
    idempotency: false
    mcp_server: false
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 22.1
  scored_at: '2026-08-30'
agentic_access:
- acting_count: 6
  human_in_the_loop: 0
  name: Canada Health Infoway Agentic Access
  operation_count: 60
  slug: canada-health-infoway-agentic-access
  summary_line: 60 operations · 6 acting
api_count: 2
apis:
- description: The CapabilityStatement API from Canada Health Infoway — 1 operation(s) for capabilitystatement.
  name: Canada Health Infoway Capability Statement API
  slug: canada-health-infoway-capabilitystatement-api
- description: The CodeSystem API from Canada Health Infoway — 5 operation(s) for codesystem.
  name: Canada Health Infoway Code System API
  slug: canada-health-infoway-codesystem-api
- description: APIs for accessing code system data
  name: Canada Health Infoway Codesystems API
  slug: canada-health-infoway-codesystems-api
- description: The ConceptMap API from Canada Health Infoway — 5 operation(s) for conceptmap.
  name: Canada Health Infoway Concept Map API
  slug: canada-health-infoway-conceptmap-api
- description: APIs for accessing map data
  name: Canada Health Infoway Maps API
  slug: canada-health-infoway-maps-api
- description: APIs for accessing user notifications
  name: Canada Health Infoway Notification API
  slug: canada-health-infoway-notification-api
- description: APIs for accessing package data
  name: Canada Health Infoway Packages API
  slug: canada-health-infoway-packages-api
- description: APIs for accessing resource location data
  name: Canada Health Infoway Resourcelocations API
  slug: canada-health-infoway-resourcelocations-api
- description: APIs for programmatically logging in
  name: Canada Health Infoway Session API
  slug: canada-health-infoway-session-api
- description: APIs for terminology subsets
  name: Canada Health Infoway Subsets API
  slug: canada-health-infoway-subsets-api
- description: The ValueSet API from Canada Health Infoway — 8 operation(s) for valueset.
  name: Canada Health Infoway Value Set API
  slug: canada-health-infoway-valueset-api
artifact_total: 18
asyncapis:
- description: ''
  name: Canada Health Infoway Notifications Webhooks
  slug: canada-health-infoway-notifications-webhooks
collections:
- collection_type: open
  name: Terminology FHIR API
  slug: open-infoway-fhir-terminology-service-api
- collection_type: open
  name: Terminology API
  slug: open-infoway-terminology-service-api
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/canada-health-infoway-domain-security.yml
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/canada-health-infoway-agentic-access.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/canada-health-infoway-authentication.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/canada-health-infoway-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/canada-health-infoway-problem-types.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/canada-health-infoway-lifecycle.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/canada-health-infoway-conformance.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/canada-health-infoway-data-model.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/canada-health-infoway-mcp.yml
- group: build
  title: ''
  type: ToolCrosswalk
  url: mcp/canada-health-infoway-tool-crosswalk.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/canada-health-infoway-llms.txt
- group: other
  title: ''
  type: Overlay
  url: overlays/canada-health-infoway-fhir-terminology-service-api-overlay.yaml
- group: other
  title: ''
  type: Overlay
  url: overlays/canada-health-infoway-terminology-service-api-overlay.yaml
- group: design
  title: ''
  type: Webhooks
  url: asyncapi/canada-health-infoway-notifications-webhooks.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://ic.infoway-inforoute.ca/en/about/tou?title=8_UserReferencesAndSupports/Terms_And_License_Agreements
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.infoway-inforoute.ca/en/privacy-policy
- group: company
  title: ''
  type: Website
  url: https://www.infoway-inforoute.ca/en/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://accelero.infoway-inforoute.ca/en/tools/developer-tools
- group: docs
  title: ''
  type: Documentation
  url: https://www.infoway-inforoute.ca/en/what-we-do/connected-care/digital-health-standards
- group: docs
  title: ''
  type: APIReference
  url: https://termapi.infoway-inforoute.ca/fhir/fhir-apidocs/v1/swagger-ui
- group: start
  title: ''
  type: SignUp
  url: https://accelero.infoway-inforoute.ca/en/register
- group: start
  title: ''
  type: Login
  url: https://auth-users.infoway-inforoute.ca/auth/UI/Login
- group: company
  title: ''
  type: Blog
  url: https://www.infoway-inforoute.ca/en/blog
- group: company
  title: ''
  type: About
  url: https://www.infoway-inforoute.ca/en/about-us
created: '2026-07-24'
description: Canada Health Infoway is an independent, federally funded not-for-profit organization that leads the adoption of digital health and pan-Canadian interoperability across Canada's province- and territory-fragmented healthcare system. Infoway stewards the pan-Canadian FHIR interoperability specifications - CA Core+ and the CA Baseline profiles developed with the Canadian Institute for Health Information (CIHI) - and operates the Canadian FHIR Registry, the Canadian URI Registry, and a national Terminology Gateway. Its developer-facing API surface, published through the Accelero developer portal, is a HAPI-FHIR R4 (4.0.1) Terminology Service exposing CodeSystem, ValueSet, and ConceptMap resources with $lookup, $expand, $translate, and $validate-code operations, alongside a companion RESTful Terminology API for browsing code systems, subsets, maps, and packages. Infoway is a standards steward and terminology infrastructure operator for the Canadian market rather than a commercial
  clinical-data platform; the terminology content APIs are gated behind free registration and a session/token login, while the FHIR CapabilityStatement is served anonymously.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/apis-json-logo.jpg
layout: provider
mcp_servers:
- description: 'Candidate MCP server derived from the Terminology Gateway OpenAPI operations. Canada Health Infoway does not publish an official hosted MCP server; this is a proposed tool surface an integrator could '
  name: Canada Health Infoway MCP Server
  slug: canada-health-infoway-mcp-server
modified: '2026-07-24'
name: Canada Health Infoway
nav: Providers
network: true
overview: 'Canada Health Infoway publishes 11 APIs on the [APIs.io](https://apis.io/) network, including Capability Statement API, Code System API, Codesystems API, and 8 more. Tagged areas include Healthcare, Canada, FHIR, HL7, and Interoperability.


  The Canada Health Infoway catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  Canada Health Infoway''s developer surface includes authentication, documentation, API reference, signup flow, engineering blog, and 20 more developer resources.'
random_paper: 6
score:
  band: developing
  composite: 42.5
  coverage:
    artifact_dirs: 19
    catalog_gap: 78.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: -0.6
  facets:
    access_clarity: 34.2
    commercial_clarity: 34.2
    contract_governance: 18.2
    contract_quality: 53.7
    developer_ergonomics: 42.3
    discoverability: 75.9
    governance: 18.2
    operational_transparency: 7.9
  previous_composite: 43.1
  provenance:
    agentic_access: derived
    conformance: first-party
    contracts:
      callable: 0.0
      derived: 0
      marker_coverage: 0.0
      total: 2
    mcp: derived
    skills: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Health
    regime_id: health
    score: 38.8
  schema_version: 0.17.2
  scored_at: '2026-08-30'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/canada-health-infoway/refs/heads/main/screenshots/canada-health-infoway-2026-07-25T204326.png
security:
- kind: authentication
  name: Canada Health Infoway Authentication
  slug: canada-health-infoway-authentication
  summary_line: apiKey/http/session · 3 schemes
- kind: domain-security
  name: Canada Health Infoway Domain Security
  slug: canada-health-infoway-domain-security
  summary_line: TLSv1.2 · HSTS · DMARC
slug: canada-health-infoway
tags:
- Healthcare
- Canada
- FHIR
- HL7
- Interoperability
- Terminology
- National Health System
- Digital Health
- Standards
- CA Core
website: https://www.infoway-inforoute.ca/en/
---
