---
access_model:
  confidence: medium
  label: Self-serve signup
  onboarding: self-serve
  pricing: unknown
  public: false
  source:
  - authentication
  trial: false
  try_now: false
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
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
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 18.3
  scored_at: '2026-09-01'
api_count: 1
apis:
- description: The Request API from CivicPlus — 1 operation(s) for request.
  name: CivicPlus Request API
  slug: civicplus-request-api
- description: The Requests.{response Format} API from CivicPlus — 1 operation(s) for requests.{response format}.
  name: CivicPlus Requests.{response Format} API
  slug: civicplus-requests-response-format-api
- description: The Services API from CivicPlus — 1 operation(s) for services.
  name: CivicPlus Services API
  slug: civicplus-services-api
- description: The Services.{response Format} API from CivicPlus — 1 operation(s) for services.{response format}.
  name: CivicPlus Services.{response Format} API
  slug: civicplus-services-response-format-api
- description: The Tokens API from CivicPlus — 1 operation(s) for tokens.
  name: CivicPlus Tokens API
  slug: civicplus-tokens-api
artifact_total: 14
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Open311 GeoReport Request API
  slug: open-civicplus-request-api
- collection_type: open
  name: Open311 GeoReport Request Requests.{response Format} API
  slug: open-civicplus-requests-response-format-api
- collection_type: open
  name: Open311 GeoReport Request Services API
  slug: open-civicplus-services-api
- collection_type: open
  name: Open311 GeoReport Request Services.{response Format} API
  slug: open-civicplus-services-response-format-api
- collection_type: open
  name: Open311 GeoReport Request Tokens API
  slug: open-civicplus-tokens-api
common:
- group: other
  title: ''
  type: CapabilityMap
  url: capabilities/civicplus-capability-edges.yml
- group: company
  title: ''
  type: Website
  url: https://www.civicplus.com/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://dev.seeclickfix.com/
- group: operate
  title: ''
  type: Support
  url: https://civicplus.help/civicplus-help-center
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/SeeClickFix
- group: operate
  title: ''
  type: StatusPage
  url: https://status.civicplus.com/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://civicplus.help/docs/civicplus-terms-of-use
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://civicplus.help/legal-center/docs/civicplus-privacy-policy
- group: auth
  title: ''
  type: Authentication
  url: authentication/civicplus-authentication.yml
- group: auth
  title: ''
  type: OAuth2
  url: authentication/civicplus-authentication.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/civicplus-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/civicplus-problem-types.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/civicplus-lifecycle.yml
- group: start
  title: ''
  type: Sandbox
  url: sandbox/civicplus-sandbox.yml
- group: build
  title: ''
  type: Packages
  url: packages/civicplus-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/civicplus-packages.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/civicplus-mcp.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/civicplus-llms.txt
- group: agent
  title: ''
  type: WellKnown
  url: well-known/civicplus-well-known.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/civicplus-domain-security.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/civicplus-conformance.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/civicplus-data-model.yml
- group: docs
  title: ''
  type: OpenAPI
  url: openapi/_original/civicplus-seeclickfix-open311-openapi-original.yml
- group: other
  title: ''
  type: Overlay
  url: overlays/civicplus-seeclickfix-open311-overlay.yaml
created: '2026-07-17'
description: CivicPlus is a govtech company providing an integrated platform for local, state, and education government operations, serving 13,000+ public-sector customers. Its product suite spans municipal websites, agenda and meeting management, recreation management, community development (permitting, licensing, code enforcement), utility billing, mass notification, public records requests (NextRequest), Municode codification, payments (CivicPlus Pay), and the SeeClickFix 311 resident-request CRM. The most developer-facing public interface in the CivicPlus family is the SeeClickFix API v2, a REST API over civic service requests (issues), comments, users, places, and questions, which additionally exposes an Open311 GeoReport v2 compatible endpoint for interoperable civic-issue reporting.
image: https://www.civicplus.com/favicon.ico
layout: provider
mcp_servers:
- description: ''
  name: CivicPlus MCP Server
  slug: civicplus-mcp-server
modified: '2026-07-18'
name: CivicPlus
nav: Providers
network: true
overview: 'CivicPlus publishes 5 APIs on the [APIs.io](https://apis.io/) network, including Request API, Requests.{response Format} API, Services API, and 2 more. Tagged areas include Company, Government, GovTech, Local Government, and 311.


  CivicPlus'' developer surface includes support, authentication, sandbox, and 21 more developer resources.'
random_paper: 12
score:
  band: thin
  composite: 36.4
  coverage:
    artifact_dirs: 17
    catalog_gap: 78.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 0.0
    commercial_clarity: 0.0
    contract_governance: 4.5
    contract_quality: 46.3
    developer_ergonomics: 64.3
    discoverability: 75.9
    governance: 4.5
    operational_transparency: 18.4
  previous_composite: 36.4
  provenance:
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 5
    mcp: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Government & Public Sector
    regime_id: government
    score: 31.5
  schema_version: 0.17.2
  scored_at: '2026-09-01'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/civicplus/refs/heads/main/screenshots/civicplus-2026-07-25T205443.png
security:
- kind: authentication
  name: Civicplus Authentication
  slug: civicplus-authentication
  summary_line: http/oauth2 · 3 schemes
- kind: domain-security
  name: Civicplus Domain Security
  slug: civicplus-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
slug: civicplus
tags:
- Company
- Government
- GovTech
- Local Government
- '311'
- Civic Engagement
- Public Records
- Service Requests
website: https://www.civicplus.com/
---
