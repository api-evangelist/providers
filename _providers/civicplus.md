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
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: documented
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: verified
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 33.3
  scored_at: '2026-08-19'
api_count: 5
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
  name: civicplus-mcp.yml
  slug: civicplus-mcpyml
modified: '2026-07-18'
name: CivicPlus
nav: Providers
network: true
overview: 'CivicPlus publishes 5 APIs on the [APIs.io](https://apis.io/) network, including Request API, Requests.{response Format} API, Services API, and 2 more. Tagged areas include Company, Government, GovTech, Local Government, and 311.


  CivicPlus'' developer surface includes support, authentication, sandbox, and 20 more developer resources.'
random_paper: 84
score:
  band: thin
  composite: 32.4
  delta: -5.4
  facets:
    access_clarity: 0.0
    commercial_clarity: 0.0
    contract_governance: 16.7
    contract_quality: 44.8
    developer_ergonomics: 35.7
    discoverability: 81.5
    governance: 16.7
    operational_transparency: 18.4
  previous_composite: 37.8
  provenance:
    conformance: derived
    contracts:
      callable: 0.0
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
  schema_version: 0.12.0
  scored_at: '2026-08-19'
  trend: falling
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
