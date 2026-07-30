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
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: derived
    asyncapi_events: true
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: documented
    idempotency: false
    mcp_server: derived
    openapi_examples: false
    rate_limit_signal: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 40.3
  scored_at: '2026-07-28'
agentic_access:
- acting_count: 6
  human_in_the_loop: 0
  name: Canada Health Infoway Agentic Access
  operation_count: 60
  slug: canada-health-infoway-agentic-access
  summary_line: 60 operations · 6 acting
api_count: 2
apis:
- description: HL7 FHIR R4 (4.0.1) terminology service from Canada Health Infoway's Terminology Gateway (HAPI FHIR), exposing CodeSystem, ValueSet, ConceptMap, and OperationDefinition resources with read/vread/histo
  name: Infoway FHIR Terminology Service API
  slug: infoway-fhir-terminology-service-api
- description: RESTful (non-FHIR) terminology API from Canada Health Infoway for browsing and downloading Canadian terminology content - code systems, subsets (value sets), maps, resource locations, and packages - w
  name: Infoway Terminology Service API
  slug: infoway-terminology-service-api
artifact_total: 7
asyncapis:
- description: ''
  name: Canada Health Infoway Notifications Webhooks
  slug: canada-health-infoway-notifications-webhooks
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
- description: ''
  name: canada-health-infoway-mcp.yml
  slug: canada-health-infoway-mcpyml
modified: '2026-07-24'
name: Canada Health Infoway
nav: Providers
network: true
overview: 'Canada Health Infoway publishes 2 APIs on the [APIs.io](https://apis.io/) network: Infoway FHIR Terminology Service API and Infoway Terminology Service API. Tagged areas include Healthcare, Canada, FHIR, HL7, and Interoperability.


  The Canada Health Infoway catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  Canada Health Infoway''s developer surface includes authentication, documentation, API reference, signup flow, engineering blog, and 20 more developer resources.'
random_paper: 35
score:
  band: thin
  composite: 40.6
  delta: -3.8
  facets:
    commercial_clarity: 34.2
    contract_quality: 55.0
    developer_ergonomics: 40.8
    discoverability: 87.0
    governance: 20.8
    operational_transparency: 7.9
  previous_composite: 44.4
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
  schema_version: 0.6
  scored_at: '2026-07-28'
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
